# Every item carries a source

**Rule.** Every item has at least one source with a real `turn_id` and a short `quote` copied from the
brief, plus the meeting, date, speaker and timestamp. Never invent a turn id, a speaker, a timestamp
or a quote. If you cannot cite it, drop the item.

**Why.** The citation is the entire difference between this document and a summary. A sourced index
can be checked a year later by someone who was not in the meeting, and it can be defended — "where
did that come from" has an answer that names a speaker and a minute. An invented citation is worse
than no citation, because it makes an unverifiable statement look verified, and the place it will be
discovered is a commercial conversation. The tool enforces the floor: `validate()` rejects an item
with empty sources and `merge` drops unsourced items and reports the count, so a fabricated citation
is the only way an unsourced statement reaches the index.

**In the index.**
- Copy the `turn_id` and the quote from the brief line you are citing
  ([`../patterns/transcript-brief.md`](../patterns/transcript-brief.md)). Do not retype either.
- The quote is short — the supporting words, not the paragraph around them.
- Some exports carry no speaker labels. Then the citation is meeting and date, and the speaker field
  is empty — not guessed.
- One well-worded item with several sources beats several near-duplicates
  ([`evidence-is-never-discarded.md`](evidence-is-never-discarded.md)).
- The verbatim quote and timestamp live in the state file, not in the rendered document
  ([`../patterns/state-file.md`](../patterns/state-file.md)).

**Breaks when.** A citation is constructed to support a statement →
[`../anti-patterns/an-invented-citation.md`](../anti-patterns/an-invented-citation.md).
