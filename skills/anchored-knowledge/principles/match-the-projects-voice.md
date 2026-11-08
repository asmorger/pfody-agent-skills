# Match the project's voice

**Rule.** Adopt what the project already uses: its filenames, its id prefixes, its terminology, its
ADR format. Record the real names in the config's file map and use them verbatim. Where an existing
structure is weak, improve the structure — never rename the file to the default.

**Why.** A rename breaks every reference anybody has already written: links from code comments,
bookmarks, story citations, a half-finished wiki page. The base's value is continuity, so an
improvement that costs continuity is usually a net loss. Vocabulary matters for the same reason one
level down — the team says "parcel" and the base says "shipment", and now every reader translates,
which is exactly the terminology drift the glossary exists to kill. Consistency beats novelty here,
including novelty that is better.

**In the base.**
- Existing filenames differ from the defaults? The recorded names win; nothing is renamed silently
  ([`../practices/adopt-an-existing-base.md`](../practices/adopt-an-existing-base.md)).
- Existing id scheme? Detect and reuse it. If you cannot reconcile it, ask the user to confirm before
  minting any new id ([`ids-are-immutable.md`](ids-are-immutable.md)).
- Reading an existing file, accept what it does — an em-dash or a colon after `Draft`, for instance.
  Write the house form in new text only
  ([`../patterns/inline-status-markers.md`](../patterns/inline-status-markers.md)).
- Reconcile aliases in the glossary rather than picking a winner by fiat: write the term as
  `**Term** (Alias)` and keep retired aliases in the definition.

**Breaks when.** Files or terms are renamed to the skill's defaults →
[`../anti-patterns/renaming-the-projects-files.md`](../anti-patterns/renaming-the-projects-files.md).
