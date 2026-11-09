# Regenerate the MOCs

**When** after promoting anything to the vault, and at every audit. The generated snapshots are
derived from the notes, so they are only true until the next note changes.

**Why.** The embedded Bases views cannot drift — they query the notes live. The snapshots beneath
them can, and they are what a reviewer on GitHub, an agent, or a diff actually reads. A stale
snapshot is worse than no snapshot, because it looks authoritative and disagrees with the view two
lines above it.

**Steps.**

1. **Run the lint first.** `python3 scripts/vault.py lint <vault>` reports dangling wikilinks,
   orphans, notes outside the vocabularies, missing `sources` on a confirmed note, oversized notes
   and duplicate ids. A markdown file with no frontmatter is skipped — the vault may share its
   folder with the repo's other docs — but frontmatter without a `type` is a malformed note. Fix
   findings before regenerating: a snapshot built over a dangling citation propagates it
   ([`../anti-patterns/a-dangling-citation.md`](../anti-patterns/a-dangling-citation.md)).
2. **Regenerate.** `python3 scripts/vault.py moc <vault>` rewrites the block between
   `<!-- generated: … -->` and `<!-- /generated -->` in every note whose frontmatter carries a
   `snapshot` spec, and touches nothing else in the note
   ([`../patterns/moc-note.md`](../patterns/moc-note.md)).
3. **Read the diff.** It is the honest summary of what the run changed: a row appearing, a status
   moving, a rule leaving the snapshot because it was superseded. A diff you did not expect means a
   note you did not mean to change.
4. **Never fix a table by editing it.** Change the note, or change the `snapshot` spec, and
   regenerate ([`../anti-patterns/a-generated-table-edited-by-hand.md`](../anti-patterns/a-generated-table-edited-by-hand.md)).
5. **Refresh the start note by hand.** `Now` and `Recently changed` are judgement, not a query —
   which is why they are the only tables in the vault a person writes
   ([`../patterns/start-note.md`](../patterns/start-note.md)).
6. **No interpreter?** Say so and stop. Hand-writing a snapshot is how the drift starts, and a MOC
   with a stale snapshot and no generator is a MOC nobody can trust again
   ([`../principles/properties-are-the-query-surface.md`](../principles/properties-are-the-query-surface.md)).
7. **Commit the vault only**, through the `git-guide` skill when the record is git-managed
   ([`promote-to-the-record.md`](promote-to-the-record.md)).

**Done when** the lint is clean or its findings are reported, every `snapshot` block matches the
notes, the start note's `Now` reflects what is actually open, and nothing between the markers was
written by hand.
