# Render the index

**When** the merge is done. Step 4 — it writes the deliverable.

**Why.** Render is pure output: it reads the state and writes the document. Keeping it separate is why
a bad extraction can be fixed and re-rendered without touching the index by hand.

**Steps.**

1. **Run it:**

       python -m tkb.cli render --out knowledge-index.md --state knowledge-index.state.json

2. **Pass `--config`** when the paths, title, intro or category order are not the defaults
   ([`../patterns/tool-config.md`](../patterns/tool-config.md)).
3. **Read the result.** Per-category tables of `| ID | Rule | Sources |`, status folded inline, and
   the evidence appendix behind every id
   ([`../patterns/rendered-index.md`](../patterns/rendered-index.md)).
4. **Check the index and state sit together.** The document gives meeting, date and speaker; the state
   file holds the verbatim quotes and timestamps. Separated, the evidence is gone
   ([`../patterns/state-file.md`](../patterns/state-file.md)).
5. **Report the counts**: items, categories, files ingested, unsourced items dropped. They tell the
   reader how much curation is left.
6. **Say what it is.** On a small corpus it is a document. On a large one it is a sourced superset to
   curate, and that must be said rather than implied
   ([`../principles/a-large-corpus-is-a-superset.md`](../principles/a-large-corpus-is-a-superset.md)).
7. **Re-render freely.** It is idempotent, so a wording or config change is one command, never an
   edit to the output.

**Done when** the index exists at the configured path with its state file beside it, the counts are
reported, and the user has been told whether they are holding a finished document or a superset to
curate.
