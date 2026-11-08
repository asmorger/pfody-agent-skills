# Backlog edited ahead of the PRD

**Smell.** An acceptance criterion fixed in the backlog because the requirement was awkward. A story
given an extra Expected Output bullet in review. A tracker item's criteria tightened directly. The
PRD still says what it said, and nobody updated it because the change was small.

**Why it is wrong.** It reverses the one dependency the document exists for. The PRD becomes a stale
summary of the backlog rather than the contract the backlog derives from, so *why is this behaviour
here?* stops having an answer. Traceability fails in a way no check can detect: the criterion cites
`R-012`, `R-012` does not say what the criterion tests, and nothing can tell which of the two is
wrong. Repeat it four times and the backlog is the real spec — unsourced, unreviewed and ungated.

**Instead.** Run `CHANGE`. The PRD first: the new source or decision, then the version, then the
affected stories regenerated with their diffs shown. If the change is too small to be worth that, it
is too small to be worth making
([`../principles/the-prd-changes-before-the-backlog.md`](../principles/the-prd-changes-before-the-backlog.md),
[`../practices/change-a-requirement.md`](../practices/change-a-requirement.md)).
