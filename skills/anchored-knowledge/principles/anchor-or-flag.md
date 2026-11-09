# Anchor or flag

**Rule.** Every durable statement either names the source it came from in `sources`, or wears its
uncertainty: `status: draft` with a date and the stakeholder it is pending on, or
`status: needs-review`. There is no third state. A note reading `status: confirmed` with an empty
`sources` is not allowed to exist.

**Why.** A knowledge base is read by people who will not check it — that is the point of having one.
So an unanchored statement is believed exactly as strongly as an anchored one, and the cost lands on
whoever builds from it. Flagging is the cheap half of the rule: a dated `Draft` marker costs one
clause and tells a reader precisely how much weight to put on the sentence, which is more useful than
a rule that is quietly right.

**In the base.**
- **Provenance has one home: the `sources` property**, holding a wikilink to each source note. The
  source note's backlinks are then the list of what it anchored, always current and maintained by
  nobody ([`../patterns/source-note.md`](../patterns/source-note.md)).
- `authority` is recorded beside it, from the source, so a later conflict can be weighed
  ([`authority-is-explicit.md`](authority-is-explicit.md)).
- A `draft` or `needs-review` note carries one callout naming the date and the stakeholder it waits
  on. A confirmed note carries none — `status`, `confirmed` and `sources` already say it
  ([`../patterns/status-callouts.md`](../patterns/status-callouts.md)).
- Status vocabulary for a rule, fact or boundary: `draft` · `confirmed` · `needs-review` ·
  `superseded` · `out-of-scope` · `rejected`
  ([`../references/vault-convention.md`](../references/vault-convention.md) §5).

**Breaks when.** A statement is recorded with neither a source nor a marker →
[`../anti-patterns/an-unanchored-rule.md`](../anti-patterns/an-unanchored-rule.md). A marker is
written without a date → [`../anti-patterns/a-draft-with-no-date.md`](../anti-patterns/a-draft-with-no-date.md).
