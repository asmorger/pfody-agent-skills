# The check is not a reviewer

**Rule.** Run `prd.py` after every mode that writes a file, and report its result together with
what it cannot judge. Exit code 0 means the structure and the traceability hold — nothing more. Never
report a passing check as a ready PRD.

**Why.** The script can prove that `R-001` is cited by a criterion, that a locator exists in the
source text, that no id repeats, that no coverage line is blank. It cannot read. Whether `SRC-07
@1:13:06` actually says what `R-001` claims, whether a slice is a sensible slice, whether a criterion
is a faithful test of its requirement — all three are the judgements that decide whether the build
succeeds, and all three are a person's. A green check reported without that boundary is worse than no
check, because it transfers confidence the script never earned.

**In the PRD.**
- Errors block; warnings may sit in a draft and must be resolved or accepted before Gate 2
  ([`../practices/run-the-checks.md`](../practices/run-the-checks.md)).
- Pass `--source SRC-07=<text copy>` so locators are verified against the real text, not trusted.
- `--backlog` additionally checks coverage, source grounding and story tags.
- State the three limits by name in the report. They are the same three every time
  ([`../practices/report-the-result.md`](../practices/report-the-result.md)).

**Breaks when.** A passing check stands in for a review →
[`../anti-patterns/a-green-check-as-approval.md`](../anti-patterns/a-green-check-as-approval.md).
