# Adopt an existing base

**When** the project already has knowledge files — someone else's structure, an older convention, or
a half-finished attempt.

**Why.** A rename breaks every reference anybody has already written: code comments, story citations,
bookmarks, links in a wiki. The base's value is continuity, so an improvement bought with continuity
is usually a net loss.

**Steps.**

1. **Record the real names** in the config, verbatim — folders, filenames, and, where there is
   already an Obsidian vault, its **property names and tag taxonomy** too
   ([`../patterns/knowledge-config.md`](../patterns/knowledge-config.md)). Nothing is renamed unless
   the user asks, because renaming a property silently empties every Bases view the team had.
2. **Detect the id scheme** from what the files already do — prefixes, widths, zero-padding, ADR
   numbering. Reuse it. If you cannot reconcile it, **ask the user to confirm before minting any new
   id** ([`../principles/ids-are-immutable.md`](../principles/ids-are-immutable.md)).
3. **Improve structure, not naming.** A rules document becomes one note per rule, keeping every id;
   a glossary without categories gains a `category` property. Say what you changed and why — a
   document-to-notes split is a large diff and the user should approve its shape first
   ([`../patterns/business-rule-note.md`](../patterns/business-rule-note.md)).
4. **Accept the vault's existing dialect when reading** — `state` instead of `status`, Title Case
   values, relative markdown links instead of wikilinks — and write what the vault writes
   ([`../patterns/note-frontmatter.md`](../patterns/note-frontmatter.md)).
5. **Adopt the project's vocabulary**, including where a better word exists. Record the team's term in
   the glossary and keep your preference out of it
   ([`../principles/match-the-projects-voice.md`](../principles/match-the-projects-voice.md)).
6. **Backfill provenance rather than rewriting content.** An unanchored rule gets
   `status: needs-review` and a question, not a deletion and not an invented source
   ([`../principles/anchor-or-flag.md`](../principles/anchor-or-flag.md)).
7. **Audit what you adopted** — run the lint, and hand the user a punch list rather than fixing it
   all silently ([`audit-the-base.md`](audit-the-base.md)).

**Done when** the config names every real folder, filename and property, the existing id scheme is
reused or explicitly confirmed, nothing was renamed, and the user has a list of what the adopted base
is missing.
