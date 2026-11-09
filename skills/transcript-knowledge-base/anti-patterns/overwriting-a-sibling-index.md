# Overwriting a sibling index

**Smell.** The tool run with its defaults — `knowledge-index.md` and `knowledge-index.state.json` —
inside a project that already keeps a knowledge base with a file of that name. The run reports
success.

**Why it is wrong.** The other document is gone, and nothing failed. The two look superficially alike,
both being generated-looking markdown full of ids, so it can go unnoticed for a while. What is
typically destroyed is the calling base's orientation document: the one file that tells a newcomer
which layers exist and which of them they are allowed to cite — so the next person cites a transcript
as source of record. The state file collision is the second half: two tools writing one state file
makes every later incremental run behave unpredictably.

**Instead.** Override `index_path` and `state_path` in the config on every embedded run, and put both
somewhere that belongs to this skill — a working directory, not the record. A caller driving this
skill is responsible for naming them; `anchored-knowledge` does exactly that, rendering to
`transcript-knowledge.md` with its own state file beside it
([`../patterns/tool-config.md`](../patterns/tool-config.md),
[`../practices/prepare-the-briefs.md`](../practices/prepare-the-briefs.md)).
