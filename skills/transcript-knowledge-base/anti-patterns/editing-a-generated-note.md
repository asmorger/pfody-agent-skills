# Editing a generated note

**Smell.** A statement reworded directly in `items/one-label-is-created-per-parcel.md`. A status
changed from `tentative` to `confirmed` in the frontmatter. A row deleted from the MOC's table
because the statement was noise. Each is the smallest possible fix, and each is in the right place
if this were a record vault.

**Why it is wrong.** It is not a record vault. Every note in this folder is rendered from the state
file, so the next run overwrites the edit without asking — and that is the lucky outcome. The unlucky
one is that nobody re-renders for a month, the edited note is the only place the correction exists,
and then a re-run silently reverts it. Worse, a reworded statement changes its filename, so the next
render writes a *new* note and deletes the one you edited: the correction does not survive even as a
conflict. A deleted MOC row comes back on the next render looking like a regression.

**Instead.** Fix the extraction and re-run. A wrong wording means `items.json` was wrong — correct it
and `merge` again, which updates the statement and keeps the provenance. A wrong status is the same
fix. Genuine noise is a curation decision, and curation happens by re-extracting a tighter set, not
by deleting output. A statement that is *right* but needs to become record does not get promoted
here at all: `anchored-knowledge` reconciles it into the project's own vault, where notes are
hand-written and edits are the point
([`../practices/merge-the-items.md`](../practices/merge-the-items.md),
[`../principles/the-tool-does-the-mechanics.md`](../principles/the-tool-does-the-mechanics.md)).
