# Caveats buried in the statement

**Smell.** `"statement": "Labels are created per parcel (pending Dana's confirmation, discussed
2026-11-08 but not finalised)."` Or an out-of-scope item rewritten into "We will not be doing bulk
printing in this phase" with `status: confirmed`.

**Why it is wrong.** The hedge is invisible to every mechanical step. The dedup compares statements,
so the parenthesised version will not merge with the same rule once it is confirmed in a later
meeting, and the index keeps both. Nothing can filter or count what is actually pending, because the
only machine-readable status field says `confirmed`. And the caveat is lost precisely when it matters:
the moment someone quotes the rule into a specification, the parenthesis is the first thing dropped.

**Instead.** The statement says what the behaviour is; `status` says how settled it is; `note` carries
the short qualifier. `status: pending` with `note: "pending operations lead confirmation"` is
filterable, countable and mergeable, and the render folds it inline on the rule anyway — so the reader
sees it without the statement having carried it. Where the statement is only true because of the
caveat, you have two items: the behaviour, and the question about it
([`../principles/status-is-a-field-not-a-sentence.md`](../principles/status-is-a-field-not-a-sentence.md),
[`../patterns/rendered-index.md`](../patterns/rendered-index.md)).
