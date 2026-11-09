# State file

**Use when** asked why a re-run skipped a file, or what the notes are regenerated from. The JSON
sidecar: the full index plus the ingestion record. Not a database — one plain file.

**Skeleton.** `knowledge-index.state.json`, in outline:

    items              keyed by id: category, statement, status, note,
                       related[], supersedes[], sources[]
    sources[]          meeting, date, speaker, timestamp, quote, file, turn_id
    categories[]       ordered, each with its name and id prefix
    ingested_files     path → content hash, for every file already folded in

The verbatim quote, the timestamp and the turn id live here for every source, keyed to the same item
whose note carries them as an evidence callout.

**Notes.**
- **This is not a second home for the quotes.** They are on the notes, where a reader needs them, and
  here because this is the **merge cache** — it is regenerable, nobody reads it as knowledge, and it
  is what makes an incremental run possible
  ([`vault-notes.md`](vault-notes.md)).
- `ingested_files` is why re-running is incremental. A file whose hash matches is skipped; a file
  whose content changed is reprocessed
  ([`../principles/the-content-hash-is-the-unit-of-work.md`](../principles/the-content-hash-is-the-unit-of-work.md)).
- Losing it costs the ingestion record, not the knowledge: the notes still hold every statement and
  its evidence, but the next run reprocesses every transcript and re-mints every id. Keep it with the
  vault it renders.
- `python -m tkb.cli status --state <state.json>` reports what it holds without opening it.
- It is generated. Never edit it to fix an item, and never edit a note either; fix the extraction and
  re-merge ([`../practices/merge-the-items.md`](../practices/merge-the-items.md),
  [`../anti-patterns/editing-a-generated-note.md`](../anti-patterns/editing-a-generated-note.md)).

**Related.** [`tool-config.md`](tool-config.md),
[`../practices/run-an-incremental-update.md`](../practices/run-an-incremental-update.md).
