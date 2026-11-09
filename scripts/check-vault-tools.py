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
             [("source: SRC-01 @18:30", "source: the discovery call"),
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
              ("4. AC-4 [X-002]", "4. AC-4 [R-777]")]),
            ("prd/shipping-labels-at-order-processing.md",
             [("## 8. Rollout and measurement", "## Rollout and measurement")]),
            ("requirements/void-a-printed-label.md",
             [("[[who-may-void-a-printed-label|Q-03]]", "[[Q-03]]")]),        # bare id
            ("moc/requirements.md",
             [("input-manifest-sha256: ", "input-manifest-sha256-was: ")]),   # no provenance
        ],
        "expect": [
            "does not open with one of the five patterns",
            "is not SRC-nn with a locator",
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
            "not to its parent FEAT-02",
            "section 8 is not present",
            "[[Q-03]] is a bare id, which Obsidian does not resolve",
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
]


def run(script: pathlib.Path, cwd: pathlib.Path, argv: list[str]):
    proc = subprocess.run([sys.executable, str(script), *argv], cwd=cwd,
                          capture_output=True, text=True)
    return proc.returncode, proc.stdout + proc.stderr


def main() -> int:
    findings = []
    for case in CASES:
        script = REPO / case["script"]
        vault = REPO / case["vault"]
        code, out = run(script, vault, case["clean"])
        if code != 0:
            findings.append(f"{case['name']}: the clean example does not pass\n{_indent(out)}")

        with tempfile.TemporaryDirectory() as tmp:
            copy = pathlib.Path(tmp) / "vault"
            shutil.copytree(vault, copy)
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
            code, out = run(script, copy, case["clean"])
            if code == 0:
                findings.append(f"{case['name']}: the BROKEN copy passed — the checker is not "
                                f"catching its own rules\n{_indent(out)}")
            for needle in case["expect"]:
                if needle not in out:
                    findings.append(f"{case['name']}: no finding matched {needle!r}")

    # The regression this file was written for.
    for rel in ("skills/anchored-knowledge/scripts/vault.py", "skills/agentic-prd/scripts/prd.py"):
        text = (REPO / rel).read_text(encoding="utf-8")
        if not re.search(r"if value == \{\}", text):
            findings.append(f"{rel}: the blank-value guard is gone. `key:` with nothing under it "
                            f"parses as {{}}, which is truthy, so every empty-field check passes.")

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
