# Ingest transcripts

**When** the source is a folder of meeting or call transcripts. This skill does not parse them.

**Why.** Reading a transcript by hand produces a summary — plausible, uncited, and quietly lossy about
the reversal at minute 73. The transcript skill produces per-turn citations and content hashes, so a
re-run folds in only what is new.

**Steps.**

1. **Confirm the folder** from the config's `transcripts_folder`, or ask for it and record the answer.
2. **Invoke the `transcript-knowledge-base` skill** on that folder. Do not hand-parse, extract or
   summarise the files here
   ([`../principles/transcripts-are-delegated.md`](../principles/transcripts-are-delegated.md)).
3. **Override both output paths.** Render the index to the config's `transcript_index` in
   `working_dir` — default `transcript-knowledge.md` — with a matching state file. The transcript
   skill's own defaults are `knowledge-index.md` and `knowledge-index.state.json`, which would
   overwrite this base's index
   ([`../anti-patterns/the-transcript-index-overwriting-the-index.md`](../anti-patterns/the-transcript-index-overwriting-the-index.md)).
4. **Register the index as a supplemental source**, with its authority level and a note saying it is
   not citable as record
   ([`../patterns/source-register-row.md`](../patterns/source-register-row.md)).
5. **Reconcile its items into the Reference Layer**
   ([`reconcile-against-the-rules.md`](reconcile-against-the-rules.md)). The index is input to
   reconciliation, not an output of it.
6. **Leave the index and the raw transcripts in the working area**, permanently. They are evidence,
   not record ([`../principles/two-directories-promote-to-commit.md`](../principles/two-directories-promote-to-commit.md)).
7. **Re-run the same way** when new transcripts land. The content hashes make it incremental, so the
   cost of staying current is small — which is the point of delegating.

**Done when** the index exists at the config's path with its own state file, the base's own index is
untouched, the index has a register row marked supplemental, and its items have been reconciled
rather than appended.

**Note.** A statement that exists only in the transcript index cannot be cited by a story or a test.
Promote it into the Reference Layer first
([`../principles/only-the-reference-layer-is-citable.md`](../principles/only-the-reference-layer-is-citable.md)).
