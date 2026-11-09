# Slice a Feature into stories

**When** a Feature needs more than one story, or you are deciding whether it does.

**Why.** The slice decides whether a sprint produces something that can be demonstrated. Slicing by
business-rule category produces stories that each document a rule and none that can be shown.

**Steps.**

1. **Use the hour bands as a sanity check**, where an estimate exists: simple (1–8 hours) one story ·
   medium (9–40) one to three · complex (40+) two to four. A Feature needing more than four is
   probably two Features, and that is a finding for a person
   ([`../principles/one-name-and-one-id-per-level.md`](../principles/one-name-and-one-id-per-level.md)).
2. **Decompose by implementable outcome, not by rule category.** "Eligibility rules" is a category;
   "persist and enforce eligibility settings" is an outcome.
3. **Apply the one-person test** to each slice: can one person build, test and demo this in one
   sprint? Too large → split along the next outcome boundary. Too small to demo → merge.
4. **Check each slice produces something real** from the buildable-output list
   ([`../principles/a-story-produces-something-buildable.md`](../principles/a-story-produces-something-buildable.md)).
5. **Watch for a hidden prerequisite.** If a developer would have to create another story before
   starting this one, the slice is wrong
   ([`../anti-patterns/a-hidden-prerequisite-story.md`](../anti-patterns/a-hidden-prerequisite-story.md)).
6. **Take the next free `US-` numbers** from the current backlog. Never reuse one; where you cannot
   find the current numbers, start at `US-01` and add an Assumption that a person must confirm they
   are free.
7. **Copy the parent ids** from the source, unchanged. Where the source has none, leave them out of
   the tags and name any parent the user gave in `Details`
   ([`../anti-patterns/an-invented-parent-id.md`](../anti-patterns/an-invented-parent-id.md)).
8. **Write them to one file** when there is more than one
   ([`../patterns/backlog-file.md`](../patterns/backlog-file.md)).

**Done when** every slice is an outcome one person could demo in a sprint, none is a prerequisite for
another, the `US-` ids are free, and no Epic or Feature was created, merged or renamed.
