# Citation repetition

**Smell.** `LABEL-2` cited in the opening sentence, again in `Details`, again in two Expected Output
bullets, and again on three criteria. Or a criterion carrying three citations — a rule, an ADR and a
file path — plus a parenthetical note about where the rule lives.

**Why it is wrong.** When every line carries an id, the reader stops seeing ids, and the one that
mattered — a rule marking a workstream boundary, say — reads like the rest. The repetition also
obscures what the consolidated list is for: a developer wants one reading list before starting, not a
scavenger hunt across sections. And a criterion with three citations no longer has a machine-readable
link from one test to one rule, which is the only reason the tag exists.

**Instead.** Cite once per story in `Details` as `Source grounding` — the reading list — and once per
criterion as its single source tag, with nothing else in it. Never cite in the opening sentence. Allow
an inline citation elsewhere only where the rule is non-obvious, marks a workstream boundary, explains
terminology, or identifies a gap or conflict
([`../principles/cite-once-per-story.md`](../principles/cite-once-per-story.md),
[`../patterns/source-tag.md`](../patterns/source-tag.md)).
