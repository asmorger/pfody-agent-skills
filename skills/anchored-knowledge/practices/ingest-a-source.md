# Ingest a source

**When** a new source arrives that is not a transcript: a SOW, requirements, an email, a Q&A, a
sample file, a chat log, a developer doc. Standing operating procedure B.

**Why.** The expensive failure is a source read, summarised and appended — because the summary is
plausible, uncited, and never checked against the rules it contradicts.

**Steps.**

1. **Get the latest first** when the record is git-managed, through the `git-guide` skill.
   Reconciling against a stale rule set produces an audit that is wrong in both directions
   ([`../principles/git-goes-through-git-guide.md`](../principles/git-goes-through-git-guide.md)).
2. **Route by type.** A folder of transcripts is not this procedure — delegate it
   ([`ingest-transcripts.md`](ingest-transcripts.md)).
3. **Read the full source.** Not the summary, not the first screen; a source worth registering is
   worth reading to the end.
4. **Capture it in intake**, in the working area: the source, raw bullets, and a triage destination
   for each one ([`../patterns/intake-entry.md`](../patterns/intake-entry.md)). Keep the bullets raw.
5. **Register the source** with its authority level and location
   ([`../patterns/source-register-row.md`](../patterns/source-register-row.md),
   [`../patterns/authority-ladder.md`](../patterns/authority-ladder.md)). Register the original, not
   an extraction of it.
6. **Invent nothing.** A behaviour the source implies but does not state is a question, not a rule
   ([`../principles/anchor-or-flag.md`](../principles/anchor-or-flag.md)).
7. **Reconcile** against the existing rules
   ([`reconcile-against-the-rules.md`](reconcile-against-the-rules.md)) — this is where the work
   actually happens.
8. **Archive the intake entry** once its durable content is promoted. It is a capture buffer, not a
   parallel record.

**Done when** the source has a register row with its authority level, every durable item from it is
either promoted, proposed in an audit, or sitting as a question or scope-watch item, and nothing was
written to the record without approval.
