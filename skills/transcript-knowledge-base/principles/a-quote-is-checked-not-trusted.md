# A quote is checked, not trusted

**Rule.** Step 5 runs on every corpus, and its findings are fixed before the vault is handed on:

    python -m tkb.cli verify --vault <vault-dir> --folder <transcript-dir>

A quote survives only if the cited cue exists in that transcript, the speaker at that cue is the
speaker named, and every quoted word is in the turns at that cue. Nothing is hand-waved: a quote the
check cannot reach is reported as **unchecked**, and that count goes in the report.

**Why.** Every other check in this skill reads shape — an item has a source, an id is stable, a note
is the right size. All of them pass an extraction that moved a sentence to the wrong timestamp, put
it in the wrong person's mouth, or smoothed "we probably won't split an order" into "orders are never
split". That is not a hypothetical failure mode; it is the *only* thing step 2 can get wrong, because
step 2 is the one step with a model in it ([`the-tool-does-the-mechanics.md`](the-tool-does-the-mechanics.md)).

The cost is specific. This vault's single purpose is to be evidence — `anchored-knowledge` carries
these quotes onto the rules they anchor, and a rule's whole claim to authority is the quote under it.
An unverifiable citation is worse than no citation, because a missing quote invites a question and a
wrong quote ends one. Somebody eventually scopes work from a sentence nobody said.

**In the index.**
- Punctuation and capitalisation are ignored when matching: the transcription service supplied them,
  so they are not evidence of anything. Word order is not ignored.
- `...` or `…` marks an elision and is allowed to skip words. It cannot reorder them.
- A quote may run past a turn boundary; the check reads the cited turn and the few that follow.
- Transcripts and originals are never edited to make a quote match. A mishearing goes in the errata
  register and the quote carries the correction visibly
  ([`../patterns/errata-register.md`](../patterns/errata-register.md)).
- Fix a failing quote by re-extracting it, never by reaching into the note
  ([`../anti-patterns/editing-a-generated-note.md`](../anti-patterns/editing-a-generated-note.md)).

**Breaks when.** A quote is written from memory of the brief rather than copied from it →
[`../anti-patterns/an-invented-citation.md`](../anti-patterns/an-invented-citation.md). A quote is
tidied into a statement → [`a-statement-is-not-a-quote.md`](a-statement-is-not-a-quote.md).
