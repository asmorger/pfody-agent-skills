# Evidence is never discarded

**Rule.** When the same rule appears in several meetings, the sources accumulate on one item. When a
rule replaces an older one, the older item is marked `superseded` and keeps its sources. Nothing is
deleted.

**Why.** The accumulated sources are the index's strongest output: a rule cited to three meetings
across four months is a different kind of fact from a rule somebody mentioned once, and only the
source list shows that. Supersession carries the same weight in reverse — "we used to think one label
per order" with its original citation is the answer to why the code looks the way it does, and
deleting the item destroys the only record that the earlier understanding was ever agreed. The tool
is built around this: merging duplicates **appends** sources rather than replacing them.

**In the index.**
- Prefer one well-worded item with several sources over several near-duplicates
  ([`../practices/extract-knowledge-items.md`](../practices/extract-knowledge-items.md)).
- Reuse an existing item's category name exactly, so a restated rule lands in the right section and
  can merge ([`../patterns/category-taxonomy.md`](../patterns/category-taxonomy.md)).
- Mark a replacement with `supersedes`, naming the id or the statement it replaces
  ([`../patterns/supersession.md`](../patterns/supersession.md)).
- Dedup is lexical, over keywords. Two phrasings of one rule may not auto-merge; lower
  `dedup_threshold`, or align the wording deliberately
  ([`../practices/curate-a-large-corpus.md`](../practices/curate-a-large-corpus.md)).

**Breaks when.** A replaced item is removed instead of marked →
[`../anti-patterns/deleting-a-superseded-item.md`](../anti-patterns/deleting-a-superseded-item.md).
