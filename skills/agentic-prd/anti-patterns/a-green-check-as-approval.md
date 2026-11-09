# A green check as approval

**Smell.** "The check passes — the PRD is ready for decomposition." A report that gives the exit code
and nothing else. A review whose Check line says "0 errors" with no statement of what was not
examined.

**Why it is wrong.** The script proves structure and traceability: ids resolve, no duplicates, no
blank coverage line, each criterion cites a requirement that exists, locators appear in the text it
was given. It cannot read. Whether `SRC-0007 @1:13:06` says what `R-001` claims, whether a slice is a
sound slice, whether a criterion faithfully tests its requirement — those three decide whether the
build succeeds, and all three are a person's judgement. Reporting the pass without the boundary
transfers confidence the script never earned, and it is the exact moment the human review gets
skipped.

**Instead.** Report the command, the exit code and the warnings, then name the three limits every
time. Then say what a person still has to judge, with the most consequential item first. A check is
evidence about the document's wiring, not about its truth
([`../principles/the-check-is-not-a-reviewer.md`](../principles/the-check-is-not-a-reviewer.md),
[`../practices/run-the-checks.md`](../practices/run-the-checks.md)).
