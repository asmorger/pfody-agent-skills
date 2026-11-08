# The PRD changes before the backlog

**Rule.** Behaviour changes in the PRD first: add the source or decision, raise the version, then
regenerate the affected User Stories and show the diff. A story, an acceptance criterion or a tracker
item is never edited to describe behaviour the PRD does not yet state.

**Why.** The direction of the dependency is the whole value of the document. If a story can be edited
directly, the PRD becomes a stale summary of the backlog instead of the contract the backlog derives
from, and the question the PRD exists to answer — *why is this behaviour here?* — stops having an
answer. The practical tell is traceability: an edited criterion cites a requirement that does not say
what the criterion tests, and no check can detect that the requirement, not the criterion, is the
thing that is wrong.

**In the PRD.**
- `CHANGE` touches the PRD, then the backlog, in that order and never the reverse
  ([`../practices/change-a-requirement.md`](../practices/change-a-requirement.md)).
- Raise the version on every behaviour change; the backlog header names the version it came from.
- `DECOMPOSE` never edits an Accepted PRD. A gap it finds is reported, and the person decides whether
  to run `CHANGE` ([`../practices/decompose-a-prd.md`](../practices/decompose-a-prd.md)).
- `REVIEW` never edits the PRD at all, even when a check fails.
- Acceptance criteria already in a tracker change only after the PRD has.

**Breaks when.** A story is fixed in place because it was faster →
[`../anti-patterns/backlog-edited-ahead-of-the-prd.md`](../anti-patterns/backlog-edited-ahead-of-the-prd.md).
