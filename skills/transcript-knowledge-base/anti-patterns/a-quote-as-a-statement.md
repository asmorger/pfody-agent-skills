# A quote as a statement

**Smell.** `"statement": "Per parcel, not per order."` `"statement": "Dana said they'd probably go
with SSO I think."` `"statement": "yeah so the address gets locked at that point"`. Faithful to the
meeting, useless in a table.

**Why it is wrong.** The statement will be read on its own, as one row, by someone who was not in the
room — so a fragment that depended on the previous turn says nothing, and a hedge reported as a hedge
cannot be built from or tested. It also breaks the mechanical half: the dedup compares statements, so
a conversational phrasing will not match the same rule said plainly in another meeting, and the index
grows two items where it should have grown one with two sources.

**Instead.** Synthesise the rule and leave the words where they belong. "One label is created per
parcel; a split order produces several labels." Present tense, declarative, self-contained, roles
instead of names, no "this" or "as above". The speaker's actual words go in the source's `quote`,
where being verbatim is the requirement — so the index gets both properties instead of a compromise
([`../principles/a-statement-is-not-a-quote.md`](../principles/a-statement-is-not-a-quote.md),
[`../patterns/knowledge-item.md`](../patterns/knowledge-item.md)).
