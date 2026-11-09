# Batch long transcripts

**When** there are many transcripts, or any of them are long.

**Why.** The dedup links repeats across meetings, so merging as you go means each batch is compared
against everything already folded in. Holding every item back to one final merge loses that, and
loses every batch's hashes if the run is interrupted.

**Steps.**

1. **Group the briefs into batches** small enough to read attentively. The limit is your attention on
   the extraction, not the tool's capacity.
2. **Extract one batch at a time** to its own `items.json`
   ([`extract-knowledge-items.md`](extract-knowledge-items.md)).
3. **Merge after each batch**, before starting the next
   ([`merge-the-items.md`](merge-the-items.md)). Two reasons: the batch's hashes land, so an
   interrupted run does not repeat work; and the next batch's items dedup against this batch's.
4. **Copy each file's hash** into its batch's `processed_files`, including files that yielded no items
   ([`../principles/the-content-hash-is-the-unit-of-work.md`](../principles/the-content-hash-is-the-unit-of-work.md)).
5. **Reuse the category names** established by the earlier batches, exactly
   ([`../patterns/category-taxonomy.md`](../patterns/category-taxonomy.md)).
6. **Watch the dropped count per batch.** It is a better signal than a single count at the end,
   because it points at which batch's extraction went wrong.
7. **Render once, at the end** ([`render-the-vault.md`](render-the-vault.md)).
8. **Expect to curate afterwards** on a corpus this size
   ([`curate-a-large-corpus.md`](curate-a-large-corpus.md)).

**Done when** every brief is in exactly one batch, every batch was merged before the next began, every
file is marked ingested, and the index was rendered once from the accumulated state.
