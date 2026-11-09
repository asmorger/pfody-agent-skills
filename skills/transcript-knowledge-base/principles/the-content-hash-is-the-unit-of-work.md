# The content hash is the unit of work

**Rule.** Copy each processed file's `hash` from the manifest into `processed_files` in `items.json`.
That is what marks the file ingested. Without it the file is processed again on every run, forever.

**Why.** The hash is why re-running is cheap, and cheap re-running is why the index stays current. It
also makes the incremental path identical to the first run — `prepare` surfaces whatever has changed,
so there is no separate initial mode to get wrong. The failure is quiet in the worst way: everything
works, the index is correct, and each run re-reads the whole corpus and re-extracts items that merge
into themselves. Nobody notices until the run takes an hour, and the usual diagnosis is that the tool
is slow.

**In the index.**
- The manifest's `files[]` carries the hash. Copy it verbatim — do not compute, shorten or guess one
  ([`../patterns/items-json.md`](../patterns/items-json.md)).
- `processed_files` lists every file you actually read in this batch, including one that yielded no
  items. A brief with nothing durable in it is still ingested
  ([`precision-over-volume.md`](precision-over-volume.md)).
- Hashes are over content, so a re-run after an edited transcript correctly reprocesses that file and
  only that file ([`../practices/run-an-incremental-update.md`](../practices/run-an-incremental-update.md)).
- Batching long corpora means merging after each batch, so each batch's hashes land
  ([`../practices/batch-long-transcripts.md`](../practices/batch-long-transcripts.md)).

**Breaks when.** The hash is left out or invented →
[`../anti-patterns/a-missing-hash.md`](../anti-patterns/a-missing-hash.md).
