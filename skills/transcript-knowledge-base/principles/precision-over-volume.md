# Precision over volume

**Rule.** A sixty-minute meeting yields a handful of durable items — three to fifteen — not dozens.
Skip greetings, scheduling, status updates, tangents and opinions in passing. If you could not write
it into a specification, it is not an item.

**Why.** Over-extraction is this skill's dominant failure, and it is self-concealing: a long index
looks thorough. What it actually does is bury the dozen real rules among sixty assignments and
progress notes, so the reader who needs the rule cannot find it and the reader who finds a status
line treats it as a requirement. Status is also the fastest-decaying content in any transcript — "X is
behind a feature flag" is false within a sprint — so a status-heavy index is stale on the day it is
rendered. A short index is read; a long one is skimmed.

**In the index.**
- Durable means: decisions, business rules, requirements, constraints, scope inclusions and
  exclusions, defined behaviours, policies, confirmed answers to open questions.
- Not durable: who is doing what, when it will ship, what is behind a flag, how the sprint is going,
  what somebody thinks might be nice.
- Standup and status meetings are the dangerous ones. Expect few items from them, or none, and that
  is a correct result ([`../anti-patterns/status-recorded-as-a-rule.md`](../anti-patterns/status-recorded-as-a-rule.md)).
- Never extract to a count. An honest empty brief is a finding, not a failure.

**Breaks when.** Project status is recorded as though it were a rule →
[`../anti-patterns/status-recorded-as-a-rule.md`](../anti-patterns/status-recorded-as-a-rule.md).
