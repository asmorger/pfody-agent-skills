# Transcripts are delegated

**Rule.** This skill does not parse transcripts. A folder of meeting or call transcripts goes to the
`transcript-knowledge-base` skill, which change-detects, parses and renders a sourced index with
per-turn citations. That index lands in the workbench, is registered as a **supplemental** source,
and is reconciled in — never cited as the source of record.

**Why.** Two different jobs with two different failure modes. Reading a transcript by hand produces a
summary: plausible, uncited, and quietly lossy about the reversal buried at minute 73. The transcript
skill produces per-turn citations with content hashes, so a re-run folds in only what is new and
every statement keeps the quote behind it. Reconciliation then does the part a parser cannot — judging
each item against the existing rules. Keeping the two separate is also what makes re-ingestion cheap,
which is what makes a base stay current.

**In the base.**
- Render into the config's `transcript_index` folder in `working_dir`, with its state file beside it
  ([`../practices/ingest-transcripts.md`](../practices/ingest-transcripts.md)).
- **It owns every file in its output folder** and deletes what it no longer generates, so that folder
  is never the record vault. Override both paths, every time
  ([`../anti-patterns/the-transcript-index-overwriting-the-index.md`](../anti-patterns/the-transcript-index-overwriting-the-index.md)).
- Promote the meeting notes it wrote into `sources/` with ids and authority, then reconcile its
  statements into the Reference Layer
  ([`../practices/reconcile-against-the-rules.md`](../practices/reconcile-against-the-rules.md)).
- The index stays in the workbench permanently. It is evidence, not record.

**Breaks when.** A transcript is read and summarised here →
[`../anti-patterns/hand-parsing-a-transcript.md`](../anti-patterns/hand-parsing-a-transcript.md).
