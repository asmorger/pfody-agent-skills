# Status is a field, not a sentence

**Rule.** Set `status` — `confirmed`, `tentative`, `draft`, `pending`, `deferred`, `superseded` — and
put a short qualifier in `note`. Never bury the caveat in the statement itself.

**Why.** The statement has to stay a clean rule, because that is what makes the rendered table
readable and the statement mergeable: the dedup compares statements, so "Labels are created per
parcel (pending Dana's confirmation)" will not match the same rule confirmed in a later meeting. The
status field is also the only version a reader can filter or count. A caveat in prose is invisible to
every mechanical step and gets lost the moment anyone quotes the rule into a specification, which is
precisely when the caveat mattered.

**In the index.**
- `deferred` and the explicit out-of-scope cases get a status, not a rewritten sentence. The statement
  still says what the behaviour is.
- `note` is short: "pending operations lead confirmation", "revisit after Phase 1". Not a paragraph.
- The render folds status inline on the rule, the way a curated document flags drafts — so the reader
  sees it without the statement having carried it
  ([`../patterns/rendered-index.md`](../patterns/rendered-index.md)).
- A statement whose truth depends on the caveat is usually two items: the behaviour, and the open
  question about it ([`one-rule-per-item.md`](one-rule-per-item.md)).

**Breaks when.** The hedge is written into the rule →
[`../anti-patterns/caveats-buried-in-the-statement.md`](../anti-patterns/caveats-buried-in-the-statement.md).
