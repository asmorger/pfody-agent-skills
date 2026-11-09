# Renumbered rule ids

**Smell.** `ORDER-4` was deprecated, so `ORDER-5`'s frontmatter was changed to `ORDER-4` and the
topic numbers run cleanly again. Or the ids were re-sorted to match the MOC's new ordering. The
snapshot is tidier than it was.

**Why it is wrong.** The id is the entire value of this base to everything downstream — a story's
source grounding, an acceptance criterion, a test name, a pull request, a tracker tag, another rule's
cross-link. Renumbering re-points every one of those at a different rule, and nothing fails: the test
still passes, against the wrong rule. The damage is also invisible from inside the base, because all
its internal cross-links were updated in the same pass.

**Instead.** Take the next free number for the topic — position, ordering and number are unrelated.
Leave gaps where rules were deprecated; a gap is information. And note what immutability does *not*
cover: the **title and filename** may be reworded whenever a better wording is found, because the id
lives in frontmatter and Obsidian rewrites the filename half of every
`[[confirmed-order-may-split-across-parcels|ORDER-5]]` that points at it. Refine wording
aggressively, never the id
([`../principles/ids-are-immutable.md`](../principles/ids-are-immutable.md),
[`../practices/write-a-business-rule.md`](../practices/write-a-business-rule.md)).
