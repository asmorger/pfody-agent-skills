# Renaming the project's files

**Smell.** `BusinessRules.md` renamed to `business-rules.md` for consistency. `decisions/` moved to
`adr/`. A team's "parcel" replaced by "shipment" because the glossary wanted one term and shipment
read better. Each change is an improvement in isolation.

**Why it is wrong.** The rename breaks every reference anybody has already written and cannot see:
code comments, story citations, bookmarks, links in a wiki, a half-finished spreadsheet. The base's
value is continuity, so an improvement bought with continuity is usually a net loss. The vocabulary
version is worse, because it makes every reader translate — the exact terminology drift the glossary
exists to kill, now introduced by the glossary.

**Instead.** Record the real names in the config's file map and use them verbatim. Improve structure
inside the file: drop a Status column, add glossary categories, split a rule that holds two ideas.
Adopt the team's word even where a better one exists, and keep retired aliases in the definition.
Rename only when the user asks for it
([`../principles/match-the-projects-voice.md`](../principles/match-the-projects-voice.md),
[`../practices/adopt-an-existing-base.md`](../practices/adopt-an-existing-base.md)).
