# Promote to the record

**When** the user has approved proposals drafted in the workbench. The one-way gate from working
knowledge to the shared source of record.

**Why.** Promotion is the single visible moment where a statement stops being a note and becomes
something a build can rely on. Keeping it explicit is what lets capture be fast without the record
filling with half-finished notes.

**Steps.**

1. **Confirm the approval covers what you are about to write** — including the existing rules the
   change also touches, not only the new ones
   ([`../principles/propose-then-apply.md`](../principles/propose-then-apply.md)).
2. **Write each approved note into the vault** with its id in `id` and `aliases`, its `sources`, its
   `status` and the dates that status needs. A confirmed rule carries no callout at all
   ([`../patterns/note-frontmatter.md`](../patterns/note-frontmatter.md)).
3. **Point each note's `sources` at its source note**, writing the source note first if it does not
   exist. Provenance is part of the change, not a follow-up; the source note's backlinks then show
   what it anchored, with nobody maintaining a list
   ([`../patterns/source-note.md`](../patterns/source-note.md)).
4. **Close the working draft** — remove it or mark it converted — and archive the intake entry whose
   content you just promoted.
5. **Lint and regenerate.** Every wikilink must resolve, no new note may be an orphan, and the
   snapshots must match the notes before you report
   ([`regenerate-the-mocs.md`](regenerate-the-mocs.md)).
6. **Leave evidence where it is.** Raw sources and the transcript index stay in the workbench
   ([`../principles/two-directories-promote-to-commit.md`](../principles/two-directories-promote-to-commit.md)).
7. **Refresh the home note's Now and Recently changed**, which are judgement rather than a query
   ([`../patterns/home-note.md`](../patterns/home-note.md)).
8. **Report the exact ids**: added, changed, deprecated, and any `CH-`, `SW-` or `Q-` notes opened.
9. **Commit through `git-guide`** when the record is git-managed: save as a private checkpoint naming
   those ids in the message, then publish to open a review. Never auto-commit, and never commit the
   workbench ([`../principles/git-goes-through-git-guide.md`](../principles/git-goes-through-git-guide.md)).

**Done when** the vault holds the approved notes with ids, sources and statuses, the lint is clean,
the snapshots match the notes, the working drafts are closed, the user has the exact id list, and
only the vault was committed.
