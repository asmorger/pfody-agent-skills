"""Check a slicing workspace: surveys that observe, briefs that decide, and the seam between them.

    python3 <skill-folder>/scripts/slice.py check   <workspace>
    python3 <skill-folder>/scripts/slice.py signals <workspace>

`check` reports the defect class that is invisible to reading. A brief frozen with decisions still
outstanding passes every human review, because the gate it failed is one line forty lines below the
rulings. A ruling citing a behaviour id no survey defines looks identical to one that resolves. A
`CHANGE` with no `new/` check reads as complete, and the check that would have caught the change is
the one nobody wrote. Each of those is mechanical to detect and none of them is visible by eye,
which is the only reason this script exists.

`signals` prints the two numbers the practice is held to: surveys outstanding and checks accumulated.
They are the difference between a delivery practice and a documentation practice, and a project that
never looks at them will not notice becoming the second one.

**What this cannot do.** It cannot tell whether a provenance tag is honest, whether a golden master
was really recorded from the running system rather than written from the survey, whether a slice is a
sound slice, or whether a deferral's stated reason is true. Those are the four ways this practice
actually fails, and all four are a person's to judge. Reporting a pass without saying so transfers
confidence the script never earned.

Standard library only, Python 3.10+. Exit code 1 on any error; warnings alone exit 0.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

import vaultlib as V

# A behaviour line in a survey: `B01  A label is created only for a confirmed order.`
BEHAVIOUR = re.compile(r"^(B\d+)\b\s*(.*)$")
# A provenance tag, anywhere in a behaviour's block of lines.
TAG = re.compile(r"\[(code|db|logs|told|assumed)\s*:([^\]]*)\]")
# A ruling row: `B02 reprint leaves two     CHANGE  void the superseded one`
VERBS = ("KEEP", "CHANGE", "DROP", "DEFER")
RULING = re.compile(r"^(B\d+)\b(.*?)\b(" + "|".join(VERBS) + r")\b(.*)$")
# `[survey B02 · PM 11-11]`, with any of the separators a human might type.
CITE = re.compile(r"\[survey\s+(B\d+)\s*[·|,:-]\s*([^\]]*)\]")
COUNT = re.compile(r"^##\s*Decisions outstanding:\s*(\d+)\s*$", re.M)
# Wording that claims nothing *references* a thing. These are the findings worth most and the
# easiest to get wrong, and the only ones that need a sweep rather than a measurement — a `[logs:]`
# claim that a behaviour never fires is evidence of a different kind, so "never" is deliberately not
# here. Narrow on purpose: a check that fires on a correct line teaches people to ignore it.
ABSENCE = re.compile(r"\b(nowhere|unused|not referenced|referenced by nothing)\b", re.I)
EXHAUSTIVE = re.compile(r"exhaustive", re.I)


def section(body: str, name: str) -> str:
    """One `## Heading` section's text, or empty. Fenced blocks are left in; nothing nests here."""
    m = re.search(rf"^##\s*{re.escape(name)}\s*$\n(.*?)(?=^##\s|\Z)", body, re.M | re.S)
    return m.group(1) if m else ""


def blocks(text: str, head: re.Pattern):
    """Group lines into (match, whole block) pairs: a head line plus its continuation lines."""
    out, current, buf = [], None, []
    for line in text.splitlines():
        m = head.match(line)
        if m:
            if current:
                out.append((current, "\n".join(buf)))
            current, buf = m, [line]
        elif current is not None:
            if line.startswith("#") or (not line.strip() and buf and not buf[-1].strip()):
                out.append((current, "\n".join(buf)))
                current, buf = None, []
            else:
                buf.append(line)
    if current:
        out.append((current, "\n".join(buf)))
    return out


def check_survey(note: V.Note, rep: V.Report) -> set[str]:
    """A survey observes. Returns the behaviour ids it defines, for the briefs to cite."""
    defined, seen = set(), {}
    for m, block in blocks(note.body, BEHAVIOUR):
        bid, rest = m.group(1), m.group(2)
        defined.add(bid)
        rep.require(bid not in seen,
                    f"{note.rel}: behaviour id {bid} is defined twice — ids are cited by briefs "
                    f"and must never be reused")
        seen[bid] = True
        tags = TAG.findall(block)
        if not rep.require(bool(tags),
                           f"{note.rel}: {bid} has no provenance tag — an untagged line is not an "
                           f"observation, and a reader cannot tell it from a guess"):
            continue
        kinds = {k for k, _ in tags}
        # An absence claim is the one kind a ranked search cannot support.
        if ABSENCE.search(rest + " " + block) and not EXHAUSTIVE.search(block):
            rep.warn(f"{note.rel}: {bid} claims an absence but no tag says the sweep was "
                     f"exhaustive — name the corpora swept, or soften the claim")
        for kind, value in tags:
            if kind == "told" and not re.search(r"\d", value):
                rep.warn(f"{note.rel}: {bid} is tagged [told:] with no date — "
                         f"'{value.strip()}' is unfalsifiable in six months")
            if kind == "logs" and not re.search(r"\d", value):
                rep.warn(f"{note.rel}: {bid} is tagged [logs:] with no number")
        if "assumed" in kinds and not re.search(r"\b(appears?|suspect|think|may|could)\b", block, re.I):
            rep.warn(f"{note.rel}: {bid} is tagged [assumed:] but reads as fact — the tag governs "
                     f"the verb")
    rep.require(bool(defined), f"{note.rel}: no behaviour lines — a survey with nothing observed "
                               f"is not yet a survey")
    rep.require(note.status != "replaced",
                f"{note.rel}: status is 'replaced' but the file is still here — replaced means "
                f"deleted, and a prose copy beside the suite is how the two start disagreeing")
    return defined


def check_brief(note: V.Note, rep: V.Report):
    """A brief decides. Returns nothing; everything it learns is reported."""
    body = note.body
    rulings = section(body, "Keep / change / drop")
    checks = section(body, "Checks")

    # The gate. One line, forty lines below the rulings, which is why nobody sees it.
    found = COUNT.search(body)
    if note.status in ("frozen", "flipped"):
        if rep.require(bool(found), f"{note.rel}: status is '{note.status}' but there is no "
                                    f"'## Decisions outstanding:' line — the gate is unstated"):
            rep.require(found.group(1) == "0",
                        f"{note.rel}: status is '{note.status}' but Decisions outstanding reads "
                        f"{found.group(1)} — building started on an unready slice")
        rep.require(bool(str(note.prop(note.status, "")).strip()),
                    f"{note.rel}: status is '{note.status}' but no '{note.status}:' date — the "
                    f"transition is an event, not a mood")

    changed, deferred, cited = set(), 0, {}
    for m, block in blocks(rulings, RULING):
        bid, verb, tail = m.group(1), m.group(3), m.group(4)
        whole = block
        cite = CITE.search(whole)
        if not rep.require(bool(cite),
                          f"{note.rel}: ruling {bid} {verb} cites no survey line — a row without "
                          f"'[survey {bid} ... ]' cannot be traced to anything observed"):
            continue
        cited[bid] = cite.group(1)
        who = cite.group(2).strip()
        rep.require(bool(who), f"{note.rel}: ruling {bid} {verb} names no decider — somebody will "
                               f"ask why the system behaves this way")
        if verb != "DEFER":
            rep.require(bool(re.search(r"\d", who)),
                        f"{note.rel}: ruling {bid} {verb} has no date against its decider")
        # The reason sits between the verb and the citation.
        reason = TAG.sub("", CITE.sub("", whole)).replace(bid, "", 1)
        reason = re.sub(r"\b" + verb + r"\b", "", reason, count=1).strip()
        if verb == "DEFER":
            deferred += 1
            rep.require(len(reason) > len(m.group(2).strip()) + 3,
                        f"{note.rel}: ruling {bid} DEFER gives no reason — a deferral says why it "
                        f"is safe to leave open, or it is a dependency wearing a deferral's label")
        # A DROP alters behaviour exactly as much as a CHANGE does — "stop writing the row" needs
        # a check that it stopped. Only KEEP and DEFER leave the old behaviour in place, and KEEP
        # is covered by the golden master, which is what recording one is for.
        if verb in ("CHANGE", "DROP"):
            changed.add(bid)

    if deferred > 3:
        rep.warn(f"{note.rel}: {deferred} deferrals in one slice — the area may not be understood "
                 f"well enough to slice, and another survey pass is the honest move")

    # Every CHANGE needs its own new/ check, and every new/ check needs a CHANGE behind it.
    new_checks = re.findall(r"^\s*(new/\S+)", checks, re.M)
    rep.require(bool(re.search(r"^\s*char/", checks, re.M)),
                f"{note.rel}: no 'char/' check — without a golden master recorded from the old "
                f"system there is nothing for the new code to be wrong against")
    if changed:
        rep.require(len(new_checks) >= len(changed),
                    f"{note.rel}: {len(changed)} CHANGE/DROP rulings but {len(new_checks)} 'new/' "
                    f"checks — a changed behaviour with no check is a change nobody verifies")
    elif new_checks:
        rep.require(False, f"{note.rel}: {len(new_checks)} 'new/' checks but no CHANGE or DROP "
                           f"ruling — scope arrived without a decision behind it")

    par = re.search(r"^\s*parallel-run\b(.*?)(?=^\S|\Z)", checks, re.M | re.S)
    if rep.require(bool(par), f"{note.rel}: no 'parallel-run' entry — the flip has no evidence "
                              f"from real traffic behind it"):
        rep.require(bool(re.search(r"\d", par.group(1))),
                    f"{note.rel}: the parallel-run entry names no threshold and no volume — "
                    f"'looks fine' is not a criterion and a clean diff over four runs proves "
                    f"nothing")

    blast = str(note.prop("blast", ""))
    if not re.search(r"\bno\b", blast, re.I):
        rep.warn(f"{note.rel}: 'blast:' does not say what the slice leaves alone — a radius "
                 f"written as negatives is the only kind a reviewer can argue with")
    rep.require(bool(str(note.prop("demo", "")).strip()),
                f"{note.rel}: no 'demo:' — a slice with no demo sentence has no agreed outcome, "
                f"and nothing to show at the flip")
    # Whether the demo sentence is really one slice is a judgement, left to the Done-when in
    # `practices/shape-a-slice.md`. Flagging every `and` would fire on correct sentences, and a
    # check people learn to ignore is worse than no check.
    return cited


def check(root: pathlib.Path) -> V.Report:
    tax = V.Taxonomy(__file__)
    notes, _ = V.load(root)
    rep = V.Report()

    surveys, briefs = {}, []
    for note in sorted(notes, key=lambda n: str(n.rel)):
        V.check_shape(note, tax, rep.require)
        if note.type == "survey":
            surveys[str(note.prop("area", ""))] = note
        elif note.type == "slice-brief":
            briefs.append(note)

    defined = {area: check_survey(note, rep) for area, note in surveys.items()}
    for note in briefs:
        area = str(note.prop("area", ""))
        cited = check_brief(note, rep)
        # A ruling resolves against the survey while the survey exists. After the flip it is gone,
        # so an unresolvable citation then is expected rather than a defect.
        if area in defined:
            for bid, ref in sorted(cited.items()):
                rep.require(ref in defined[area],
                            f"{note.rel}: ruling {bid} cites {ref}, which survey/{area} does not "
                            f"define — the id was renumbered, or the ruling is about nothing")
                if ref != bid:
                    rep.warn(f"{note.rel}: ruling {bid} cites {ref} rather than its own "
                             f"behaviour — intended, or a copied row?")
        # The cleanup step is the one everybody forgets, because nothing stops working without it.
        if note.status == "flipped" and area in surveys:
            rep.require(False,
                        f"{surveys[area].rel}: survives a flipped slice ({note.rel}) — the survey "
                        f"is deleted at the flip, because its content now lives in the suite")
    return rep


def signals(root: pathlib.Path) -> list[str]:
    """The two numbers a project is held to, and nothing else."""
    notes, _ = V.load(root)
    by_status: dict[str, int] = {}
    for note in notes:
        if note.type in ("survey", "slice-brief"):
            by_status[f"{note.type}:{note.status}"] = by_status.get(f"{note.type}:{note.status}", 0) + 1
    suite = sum(1 for p in root.rglob("*") if p.is_file()
                and "characterization" in str(p.relative_to(root)).replace("\\", "/"))
    out = [f"surveys outstanding   {sum(v for k, v in by_status.items() if k.startswith('survey:'))}"]
    out += [f"  {k.split(':', 1)[1] or '(no status)':<22} {v}"
            for k, v in sorted(by_status.items()) if k.startswith("survey:")]
    out.append(f"briefs                {len(notes) and sum(v for k, v in by_status.items() if k.startswith('slice-brief:'))}")
    out += [f"  {k.split(':', 1)[1] or '(no status)':<22} {v}"
            for k, v in sorted(by_status.items()) if k.startswith("slice-brief:")]
    out.append(f"checks accumulated    {suite}")
    out.append("")
    out.append("Across slices the first number trends down and the last trends up. If neither has")
    out.append("moved in several slices, the loop is not running and this has become paperwork.")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="command", required=True)
    for name, helptext in (("check", "report defects in surveys and briefs"),
                           ("signals", "print the two health numbers")):
        p = sub.add_parser(name, help=helptext)
        p.add_argument("workspace", type=pathlib.Path, help="the folder holding survey/ and slices/")
    args = ap.parse_args()
    root = args.workspace.resolve()
    if not root.is_dir():
        sys.exit(f"slice.py: {args.workspace} is not a directory")

    if args.command == "signals":
        print("\n".join(signals(root)))
        return 0

    rep = check(root)
    for line in rep.errors:
        print(f"  {line}")
    for line in rep.warnings:
        print(f"  warning: {line}")
    if rep.errors:
        print(f"{len(rep.errors)} findings, {len(rep.warnings)} warnings.")
    else:
        print(f"ok — {rep.checks} checks"
              + (f", {len(rep.warnings)} warnings" if rep.warnings else "")
              + ". Nothing here judges whether a tag is honest, whether a golden master came from"
                " the running system, or whether a slice is a sound slice.")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
