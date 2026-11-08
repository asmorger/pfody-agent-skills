# One behaviour per requirement

**Rule.** A requirement states one behaviour, in one of the five patterns, in terms an observer could
check. One id, one behaviour, one Feature. "And" joining two behaviours means two requirements.

**Why.** A requirement is the unit everything downstream counts: an acceptance criterion cites it, a
coverage row tracks it, a test names it, a change regenerates the stories that carry it. Two
behaviours under one id break all four at once — the criterion can only test half, the coverage row
can only be half Covered, and a change to one behaviour forces a rewrite of the other. Observability
is the second half of the rule: a behaviour nobody can watch cannot be given a verify method, so it
cannot be accepted or refused.

**In the PRD.**
- The patterns are *Always*, *Event*, *State*, *Unwanted* and *Optional*
  ([`../patterns/requirement-row.md`](../patterns/requirement-row.md)). Start each requirement with
  the pattern's words — the check script looks for them.
- Describe what the system does, not how. Name a technology only where a constraint fixes it.
- No vague adjective without a threshold beside it: "fast", "simple", "appropriate", "robust".
- Each requirement gets a verify method: `Auto`, `Manual`, `Eval` or `Telemetry`.

**Breaks when.** Two behaviours share an id →
[`../anti-patterns/requirement-with-two-behaviours.md`](../anti-patterns/requirement-with-two-behaviours.md).
A threshold is missing → [`../anti-patterns/vague-requirement.md`](../anti-patterns/vague-requirement.md).
