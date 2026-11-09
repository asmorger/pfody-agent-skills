# Ids are never reused

**Rule.** An id, once issued, belongs to that item forever. A dropped requirement is marked `Retired`
in place and keeps its number; the next requirement takes the next free number. Nothing is
renumbered, in the PRD or in the backlog, ever.

**Why.** The id is the only thing holding the chain together: a criterion cites `R-001`, a coverage
row tracks `R-001`, a test is named for `R-001`, a pull request references it, a tracker item is
tagged with it. Reuse silently re-points every one of those at a different behaviour, and nothing
fails — the tests still pass, against the wrong requirement. Retiring in place also leaves the
history readable: a reader can see that a behaviour was once specified and then dropped, which is
usually the question being asked.

**In the PRD.**
- Retired requirement: keep the note, set `status: retired` and `coverage: retired`, keep the
  id.
- `CHANGE` keeps every existing `EPIC`, `FEAT`, `US` and `R` id and regenerates only affected stories
  ([`../practices/change-a-requirement.md`](../practices/change-a-requirement.md)).
- Gaps in the numbering are normal and are never closed up.
- Acceptance criteria are the one exception: `AC-n` restarts within each User Story, because the
  requirement id in the criterion carries the link
  ([`../patterns/acceptance-criterion.md`](../patterns/acceptance-criterion.md)).

**Breaks when.** Ids are tidied after a deletion →
[`../anti-patterns/renumbered-ids.md`](../anti-patterns/renumbered-ids.md).
