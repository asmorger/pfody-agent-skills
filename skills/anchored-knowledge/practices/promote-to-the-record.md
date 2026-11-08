# Promote to the record

**When** the user has approved proposals drafted in the working area. The one-way gate from working
knowledge to the shared source of record.

**Why.** Promotion is the single visible moment where a statement stops being a note and becomes
something a build can rely on. Keeping it explicit is what lets capture be fast without the record
filling with half-finished notes.

**Steps.**

1. **Confirm the approval covers what you are about to write** — including the existing rules the
   change also touches, not only the new ones
   ([`../principles/propose-then-apply.md`](../principles/propose-then-apply.md)).
2. **Write each approved entry into the record** with its id, its anchors, and the right marker: a
   confirmed rule has no `Draft` marker and carries `(confirmed YYYY-MM-DD)` on the decided clause
   ([`../patterns/inline-status-markers.md`](../patterns/inline-status-markers.md)).
3. **Update the Source Register row** for each source to name the rule ids it updated. The provenance
   is part of the change, not a follow-up
   ([`../patterns/source-register-row.md`](../patterns/source-register-row.md)).
4. **Close the working draft** — remove it or mark it converted — and archive the intake entry whose
   content you just promoted.
5. **Leave evidence where it is.** Raw sources and the transcript index stay in the working area
   ([`../principles/two-directories-promote-to-commit.md`](../principles/two-directories-promote-to-commit.md)).
6. **Report the exact ids**: added, changed, deprecated, and any `CH-`, `SW-` or `Q-` entries opened.
7. **Commit through `git-guide`** when the record is git-managed: save as a private checkpoint naming
   those ids in the message, then publish to open a review. Never auto-commit, and never commit the
   working area ([`../principles/git-goes-through-git-guide.md`](../principles/git-goes-through-git-guide.md)).

**Done when** the record holds the approved entries with ids, anchors and correct markers, every
touched source row names the ids it updated, the working drafts are closed, the user has the exact
id list, and only the record was committed.
