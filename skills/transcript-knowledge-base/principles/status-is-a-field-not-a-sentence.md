# Status is a field, not a sentence

**Rule.** Set `status` — `confirmed`, `tentative`, `draft`, `pending`, `deferred`, `superseded` — and
put a short qualifier in `note`. Never bury the caveat in the statement itself.

**Why.** The statement has to stay a clean rule, because that is what makes the note's heading
readable and the statement mergeable: the dedup compares statements, so "Labels are created per
parcel (pending Dana's confirmation)" will not match the same rule confirmed in a later meeting. The
status property is also the only version anything can filter, count or query — a Bases view reads
`status`, and so does every downstream tool. A caveat in prose is invisible to all of it, and gets
lost the moment anyone quotes the rule into a specification, which is precisely when it mattered.

**In the index.**
- `deferred` and the explicit out-of-scope cases get a status, not a rewritten sentence. The statement
  still says what the behaviour is.
- `note` is short: "pending operations lead confirmation", "revisit after Phase 1". Not a paragraph.
- The render puts `status` in the note's frontmatter and, for anything other than `confirmed`, adds
  one callout carrying `note` — so the reader sees it without the statement having carried it
  ([`../patterns/vault-notes.md`](../patterns/vault-notes.md)).
- A statement whose truth depends on the caveat is usually two items: the behaviour, and the open
  question about it ([`one-rule-per-item.md`](one-rule-per-item.md)).

**Breaks when.** The hedge is written into the rule →
[`../anti-patterns/caveats-buried-in-the-statement.md`](../anti-patterns/caveats-buried-in-the-statement.md).
