# A note that grew into a document

**Smell.** `rules/labels.md` with `## Creation`, `## Voiding` and `## Bulk printing`, six rules under
them, and a table of ids near the top. It started as one rule and accreted the neighbours, because
each one was related and the file was already open.

**Why it is wrong.** Everything a note can do, it can now only do to the wrong scope. Marking the
voiding rule draft makes the whole note look unsettled; superseding one statement means a diff
touching five others; a story citing the note cites all six rules, so nobody can tell which one its
criterion tests. Backlinks degrade the same way — the note collects every inbound link to anything
inside it, so "what depends on this rule?" has no answer any more. And the contradiction that
reconciliation exists to catch is now *inside* a paragraph, where no query and no reader will find
it.

**Instead.** One note, one statement, 25 lines of body. Split what grew: each rule keeps its own id,
status, source and dates, and the notes cross-link. The grouping you wanted is a property — `topic:
labels` — and the view of it is the MOC, which costs nothing to maintain. Where the long content is
genuinely one thing, a field map or a state machine, it is a reference note and the rules link to it
([`../principles/one-note-one-fact.md`](../principles/one-note-one-fact.md),
[`../patterns/reference-note.md`](../patterns/reference-note.md)).
