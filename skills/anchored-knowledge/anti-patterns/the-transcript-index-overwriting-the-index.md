# The transcript index overwriting the record

**Smell.** `transcript-knowledge-base` pointed at the record vault, because "the notes all go in the
vault anyway". Or run with its defaults from inside the vault's folder, so it writes `moc/`,
`items/`, `meetings/` and `bases/` alongside the record. The run reports success.

**Why it is wrong.** That renderer **owns every file it writes** and deletes the ones it no longer
generates on the next run; it cannot tell a hand-written rule from a statement it rendered last
month. Its manifest limits the deletions to files it created, so a promoted note survives — what does
not survive is the distinction. The vault now holds `transcript-item` notes in the same graph, the
same searches and the same Bases views as the rules, every one of them a thing somebody said once
rather than a thing the project agreed. So the next person cites a transcript as source of record
([`citing-a-transcript-as-record.md`](citing-a-transcript-as-record.md)). A state-file collision
makes the next incremental run behave unpredictably on top of that.

**Instead.** Override both paths on every run: render into the config's `transcript_index` folder in
the workbench — default `knowledge-working/transcript-knowledge/` — with its state file beside it.
Then **promote** what belongs in the record: the meeting notes become source notes with ids and
authority, and the statements are reconciled into rules rather than copied. The config holds both
paths so the collision is checked once rather than remembered every time
([`../practices/ingest-transcripts.md`](../practices/ingest-transcripts.md),
[`../patterns/knowledge-config.md`](../patterns/knowledge-config.md)).
