"""Check the tools that check the vaults: run each skill's checker against its worked example,
then against a deliberately broken copy, and assert it catches what it claims to.

    python3 scripts/check-vault-tools.py

A clean example must pass. A mutated copy must produce a specific finding for every defect injected.
That second half is the point: a checker that reports nothing on a clean vault and also nothing on a
broken one is worse than no checker, and the only way to know the difference is to break something
on purpose. This file exists because a front-matter parser bug — `key:` with a blank value parsing
as an empty mapping, which reads as truthy — made several "is this field filled in?" checks pass
silently. Exit code 1 on any finding.
"""
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parents[1]

# (skill, script, argv for the clean run, mutations, expected finding substrings)
CASES = [
    {
        "name": "anchored-knowledge / vault.py lint",
        "script": "skills/anchored-knowledge/scripts/vault.py",
        "vault": "skills/anchored-knowledge/examples/vault",
        "clean": ["lint", "."],
        "mutate": [
            ("rules/order-address-frozen-on-confirmation.md",
             [("(see [[confirmed-order-may-split-across-parcels|ORDER-5]])", "(see [[ORDER-99]])"),
              ("status: confirmed", "status: agreed")]),
            ("rules/credit-hold-blocks-labelling.md",
             [('sources: ["[[operations-lead-on-credit-holds]]"]', "sources: []")]),
            ("rules/one-label-per-order.md",
             [('superseded-by: "[[one-label-per-parcel|LABEL-1]]"\n', "")]),
            ("glossary/parcel.md", [("updated: 2026-11-08", "updated:")]),
            # The five that exist because the alias-permissive linter could not see them.
            ("rules/a-printed-label-may-be-voided.md",
             [("[[who-may-void-a-printed-label|Q-0003]]", "[[Q-0003]]")]),            # bare id
            ("rules/bulk-printing-across-orders.md",
             [("[[order-splitting-across-parcels|SW-0002]]",
               "[[order-splitting-across-parcels|SW-9999]]")]),                       # wrong id shown
            ("scope/label-creation-included.md",
             [("[[one-label-per-parcel|LABEL-1]]",
               "[[one-label-per-parcel#No Such Heading|LABEL-1]]")]),                 # dead anchor
            ("moc/decisions.md",
             [("managed-block-sha256: ", "managed-block-sha256: 0000")]),             # hand edit
            ("moc/glossary.md",
             [("input-manifest-sha256: ", "input-manifest-sha256-was: ")]),           # no provenance
        ],
        "expect": [
            "dangling wikilink [[ORDER-99]]",
            "status 'agreed' is not valid",
            "status confirmed with no sources",
            "superseded with no superseded-by",
            "[[Q-0003]] is a bare id, which Obsidian does not resolve",
            "whose id is SW-0002",
            "no such heading in rules/one-label-per-parcel.md",
            "the generated block was edited by hand",
            "moc/glossary.md: generated note is missing input-manifest-sha256",
        ],
    },
    {
        "name": "anchored-knowledge / vault.py moc --check",
        "script": "skills/anchored-knowledge/scripts/vault.py",
        "vault": "skills/anchored-knowledge/examples/vault",
        "clean": ["moc", ".", "--check"],
        "mutate": [
            # A rule whose title changed makes every index that lists it stale. The old `moc` would
            # have rewritten the table in silence; `--check` has to say so instead.
            ("rules/one-label-per-parcel.md",
             [("# LABEL-1 — One label per parcel", "# LABEL-1 — Exactly one label per parcel")]),
        ],
        "expect": [
            "moc/business-rules.md: the generated block is stale",
        ],
    },
    {
        # A derived narrative is the readable surface people actually read, so it is the one place a
        # stale summary does the most damage. The prose is written by hand; these are the parts a
        # script can hold it to.
        "name": "anchored-knowledge / vault.py lint (narrative)",
        "script": "skills/anchored-knowledge/scripts/vault.py",
        "vault": "skills/anchored-knowledge/examples/vault",
        "clean": ["lint", "."],
        "mutate": [
            ("narrative/how-labelling-works.md", [
                ("- One label per parcel, so a split order gets one label per box\n"
                 "  ([[one-label-per-parcel|LABEL-1]]).",
                 "- One label per parcel is how the warehouse has always done it, and that is "
                 "settled."),
                ("## Gaps found while deriving", "## Loose ends"),
                ("# How labelling works", "# How labelling works\n\nLast updated: 2026-11-08."),
            ]),
        ],
        "expect": [
            "makes a claim with no link to the note that holds it",
            "no '## Gaps found while deriving' section",
            "a hand-written date in the prose",
        ],
    },
    {
        "name": "anchored-knowledge / vault.py narrative --check",
        "script": "skills/anchored-knowledge/scripts/vault.py",
        "vault": "skills/anchored-knowledge/examples/vault",
        "clean": ["narrative", ".", "--check"],
        "mutate": [
            # Touch a note the narrative derives from. The story now describes an older vault, and
            # nothing about the narrative's own text would ever reveal it.
            ("rules/one-label-per-parcel.md",
             [("# LABEL-1 — One label per parcel", "# LABEL-1 — One label for each parcel")]),
        ],
        "expect": [
            "narrative/how-labelling-works.md: stale — the notes it derives from have changed",
        ],
    },
    {
        "name": "agentic-prd / prd.py check",
        "script": "skills/agentic-prd/scripts/prd.py",
        "vault": "skills/agentic-prd/examples/vault",
        "clean": ["check", "."],
        "mutate": [
            ("requirements/create-a-label-on-order-confirmation.md",
             [("# R-001 — When a clerk confirms an order, the system shall create a carrier label "
               "for the order's shipping address.",
               "# R-001 — Labels should be created quickly.")]),
            ("requirements/show-the-carrier-rejection-reason.md",
             [("source: SRC-0002 @18:30", "source: the discovery call"),
              ("priority: P0", "priority: High"), ("verify: Auto", "verify: Someone checks")]),
            ("requirements/refuse-a-label-on-credit-hold.md",
             [('stories: ["[[create-a-label-for-a-confirmed-order|US-01]]"]', "stories: []")]),
            ("requirements/record-every-label-action.md", [("applies-to: [All]", "applies-to: []")]),
            ("questions/who-may-void-a-printed-label.md",
             [("owner: Example Operations Lead", "owner:"), ("needed-by: 2026-11-20", "needed-by:")]),
            ("metrics/address-error-rate-on-parcels.md",
             [("denominator: Parcels shipped", "denominator:")]),
            ("backlog/create-and-print-a-label.md",
             [('  error-state: "[[show-the-carrier-rejection-reason|R-002]]"',
               '  error-state: ""'),
              ('  current-records-and-data-migration: "N/A — labels did not exist before this '
               'release."', '  current-records-and-data-migration: "N/A"')]),
            ("backlog/create-a-label-for-a-confirmed-order.md",
             [('parent: "[[create-and-print-a-label|FEAT-01]]"',
               'parent: "[[void-a-label|FEAT-02]]"'),
              ("**Assumptions**\n- None identified.\n\n", ""),
              # The label that restated `parent`. It was in the required set until it was dropped,
              # so a story written to the old shape still carries one and nothing else would say so.
              ("**Acceptance Criteria**", "**Tags**\n- EPIC-01, FEAT-01\n\n**Acceptance Criteria**"),
              ("4. AC-4 [X-002]", "4. AC-4 [R-777]")]),
            ("prd/shipping-labels-at-order-processing.md",
             [("## 8. Rollout and measurement", "## Rollout and measurement")]),
            ("requirements/void-a-printed-label.md",
             [("[[who-may-void-a-printed-label|Q-0003]]", "[[Q-0003]]")]),    # bare id
            ("moc/requirements.md",
             [("input-manifest-sha256: ", "input-manifest-sha256-was: ")]),   # no provenance
        ],
        "expect": [
            "does not open with one of the five patterns",
            "is not SRC-nnnn with a locator",
            "priority 'High' is not one of",
            "verify 'Someone checks' is not one of",
            "coverage is covered but no story is named",
            "a cross-cutting requirement must name what it applies to",
            "a question with no owner cannot close",
            "a question with no needed-by cannot close",
            "denominator is empty, so this is not yet a metric",
            "coverage line 'error-state' is blank",
            "is N/A with no reason",
            "missing story labels",
            "a criterion cites unknown requirement R-777",
            "**Tags** restates `parent` and `priority`",
            "not to its parent FEAT-02",
            "section 8 is not present",
            "[[Q-0003]] is a bare id, which Obsidian does not resolve",
            "moc/requirements.md: generated note is missing input-manifest-sha256",
        ],
    },
    {
        # The readable rendition of a PRD exists for readers who cannot resolve an embed, which is
        # also why none of them can tell that it has gone stale. Only the check can.
        "name": "agentic-prd / prd.py render --check",
        "script": "skills/agentic-prd/scripts/prd.py",
        "vault": "skills/agentic-prd/examples/vault",
        "clean": ["render", ".", "--out", "render/prd-001.md", "--check"],
        "mutate": [
            ("requirements/create-a-label-on-order-confirmation.md",
             [("coverage: covered", "coverage: blocked")]),
        ],
        "expect": [
            "is stale — the notes have changed since it was rendered",
        ],
    },
    {
        # The one case that is not about a single skill. A project installs these together and they
        # write into one `docs/` tree by design — `questions/`, `sources/`, `decisions/`, `moc/` and
        # `backlog/` are shared folders, and the PRD cites the knowledge base's rule ids. Until this
        # case existed every checker ran on its own skill's example and passed, which is how the
        # same three note types came to carry two id widths, two decision prefixes and two status
        # casings, and how six of the PRD's types stayed `unknown type` to the knowledge linter.
        #
        # The clean half asserts both checkers pass one vault holding all three skills' notes. The
        # broken half injects the four defects that only show up when the vaults meet.
        #
        # The record layer is overlaid last: where a note exists in both examples — the open
        # question, the credit-hold decision — the knowledge base's copy is the one kept, because
        # it is the system of record and the PRD cites it rather than the reverse.
        "name": "combined vault / both checkers",
        "vault": ["skills/agentic-prd/examples/vault",
                  "skills/anchored-knowledge/examples/vault"],
        "copy": [("skills/user-story-builder/examples/vault/backlog/void-a-printed-label-story.md",
                  "backlog/void-a-printed-label-story.md")],
        "runs": [
            {"script": "skills/anchored-knowledge/scripts/vault.py", "argv": ["lint", "."],
             "expect": ["duplicate file name void-a-printed-label.md",
                        "status 'accepted' is not valid",
                        "id 'SRC-9' does not match the source pattern",
                        "no 'topic' — a requirement is grouped by it"]},
            {"script": "skills/agentic-prd/scripts/prd.py", "argv": ["check", "."],
             "expect": ["duplicate file name void-a-printed-label.md",
                        "status 'accepted' is not valid",
                        "id 'SRC-9' does not match the source pattern",
                        "no 'topic' — a requirement is grouped by it"]},
            # The story checker, run where a Mode A story's citations actually resolve. On the
            # standalone backlog above the same citations are warnings; here they must be silent,
            # which is the half that proves the two vaults really do form one.
            {"script": "skills/user-story-builder/scripts/story.py", "argv": ["check", "."],
             "expect": ["duplicate file name void-a-printed-label.md",
                        "status 'accepted' is not valid"]},
        ],
        "mutate": [
            # The story's status reverts to the PRD's word. One ladder per type, or the two skills
            # write the same `type: user-story` with two vocabularies again.
            ("backlog/void-a-printed-label-story.md", [("status: draft", "status: accepted")]),
            # A source id reverts to the narrow width the PRD example used to carry.
            ("sources/2026-11-08-operations-review.md",
             [("id: SRC-0010", "id: SRC-9"), ("aliases: [SRC-0010]", "aliases: [SRC-9]")]),
            # The grouping key removed. There is no `tags` property to fall back on.
            ("requirements/create-a-label-on-order-confirmation.md", [("topic: orders\n", "")]),
        ],
        # A story named for the behaviour its requirement is also named for. Obsidian resolves a
        # wikilink by file name, so every `[[void-a-printed-label|R-012]]` in the vault would start
        # opening whichever of the two is nearer — a hollow citation layer with no visible symptom.
        "mutate_rename": [("backlog/void-a-printed-label-story.md",
                           "backlog/void-a-printed-label.md")],
        "expect": [],
    },
    {
        # The backlog this skill writes. Until it shipped a checker, its notes were held to nothing
        # of their own and its `moc/backlog.md` was the only generated block in the repo with no
        # generator behind it — so it carried no provenance and "is this index current?" had no
        # mechanical answer.
        #
        # The clean run is the standalone backlog, which reports warnings and no errors: a backlog
        # on its own genuinely cannot resolve a Mode A story's citations into a record vault it was
        # not given. The composed case below runs the same check where they do resolve.
        "name": "user-story-builder / story.py check",
        "script": "skills/user-story-builder/scripts/story.py",
        "vault": "skills/user-story-builder/examples/vault",
        "clean": ["check", "."],
        "mutate": [
            ("backlog/void-a-printed-label-story.md",
             [# Published with nothing to update against: the next run creates a duplicate.
              ("status: draft", "status: published"),
              # The one duplication the shape allows, now disagreeing with itself.
              ("- Source grounding: [[a-printed-label-may-be-voided|LABEL-2]]",
               "- Source grounding: [[a-printed-label-may-be-voided|LABEL-9]]"),
              # A criterion renumbered, so AC-2 in the tracker is AC-3 in the note.
              ("2. AC-2 [LABEL-3] Given a collected parcel", "3. AC-3 [LABEL-3] Given a collected parcel"),
              # A label dropped. An adapter maps them positionally.
              ("**Open Questions**\n- Does voiding require supervisor approval, or may any clerk do it?\n\n", ""),
              ("review-required: true", ""),
              ("source-mode: A", "source-mode: D")]),
            ("backlog/export-the-days-labels.md",
             [# Mode C means nothing but what the user asked for. This claims a source anyway.
              ("sources: []", 'sources: ["[[a-printed-label-may-be-voided|LABEL-2]]"]'),
              # A source tag sent to a tracker verbatim cannot be a wikilink.
              ("1. AC-1 [Request]", "1. AC-1 [[[a-printed-label-may-be-voided|LABEL-2]]]")]),
        ],
        "expect": [
            "status is published but `tracker-id` is empty",
            "but Source grounding names",
            "numbered 3/AC-3 but is criterion 2",
            "missing story labels: **Open Questions**",
            "no `review-required`",
            "source-mode C means nothing but what the user asked for",
            "the source tag is a wikilink",
            "source-mode 'D' is not one of A | B | C",
        ],
    },
    {
        "name": "user-story-builder / story.py moc --check",
        "script": "skills/user-story-builder/scripts/story.py",
        "vault": "skills/user-story-builder/examples/vault",
        "clean": ["moc", ".", "--check"],
        "mutate": [
            # A story's title changed, so the index that lists it is describing an older backlog.
            ("backlog/export-the-days-labels.md",
             [("# US-07 — Export the day's labels", "# US-07 — Export a day's labels")]),
        ],
        "expect": ["moc/backlog.md: the generated block is stale"],
    },
    {
        "name": "agentic-prd / prd.py moc --check",
        "script": "skills/agentic-prd/scripts/prd.py",
        "vault": "skills/agentic-prd/examples/vault",
        "clean": ["moc", ".", "--check"],
        "mutate": [
            ("requirements/void-a-printed-label.md",
             [("priority: P1", "priority: P2")]),
        ],
        "expect": [
            "the generated block is stale",
        ],
    },
    {
        # A survey observes and a brief decides, so every defect here is a leak across that seam:
        # a gate that reads clean because its one line is forty lines below the rulings, a ruling
        # pointing at a behaviour nobody observed, a changed behaviour with no check behind it.
        # None of them is visible by eye, which is why the example is mutated rather than reviewed.
        "name": "legacy-slicing / slice.py check",
        "script": "skills/legacy-slicing/scripts/slice.py",
        "vault": "skills/legacy-slicing/examples",
        "clean": ["check", "."],
        "mutate": [
            ("slices/reprint-a-label.md", [
                # Building started on an unready slice.
                ("## Decisions outstanding: 0", "## Decisions outstanding: 2"),
                # A deferral with nothing behind it — the evasion this count exists to catch.
                ("B05 rush repricing         DEFER   safe: the reprint path does not price",
                 "B05 rush repricing         DEFER"),
                # A ruling about a behaviour the survey does not define.
                ("[survey B07 · PM 11-11]", "[survey B99 · PM 11-11]"),
                # No golden master, so there is nothing for the new code to be wrong against.
                ("char/label_reprint_*.approved", "dropped_the_reprint_master"),
                ("char/label_create_*.approved", "dropped_the_create_master"),
                # A parallel run with no threshold and no volume.
                ("    5 working days. Every reprint resolves both paths and logs a label-row diff.\n"
                 "    Flip required 0 diffs over at least 500 reprints. Actual: 0 over 612.",
                 "    Ran both paths for a while and the diffs looked fine."),
                # Flipped, so the survey should be gone.
                ("status: frozen", "status: flipped"),
            ]),
            ("survey/label-printing.md", [
                # An observation with no provenance, indistinguishable from a guess.
                ("        [db: trigger tr_label_post]", ""),
                # A reused behaviour id, which silently repoints whatever cites it.
                ("B06  Credit hold appears to be bypassed",
                 "B01  Credit hold appears to be bypassed"),
            ]),
        ],
        "expect": [
            "Decisions outstanding reads 2",
            "ruling B05 DEFER gives no reason",
            "cites B99, which survey/label-printing does not define",
            "no 'char/' check",
            "names no threshold and no volume",
            "survives a flipped slice",
            "B04 has no provenance tag",
            "behaviour id B01 is defined twice",
        ],
    },
]


def run(script: pathlib.Path, cwd: pathlib.Path, argv: list[str]):
    proc = subprocess.run([sys.executable, str(script), *argv], cwd=cwd,
                          capture_output=True, text=True)
    return proc.returncode, proc.stdout + proc.stderr


def compose(case, dest: pathlib.Path) -> None:
    """Build the case's vault at `dest`: one example, or several overlaid in order.

    A composed case is the integration test the repo did not have. Each skill's worked example
    passed its own checker in isolation, which is exactly why the id widths, the status casings and
    the type lists could disagree for as long as they did.
    """
    sources = case["vault"] if isinstance(case["vault"], list) else [case["vault"]]
    dest.mkdir(parents=True, exist_ok=True)
    for rel in sources:
        shutil.copytree(REPO / rel, dest, dirs_exist_ok=True)
    for src, into in case.get("copy", []):
        target = dest / into
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPO / src, target)


def runs_of(case):
    """A case runs one script, or several over the same vault."""
    return case.get("runs") or [{"script": case["script"], "argv": case["clean"],
                                 "expect": case["expect"]}]


def main() -> int:
    findings = []
    for case in CASES:
        with tempfile.TemporaryDirectory() as tmp:
            clean = pathlib.Path(tmp) / "clean"
            compose(case, clean)
            for spec in runs_of(case):
                code, out = run(REPO / spec["script"], clean, spec["argv"])
                if code != 0:
                    findings.append(f"{case['name']}: the clean example does not pass "
                                    f"{' '.join(spec['argv'])}\n{_indent(out)}")

        with tempfile.TemporaryDirectory() as tmp:
            copy = pathlib.Path(tmp) / "vault"
            compose(case, copy)
            for rel, pairs in case["mutate"]:
                path = copy / rel
                text = path.read_text(encoding="utf-8")
                for old, new in pairs:
                    if old not in text:
                        findings.append(f"{case['name']}: mutation target missing in {rel}: "
                                        f"{old[:60]!r}")
                        continue
                    text = text.replace(old, new, 1)
                path.write_text(text, encoding="utf-8")
            for rel in case.get("mutate_rename", []):
                (copy / rel[0]).rename(copy / rel[1])
            for spec in runs_of(case):
                code, out = run(REPO / spec["script"], copy, spec["argv"])
                if code == 0:
                    findings.append(f"{case['name']}: the BROKEN copy passed "
                                    f"{' '.join(spec['argv'])} — the checker is not catching its "
                                    f"own rules\n{_indent(out)}")
                for needle in spec["expect"]:
                    if needle not in out:
                        findings.append(f"{case['name']}: no finding matched {needle!r}")

    # `moc/backlog.md` has two possible owners: `user-story-builder` writes stories, and
    # `agentic-prd` writes them too when a whole backlog is decomposed at once. A project with both
    # installed must not get a different index depending on which tool ran last, so each generator
    # has to report the other's block as current. The two `_cell` implementations are separate code
    # and nothing but this would notice them drifting apart.
    pairs = [("skills/user-story-builder/examples/vault",
              "skills/agentic-prd/scripts/prd.py", "story.py"),
             ("skills/agentic-prd/examples/vault",
              "skills/user-story-builder/scripts/story.py", "prd.py")]
    for vault, foreign, native in pairs:
        code, out = run(REPO / foreign, REPO / vault, ["moc", ".", "--check"])
        if code != 0:
            findings.append(f"cross-generator: {pathlib.Path(foreign).name} reports "
                            f"{native}'s block in {vault} as stale, so the two disagree about a "
                            f"file they can both own\n{_indent(out)}")

    # The regression this file was written for. The parser now lives in `vaultlib.py`, so the
    # guard follows it there — and to every copy, because a skill runs from its own.
    parsers = [REPO / "shared" / "vaultlib.py"] + sorted((REPO / "skills").glob("*/scripts/vaultlib.py"))
    if len(parsers) < 2:
        findings.append("no vaultlib.py copies found — the shared parser has moved or gone")
    for path in parsers:
        rel = path.relative_to(REPO)
        if not re.search(r"if value == \{\}", path.read_text(encoding="utf-8")):
            findings.append(f"{rel}: the blank-value guard is gone. `key:` with nothing under it "
                            f"parses as {{}}, which is truthy, so every empty-field check passes.")
    # And the scripts must not have grown their own parser back.
    for rel in ("skills/anchored-knowledge/scripts/vault.py", "skills/agentic-prd/scripts/prd.py",
                "skills/user-story-builder/scripts/story.py"):
        text = (REPO / rel).read_text(encoding="utf-8")
        if "def split_front_matter" in text or "def _split(" in text:
            findings.append(f"{rel}: has its own front matter parser again. One parser, in "
                            f"vaultlib.py, or they drift the way they already did once.")

    for case in CASES:
        print(f"{case['name']}: {'ok' if not [f for f in findings if f.startswith(case['name'])] else 'FAILED'}")
    for f in findings:
        print(f"  {f}")
    print(f"{len(findings)} findings.")
    return 1 if findings else 0


def _indent(text: str) -> str:
    return "\n".join("    " + line for line in text.strip().splitlines())


if __name__ == "__main__":
    sys.exit(main())
