# Renaming the project's files

**Smell.** An existing vault's `Decisions/` moved to `decisions/` for consistency. Its `state`
property rewritten to `status`. Its `#adr` tag changed to `#decision`. A team's "parcel" replaced by
"shipment" because the glossary wanted one term and shipment read better. Each is an improvement in
isolation.

**Why it is wrong.** The rename breaks every reference anybody has written and cannot see: code
comments, story citations, bookmarks, a half-finished spreadsheet. Obsidian rewrites the links inside
the vault, which is exactly what makes this dangerous — it looks clean from inside and is broken
everywhere else. A renamed **property** is worse than a renamed folder, because it silently empties
every Bases view and template the team already had. The vocabulary version is worst: it makes every
reader translate, which is the terminology drift the glossary exists to kill.

**Instead.** Record the vault's real folders, property names and tags in the config and write what
the vault writes. Improve structure without renaming: split a note that holds two ideas, add the
missing `sources`, give a term its retired alias. Adopt the team's word even where a better one
exists. Rename only when the user asks for it
([`../principles/match-the-projects-voice.md`](../principles/match-the-projects-voice.md),
[`../practices/adopt-an-existing-base.md`](../practices/adopt-an-existing-base.md)).
