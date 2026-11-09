# A freshness date is derived

**Rule.** Two kinds of date, and only one may be typed.

- An **event date** records something that happened: `decided`, `confirmed`, `identified`,
  `source-date`, `meeting-date`, `needed-by`. It is a fact, it is written by a person, and no
  generator may touch it. Once written it changes only if the event is corrected.
- A **freshness date** is a claim about the file: `created`, `updated`, `generated`,
  `covers-through`. `created` is written once and never rewritten. `generated` and `covers-through`
  are written by the scripts and never by hand. `updated` is checkable against git.

**Why.** An event date is evidence; a freshness date is a promise. Nobody keeps it. A rule gets a
correction and `updated` keeps its old value, because bumping it is a second edit with no visible
reward — and the MOC tables, the Bases views and the audit all sort and filter on `updated`, so they
quietly sort on fiction. The dangerous part is that a stale freshness date is *more* harmful than a
missing one: a missing date prompts somebody to look, and a wrong one closes the question.

Version control already knows when each note last changed, exactly and without anybody remembering.
So `updated` does not need a new discipline, it needs to be checked against something that cannot
forget ([`properties-are-the-query-surface.md`](properties-are-the-query-surface.md)).

**In the base.**
- `python3 scripts/vault.py lint <vault> --git` reports any note whose `updated` predates the last
  commit that touched it. It reads the **author** date, which survives a rebase — a check that fires
  on the whole vault after every history rewrite is a check people switch off.
- It is **opt-in**, because a vault's dates may legitimately not match its commits: this skill's own
  worked example is dated in an invented timeline. Turn it on for a real vault, in review or in CI.
- No git, or no `git` on the path, and it reports nothing rather than guessing. A wrong staleness
  claim is the failure it exists to prevent.
- `created` is read back from the existing note and preserved on any regeneration, never recomputed —
  `transcript-knowledge-base` has always done this, and it is why a re-run there is safe.
- A derived note states what it was derived *from*, not merely when: `generator`, `input-paths` and
  `input-manifest-sha256` ([`../patterns/moc-note.md`](../patterns/moc-note.md),
  [`../patterns/narrative-note.md`](../patterns/narrative-note.md)).

**Breaks when.** A draft carries no date at all, so nobody can tell whether it is being worked on →
[`../anti-patterns/a-draft-with-no-date.md`](../anti-patterns/a-draft-with-no-date.md). A generated
table is dated by hand →
[`../anti-patterns/a-generated-table-edited-by-hand.md`](../anti-patterns/a-generated-table-edited-by-hand.md).
