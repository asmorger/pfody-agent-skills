# Conflicts are recorded, not resolved

**Rule.** When an incoming item contradicts the record, prefer the higher authority and **record the
conflict**: a change-log entry naming both anchors, a dated note on the affected rule, and an open
question where authority does not settle it. Never pick the more reasonable statement.

**Why.** Which of two conflicting statements holds is a question about authority and about what has
happened since — not about the statements. An agent reading both has neither fact. A quietly resolved
conflict is the most expensive thing this base can carry, because it looks settled: it is cited by
stories, built, and discovered by the stakeholder who said the other thing. Recording it costs one
entry and one question, and it leaves a trail the next reader can follow instead of re-arguing.

**In the base.**
- Classify every contradiction: a genuine conflict, a refinement, or a terminology shift. The three
  get different treatment
  ([`../practices/log-a-knowledge-shift.md`](../practices/log-a-knowledge-shift.md)).
- A newer source that refines, contradicts or supersedes older understanding gets a `CH-NNNN` entry
  with both anchors and the previous and new understanding
  ([`../patterns/knowledge-change-entry.md`](../patterns/knowledge-change-entry.md)).
- Add a dated History or amendment note to each affected entry, and preserve the superseded
  assumption with its anchors.
- Valid knowledge that may exceed the scope baseline is not a conflict — it is a `SW-NNNN` scope watch
  item ([`../patterns/scope-watch-item.md`](../patterns/scope-watch-item.md)).

**Breaks when.** The base states one side and never mentions the other →
[`../anti-patterns/resolving-a-conflict-silently.md`](../anti-patterns/resolving-a-conflict-silently.md).
