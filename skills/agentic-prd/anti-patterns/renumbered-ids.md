# Renumbered ids

**Smell.** `R-007` was dropped, so `R-008`'s front matter became `R-007` and the ids have no gaps. Or the stories
were re-sliced and `US-01`…`US-05` were reassigned to the new set. The result looks tidier than it
did before.

**Why it is wrong.** The id is the only thing holding the chain together — a criterion cites it, a
coverage row tracks it, a test is named for it, a pull request references it, a tracker item is
tagged with it. Renumbering re-points every one of those at a different behaviour, and nothing fails:
the tests still pass, against the wrong requirement. The history goes too. A reader asking "was
voiding ever specified?" can no longer see that it was, and was dropped.

**Instead.** Retire in place: keep the note, keep the id, set `status: retired` and write `Retired` at the start of the
Requirement column, and take the next free number for anything new. Gaps in the numbering are normal
and are never closed up — in the PRD, in the backlog, or in the tracker
([`../principles/ids-are-never-reused.md`](../principles/ids-are-never-reused.md)).
