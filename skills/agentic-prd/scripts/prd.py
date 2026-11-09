#!/usr/bin/env python3
"""Check an Agentic PRD vault, and regenerate its MOC snapshots.

    python3 scripts/prd.py check <vault> [--prd PRD-001] [--source SRC-01=path]
    python3 scripts/prd.py moc   <vault>

Work item levels: Epic (EPIC-01), Feature (FEAT-01), User Story (US-01). Standard library only.
Exit code 0 means no errors; warnings do not fail the check.

The script reads front matter, so it finds structure and never meaning. It cannot tell whether a
citation supports the requirement that cites it, whether a statement is the behaviour anybody
wanted, or whether an acceptance criterion tests the thing it names. Say what it did not cover.
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import pathlib
import re
import sys

STATUSES = ("Draft", "In Review", "Accepted", "Superseded")
SECTIONS_BY_SIZE = {"Small": (1, 2, 4, 6, 7), "Standard": tuple(range(1, 9)),
                    "Large": tuple(range(1, 9))}
PRIORITIES = ("P0", "P1", "P2", "P3")
VERIFY = ("Auto", "Manual", "Eval", "Telemetry")
COVERAGE = ("covered", "blocked", "skipped-proposed", "skipped-p3", "retired")
CHECKS = ("empty-state", "loading-state", "error-state", "permissions",
          "bad-input-and-boundaries", "concurrency", "current-records-and-data-migration")
METRIC_FIELDS = ("baseline", "target", "owner", "source-system", "population",
                 "denominator", "window")
LOCATOR = r"(?:@[\d:]+|p\.\d+|L\d+|[A-Z]{2}-\d+|[A-Z][a-z]+)"
SOURCE_VALUE = re.compile(r"^(SRC-\d+(\s+" + LOCATOR + r")?|DEC-\d+|A-\d+|PROPOSED)$")
PATTERN_START = re.compile(r"^(The system shall|When |While |If |Where )")
VAGUE = re.compile(r"\b(fast|quick|simple|easy|appropriate|intuitive|user-friendly|robust|"
                   r"seamless)\b", re.I)
STORY_LABELS = ("**Expected Output**", "**Details**", "**Assumptions**", "**Testing Strategy**",
                "**Open Questions**", "**Technical Notes**", "**Acceptance Criteria**", "**Tags**")
WIKILINK = re.compile(r"!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
GEN = re.compile(r"(<!-- generated:[^\n]*-->\n)(.*?)(<!-- /generated -->)", re.S)
LEVELS = {"epic": "EPIC", "feature": "FEAT", "user-story": "US"}


# ---------------------------------------------------------------------------- #
# Notes
# ---------------------------------------------------------------------------- #
class Note:
    def __init__(self, path: pathlib.Path, vault: pathlib.Path):
        self.path, self.rel = path, path.relative_to(vault)
        text = path.read_text(encoding="utf-8")
        self.has_fm = text.startswith("---\n")
        self.meta, self.body = split_front_matter(text)
        self.id = str(self.meta.get("id", "") or "")
        self.type = str(self.meta.get("type", "") or "")
        self.status = str(self.meta.get("status", "") or "")
        self.stem = path.stem
        self.aliases = as_list(self.meta.get("aliases"))
        self.links = {m.group(1).strip() for m in WIKILINK.finditer(text)}

    @property
    def title(self) -> str:
        for line in self.body.splitlines():
            if line.startswith("# "):
                head = line[2:].strip()
                if self.id and head.startswith(self.id):
                    head = head[len(self.id):].lstrip(" -—–:")
                return head or self.stem.replace("-", " ")
        return self.stem.replace("-", " ")

    def prop(self, key, default=""):
        return self.meta.get(key, default)


def split_front_matter(text: str):
    """Front matter as a flat dict: scalars, inline lists, and one level of nesting."""
    meta, body = {}, text
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            raw, body = text[4:end], text[end + 4:].lstrip("\n")
            parent = None
            for line in raw.splitlines():
                if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
                    continue
                indented = line[0] in " \t"
                key, _, val = line.strip().partition(":")
                key, val = key.strip(), val.strip()
                if indented and parent is not None and isinstance(meta.get(parent), dict):
                    meta[parent][key] = scalar(val)
                    continue
                if val == "":
                    parent, meta[key] = key, {}
                else:
                    parent, meta[key] = None, scalar(val)
            # `key:` with nothing under it is an empty value, not an empty mapping. Left as {} it
            # reads as truthy, and every "is this field filled in?" check silently passes.
            for key, value in list(meta.items()):
                if value == {}:
                    meta[key] = ""
    return meta, body


def scalar(val: str):
    val = val.strip()
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1].strip()
        return [p.strip().strip("\"'") for p in inner.split(",") if p.strip()] if inner else []
    return val.strip("\"'")


def as_list(val):
    if val is None or val == "":
        return []
    return val if isinstance(val, list) else [val]


def ids_in(val) -> list[str]:
    """Every id named in a property, whether written as a wikilink or bare."""
    out = []
    for item in as_list(val):
        text = str(item)
        out += [m.group(1).strip() for m in WIKILINK.finditer(text)] or \
               [t for t in re.findall(r"[A-Z]+-\d+", text)]
    return out


def load(vault: pathlib.Path):
    notes, others = [], set()
    for dirpath, dirnames, filenames in os.walk(vault):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for name in sorted(filenames):
            path = pathlib.Path(dirpath) / name
            if name.endswith(".md"):
                note = Note(path, vault)
                if note.has_fm:
                    notes.append(note)
                else:
                    # No front matter: not a PRD note, and not this script's business. The vault
                    # may share its folder with the repo's other docs.
                    others.update({name, path.stem})
            elif not name.startswith("."):
                others.update({name, path.stem})
    return notes, others


# ---------------------------------------------------------------------------- #
# Report
# ---------------------------------------------------------------------------- #
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


# ---------------------------------------------------------------------------- #
# Checks
# ---------------------------------------------------------------------------- #
def check(vault: pathlib.Path, report: Report, want_prd: str | None, sources: dict) -> list[str]:
    notes, others = load(vault)
    by_type = collections.defaultdict(list)
    for n in notes:
        by_type[n.type].append(n)
    resolvable = set(others)
    for n in notes:
        resolvable |= {n.stem, *n.aliases} | ({n.id} if n.id else set())
    by_id = {n.id: n for n in notes if n.id}

    prds = by_type["prd"]
    report.require(bool(prds), "No PRD hub note found (a note with `type: prd`)")
    if want_prd:
        prds = [p for p in prds if p.id == want_prd]
        report.require(bool(prds), f"No PRD hub note with id {want_prd}")
    prd = prds[0] if prds else None

    status = size = ""
    if prd:
        status, size = str(prd.prop("status")), str(prd.prop("size"))
        report.require(status in STATUSES, f"{prd.rel}: invalid status {status!r}")
        report.require(size in SECTIONS_BY_SIZE, f"{prd.rel}: invalid size {size!r}")
        report.require(bool(re.fullmatch(r"PRD-\d+", prd.id)), f"{prd.rel}: invalid id {prd.id!r}")
        hub = prd.body.split("## Agent protocol")[0]
        report.require(not re.search(r"\bCAP-\d+", hub),
                       f"{prd.rel}: uses an old CAP id. Use EPIC-01 and FEAT-01.")
        for number in SECTIONS_BY_SIZE.get(size, ()):
            report.require(re.search(rf"^## {number}\. ", hub, flags=re.M) is not None,
                           f"{prd.rel}: section {number} is not present")
        owner = str(prd.prop("owner", "")).strip()
        if owner.lower() in ("", "unknown") or owner.startswith("<"):
            report.warn(f"{prd.rel}: the PRD has no named owner")
    lenient = status != "Accepted"

    # ---- duplicate ids, dangling links
    seen = collections.defaultdict(list)
    for n in notes:
        if n.id:
            seen[n.id].append(str(n.rel))
    for ident, where in sorted(seen.items()):
        report.require(len(where) == 1, f"duplicate id {ident}: {', '.join(where)}")
    for n in notes:
        for target in sorted(n.links):
            if target not in resolvable and target.rsplit("/", 1)[-1] not in resolvable:
                report.require(False, f"{n.rel}: dangling wikilink [[{target}]]")
        if n.id and n.id not in n.aliases:
            report.require(False, f"{n.rel}: id {n.id} is not in aliases, so [[{n.id}]] will not "
                                  f"resolve")

    reqs = check_requirements(by_type["requirement"], report, status, lenient)
    questions = check_questions(by_type["open-question"], report, lenient)
    check_metrics(by_type["outcome-metric"], report)
    stories, covered = check_backlog(by_type, reqs, report, status, by_id)
    check_coverage(by_type["feature"], reqs, questions, report, lenient)

    for q, blocks in questions.items():
        for rid in blocks:
            if rid not in reqs and not rid.startswith(("FEAT", "EPIC", "US", "OUT")):
                report.require(False, f"{q} blocks unknown requirement {rid}")
            if reqs.get(rid, {}).get("priority") == "P0":
                report.warn(f"{rid} is P0 and {q} blocks it")

    if sources:
        report.checks += 1
        print(f"Locators checked: {check_locators(notes, sources, report)}")

    proposed = sorted(r for r, v in reqs.items() if str(v["source"]) == "PROPOSED")
    if status == "Accepted":
        for rid in proposed:
            report.require(False, f"{rid} is PROPOSED in an Accepted PRD")
    elif proposed:
        report.warn(f"PROPOSED requirements need a decision: {', '.join(proposed)}")
    active = [v["priority"] for v in reqs.values() if v["coverage"] != "retired"]
    if len(active) > 2 and set(active) == {"P0"}:
        report.warn("All requirements are P0, so priority does not help a person decide")

    return [f"Status: {status or '—'}", f"Epics: {len(by_type['epic'])}",
            f"Features: {len(by_type['feature'])}", f"Requirements: {len(reqs)}",
            f"Questions: {len(questions)}", f"Proposed: {len(proposed)}",
            f"User Stories: {stories}", f"Covered: {covered}"]


def check_requirements(notes, report, status, lenient) -> dict:
    out = {}
    for n in notes:
        rel = n.rel
        report.require(bool(re.fullmatch(r"(R|X)-\d+", n.id)),
                       f"{rel}: requirement id {n.id!r} is not R-NNN or X-NNN")
        statement = n.title
        coverage = str(n.prop("coverage", ""))
        retired = coverage == "retired" or statement.lower().startswith("retired")
        if not retired:
            report.require(PATTERN_START.search(statement) is not None,
                           f"{n.id}: statement does not open with one of the five patterns "
                           f"(The system shall / When / While / If / Where)")
            vague = VAGUE.search(statement)
            if vague:
                report.warn(f"{n.id}: vague word {vague.group(0)!r} in the statement")
        source = str(n.prop("source", ""))
        report.require(SOURCE_VALUE.match(source) is not None,
                       f"{n.id}: source {source!r} is not SRC-nn with a locator, DEC-nn, A-nn or "
                       f"PROPOSED")
        report.require(str(n.prop("priority", "")) in PRIORITIES,
                       f"{n.id}: priority {n.prop('priority')!r} is not one of {PRIORITIES}")
        report.require(str(n.prop("verify", "")) in VERIFY,
                       f"{n.id}: verify {n.prop('verify')!r} is not one of {VERIFY}")
        report.require(coverage in COVERAGE,
                       f"{n.id}: coverage {coverage!r} is not one of {COVERAGE}")
        if n.id.startswith("X-"):
            report.require(bool(as_list(n.prop("applies-to"))),
                           f"{n.id}: a cross-cutting requirement must name what it applies to")
        if coverage == "covered":
            report.require(bool(ids_in(n.prop("stories"))),
                           f"{n.id}: coverage is covered but no story is named")
        if coverage == "blocked":
            report.require(bool(ids_in(n.prop("questions"))),
                           f"{n.id}: coverage is blocked but no question is named")
        out[n.id] = {"source": source, "priority": str(n.prop("priority", "")),
                     "verify": str(n.prop("verify", "")), "coverage": coverage,
                     "stories": ids_in(n.prop("stories")), "statement": statement,
                     "note": n}
    return out


def check_questions(notes, report, lenient) -> dict:
    out = {}
    for n in notes:
        report.require(bool(re.fullmatch(r"Q-\d+", n.id)), f"{n.rel}: question id {n.id!r} is not "
                                                           f"Q-NN")
        owner = str(n.prop("owner", "")).strip()
        report.require(bool(owner) and not owner.startswith("<"),
                       f"{n.id}: a question with no owner cannot close")
        needed = str(n.prop("needed-by", "")).strip()
        report.require(bool(needed) and not needed.startswith("<"),
                       f"{n.id}: a question with no needed-by cannot close")
        out[n.id] = ids_in(n.prop("blocks"))
    return out


def check_metrics(notes, report) -> None:
    for n in notes:
        report.require(bool(re.fullmatch(r"OUT-\d+", n.id)),
                       f"{n.rel}: metric id {n.id!r} is not OUT-N")
        for field in METRIC_FIELDS:
            value = str(n.prop(field, "")).strip()
            report.require(bool(value) and not value.startswith("<"),
                           f"{n.id}: {field} is empty, so this is not yet a metric")
            if value.lower() == "unknown":
                report.warn(f"{n.id}: {field} is Unknown — it needs an open question, not a guess")


def check_coverage(features, reqs, questions, report, lenient) -> None:
    for n in features:
        checks = n.prop("checks")
        if not isinstance(checks, dict):
            report.require(False, f"{n.id}: no `checks` mapping, so the seven coverage lines are "
                                  f"unanswered")
            continue
        for line in CHECKS:
            value = str(checks.get(line, "")).strip()
            if not report.require(bool(value), f"{n.id}: coverage line {line!r} is blank"):
                continue
            if value.upper().startswith("N/A"):
                report.require(len(value) > 5,
                               f"{n.id}: {line!r} is N/A with no reason, which is a blank line "
                               f"wearing a label")
            elif value.startswith("Gap"):
                for qid in re.findall(r"Q-\d+", value):
                    report.require(qid in questions,
                                   f"{n.id}: {line!r} names a gap {qid} that has no question note")
            else:
                for rid in re.findall(r"(?:R|X)-\d+", value):
                    report.require(rid in reqs,
                                   f"{n.id}: {line!r} names unknown requirement {rid}")


def check_backlog(by_type, reqs, report, status, by_id):
    stories = by_type["user-story"]
    for level, prefix in LEVELS.items():
        for n in by_type[level]:
            report.require(bool(re.fullmatch(prefix + r"-\d{2,}", n.id)),
                           f"{n.rel}: {level} id {n.id!r} is not {prefix}-NN")
            parent = ids_in(n.prop("parent"))
            if level == "epic":
                report.require(bool(parent) and parent[0].startswith("PRD-"),
                               f"{n.id}: an Epic's parent must be the PRD")
            else:
                want = "EPIC" if level == "feature" else "FEAT"
                report.require(bool(parent) and parent[0].startswith(want),
                               f"{n.id}: parent {parent or '(none)'} is not a {want}")
                for pid in parent:
                    report.require(pid in by_id, f"{n.id}: parent {pid} has no note")
    for n in stories:
        missing = [lbl for lbl in STORY_LABELS if lbl not in n.body]
        report.require(not missing, f"{n.id}: missing story labels: {', '.join(missing)}")
        tagged = re.findall(r"^\s*\d+\.\s*AC-\d+\s*\[([^\]]+)\]", n.body, flags=re.M)
        report.require(bool(tagged), f"{n.id}: no acceptance criterion carries a source tag")
        for tag in tagged:
            for rid in re.findall(r"(?:R|X)-\d+", tag):
                report.require(rid in reqs, f"{n.id}: a criterion cites unknown requirement {rid}")
        if status != "Accepted":
            report.require("PREVIEW" in n.body[:400] or "preview" in str(n.prop("status", "")),
                           f"{n.id}: the PRD is not Accepted, so the story must be marked PREVIEW")
    covered = sum(1 for v in reqs.values() if v["coverage"] == "covered")
    for v in reqs.values():
        for sid in v["stories"]:
            report.require(sid in by_id, f"{v['note'].id}: names story {sid}, which has no note")
    # A story slices one Feature, so every requirement it covers belongs to that Feature — unless it
    # is cross-cutting, which belongs to all of them. A mismatch is a slicing error, and it is
    # invisible once the backlog is published.
    for n in stories:
        parent = (ids_in(n.prop("parent")) or [""])[0]
        for rid in ids_in(n.prop("requirements")):
            if rid.startswith("X-") or rid not in reqs:
                continue
            owner = (ids_in(reqs[rid]["note"].prop("feature")) or [""])[0]
            report.require(owner in ("", parent),
                           f"{n.id}: covers {rid}, which belongs to {owner}, not to its parent "
                           f"{parent or '(none)'}")
    return len(stories), covered


def check_locators(notes, sources: dict, report) -> int:
    """Confirm each SRC-nn @time / Lnn locator actually appears in the named file."""
    checked = 0
    text = "\n".join(n.path.read_text(encoding="utf-8") for n in notes)
    cache = {}
    for sid, path in sources.items():
        try:
            cache[sid] = pathlib.Path(path).read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            report.require(False, f"--source {sid}: cannot read {path}: {exc}")
    for sid, body in cache.items():
        for locator in set(re.findall(rf"{sid}\s+(@[\d:]+|L\d+|p\.\d+)", text)):
            checked += 1
            needle = locator[1:] if locator.startswith("@") else locator
            if locator.startswith("L"):
                line = int(locator[1:])
                ok = line <= len(body.splitlines())
            else:
                ok = needle in body
            report.require(ok, f"{sid} {locator} does not appear in the named source")
    return checked


# ---------------------------------------------------------------------------- #
# MOC snapshots
# ---------------------------------------------------------------------------- #
def moc(vault: pathlib.Path) -> list[str]:
    notes, _ = load(vault)
    by_type = collections.defaultdict(list)
    for n in notes:
        by_type[n.type].append(n)
    written = []
    for n in notes:
        spec = n.prop("snapshot")
        if not isinstance(spec, dict) or not spec.get("type"):
            continue
        kind = spec["type"]
        if kind == "coverage":
            body = _coverage_table(by_type["requirement"])
            rows = by_type["requirement"]
        else:
            rows = [x for x in by_type.get(kind, [])
                    if x.status not in as_list(spec.get("exclude-status"))]
            body = _table(rows, spec)
        text = n.path.read_text(encoding="utf-8")
        m = GEN.search(text)
        if not m:
            written.append(f"{n.rel}: snapshot spec but no <!-- generated --> markers")
            continue
        if m.group(2) == body:
            continue
        new = GEN.sub(lambda mm: f"{m.group(1)}{body}{mm.group(3)}", text, count=1)
        n.path.write_text(new, encoding="utf-8")
        written.append(f"{n.rel}: {len(rows)} rows")
    return written


def _table(rows, spec) -> str:
    columns = as_list(spec.get("columns")) or ["id", "title", "status"]
    group = spec.get("group-by")
    groups = collections.defaultdict(list)
    for r in rows:
        groups[str(r.prop(group, "")) if group else ""].append(r)
    fallback = str(spec.get("group-fallback", "Cross-cutting"))
    out = []
    for key in sorted(groups, key=lambda k: (k == "", k)):
        if group:
            out.append(f"### {key or fallback}\n")
        out.append("| " + " | ".join(_header(c) for c in columns) + " |")
        out.append("|" + "---|" * len(columns))
        for r in sorted(groups[key], key=lambda x: _idkey(x.id)):
            out.append("| " + " | ".join(_cell(r, c) for c in columns) + " |")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def _coverage_table(requirements) -> str:
    """One row per requirement, including the cross-cutting ones. Coverage is read from each
    requirement note, so it cannot disagree with the notes the way a hand-kept table does."""
    out = ["| Requirement | Pri | Verify | Story | Coverage |", "|---|---|---|---|---|"]
    counts = collections.Counter()
    for r in sorted(requirements, key=lambda x: _idkey(x.id)):
        coverage = str(r.prop("coverage", "")) or "—"
        counts[coverage] += 1
        stories = ids_in(r.prop("stories")) or ids_in(r.prop("questions"))
        shown = " · ".join(f"[[{s}]]" for s in stories) or "None"
        out.append(f"| [[{r.id}]] | {r.prop('priority', '—')} | {r.prop('verify', '—')} | "
                   f"{shown} | {coverage} |")
    out += ["", "**Counts.** " + " · ".join(
        f"{k}: {v}" for k, v in [("Requirements", len(requirements))] + sorted(counts.items()))]
    return "\n".join(out).rstrip() + "\n"


def _header(column: str) -> str:
    return "ID" if column == "id" else column.replace("-", " ").capitalize()


def _cell(note: Note, column: str) -> str:
    if column == "title":
        return re.sub(r"\s+", " ", note.title.replace("|", "\\|")).strip()
    if column == "id":
        return f"[[{note.id}]]" if note.id else f"[[{note.stem}]]"
    value = note.prop(column, "")
    if isinstance(value, list):
        return " · ".join(str(v) for v in value) or "—"
    return str(value).replace("|", "\\|") or "—"


def _idkey(ident: str):
    m = re.match(r"([A-Za-z-]*)(\d*)", ident or "")
    return (m.group(1), int(m.group(2) or 0))


# ---------------------------------------------------------------------------- #
def main() -> int:
    parser = argparse.ArgumentParser(description="Check an Agentic PRD vault.")
    parser.add_argument("command", choices=("check", "moc"))
    parser.add_argument("vault", type=pathlib.Path)
    parser.add_argument("--prd", help="check only this PRD id, e.g. PRD-001")
    parser.add_argument("--source", action="append", default=[], metavar="SRC-NN=path",
                        help="check SRC-NN @time and Lnn locators against this text file")
    args = parser.parse_args()
    if not args.vault.is_dir():
        parser.error(f"not a directory: {args.vault}")

    if args.command == "moc":
        lines = moc(args.vault.resolve())
        for line in lines:
            print(line)
        if not lines:
            print("no changes")
        return 0

    sources = {}
    for item in args.source:
        if "=" not in item:
            parser.error(f"--source needs SRC-NN=path, got {item}")
        sid, path = item.split("=", 1)
        sources[sid] = path

    report = Report()
    summary = check(args.vault.resolve(), report, args.prd, sources)
    print(" | ".join(summary))
    for message in report.warnings:
        print("WARNING", message)
    for message in report.errors:
        print("ERROR  ", message)
    print(f"Checks: {report.checks}. Errors: {len(report.errors)}. "
          f"Warnings: {len(report.warnings)}.")
    print("This found structure, never meaning. It cannot tell whether a citation supports the "
          "requirement that cites it.")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
