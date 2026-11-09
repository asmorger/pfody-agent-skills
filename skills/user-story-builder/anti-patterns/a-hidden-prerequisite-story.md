# A hidden prerequisite story

**Smell.** "US-05 Show label costs by week" in a backlog where nothing yet records a label's cost. A
story whose first implementation step is building something no other story covers. Often it reads as
the smallest story in the set.

**Why it is wrong.** The slice is wrong, and the discovery happens at the worst moment: the developer
picks it up, finds the missing half, and either stops — losing the sprint — or builds it silently,
which means unestimated, unreviewed work enters the release under another story's id. The backlog's
coverage table still reads complete, because the prerequisite was never a requirement anybody dropped;
it was never named.

**Instead.** Run the test explicitly while slicing: would a developer have to create another story
before starting this one? If yes, either fold the prerequisite into this story — it is part of the
same outcome — or make it its own story and order the two. A slice that cannot stand alone is not a
vertical slice. Where the prerequisite is genuinely out of scope and someone else owns it, say so once
in `Details` as a workstream boundary
([`../practices/slice-a-feature-into-stories.md`](../practices/slice-a-feature-into-stories.md),
[`../principles/a-story-produces-something-buildable.md`](../principles/a-story-produces-something-buildable.md)).
