# Deleting a superseded item

**Smell.** The November meeting established labels are per parcel, so `LABEL-1` — one label per order,
agreed in January — was removed from the index. Or an item quietly rewritten in place to the new
understanding, keeping its id and dropping its January sources.

**Why it is wrong.** The superseded item with its original citation is the answer to the question
people actually ask: why does the existing code assume one label per order? Delete it and the answer
is gone, along with the evidence that the earlier understanding was ever agreed — which is a
commercial record, not just a historical one. Rewriting in place is worse, because the item now
carries January's sources in support of November's rule, which is a false citation created by an
otherwise reasonable edit.

**Instead.** Add the new item with `supersedes` naming the old id. The merge marks the old one
`superseded` and keeps its text, its id and all its sources; the render folds the status inline so a
reader sees both rules and which one holds. Use `note` to say in a clause what changed. Nothing is
deleted, and the index gains the history for free
([`../principles/evidence-is-never-discarded.md`](../principles/evidence-is-never-discarded.md),
[`../patterns/supersession.md`](../patterns/supersession.md)).
