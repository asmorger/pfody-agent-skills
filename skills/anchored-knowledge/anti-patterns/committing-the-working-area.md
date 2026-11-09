# Committing the workbench

**Smell.** `knowledge-intake.md` in the repository. A `drafts/` folder pushed with six proposed rules
nobody approved. The transcript index committed beside the business rules. Often the workbench was
never gitignored, so it went up with everything else.

**Why it is wrong.** Everything in the record is read as knowledge — that is what being in the record
means. Half-finished notes and unapproved proposals there get cited, and the team learns that the base
cannot be trusted, which ends with people not writing things down until they are certain. That is how
knowledge gets lost. The transcript index is a particular hazard: committed, it looks like Reference
Layer and gets cited as record.

**Instead.** Two directories. Capture and draft in the workbench, which is gitignored when it sits
inside the repository and recorded as such in the config. Promote approved entries into the record and
commit only those, naming the ids in the save message. Raw sources and the transcript index stay in
the workbench permanently — they are evidence, not record
([`../principles/two-directories-promote-to-commit.md`](../principles/two-directories-promote-to-commit.md),
[`../practices/promote-to-the-record.md`](../practices/promote-to-the-record.md)).
