# State file

**Use when** asked where a rule's exact words are, or why a re-run skipped a file. The JSON sidecar
beside the index: the full index plus the ingestion record. Not a database — one plain file.

**Skeleton.** `knowledge-index.state.json`, in outline:

    items              keyed by id: category, statement, status, note,
                       related[], supersedes[], sources[]
    sources[]          meeting, date, speaker, timestamp, quote, file, turn_id
    categories[]       ordered, each with its name and id prefix
    ingested_files     path → content hash, for every file already folded in

The full verbatim quote, the timestamp and the turn id live here for every source, keyed to the same
item that appears in the rendered document.

**Notes.**
- This is the answer to "what exactly did they say": the rendered table gives meeting and speaker, the
  state file gives the words ([`rendered-index.md`](rendered-index.md)).
- `ingested_files` is why re-running is incremental. A file whose hash matches is skipped; a file
  whose content changed is reprocessed
  ([`../principles/the-content-hash-is-the-unit-of-work.md`](../principles/the-content-hash-is-the-unit-of-work.md)).
- Keep it beside the index and keep both together. Losing the state file means losing the quotes and
  the ingestion record — the next run reprocesses everything and the evidence appendix is gone.
- `python -m tkb.cli status --state <state.json>` reports what it holds without opening it.
- It is generated. Never edit it to fix an item; fix the extraction and re-merge
  ([`../practices/merge-the-items.md`](../practices/merge-the-items.md)).

**Related.** [`tool-config.md`](tool-config.md),
[`../practices/run-an-incremental-update.md`](../practices/run-an-incremental-update.md).
