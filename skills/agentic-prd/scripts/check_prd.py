#!/usr/bin/env python3
"""Check the structure and traceability of an Agentic PRD and its backlog.

Work item levels: Epic (EPIC-01), Feature (FEAT-01), User Story (US-01).
Standard library only. Exit code 0 means no errors. Warnings do not fail the check.
The script cannot prove that a citation means what a requirement says.

Usage:
  python check_prd.py prd.md
  python check_prd.py prd.md --backlog backlog.md
  python check_prd.py prd.md --backlog backlog.md --source SRC-07=transcript.txt
"""
import argparse
import pathlib
import re
import sys

STATUSES = ("Draft", "In Review", "Accepted", "Superseded")
SECTIONS_BY_SIZE = {"Small": (1, 2, 4, 6, 7), "Standard": range(1, 9), "Large": range(1, 9)}
PRIORITIES = ("P0", "P1", "P2", "P3")
VERIFY = ("Auto", "Manual", "Eval", "Telemetry")
CHECK_LINES = ("Empty state", "Loading state", "Error state", "Permissions",
               "Bad input and boundaries", "Concurrency", "Current records and data migration")
STORY_LABELS = ("**Expected Output**", "**Details**", "**Assumptions**", "**Testing Strategy**",
                "**Open Questions**", "**Technical Notes**", "**Acceptance Criteria**", "**Tags**")
LOCATOR = r"(?:@[\d:]+|p\.\d+|L\d+|[A-Z]{2}-\d+|[A-Z][a-z]+)"
SOURCE_VALUE = re.compile(r"(SRC-\d+( " + LOCATOR + r")?|DEC-\d+|A-\d+|PROPOSED)")
PATTERN_START = re.compile(r"(The system shall|When |While |If |Where )")
VAGUE = re.compile(r"\b(fast|quick|simple|easy|appropriate|intuitive|user-friendly|robust|seamless)\b", re.I)
REF_KINDS = {"SRC": r"SRC-\d+", "DEC": r"DEC-\d+", "A": r"(?<![\w-])A-\d+", "Q": r"(?<![\w-])Q-\d+",
             "DEP": r"DEP-\d+", "OUT": r"OUT-\d+", "EPIC": r"EPIC-\d+", "FEAT": r"FEAT-\d+"}
EPIC_ID = re.compile(r"EPIC-\d{2,}")
FEAT_ID = re.compile(r"FEAT-\d{2,}")
STORY_ID = re.compile(r"US-\d{2,}")


class Report:
    def __init__(self):
        self.errors, self.warnings, self.checks = [], [], 0

    def require(self, ok, message):
        self.checks += 1
        if not ok:
            self.errors.append(message)
        return ok

    def warn(self, message):
        self.warnings.append(message)


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def table_rows(text):
    return [cells(l) for l in text.splitlines() if l.lstrip().startswith("|")]


def front_matter(text):
    match = re.match(r"---\n(.*?)\n---", text.replace("\r\n", "\n"), flags=re.S)
    fields = {}
    if match:
        for line in match.group(1).splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                fields[key.strip()] = value.split("#")[0].strip()
    return fields


def same_name(left, right):
    return left == right or left.startswith("<") or right.startswith("<")


def work_items(body, report):
    """Read the work item map and the Section 4 headings. Return epics, features, requirement owners."""
    epics, features = {}, {}
    for c in table_rows(body):
        if len(c) != 5 or c[1] not in ("Epic", "Feature"):
            continue
        if c[1] == "Epic":
            report.require(EPIC_ID.fullmatch(c[0]) is not None, f"Invalid Epic ID: {c[0]} (use EPIC-01)")
            report.require(c[0] not in epics, f"Duplicate Epic in the work item map: {c[0]}")
            epics[c[0]] = c[2]
        else:
            report.require(FEAT_ID.fullmatch(c[0]) is not None, f"Invalid Feature ID: {c[0]} (use FEAT-01)")
            report.require(c[0] not in features, f"Duplicate Feature in the work item map: {c[0]}")
            report.require(c[3] in epics, f"{c[0]} has parent {c[3]!r}, which is not an Epic in the map")
            features[c[0]] = dict(name=c[2], parent=c[3])
    report.require(bool(epics), "The work item map has no Epic")
    report.require(bool(features), "The work item map has no Feature")

    owners, seen_epics, seen_features = {}, set(), set()
    epic = feature = None
    for line in body.splitlines():
        heading = re.match(r"^(#{2,4}) (?:(EPIC-\S+?|FEAT-\S+?): (.+))?", line)
        if heading:
            level, wid, name = heading.groups()
            if level == "##" or (level == "###" and not (wid or "").startswith("EPIC")):
                epic = feature = None
            if level == "###" and wid and wid.startswith("EPIC"):
                epic, feature = wid, None
                seen_epics.add(wid)
                report.require(wid in epics, f"Heading {wid} is not in the work item map")
                if wid in epics:
                    report.require(same_name(name.strip(), epics[wid]), f"{wid} name differs from the work item map")
            if level == "####" and wid and wid.startswith("FEAT"):
                feature = wid
                seen_features.add(wid)
                report.require(epic is not None, f"{wid} is not under an Epic heading")
                report.require(wid in features, f"Heading {wid} is not in the work item map")
                if wid in features:
                    report.require(features[wid]["parent"] == epic, f"{wid} is under {epic}, but its map parent is {features[wid]['parent']}")
                    report.require(same_name(name.strip(), features[wid]["name"]), f"{wid} name differs from the work item map")
        first = cells(line)[0] if line.lstrip().startswith("|") else ""
        if re.fullmatch(r"R-\d{3}", first):
            report.require(feature is not None, f"{first} is not under a Feature heading")
            owners[first] = feature
    for wid in sorted(set(epics) - seen_epics):
        report.require(False, f"{wid} is in the work item map but has no heading")
    for wid in sorted(set(features) - seen_features):
        report.require(False, f"{wid} is in the work item map but has no heading")
    for wid in sorted(epics):
        report.require(any(f["parent"] == wid for f in features.values()), f"{wid} has no Feature")
    return epics, features, owners


def requirements(body, report, lenient):
    rows = {}
    for c in table_rows(body):
        is_r = re.fullmatch(r"R-\d{3}", c[0]) and len(c) == 5
        is_x = re.fullmatch(r"X-\d{3}", c[0]) and len(c) == 6
        if not (is_r or is_x):
            continue
        report.require(c[0] not in rows, f"Duplicate requirement ID: {c[0]}")
        row = dict(zip(("text", "pri", "src", "verify"), c[1:] if is_r else c[2:]))
        row["applies"] = c[1] if is_x else None
        rows[c[0]] = row
    for rid, r in rows.items():
        if r["text"].startswith("Retired"):
            continue
        if r["applies"] is not None:
            parts = [p.strip() for p in r["applies"].split(",")]
            report.require(parts == ["All"] or all(FEAT_ID.fullmatch(p) for p in parts),
                           f"{rid} Applies to must be All or FEAT IDs: {r['applies']!r}")
        if not r["text"]:
            (report.warn if lenient else report.errors.append)(f"{rid} has no requirement text")
            continue
        if r["applies"] is not None and r["text"].startswith("<"):
            continue
        report.require(PATTERN_START.match(r["text"]) is not None,
                       f"{rid} does not use a requirement pattern: {r['text'][:50]}")
        report.require(r["pri"] in PRIORITIES, f"{rid} has an invalid priority: {r['pri']!r}")
        report.require(r["verify"] in VERIFY, f"{rid} has an invalid verify value: {r['verify']!r}")
        if not r["src"] and lenient:
            report.warn(f"{rid} has no source")
        else:
            report.require(SOURCE_VALUE.fullmatch(r["src"]) is not None,
                           f"{rid} has an invalid source: {r['src']!r}")
        if r["text"].count("shall") > 1:
            report.warn(f"{rid} can have more than one behavior")
        if VAGUE.search(r["text"]):
            report.warn(f"{rid} has a vague word: {VAGUE.search(r['text']).group(0)}")
    return rows


def check_references(text, body, report, label):
    for kind, pattern in REF_KINDS.items():
        defined = set(re.findall(r"^\s*\|\s*(" + pattern + r")\s*\|", body, flags=re.M))
        for ref in sorted(set(re.findall(pattern, text)) - defined):
            report.require(False, f"{label}: {ref} has no definition in the PRD tables")


def check_coverage_lines(body, rows, report, lenient):
    blocks = re.split(r"^#### (FEAT-\d+)", body, flags=re.M)
    feats = blocks[1::2]
    for feat, block in zip(feats, blocks[2::2]):
        found = {c[0]: c for c in table_rows(block) if len(c) == 2 and c[0] in CHECK_LINES}
        for line in CHECK_LINES:
            if not report.require(line in found, f"{feat} has no coverage line: {line}"):
                continue
            value = found[line][1]
            if not value:
                (report.warn if lenient else report.errors.append)(f"{feat} {line} is blank")
                continue
            for ref in re.findall(r"[RX]-\d{3}", value):
                report.require(ref in rows, f"{feat} {line} names unknown requirement {ref}")
            if value.startswith("Gap"):
                report.require(re.search(r"Q-\d+", value) is not None,
                               f"{feat} {line} has a gap with no open question")


def open_questions(body, report, status, lenient):
    blocked = {}
    section = body.split("**Open questions.**")
    if len(section) < 2:
        report.require(False, "The PRD has no open questions table")
        return blocked
    for c in table_rows(section[1].split("\n## ")[0]):
        if not re.fullmatch(r"Q-\d+", c[0]) or len(c) != 6:
            continue
        if c[5] != "Open":
            continue
        if c[1]:
            report.require(bool(c[2]), f"{c[0]} has no owner")
            report.require(bool(c[3]), f"{c[0]} has no needed-by value")
            if status == "Accepted" and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", c[3]):
                report.warn(f"{c[0]} has no needed-by date")
        elif not lenient:
            report.require(False, f"{c[0]} has no question text")
        for rid in re.findall(r"[RX]-\d{3}", c[4]):
            blocked[rid] = c[0]
    return blocked


def check_locators(text, sources, report):
    count = 0
    for sid, path in sources.items():
        source = pathlib.Path(path).read_text(encoding="utf8", errors="replace")
        for stamp in sorted(set(re.findall(re.escape(sid) + r" @([\d:]+)", text))):
            count += 1
            report.require(re.search(r"(?<![\d:])" + re.escape(stamp) + r"(?![\d:])", source) is not None,
                           f"{sid} @{stamp} is not in {pathlib.Path(path).name}")
        lines = len(source.splitlines())
        for number in sorted(set(re.findall(re.escape(sid) + r" L(\d+)", text)), key=int):
            count += 1
            report.require(1 <= int(number) <= lines, f"{sid} L{number} is past the end of {pathlib.Path(path).name}")
    return count


def parse_backlog(backlog, epics, features, report):
    """Walk the headings. Return the User Stories with their Epic and Feature."""
    stories, epic_heads, feat_heads = [], [], []
    epic = feature = current = None
    for line in backlog.splitlines():
        epic_match = re.match(r"^# Epic: .*\((\S+)\)\s*$", line)
        feat_match = re.match(r"^## Feature: (.*) \((\S+)\)\s*$", line)
        story_match = re.match(r"^### User Story: (\S+) (.+)$", line)
        if epic_match:
            epic, feature, current = epic_match.group(1), None, None
            epic_heads.append(epic)
            report.require(epic in epics, f"Backlog Epic {epic} is not in the PRD work item map")
        elif feat_match:
            feature, current = feat_match.group(2), None
            feat_heads.append(feature)
            report.require(feature in features, f"Backlog Feature {feature} is not in the PRD work item map")
            report.require(epic is not None, f"Backlog Feature {feature} is not under an Epic heading")
            if feature in features:
                report.require(features[feature]["parent"] == epic, f"Backlog Feature {feature} is under {epic}, but its parent is {features[feature]['parent']}")
                report.require(same_name(feat_match.group(1).strip(), features[feature]["name"]), f"Backlog Feature {feature} name differs from the PRD")
        elif story_match:
            report.require(STORY_ID.fullmatch(story_match.group(1)) is not None, f"Invalid User Story ID: {story_match.group(1)} (use US-01)")
            report.require(feature is not None, f"{story_match.group(1)} is not under a Feature heading")
            current = dict(id=story_match.group(1), title=story_match.group(2).strip(), epic=epic, feature=feature, text="")
            stories.append(current)
        elif re.match(r"^#{1,3} ", line):
            current = None
            if line.startswith("# "):
                epic = feature = None
        elif current is not None:
            current["text"] += line + "\n"
    ids = [s["id"] for s in stories]
    for sid in sorted({i for i in ids if ids.count(i) > 1}):
        report.require(False, f"Duplicate User Story ID: {sid}")
    return stories, epic_heads, feat_heads


def check_backlog(backlog, rows, owners, epics, features, blocked, status, report):
    report.require(not re.search(r"\bCAP-\d+|\bS-\d{2,}\b|^## Title:", backlog, flags=re.M),
                   "The backlog uses an old ID or heading. Use EPIC-01, FEAT-01, and US-01.")
    if status != "Accepted":
        report.require("PREVIEW" in "\n".join(backlog.splitlines()[:5]),
                       "The PRD is not Accepted, so the backlog must say PREVIEW at the top")
    proposed = {k for k, r in rows.items() if r["src"] == "PROPOSED"}
    p3 = {k for k, r in rows.items() if r["pri"] == "P3"}
    retired = {k for k, r in rows.items() if r["text"].startswith("Retired")}
    excluded = set(blocked) | proposed | p3 | retired
    in_scope = set(rows) - excluded

    stories, epic_heads, feat_heads = parse_backlog(backlog, epics, features, report)
    criteria = {}
    for story in stories:
        sid, text = story["id"], story["text"]
        for label in STORY_LABELS:
            report.require(label in text, f"{sid} has no label {label}")
        report.require(re.search(r"^As an? .+, I want .+, so that .+\.$", text, flags=re.M) is not None,
                       f"{sid} has no valid story sentence")
        tagged = re.findall(r"AC-(\d+) \[([RX]-\d{3})\] Given .+?, when .+?, then .+", text)
        report.require(bool(tagged), f"{sid} has no valid acceptance criteria")
        numbers = [int(n) for n, _ in tagged]
        report.require(numbers == list(range(1, len(numbers) + 1)), f"{sid} criteria are not in sequence: {numbers}")
        for number, rid in tagged:
            criteria.setdefault(rid, []).append((sid, f"AC-{number}"))
            if rid in owners and owners[rid] is not None:
                report.require(owners[rid] == story["feature"], f"{rid} belongs to {owners[rid]}, but {sid} is in {story['feature']}")
            applies = rows.get(rid, {}).get("applies")
            if applies and applies != "All":
                report.require(story["feature"] in [p.strip() for p in applies.split(",")],
                               f"{rid} applies to {applies}, but {sid} is in {story['feature']}")
        grounding = re.search(r"Source grounding:(.*)", text)
        if report.require(grounding is not None, f"{sid} has no Source grounding"):
            named = set(re.findall(r"[RX]-\d{3}", grounding.group(1)))
            report.require(named == {r for _, r in tagged},
                           f"{sid} Source grounding differs from its criteria: {sorted(named ^ {r for _, r in tagged})}")
        tags = text.split("**Tags**")[-1]
        report.require(story["feature"] in tags and (story["epic"] or "?") in tags,
                       f"{sid} tags must name {story['epic']} and {story['feature']}")
        if any(rows.get(r, {}).get("pri") == "P2" for _, r in tagged) and "Stretch" not in tags:
            report.warn(f"{sid} has a P2 requirement and no Stretch tag")

    summary = {c[0]: c for c in table_rows(backlog) if len(c) == 4 and c[1] in ("Epic", "Feature", "User Story")}
    for epic in epic_heads:
        report.require(epic in summary, f"The work item summary has no row for {epic}")
    for feat in feat_heads:
        if report.require(feat in summary, f"The work item summary has no row for {feat}"):
            report.require(summary[feat][3] == features.get(feat, {}).get("parent"), f"Work item summary has the wrong parent for {feat}")
    for story in stories:
        if report.require(story["id"] in summary, f"The work item summary has no row for {story['id']}"):
            row = summary[story["id"]]
            report.require(row[3] == story["feature"], f"Work item summary has the wrong parent for {story['id']}")
            report.require(row[2] == story["title"], f"Work item summary has the wrong title for {story['id']}")
    for wid in sorted(set(summary) - set(epic_heads) - set(feat_heads) - {s["id"] for s in stories}):
        report.require(False, f"The work item summary names {wid}, which has no heading")

    dod = {rid: f"DoD-{n}" for n, rid in re.findall(r"DoD-(\d+) \[(X-\d{3})\]", backlog)}
    for rid in sorted(in_scope):
        if rid.startswith("R-"):
            found = {s for s, _ in criteria.get(rid, [])}
            report.require(len(found) == 1, f"{rid} must be in exactly one User Story, found: {sorted(found)}")
        elif rows[rid]["applies"] == "All":
            report.require(rid in dod, f"{rid} applies to All, so it must be in the Definition of Done")
        else:
            report.require(rid in criteria, f"{rid} is in no User Story")
    for rid in sorted(excluded):
        report.require(rid not in criteria and rid not in dod, f"{rid} is excluded but has a criterion")
    for rid in sorted((set(criteria) | set(dod)) - set(rows)):
        report.require(False, f"The backlog names unknown requirement {rid}")

    parts = backlog.split("# Coverage")
    if not report.require(len(parts) > 1, "The backlog has no coverage section"):
        return len(stories), 0
    coverage = {}
    for c in table_rows(parts[-1]):
        if re.fullmatch(r"[RX]-\d{3}", c[0]) and len(c) == 6:
            report.require(c[0] not in coverage, f"Two coverage rows for {c[0]}")
            coverage[c[0]] = c
    active = set(rows) - retired
    for rid in sorted(active - set(coverage)):
        report.require(False, f"{rid} has no coverage row")
    for rid in sorted(set(coverage) - set(rows)):
        report.require(False, f"Coverage names unknown requirement {rid}")
    for rid, c in coverage.items():
        if rid not in rows:
            continue
        report.require(c[1] == rows[rid]["pri"] and c[2] == rows[rid]["verify"],
                       f"{rid} coverage priority or verify value differs from the PRD")
        if rid in blocked:
            report.require(c[5] == f"Blocked by {blocked[rid]}", f"{rid} coverage must say Blocked by {blocked[rid]}")
        elif rid in proposed:
            report.require(c[5] == "Skipped: PROPOSED", f"{rid} coverage must say Skipped: PROPOSED")
        elif rid in p3:
            report.require(c[5] == "Skipped: P3", f"{rid} coverage must say Skipped: P3")
        elif rid in dod:
            report.require(c[3] == "All" and c[4] == dod[rid] and c[5] == "Covered", f"{rid} coverage must name {dod[rid]}")
        else:
            report.require((c[3], c[4]) in criteria.get(rid, []) and c[5] == "Covered",
                           f"{rid} coverage names {c[3]} {c[4]}, which is not a real criterion for it")
    counts = {
        "Requirements": len(coverage), "Covered": sum(c[5] == "Covered" for c in coverage.values()),
        "Blocked": sum(c[5].startswith("Blocked") for c in coverage.values()),
        "Epics": len(epic_heads), "Features": len(feat_heads), "User Stories": len(stories),
    }
    for name, value in counts.items():
        match = re.search(name + r": (\d+)\.", parts[-1])
        if report.require(match is not None, f"The counts line has no {name} value"):
            report.require(int(match.group(1)) == value, f"Counts line says {name}: {match.group(1)}, actual: {value}")
    return len(stories), counts["Covered"]


def main():
    parser = argparse.ArgumentParser(description="Check an Agentic PRD and its backlog.")
    parser.add_argument("prd", type=pathlib.Path)
    parser.add_argument("--backlog", type=pathlib.Path)
    parser.add_argument("--source", action="append", default=[], metavar="SRC-NN=path",
                        help="Check SRC-NN @time and L-line locators against this text file. Repeat for each source.")
    args = parser.parse_args()

    report = Report()
    text = args.prd.read_text(encoding="utf8").replace("\r\n", "\n")
    fields = front_matter(text)
    status = fields.get("status", "")
    size = fields.get("size", "")
    report.require(status in STATUSES, f"Invalid status in front matter: {status!r}")
    report.require(size in SECTIONS_BY_SIZE, f"Invalid size in front matter: {size!r}")
    report.require(bool(re.fullmatch(r"PRD-\d+", fields.get("prd_id", ""))), "Invalid prd_id in front matter")
    lenient = status != "Accepted"

    body = text.split("## Agent protocol")[0]
    report.require(not re.search(r"\bCAP-\d+", body), "The PRD uses an old CAP ID. Use EPIC-01 and FEAT-01.")
    for number in SECTIONS_BY_SIZE.get(size, ()):
        report.require(re.search(rf"^## {number}\. ", body, flags=re.M) is not None, f"Section {number} is not present")

    epics, features, owners = work_items(body, report)
    rows = requirements(body, report, lenient)
    check_references(body, body, report, "PRD")
    check_coverage_lines(body, rows, report, lenient)
    blocked = open_questions(body, report, status, lenient)
    for rid in sorted(set(blocked) - set(rows)):
        report.require(False, f"An open question blocks unknown requirement {rid}")

    proposed = sorted(k for k, r in rows.items() if r["src"] == "PROPOSED")
    if status == "Accepted":
        for rid in proposed:
            report.require(False, f"{rid} is PROPOSED in an Accepted PRD")
    elif proposed:
        report.warn(f"PROPOSED requirements need a decision: {', '.join(proposed)}")
    for rid in sorted(blocked):
        if rows.get(rid, {}).get("pri") == "P0":
            report.warn(f"{rid} is P0 and {blocked[rid]} blocks it")
    if fields.get("owner", "").lower() in ("", "unknown") or fields.get("owner", "").startswith("<"):
        report.warn("The PRD has no named owner")
    active = [r["pri"] for r in rows.values() if r["text"] and r["pri"] in PRIORITIES]
    if len(active) > 2 and set(active) == {"P0"}:
        report.warn("All requirements are P0, so priority does not help a person decide")
    if re.search(r"^\|\s*OUT-\d+.*Unknown", body, flags=re.M):
        report.warn("At least one outcome has an Unknown value")

    combined = text
    summary = [f"Status: {status}", f"Epics: {len(epics)}", f"Features: {len(features)}",
               f"Requirements: {len(rows)}", f"Blocked: {len(blocked)}", f"Proposed: {len(proposed)}"]
    if args.backlog:
        backlog = args.backlog.read_text(encoding="utf8").replace("\r\n", "\n")
        check_references(backlog, body, report, "Backlog")
        stories, covered = check_backlog(backlog, rows, owners, epics, features, blocked, status, report)
        summary += [f"User Stories: {stories}", f"Covered: {covered}"]
        combined += backlog

    sources = {}
    for item in args.source:
        if "=" not in item:
            parser.error(f"--source needs SRC-NN=path, got {item}")
        sid, path = item.split("=", 1)
        sources[sid] = path
    if sources:
        summary.append(f"Locators checked: {check_locators(combined, sources, report)}")

    print(" | ".join(summary))
    for message in report.warnings:
        print("WARNING", message)
    for message in report.errors:
        print("ERROR  ", message)
    print(f"Checks: {report.checks}. Errors: {len(report.errors)}. Warnings: {len(report.warnings)}.")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
