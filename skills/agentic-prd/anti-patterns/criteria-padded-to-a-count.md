# Criteria padded to a count

**Smell.** Every story with exactly five acceptance criteria. The fourth and fifth restate the first
in other words, or test the framework: "Given the page, when it loads, then the page displays."
Sometimes a criterion tests behaviour its requirement never states, invented to round the set out.

**Why it is wrong.** Padding makes coverage unreadable. A reviewer can no longer tell which criteria
are the behaviour and which are filler, so they check none of them, and the real gap — the edge case
nobody specified — is hidden among four restatements. Criteria that test nothing still cost: each
becomes a test somebody writes and maintains. And a criterion specifying behaviour its requirement
lacks is an unsourced requirement that has skipped the gate.

**Instead.** Write the criteria the requirement actually implies: often one, sometimes three.
Order them from the main output outward to the edges and stop. If the requirement feels under-tested,
the requirement is under-specified — that is a `CHANGE`, not more criteria
([`../patterns/acceptance-criterion.md`](../patterns/acceptance-criterion.md),
[`../principles/the-prd-changes-before-the-backlog.md`](../principles/the-prd-changes-before-the-backlog.md)).
