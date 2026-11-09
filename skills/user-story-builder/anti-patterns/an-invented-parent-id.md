# An invented parent id

**Smell.** `Tags: EPIC-02, FEAT-05` on a story whose source names no Epic or Feature. A Feature
renamed because its source title was clumsy. Two source Features merged into one because they
overlapped. A parent's tracker id guessed at publish time because the lookup was inconvenient.

**Why it is wrong.** The hierarchy looks like a decision somebody made about how the work is
organised, and nobody made it — a person owns that call. The tracker then carries a structure the
backlog does not have, reporting rolls up against it, and unpicking it means touching every child. The
guessed tracker id is the sharper version: the story is parented under something unrelated, silently,
and the only symptom is a report that looks odd.

**Instead.** Copy `EPIC-` and `FEAT-` ids and names from the source, unchanged. Where the source has
none, leave them out of the tags and name any parent the user gave in `Details` — an absent parent is
a true statement. At publish time, find the parent's tracker id in the PRD's work item map or ask for
it. Never guess it
([`../principles/one-name-and-one-id-per-level.md`](../principles/one-name-and-one-id-per-level.md),
[`../practices/publish-to-a-tracker.md`](../practices/publish-to-a-tracker.md)).
