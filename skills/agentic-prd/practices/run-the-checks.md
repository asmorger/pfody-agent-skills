# Run the checks

**When** after every mode that writes a file, and before reporting anything as done.

**Why.** The script catches the defect class that is invisible to reading: a requirement no story
covers, a criterion citing an id that no longer exists, a duplicate id, a blank coverage line, a
story slicing the wrong Feature. Reading frontmatter rather than parsing tables is what makes that
list possible — and it still catches nothing about meaning, so reporting a pass without saying so
transfers confidence it never earned.

**Steps.**

1. **Run both commands with the full path**, because the vault is usually in another folder:

       python3 <skill-folder>/scripts/prd.py check <vault>
       python3 <skill-folder>/scripts/prd.py check <vault> --prd PRD-001
       python3 <skill-folder>/scripts/prd.py check <vault> --source SRC-0007=<transcript.txt>
       python3 <skill-folder>/scripts/prd.py moc   <vault>

2. **Regenerate the MOCs before reporting.** The coverage table is built from the requirement notes,
   so a stale snapshot is the one way coverage can still be wrong
   ([`../patterns/coverage-moc.md`](../patterns/coverage-moc.md)).
3. **Pass `--source` wherever you have a text copy.** It is the only mechanical confirmation that a
   time or line locator exists at all ([`read-a-binary-source.md`](read-a-binary-source.md)).
4. **Treat errors as blocking.** Exit code 0 means no structure or traceability error. A non-zero
   exit after `DECOMPOSE` or `CHANGE` is not reportable as success.
5. **Treat warnings as a person's to settle.** A warning may sit in a draft — an `Unknown` outcome
   value, a `PROPOSED` requirement, a requirement that may hold two behaviours, an all-`P0` priority
   list, a missing owner. Each must be resolved or accepted before Gate 2, by a person
   ([`../principles/only-a-person-crosses-a-gate.md`](../principles/only-a-person-crosses-a-gate.md)).
6. **Never edit to satisfy the script.** In `REVIEW` the finding goes in the review file. Elsewhere,
   fix the defect the warning points at — not the text that triggered it.
7. **State the three limits by name** in every report. The script cannot judge whether a citation
   supports its requirement, whether a slice is a sound slice, or whether a criterion is a faithful
   test of its requirement
   ([`../principles/the-check-is-not-a-reviewer.md`](../principles/the-check-is-not-a-reviewer.md)).

**Done when** both commands have run, the exit code is reported, every error is fixed or named,
every warning is listed for the person, the MOC snapshots match the notes, and the three limits are
stated rather than implied.
