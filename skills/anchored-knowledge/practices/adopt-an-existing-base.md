# Adopt an existing base

**When** the project already has knowledge files — someone else's structure, an older convention, or
a half-finished attempt.

**Why.** A rename breaks every reference anybody has already written: code comments, story citations,
bookmarks, links in a wiki. The base's value is continuity, so an improvement bought with continuity
is usually a net loss.

**Steps.**

1. **Record the real names** in the config's file map, verbatim, and use them for the rest of the run
   ([`../patterns/knowledge-config.md`](../patterns/knowledge-config.md)). Nothing is renamed unless
   the user asks.
2. **Detect the id scheme** from what the files already do — prefixes, widths, zero-padding, ADR
   numbering. Reuse it. If you cannot reconcile it, **ask the user to confirm before minting any new
   id** ([`../principles/ids-are-immutable.md`](../principles/ids-are-immutable.md)).
3. **Improve structure, not naming.** A `business-rules.md` with a Status column keeps its filename
   and loses the column; a glossary without categories gains headings. Say what you changed and why.
4. **Accept the file's existing dialect when reading** — an em-dash or a colon after `Draft`, a
   different date format — and write the house form only in new text
   ([`../patterns/inline-status-markers.md`](../patterns/inline-status-markers.md)).
5. **Adopt the project's vocabulary**, including where a better word exists. Record the team's term in
   the glossary and keep your preference out of it
   ([`../principles/match-the-projects-voice.md`](../principles/match-the-projects-voice.md)).
6. **Backfill provenance rather than rewriting content.** An unanchored rule gets a `Needs Review`
   marker and a question, not a deletion and not an invented source
   ([`../principles/anchor-or-flag.md`](../principles/anchor-or-flag.md)).
7. **Audit what you adopted** and hand the user a punch list rather than fixing it all silently
   ([`audit-the-base.md`](audit-the-base.md)).

**Done when** the config names every real file, the existing id scheme is reused or explicitly
confirmed, nothing was renamed, and the user has a list of what the adopted base is missing.
