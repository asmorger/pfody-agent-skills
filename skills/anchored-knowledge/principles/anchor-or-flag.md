# Anchor or flag

**Rule.** Every durable statement either names the source it came from, or wears its uncertainty:
`Draft` with a date and the stakeholder it is pending on, or `Needs Review`. There is no third state.
A confirmed-looking rule with no provenance is not allowed to exist.

**Why.** A knowledge base is read by people who will not check it — that is the point of having one.
So an unanchored statement is believed exactly as strongly as an anchored one, and the cost lands on
whoever builds from it. Flagging is the cheap half of the rule: a dated `Draft` marker costs one
clause and tells a reader precisely how much weight to put on the sentence, which is more useful than
a rule that is quietly right.

**In the base.**
- A rule with no inline marker is confirmed. Every other state is an inline marker, and every marker
  carries a date ([`../patterns/inline-status-markers.md`](../patterns/inline-status-markers.md)).
- Provenance lives in two places that must agree: the inline date in the rule, and the Source
  Register row naming the rule ids that source updated
  ([`../patterns/source-register-row.md`](../patterns/source-register-row.md)).
- Add an explicit `SRC-…` inline only when two or more sources share a date and the date alone cannot
  identify which one.
- Status vocabulary across the base: `Draft` · `Confirmed` · `Needs Review` · `Superseded` ·
  `Rejected` · `Scope Watch`.

**Breaks when.** A statement is recorded with neither a source nor a marker →
[`../anti-patterns/an-unanchored-rule.md`](../anti-patterns/an-unanchored-rule.md). A marker is
written without a date → [`../anti-patterns/a-draft-with-no-date.md`](../anti-patterns/a-draft-with-no-date.md).
