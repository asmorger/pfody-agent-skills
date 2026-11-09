# A large corpus yields a superset

**Rule.** With dozens of transcripts, treat the generated index as a fully-sourced **superset to
curate**, not a finished document. Say so when you hand it over, and name the two things that need
curation: status items to prune, near-duplicates to merge.

**Why.** Both limits are structural, not bugs to be fixed by trying harder. Dedup is lexical — Jaccard
over keywords — so the same rule phrased differently across two meetings will sometimes not merge, and
one topic sprawls across several items. Extraction over-reaches on status-heavy meetings, because a
standup sentence looks grammatically identical to a rule. Presenting the output as finished transfers
confidence it has not earned; presenting it as a sourced superset is accurate and still valuable,
because every line in it can be checked, which is the expensive part.

**In the index.**
- Expect sprawl on a large corpus and name it. Lower `dedup_threshold` to merge more aggressively, or
  add a curation pass ([`../practices/curate-a-large-corpus.md`](../practices/curate-a-large-corpus.md)).
- A person, or a dedicated consolidation step, prunes and merges. The tool will not do it, and neither
  should a single extraction pass.
- The deterministic steps do scale — thousands of items, large `.docx` corpora, sub-second merges. The
  quality limit is extraction, and it is domain-independent.
- Report the counts: items, categories, files ingested, unsourced items dropped. They are what tell a
  reader how much curation is left.

**Breaks when.** The generated index is handed over as a finished document →
[`../anti-patterns/the-generated-index-shipped-as-finished.md`](../anti-patterns/the-generated-index-shipped-as-finished.md).
