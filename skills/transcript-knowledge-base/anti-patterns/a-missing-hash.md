# A missing hash

**Smell.** `processed_files` entries with `path`, `name`, `meeting` and `date` and no `hash` — or a
hash that was shortened, recomputed or made up because the manifest was not to hand. Everything works.
The index is correct.

**Why it is wrong.** The hash is what marks a file ingested, so without it the file is processed again
on every run, forever. The failure is quiet in the worst way: nothing errors, and each run re-reads
the whole corpus and re-extracts items that merge harmlessly into themselves. Nobody notices until a
run takes an hour, and the usual diagnosis is that the tool is slow. An *invented* hash is worse — it
marks a file ingested that may never have been read, so a real transcript is skipped permanently and
silently.

**Instead.** Copy the `hash` from the manifest's `files[]`, verbatim, for every file in the batch —
including a file that yielded no items, because an empty brief is still ingested. On a batched run,
merge after each batch so the hashes land as you go
([`../principles/the-content-hash-is-the-unit-of-work.md`](../principles/the-content-hash-is-the-unit-of-work.md),
[`../practices/batch-long-transcripts.md`](../practices/batch-long-transcripts.md)).
