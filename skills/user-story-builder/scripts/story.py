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

The notes, links, front matter and generated-block machinery live in `vaultlib.py` beside this
file, shared byte-for-byte with the other skills' checkers. This script holds what is specific to a
story. It deliberately does not re-check what is already checked: links across a whole vault,
anchors and orphans are vault-wide properties that `anchored-knowledge`'s `vault.py lint` and
`agentic-prd`'s `prd.py check` cover, and the repo's `check-vault-tools.py` runs both over a
composed vault holding these story notes.
"""
from __future__ import annotations

import argparse
import collections
import pathlib
import re
import sys

import vaultlib
from vaultlib import (GEN, IDLIKE, Note, Report, as_list, check_shape, ids_in, load, new_only,
                      refs)

TAX = vaultlib.Taxonomy(__file__)
TYPES = TAX.types
MODES = ("A", "B", "C")
# The eight labels, in order. There is no `**Tags**`: it restated `parent` and `priority`, which
# the publish step reads from front matter.
LABELS = ("**Expected Output**", "**Details**", "**Assumptions**", "**Testing Strategy**",
          "**Open Questions**", "**Technical Notes**", "**Acceptance Criteria**")
FORBIDDEN_LABELS = ("**Tags**",)
CRITERION = re.compile(r"^\s*(\d+)\.\s*AC-(\d+)\s*\[([^\]]*)\]\s*(.*)$", re.M)
GIVEN_WHEN_THEN = re.compile(r"\bGiven\b.*?\bwhen\b.*?\bthen\b", re.S | re.I)
GROUNDING = re.compile(r"^- Source grounding: *(.+?)(?:\.\s|\.$|$)", re.M | re.S)


# ---------------------------------------------------------------------------- #
# Checks
# ---------------------------------------------------------------------------- #
def check(vault: pathlib.Path, report: Report, knowledge: pathlib.Path | None) -> list[str]:
    notes, others = load(vault)
    reachable = dict()
    for n in notes:
        for key in vaultlib.link_targets(n):
            reachable.setdefault(key, n)
    # The record vault, when it was given. A Mode A story cites rule and decision ids that live
    # there, and a backlog on its own cannot tell a missing note from an uninstalled vault.
    external = set(others)
    if knowledge:
        extra, extra_others = load(knowledge)
        external |= extra_others
        for n in extra:
            external |= vaultlib.link_targets(n)

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
        check_shape(n, TAX, report.require)
        check_links(n, report, reachable, external, by_id)
    for n in stories:
        check_story(n, report, reachable, external)
    modes = collections.Counter(str(n.prop("source-mode", "")) for n in stories)
    published = sum(1 for n in stories if n.status == "published")
    return [f"Stories: {len(stories)}", f"Published: {published}",
            "Modes: " + (" ".join(f"{k or '—'}:{v}" for k, v in sorted(modes.items())) or "—")]


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
        body = vaultlib.table(rows, spec)
        text = n.path.read_text(encoding="utf-8")
        m = GEN.search(text)
        if not m:
            findings.append(f"{n.rel}: snapshot spec but no <!-- generated --> markers")
            continue
        manifest = vaultlib.manifest(rows)
        if m.group(2) == body and str(n.prop("input-manifest-sha256", "")) == manifest:
            continue
        if check_only:
            why = "rows have changed" if m.group(2) != body else "inputs have changed"
            findings.append(f"{n.rel}: the generated block is stale — {why}")
            continue
        new = GEN.sub(lambda mm: f"{m.group(1)}{body}{mm.group(3)}", text, count=1)
        new = vaultlib.stamp(new, vaultlib.provenance("story.py moc", rows, body))
        n.path.write_text(new, encoding="utf-8")
        written.append(f"{n.rel}: {len(rows)} rows")
    return findings, written + skipped


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
    errors = new_only(report.errors, args.baseline)
    warnings = new_only(report.warnings, args.baseline)
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
