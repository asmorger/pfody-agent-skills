# An unanchored rule

**Smell.** A rule note that reads like settled fact, with `status: confirmed` and `sources: []`. "An
order on credit hold cannot be labelled." True, probably. From where, nobody knows.

**Why it is wrong.** A knowledge base is read by people who will not check it — that is the whole
point of having one — so an unanchored rule is believed exactly as strongly as an anchored one. The
cost lands on whoever builds from it, and it compounds: the next source arrives, contradicts the rule,
and reconciliation cannot weigh the conflict because one side has no authority level. The empty
`sources` also leaves the note an orphan in the graph, so nothing leads a reader to the evidence that
does not exist. And it cannot be defended commercially — "we never agreed to that" has no answer.

**Instead.** Anchor it or flag it. Anchored means `sources` holds a wikilink to a real source note,
with `authority` beside it. Flagged means `status: draft` with a dated callout naming the stakeholder
it waits on, or `status: needs-review` when it was inherited and nobody knows. Both take one property
and one callout. Backfilling an adopted base means adding statuses and questions, never inventing the
source that would have justified it
([`../principles/anchor-or-flag.md`](../principles/anchor-or-flag.md),
[`../patterns/source-note.md`](../patterns/source-note.md)).
