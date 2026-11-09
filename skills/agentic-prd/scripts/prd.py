#!/usr/bin/env python3
"""Check an Agentic PRD vault, and regenerate its MOC snapshots.

    python3 scripts/prd.py check <vault> [--prd PRD-001] [--source SRC-01=path] [--baseline FILE]
    python3 scripts/prd.py moc   <vault> [--check]

Work item levels: Epic (EPIC-01), Feature (FEAT-01), User Story (US-01). Standard library only.
Exit code 0 means no errors; warnings do not fail the check.

Links are resolved the way Obsidian resolves them: by file name or path, never through `aliases`.
So the citable form is `[[create-a-label-on-order-confirmation|R-001]]`, and a bare `[[R-001]]` is
a dangling link that opens a new empty note. `moc --check` fails on a stale generated block instead
of repairing it in silence, and `--baseline FILE` reports only what a change broke.

The script reads front matter, so it finds structure and never meaning. It cannot tell whether a
citation supports the requirement that cites it, whether a statement is the behaviour anybody
wanted, or whether an acceptance criterion tests the thing it names. Say what it did not cover.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
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
WIKILINK = re.compile(r"(!?)\[\[([^\]|#]+)(#[^\]|]*)?(?:\|([^\]]*))?\]\]")
GEN = re.compile(r"(<!-- generated:[^\n]*-->\n)(.*?)(<!-- /generated -->)", re.S)
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.M)
BLOCK_ID = re.compile(r"(?:^|\s)\^([A-Za-z0-9-]+)\s*$", re.M)
FENCED = re.compile(r"```.*?```", re.S)
IDLIKE = re.compile(r"^[A-Z][A-Za-z]*-\d+$")
PROV = ("generator", "generated", "input-paths", "input-manifest-sha256", "managed-block-sha256")
LEVELS = {"epic": "EPIC", "feature": "FEAT", "user-story": "US"}


def refs(text: str) -> list[dict]:
    """Every wikilink, with its anchor and display text. `\\|` is a table cell's escaped pipe."""
    out = []
    for m in WIKILINK.finditer(FENCED.sub("", text).replace("\\|", "|")):
        embed, target, anchor, display = m.groups()
        out.append({"embed": bool(embed), "target": target.strip(),
                    "anchor": (anchor or "")[1:].strip(),
                    "display": (display or "").strip()})
    return out


def norm_anchor(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[#|^:\[\]]|%%", " ", text)).strip().lower()


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
        self.refs = refs(text)
        self.links = {r["target"] for r in self.refs}
        prose = FENCED.sub("", self.body)
        self.headings = {norm_anchor(h) for h in HEADING.findall(prose)}
        self.blocks = {b.lower() for b in BLOCK_ID.findall(prose)}

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
    """Every id named in a property, whether written as a wikilink or bare.

    Under the `[[stem|ID]]` convention the id is the link's *display* text, not its target, so read
    the display first and fall back to the target for a link that carries no id.
    """
    out = []
    for item in as_list(val):
        text = str(item)
        found = [(r["display"] if IDLIKE.match(r["display"]) else r["target"])
                 for r in refs(text)]
        out += found or [t for t in re.findall(r"[A-Z]+-\d+", text)]
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
    # File names and paths only. **Not `aliases`, and not `id`** — Obsidian resolves neither, so a
    # checker that accepted them would pass every bare-id citation in the vault while each one
    # opens a new empty note.
    resolvable = set(others)
    for n in notes:
        rel = str(n.rel).replace(os.sep, "/")
        resolvable |= {n.stem, rel, rel[:-3] if rel.endswith(".md") else rel}
    by_id = {n.id: n for n in notes if n.id}
    by_stem = collections.defaultdict(list)
    for n in notes:
        by_stem[n.stem].append(str(n.rel))

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
    for stem, where in sorted(by_stem.items()):
        report.require(len(where) == 1,
                       f"duplicate file name {stem}.md: {', '.join(where)} — a file name is the "
                       f"link target, so two notes cannot share one")
    for n in notes:
        for ref in n.refs:
            target = ref["target"]
            if target not in resolvable and target.rsplit("/", 1)[-1] not in resolvable:
                if target in by_id:
                    report.require(False, f"{n.rel}: [[{target}]] is a bare id, which Obsidian "
                                          f"does not resolve — write "
                                          f"[[{by_id[target].stem}|{target}]]")
                else:
                    report.require(False, f"{n.rel}: dangling wikilink [[{target}]]")
                continue
            dest = next((x for x in notes if x.stem == target.rsplit("/", 1)[-1]), None)
            if dest is None:
                continue
            if ref["anchor"]:
                anchor = ref["anchor"]
                if anchor.startswith("^"):
                    report.require(anchor[1:].lower() in dest.blocks,
                                   f"{n.rel}: [[{target}#{anchor}]] — no such block in {dest.rel}")
                else:
                    report.require(norm_anchor(anchor) in dest.headings,
                                   f"{n.rel}: [[{target}#{anchor}]] — no such heading in "
                                   f"{dest.rel}")
            shown = ref["display"]
            if shown and IDLIKE.match(shown) and dest.id and shown != dest.id:
                report.require(False, f"{n.rel}: [[{target}|{shown}]] opens {dest.rel}, whose id "
                                      f"is {dest.id}")
        if n.prop("snapshot"):
            missing = [k for k in PROV if not str(n.prop(k, ""))]
            report.require(not missing,
                           f"{n.rel}: generated note is missing {', '.join(missing)}")

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
def moc(vault: pathlib.Path, check_only: bool = False) -> tuple[list[str], list[str]]:
    """Rewrite each generated block, or (check_only) report the ones that would change.

    Returns (findings, written). A stale block is reported rather than quietly repaired: repairing
    it in silence hides a committed index that disagrees with its notes, and throws away a hand
    edit without telling anyone it existed.
    """
    notes, _ = load(vault)
    by_type = collections.defaultdict(list)
    for n in notes:
        by_type[n.type].append(n)
    by_id = {n.id: n for n in notes if n.id}
    findings, written = [], []
    for n in notes:
        spec = n.prop("snapshot")
        if not isinstance(spec, dict) or not spec.get("type"):
            continue
        kind = spec["type"]
        if kind == "coverage":
            body = _coverage_table(by_type["requirement"], by_id)
            rows = by_type["requirement"]
        else:
            rows = [x for x in by_type.get(kind, [])
                    if x.status not in as_list(spec.get("exclude-status"))]
            body = _table(rows, spec)
        text = n.path.read_text(encoding="utf-8")
        m = GEN.search(text)
        if not m:
            findings.append(f"{n.rel}: snapshot spec but no <!-- generated --> markers")
            continue
        manifest = _manifest(rows)
        if m.group(2) == body and str(n.prop("input-manifest-sha256", "")) == manifest:
            continue
        if check_only:
            why = "rows have changed" if m.group(2) != body else "inputs have changed"
            findings.append(f"{n.rel}: the generated block is stale — {why}")
            continue
        new = GEN.sub(lambda mm: f"{m.group(1)}{body}{mm.group(3)}", text, count=1)
        new = _stamp(new, {
            "generator": "prd.py moc",
            "generated": _today(),
            "input-paths": sorted({str(pathlib.PurePosixPath(r.rel).parent) + "/" for r in rows}),
            "input-manifest-sha256": manifest,
            "managed-block-sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
        })
        n.path.write_text(new, encoding="utf-8")
        written.append(f"{n.rel}: {len(rows)} rows")
    return findings, written


def render(vault: pathlib.Path, out: pathlib.Path, want_prd: str | None,
           check_only: bool = False) -> tuple[list[str], list[str]]:
    """Flatten a PRD into one readable document, with every embed resolved in place.

    The hub is the right shape inside Obsidian and unreadable outside it: `![[note]]` renders as
    nothing on GitHub, in a diff, or to an agent reading the raw file — which is most of the readers
    a PRD has. So the readable version is *derived*, never retyped: embeds are resolved from the
    notes, links are flattened to text plus id, and the result carries the hash of its inputs so a
    stale rendition is provable rather than a matter of trust.
    """
    notes, _ = load(vault)
    by_stem = {n.stem: n for n in notes}
    prds = [n for n in notes if n.type == "prd" and (not want_prd or n.id == want_prd)]
    if not prds:
        return ([f"no PRD hub note{' with id ' + want_prd if want_prd else ''}"], [])
    if len(prds) > 1:
        return ([f"{len(prds)} PRDs here; name one with --prd"], [])
    prd = prds[0]

    body = _resolve(prd.body, by_stem, depth=0)
    manifest = _manifest([n for n in notes if n.type != "moc"])
    text = (
        "<!-- generated by prd.py render — do not edit; change the notes and re-render -->\n"
        f"<!-- source: {prd.rel} · inputs: {manifest[:16]} -->\n\n"
        + _flatten(body).rstrip() + "\n")
    if check_only:
        if not out.exists():
            return ([f"{out} has not been rendered yet"], [])
        if out.read_text(encoding="utf-8") != text:
            return ([f"{out} is stale — the notes have changed since it was rendered"], [])
        return ([], [])
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    return ([], [f"{out}: {prd.id} rendered from {len(notes)} notes"])


def _resolve(text: str, by_stem: dict, depth: int) -> str:
    """Replace each `![[note]]` with that note's body, headings demoted one level."""
    if depth > 4:
        return text

    def sub(m):
        target = m.group(2).strip().rsplit("/", 1)[-1]
        note = by_stem.get(target)
        if note is None:
            return f"*[missing note: {target}]*"
        inner = re.sub(r"^(#{1,5}) ", r"#\1 ", _resolve(note.body, by_stem, depth + 1), flags=re.M)
        # An embed written mid-sentence ("**Outcomes.** ![[…]]") still resolves to a block, so it
        # needs its own line or the note's heading lands inside somebody's paragraph.
        lead = "" if m.start() == 0 or text[:m.start()].endswith("\n") else "\n\n"
        return lead + inner.strip()

    return re.sub(r"(!)\[\[([^\]\n|#]+)(?:[|#][^\]\n]*)?\]\]", sub, text)


def _flatten(text: str) -> str:
    """`[[create-a-label|R-001]]` -> `R-001`; a plain `[[stem]]` -> its words.

    A reader outside Obsidian cannot follow a wikilink, so leaving the brackets in is noise. The id
    survives, because the id is what makes the statement traceable back to its note.
    """
    def sub(m):
        target, display = m.group(2).strip(), (m.group(4) or "").strip()
        return display.replace("\\|", "|") or target.replace("-", " ")
    return re.sub(r"(!?)\[\[([^\]\n|#]+)(#[^\]\n|]*)?(?:\|([^\]\n]*))?\]\]", sub, text)


def _manifest(rows) -> str:
    """A hash over the input notes: the generated view's claim to be reproducible from them."""
    h = hashlib.sha256()
    for r in sorted(rows, key=lambda x: str(x.rel)):
        h.update(str(r.rel).encode("utf-8"))
        h.update(r.path.read_bytes())
    return h.hexdigest()


def _today() -> str:
    import datetime
    return datetime.date.today().isoformat()


def _stamp(text: str, fields: dict) -> str:
    """Set each field in the front matter, inserting what is not there yet.

    A generated note has to say what produced it, from what, and at which version of the inputs.
    Without that, "is this index current?" is answered by re-reading everything it indexes.
    """
    end = text.find("\n---", 4)
    if not text.startswith("---\n") or end == -1:
        return text
    lines = text[4:end].splitlines()
    tail = text[end:]
    for key, value in fields.items():
        rendered = ("[" + ", ".join(str(v) for v in value) + "]"
                    if isinstance(value, list) else str(value))
        line = f"{key}: {rendered}"
        for i, existing in enumerate(lines):
            if existing.split(":", 1)[0].strip() == key and not existing[:1].isspace():
                lines[i] = line
                break
        else:
            lines.append(line)
    return "---\n" + "\n".join(lines) + tail


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


def _coverage_table(requirements, by_id) -> str:
    """One row per requirement, including the cross-cutting ones. Coverage is read from each
    requirement note, so it cannot disagree with the notes the way a hand-kept table does."""
    out = ["| Requirement | Pri | Verify | Story | Coverage |", "|---|---|---|---|---|"]
    counts = collections.Counter()
    for r in sorted(requirements, key=lambda x: _idkey(x.id)):
        coverage = str(r.prop("coverage", "")) or "—"
        counts[coverage] += 1
        stories = ids_in(r.prop("stories")) or ids_in(r.prop("questions"))
        shown = " · ".join(_cite(s, by_id) for s in stories) or "None"
        out.append(f"| {_cite(r.id, by_id)} | {r.prop('priority', '—')} | "
                   f"{r.prop('verify', '—')} | {shown} | {coverage} |")
    out += ["", "**Counts.** " + " · ".join(
        f"{k}: {v}" for k, v in [("Requirements", len(requirements))] + sorted(counts.items()))]
    return "\n".join(out).rstrip() + "\n"


def _cite(ident: str, by_id) -> str:
    """An id as a link Obsidian can resolve: the file name, with the id as display text.

    The pipe is escaped because every caller writes into a table cell. A generator that emitted
    `[[R-001]]` would plant the one link form Obsidian cannot follow, once per row.
    """
    note = by_id.get(ident)
    return f"[[{note.stem}\\|{ident}]]" if note else ident


def _header(column: str) -> str:
    return "ID" if column == "id" else column.replace("-", " ").capitalize()


def _cell(note: Note, column: str) -> str:
    if column == "title":
        return re.sub(r"\s+", " ", note.title.replace("|", "\\|")).strip()
    if column == "id":
        return f"[[{note.stem}\\|{note.id}]]" if note.id else f"[[{note.stem}]]"
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
    parser.add_argument("command", choices=("check", "moc", "render"))
    parser.add_argument("vault", type=pathlib.Path)
    parser.add_argument("--prd", help="check only this PRD id, e.g. PRD-001")
    parser.add_argument("--source", action="append", default=[], metavar="SRC-NN=path",
                        help="check SRC-NN @time and Lnn locators against this text file")
    parser.add_argument("--check", action="store_true",
                        help="moc: write nothing and fail if a generated block is stale")
    parser.add_argument("--baseline", metavar="FILE",
                        help="check: report only errors absent from an earlier run's output")
    parser.add_argument("--out", type=pathlib.Path,
                        help="render: where the readable document goes")
    args = parser.parse_args()
    if not args.vault.is_dir():
        parser.error(f"not a directory: {args.vault}")

    if args.command == "render":
        out = args.out or (args.vault / "render" / "prd.md")
        problems, written = render(args.vault.resolve(), out, args.prd, args.check)
        for line in written:
            print(line)
        for line in problems:
            print(f"  {line}")
        if not problems and args.check:
            print("ok — the rendered document matches the notes")
        return 1 if problems else 0

    if args.command == "moc":
        problems, lines = moc(args.vault.resolve(), args.check)
        for line in lines:
            print(line)
        for line in problems:
            print(f"  {line}")
        if problems:
            print(f"{len(problems)} findings")
        elif args.check:
            print("ok — every generated block is current")
        elif not lines:
            print("no changes")
        return 1 if problems else 0

    sources = {}
    for item in args.source:
        if "=" not in item:
            parser.error(f"--source needs SRC-NN=path, got {item}")
        sid, path = item.split("=", 1)
        sources[sid] = path

    report = Report()
    summary = check(args.vault.resolve(), report, args.prd, sources)
    if args.baseline:
        # Judge a change by what it broke. The first run on an adopted vault reports everything at
        # once, and a list nobody has time to read is a checker nobody runs.
        known = {line.strip().lstrip("- ").strip()
                 for line in pathlib.Path(args.baseline).read_text(encoding="utf-8").splitlines()
                 if line.strip()}
        report.errors = [e for e in report.errors if e not in known]
        report.warnings = [w for w in report.warnings if w not in known]
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
