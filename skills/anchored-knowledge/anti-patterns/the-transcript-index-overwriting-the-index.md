# The transcript index overwriting the index

**Smell.** `transcript-knowledge-base` run with its defaults, which render to `knowledge-index.md`
and `knowledge-index.state.json`. This base's orientation document is also `knowledge-index.md`. The
run reports success.

**Why it is wrong.** The base's index is gone, replaced by a transcript index, and nothing failed.
Worse, the two documents look superficially similar — both are generated-looking Markdown full of ids
— so a reader may not notice for a while. What is lost is the one file that tells a newcomer which
layers exist and which files they are allowed to cite, which means the next person cites a transcript
([`citing-a-transcript-as-record.md`](citing-a-transcript-as-record.md)). The state file collision
also makes the next incremental run behave unpredictably.

**Instead.** Override both paths on every run: render to the config's `transcript_index` in the
working area — default `transcript-knowledge.md` — with a matching state file beside it. The config
holds both names and requires `transcript_index` to differ from `index`, so the collision is checked
once rather than remembered every time
([`../practices/ingest-transcripts.md`](../practices/ingest-transcripts.md),
[`../patterns/knowledge-config.md`](../patterns/knowledge-config.md)).
