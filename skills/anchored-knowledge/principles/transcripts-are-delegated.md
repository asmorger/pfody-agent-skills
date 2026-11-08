# Transcripts are delegated

**Rule.** This skill does not parse transcripts. A folder of meeting or call transcripts goes to the
`transcript-knowledge-base` skill, which change-detects, parses and renders a sourced index with
per-turn citations. That index lands in the working area, is registered as a **supplemental** source,
and is reconciled in — never cited as the source of record.

**Why.** Two different jobs with two different failure modes. Reading a transcript by hand produces a
summary: plausible, uncited, and quietly lossy about the reversal buried at minute 73. The transcript
skill produces per-turn citations with content hashes, so a re-run folds in only what is new and
every statement keeps the quote behind it. Reconciliation then does the part a parser cannot — judging
each item against the existing rules. Keeping the two separate is also what makes re-ingestion cheap,
which is what makes a base stay current.

**In the base.**
- Render the index to the config's `transcript_index` path in `working_dir`, with a matching state
  file ([`../practices/ingest-transcripts.md`](../practices/ingest-transcripts.md)).
- Its default output name collides with this base's `knowledge-index.md`. Override both the output and
  the state file, every time
  ([`../anti-patterns/the-transcript-index-overwriting-the-index.md`](../anti-patterns/the-transcript-index-overwriting-the-index.md)).
- Register the index in the Source Register with its authority level, then reconcile its items into
  the Reference Layer ([`../practices/reconcile-against-the-rules.md`](../practices/reconcile-against-the-rules.md)).
- The index stays in the working area permanently. It is evidence, not record.

**Breaks when.** A transcript is read and summarised here →
[`../anti-patterns/hand-parsing-a-transcript.md`](../anti-patterns/hand-parsing-a-transcript.md).
