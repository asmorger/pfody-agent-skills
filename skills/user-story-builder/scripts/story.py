#!/usr/bin/env python3
"""Check a backlog of user story notes, and regenerate its index snapshot.

    python3 scripts/story.py check <vault> [--knowledge DIR] [--baseline FILE]
    python3 scripts/story.py moc   <vault> [--check]

`check` holds a story to the shape this skill promises: the eight labels in order, one source tag
per criterion, `sources` and the `Source grounding:` line agreeing, a `parent` that resolves, a
source mode that matches what the note actually cites, and the publish state consistent with
`tracker-id`. `moc` rewrites the generated table in `moc/backlog.md` and stamps its provenance, so
"is this index current?" has a mechanical answer instead of a hand-kept table nobody re-reads.

`--knowledge DIR` adds the record vault, so a Mode A story's `sources` can be resolved. Without it,
a citation to a note that is not here is a **warning**, not an error: a backlog on its own genuinely
cannot verify a citation into a knowledge base it was not given. A **bare id** citation is an error
either way, because that is a fact about the link's form — `[[LABEL-2]]` opens a new empty note
whatever else is installed, and the alias it looks like it resolves through is never consulted.

Exit code 0 means no errors; warnings do not fail the check. Standard library only, Python 3.10+.

This script deliberately does not re-check what is already checked. Links across a whole vault,
anchors, orphans and the generated-block hash are vault-wide properties that `anchored-knowledge`'s
`vault.py lint` and `agentic-prd`'s `prd.py check` already cover, and the repo's
`check-vault-tools.py` runs both over a composed vault holding these story notes. What is here is
what is specific to a story.
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

UNLIMITED = 10 ** 6


def _taxonomy():
    """The note taxonomy, read from this skill's copy of the shared registry.

    Byte-identical to `shared/vault-taxonomy.json`, verified by the repo's `check-taxonomy.py`, and
    carried inside the skill so the skill installs on its own.
    """
    here = pathlib.Path(__file__).resolve()
    for path in (here.parent.parent / "references" / "vault-taxonomy.json",
                 here.parents[3] / "shared" / "vault-taxonomy.json"):
        if path.is_file():
            return json.loads(path.read_text(encoding="utf-8"))
    sys.exit("story.py: references/vault-taxonomy.json is missing — copy it from the skill folder")


TAXONOMY = _taxonomy()
TYPES = TAXONOMY["types"]
STORY = TYPES["user-story"]
MODES = ("A", "B", "C")
# The eight labels, in order. There is no `**Tags**`: it restated `parent` and `priority`, which the
# publish step reads from front matter
# ([`../anti-patterns/...`] — see agentic-prd's a-tags-label-restating-the-parent.md).
LABELS = ("**Expected Output**", "**Details**", "**Assumptions**", "**Testing Strategy**",
          "**Open Questions**", "**Technical Notes**", "**Acceptance Criteria**")
FORBIDDEN_LABELS = ("**Tags**",)
WIKILINK = re.compile(r"(!?)\[\[([^\]|#]+)(#[^\]|]*)?(?:\|([^\]]*))?\]\]")
FENCED = re.compile(r"```.*?```", re.S)
IDLIKE = re.compile(r"^[A-Z][A-Za-z]*-\d+$")
GEN = re.compile(r"(<!-- generated:[^\n]*-->\n)(.*?)(<!-- /generated -->)", re.S)
CRITERION = re.compile(r"^\s*(\d+)\.\s*AC-(\d+)\s*\[([^\]]*)\]\s*(.*)$", re.M)
GIVEN_WHEN_THEN = re.compile(r"\bGiven\b.*?\bwhen\b.*?\bthen\b", re.S | re.I)
GROUNDING = re.compile(r"^- Source grounding: *(.+?)(?:\.\s|\.$|$)", re.M | re.S)
PROV = ("generator", "generated", "input-paths", "input-manifest-sha256", "managed-block-sha256")


# ---------------------------------------------------------------------------- #
# Notes
# ---------------------------------------------------------------------------- #
class Note:
    def __init__(self, path: pathlib.Path, root: pathlib.Path):
        self.path, self.rel = path, path.relative_to(root)
        text = path.read_text(encoding="utf-8")
        self.has_fm = text.startswith("---\n")
        self.meta, self.body = split_front_matter(text)
        self.id = str(self.meta.get("id", "") or "")
        self.type = str(self.meta.get("type", "") or "")
        self.status = str(self.meta.get("status", "") or "")
        self.stem = path.stem
        self.aliases = as_list(self.meta.get("aliases"))
        self.refs = refs(text)

    def prop(self, key, default=""):
        return self.meta.get(key, default)

    @property
    def title(self) -> str:
        for line in self.body.splitlines():
            if line.startswith("# "):
                head = line[2:].strip()
                if self.id and head.startswith(self.id):
                    head = head[len(self.id):].lstrip(" -—–:")
                return head or self.stem.replace("-", " ")
        return self.stem.replace("-", " ")


def refs(text: str) -> list[dict]:
    """Every wikilink, with its display text. `\\|` is a table cell's escaped pipe."""
    out = []
    for m in WIKILINK.finditer(FENCED.sub("", text).replace("\\|", "|")):
        _, target, _, display = m.groups()
        out.append({"target": target.strip(), "display": (display or "").strip()})
    return out


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
    """Every id named in a property, read from the wikilink's display text under `[[stem|ID]]`."""
    out = []
    for item in as_list(val):
        text = str(item)
        found = [(r["display"] if IDLIKE.match(r["display"]) else r["target"]) for r in refs(text)]
        out += found or [t for t in re.findall(r"[A-Z][A-Za-z]*-\d+", text)]
    return out


def load(root: pathlib.Path):
    """Notes, plus every other file name a wikilink may legitimately reach."""
    notes, others = [], set()
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for name in sorted(filenames):
            path = pathlib.Path(dirpath) / name
            if name.endswith(".md"):
                note = Note(path, root)
                if note.has_fm:
                    notes.append(note)
                else:
                    others.update({name, path.stem})
            elif not name.startswith("."):
                others.update({name, path.stem})
    return notes, others


class Report:
    def __init__(self):
        self.errors, self.warnings, self.checks = [], [], 0

    def require(self, ok, message) -> bool:
        self.checks += 1
        if not ok:
            self.errors.append(message)
        return bool(ok)

    def warn(self, message):
        self.warnings.append(message)


# ---------------------------------------------------------------------------- #
# Checks
# ---------------------------------------------------------------------------- #
def check(vault: pathlib.Path, report: Report, knowledge: pathlib.Path | None) -> list[str]:
    notes, others = load(vault)
    reachable = dict()
    for n in notes:
        rel = str(n.rel).replace(os.sep, "/")
        for key in (n.stem, rel, rel[:-3] if rel.endswith(".md") else rel):
            reachable.setdefault(key, n)
    # The record vault, when it was given. A Mode A story cites rule and decision ids that live
    # there, and a backlog on its own cannot tell a missing note from an uninstalled vault.
    external = set(others)
    if knowledge:
        extra, extra_others = load(knowledge)
        external |= extra_others
        for n in extra:
            rel = str(n.rel).replace(os.sep, "/")
            external |= {n.stem, rel, rel[:-3] if rel.endswith(".md") else rel}
            for ident in ([n.id] if n.id else []):
                reachable.setdefault(ident + "\0id", n)

    by_id = {n.id: n for n in notes if n.id}
    by_stem = collections.defaultdict(list)
    for n in notes:
        by_stem[n.stem].append(str(n.rel))
    for stem, where in sorted(by_stem.items()):
        report.require(len(where) == 1,
                       f"duplicate file name {stem}.md: {', '.join(where)} — a file name is the "
                       f"link target, so two notes cannot share one")
    seen = collections.defaultdict(list)
    for n in notes:
        if n.id:
            seen[n.id].append(str(n.rel))
    for ident, where in sorted(seen.items()):
        report.require(len(where) == 1, f"duplicate id {ident}: {', '.join(where)}")

    stories = [n for n in notes if n.type == "user-story"]
    report.require(bool(stories), "no story notes found (a note with `type: user-story`)")
    for n in notes:
        check_shape(n, report)
        check_links(n, report, reachable, external, by_id)
    for n in stories:
        check_story(n, report, reachable, external)
    modes = collections.Counter(str(n.prop("source-mode", "")) for n in stories)
    published = sum(1 for n in stories if n.status == "published")
    return [f"Stories: {len(stories)}", f"Published: {published}",
            "Modes: " + (" ".join(f"{k or '—'}:{v}" for k, v in sorted(modes.items())) or "—")]


def check_shape(n: Note, report: Report) -> None:
    """What the shared taxonomy promises about any note, whichever skill wrote it."""
    if not n.type:
        report.require(False, f"{n.rel}: no type")
        return
    if n.type not in TYPES:
        report.require(False, f"{n.rel}: unknown type '{n.type}'")
        return
    spec = TYPES[n.type]
    if n.status:
        report.require(n.status in spec["status"],
                       f"{n.rel}: status '{n.status}' is not valid for '{n.type}' "
                       f"({' | '.join(spec['status']) or 'this type has no status'})")
    pattern = spec["id"]
    if pattern:
        report.require(bool(n.id) and bool(re.fullmatch(pattern, n.id)),
                       f"{n.rel}: id {n.id or '(none)'!r} does not match the {n.type} pattern "
                       f"{pattern}")
    elif n.id:
        report.require(False, f"{n.rel}: a '{n.type}' is cited by file name and carries no id, "
                              f"but this one has id '{n.id}'")
    if n.id:
        report.require(n.id in n.aliases, f"{n.rel}: id '{n.id}' is not in aliases")
    key = spec["group-by"]
    if key:
        report.require(bool(str(n.prop(key, "")).strip()),
                       f"{n.rel}: no '{key}' — a '{n.type}' is grouped by it, and there is no "
                       f"`tags` property to fall back on")
    limit = UNLIMITED if spec["body-budget"] is None else spec["body-budget"]
    lines = len([l for l in n.body.splitlines() if l.strip()])
    report.require(lines <= limit, f"{n.rel}: body is {lines} lines, budget {limit}")


def check_links(n: Note, report: Report, reachable: dict, external: set, by_id: dict) -> None:
    """The one link rule that holds whatever else is installed."""
    for ref in n.refs:
        target = ref["target"]
        last = target.rsplit("/", 1)[-1]
        here = reachable.get(target) or reachable.get(last)
        if here is None and target not in external and last not in external:
            if target in by_id:
                report.require(False, f"{n.rel}: [[{target}]] is a bare id, which Obsidian does "
                                      f"not resolve — write [[{by_id[target].stem}|{target}]]")
            elif IDLIKE.match(target):
                # A bare id is wrong whether or not the note it names is installed: Obsidian never
                # resolves a wikilink through `aliases`, so this opens a new empty note.
                report.require(False, f"{n.rel}: [[{target}]] is a bare id, which Obsidian does "
                                      f"not resolve — write [[<file-name>|{target}]]")
            else:
                report.warn(f"{n.rel}: [[{target}]] is not in this backlog — pass --knowledge "
                            f"<dir> if it lives in the record vault")
            continue
        shown = ref["display"]
        if here is not None and shown and IDLIKE.match(shown) and here.id and shown != here.id:
            report.require(False, f"{n.rel}: [[{target}|{shown}]] opens {here.rel}, whose id is "
                                  f"{here.id}")


def check_story(n: Note, report: Report, reachable: dict, external: set) -> None:
    body = n.body
    # ---- the labels, in order
    found = [(body.index(lbl), lbl) for lbl in LABELS if lbl in body]
    missing = [lbl for lbl in LABELS if lbl not in body]
    report.require(not missing, f"{n.id}: missing story labels: {', '.join(missing)}")
    if not missing:
        report.require([lbl for _, lbl in sorted(found)] == list(LABELS),
                       f"{n.id}: the labels are out of order — a publishing adapter maps them "
                       f"positionally")
    for lbl in FORBIDDEN_LABELS:
        report.require(lbl not in body,
                       f"{n.id}: {lbl} restates `parent` and `priority`, which the publish step "
                       f"reads from front matter — drop the label")

    # ---- mode honesty
    mode = str(n.prop("source-mode", "")).strip()
    report.require(mode in MODES,
                   f"{n.id}: source-mode {mode or '(none)'!r} is not one of {' | '.join(MODES)} — "
                   f"a mode nobody can query is a sentence somebody wrote once")
    sources = ids_in(n.prop("sources"))
    if mode == "A":
        report.require(bool(sources),
                       f"{n.id}: source-mode A claims a sourced corpus but `sources` is empty")
    if mode == "C":
        report.require(not sources,
                       f"{n.id}: source-mode C means nothing but what the user asked for, yet "
                       f"`sources` names {', '.join(sources)}")

    # ---- `sources` and the Source grounding line say the same thing, which is the one duplication
    # the shape allows. Allowed only because they are checked against each other.
    grounding = GROUNDING.search(body)
    if sources:
        if report.require(grounding is not None,
                          f"{n.id}: `sources` is set but the Details label has no "
                          f"`- Source grounding:` line, which is what the tracker receives"):
            shown = ids_in(grounding.group(1))
            report.require(set(shown) == set(sources),
                           f"{n.id}: `sources` is {sorted(sources)} but Source grounding names "
                           f"{sorted(shown)} — one of them is out of date")

    # ---- acceptance criteria
    criteria = CRITERION.findall(body)
    report.require(bool(criteria), f"{n.id}: no acceptance criterion in the "
                                   f"`AC-n [tag] Given … when … then …` form")
    for index, (number, ac, tag, rest) in enumerate(criteria, start=1):
        label = f"{n.id} AC-{ac}"
        report.require(int(number) == index and int(ac) == index,
                       f"{label}: numbered {number}/AC-{ac} but is criterion {index} — numbering "
                       f"restarts at 1 in each story and does not skip")
        report.require(bool(tag.strip()),
                       f"{label}: empty source tag. Every criterion traces to a named source")
        report.require("[[" not in tag,
                       f"{label}: the source tag is a wikilink. It stays a bare id — it is sent to "
                       f"the tracker verbatim")
        report.require(len(tag.split(",")) == 1,
                       f"{label}: {len(tag.split(','))} ids in one tag. One tag per criterion")
        report.require(GIVEN_WHEN_THEN.search(rest) is not None,
                       f"{label}: not in Given … when … then … form, so it is not testable")
        if mode == "C":
            report.require(not IDLIKE.match(tag.strip()),
                           f"{label}: source-mode C has no source ids to cite, yet the tag is "
                           f"{tag.strip()!r}")
        elif sources:
            report.require(tag.strip() in sources or not IDLIKE.match(tag.strip()),
                           f"{label}: cites {tag.strip()!r}, which is not in this story's "
                           f"`sources`")

    # ---- parentage, copied and never invented
    parent = ids_in(n.prop("parent"))
    report.require(len(parent) <= 1, f"{n.id}: more than one parent")
    if parent:
        target = (refs(str(n.prop("parent"))) or [{"target": ""}])[0]["target"]
        last = target.rsplit("/", 1)[-1]
        known = (reachable.get(target) or reachable.get(last)
                 or target in external or last in external)
        if target and not known:
            report.warn(f"{n.id}: parent {parent[0]} is not in this backlog — pass --knowledge "
                        f"<dir> if the Feature lives beside the PRD")

    # ---- the publish state, which is the point of `tracker-id`
    tracker = str(n.prop("tracker-id", "")).strip()
    url = str(n.prop("tracker-url", "")).strip()
    if n.status == "published":
        report.require(bool(tracker), f"{n.id}: status is published but `tracker-id` is empty — a "
                                      f"later run would create a duplicate instead of updating")
        report.require(bool(url), f"{n.id}: status is published but `tracker-url` is empty, so a "
                                  f"reviewer in the tracker cannot get back to the sourced note")
    else:
        report.require(not tracker,
                       f"{n.id}: `tracker-id` is {tracker!r} but status is {n.status!r} — a "
                       f"published story says so, or 'what is still unpublished?' stops being a "
                       f"query")
    report.require(str(n.prop("review-required", "")) != "",
                   f"{n.id}: no `review-required` — whether a person still has to read it is not "
                   f"something to infer")


# ---------------------------------------------------------------------------- #
# The index
# ---------------------------------------------------------------------------- #
def moc(vault: pathlib.Path, check_only: bool = False) -> tuple[list[str], list[str]]:
    """Rewrite each generated block, or (check_only) report the ones that would change.

    A stale block is reported rather than quietly repaired. Repairing it in silence hides a
    committed index that disagrees with its notes and discards a hand edit without saying so. This
    file used to be the one generated block in the repo with no generator behind it, so it carried
    no provenance and nothing could answer "is this current?".
    """
    notes, _ = load(vault)
    by_type = collections.defaultdict(list)
    for n in notes:
        by_type[n.type].append(n)
    findings, written, skipped = [], [], []
    for n in notes:
        spec = n.prop("snapshot")
        if not isinstance(spec, dict) or not spec.get("type"):
            continue
        # This generator owns the story index and nothing else. `agentic-prd`'s coverage table and
        # its grouped requirement views are built from notes this skill does not write, so
        # rebuilding them here would produce a wrong table confidently. Leaving them alone is what
        # lets the two tools share a vault: on a `user-story` snapshot they agree byte for byte,
        # and outside it each one keeps its own.
        if spec["type"] != "user-story" or spec.get("group-by"):
            skipped.append(f"{n.rel}: not a story snapshot — `prd.py moc` owns it")
            continue
        rows = [x for x in by_type.get(spec["type"], [])
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
            "generator": "story.py moc",
            "generated": _today(),
            "input-paths": sorted({str(pathlib.PurePosixPath(r.rel).parent) + "/" for r in rows}),
            "input-manifest-sha256": manifest,
            "managed-block-sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
        })
        n.path.write_text(new, encoding="utf-8")
        written.append(f"{n.rel}: {len(rows)} rows")
    return findings, written + skipped


def _table(rows, spec) -> str:
    columns = as_list(spec.get("columns")) or ["id", "title", "status"]
    out = ["| " + " | ".join(_header(c) for c in columns) + " |", "|" + "---|" * len(columns)]
    for r in sorted(rows, key=lambda x: _idkey(x.id)):
        out.append("| " + " | ".join(_cell(r, c) for c in columns) + " |")
    return "\n".join(out).rstrip() + "\n"


def _header(column: str) -> str:
    return "ID" if column == "id" else column.replace("-", " ").capitalize()


def _cell(note: Note, column: str) -> str:
    """Byte-for-byte what `agentic-prd`'s `prd.py moc` writes for the same column.

    `moc/backlog.md` has two possible owners — this skill writes stories, and `agentic-prd` writes
    them too when a whole backlog is decomposed at once — so a project with both installed must not
    get a different index depending on which tool last ran. The repo's `check-vault-tools.py`
    asserts each generator reports the other's block as current.
    """
    if column == "title":
        return re.sub(r"\s+", " ", note.title.replace("|", "\\|")).strip()
    if column == "id":
        # The file name as target, the id as display text. A generator that emitted `[[US-03]]`
        # would plant the one link form Obsidian cannot follow, once per row.
        return f"[[{note.stem}\\|{note.id}]]" if note.id else f"[[{note.stem}]]"
    value = note.prop(column, "")
    if isinstance(value, list):
        return " · ".join(str(v) for v in value) or "—"
    return str(value).replace("|", "\\|") or "—"


def _idkey(ident: str):
    m = re.match(r"([A-Za-z]+)-(\d+)", ident or "")
    return (m.group(1), int(m.group(2))) if m else (ident or "", 0)


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
    """Set each field in the front matter, inserting what is not there yet."""
    end = text.find("\n---", 4)
    if not text.startswith("---\n") or end == -1:
        return text
    lines, tail = text[4:end].splitlines(), text[end:]
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


def _new_only(findings: list[str], baseline: pathlib.Path | None) -> list[str]:
    """Only what is not already in the baseline, so a change is judged by what it broke."""
    if not baseline or not baseline.exists():
        return findings
    known = {l.strip() for l in baseline.read_text(encoding="utf-8").splitlines() if l.strip()}
    return [f for f in findings if f.strip() not in known]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="command", required=True)
    c = sub.add_parser("check", help="hold every story to the shape this skill promises")
    c.add_argument("vault", type=pathlib.Path)
    c.add_argument("--knowledge", type=pathlib.Path,
                   help="the record vault, so a Mode A story's sources resolve")
    c.add_argument("--baseline", type=pathlib.Path,
                   help="an earlier run's output; report only what a change broke")
    m = sub.add_parser("moc", help="rewrite the generated index table and stamp its provenance")
    m.add_argument("vault", type=pathlib.Path)
    m.add_argument("--check", action="store_true", help="write nothing; fail on a stale block")
    args = ap.parse_args()

    if args.command == "moc":
        findings, written = moc(args.vault.resolve(), args.check)
        for line in written:
            print(line)
        for line in findings:
            print(f"  {line}")
        if findings:
            print(f"{len(findings)} findings")
        elif args.check:
            print("ok — every generated block is current")
        return 1 if findings else 0

    report = Report()
    summary = check(args.vault.resolve(), report, args.knowledge.resolve()
                    if args.knowledge else None)
    errors = _new_only(report.errors, args.baseline)
    warnings = _new_only(report.warnings, args.baseline)
    print(" | ".join(summary))
    for e in errors:
        print(f"ERROR   {e}")
    for w in warnings:
        print(f"WARN    {w}")
    print(f"Checks: {report.checks}. Errors: {len(errors)}. Warnings: {len(warnings)}.")
    print("This found structure, never meaning. It cannot tell whether a source supports the "
          "criterion that cites it.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
