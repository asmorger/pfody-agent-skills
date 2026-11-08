# Report the result

**When** ending any mode. The report is the part the person actually reads, and the only place the
work's limits get stated.

**Why.** Everything this skill protects fails quietly if the report is a success message: a gap the
person never hears about is a gap an agent will fill, and a check reported without its limits buys
confidence that nothing earned.

**Steps.**

1. **Say what you wrote and where** — the full path of every file.
2. **Give the counts**: Epics, Features and User Stories; requirements covered, blocked and proposed.
   Blocked and skipped are results, not failures; report them as such.
3. **Say which mode you ran** and why, if the request did not name one.
4. **Report the check**: the command, the exit code, every warning, and the three things the script
   cannot judge
   ([`../principles/the-check-is-not-a-reviewer.md`](../principles/the-check-is-not-a-reviewer.md)).
5. **Report what you could not read** — an excluded source, an unextractable PDF, a link you have no
   access to. This is the item most often left out and the one most likely to matter.
6. **Flag internal-only citations** before the person shares the document outside the team
   ([`../principles/link-the-source-never-copy-it.md`](../principles/link-the-source-never-copy-it.md)).
7. **End with the decisions that are the person's**, most consequential first: unsettled conflicts,
   open questions blocking a `P0`, a gate waiting on approval, a `PROPOSED` requirement needing a
   source. One line each, naming what each answer would change.

**Done when** the person can tell from the report alone what exists, what is missing, what nobody has
answered, what the check did and did not prove, and what they have to decide next.
