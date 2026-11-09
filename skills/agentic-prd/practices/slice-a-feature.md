# Slice a Feature

**When** turning one Feature into User Stories, inside `DECOMPOSE` or `CHANGE`.

**Why.** The slice decides whether a sprint produces something that can be shown, accepted and
refused. A layer slice produces none of the three, and the feedback the sprint existed to generate
never arrives.

**Steps.**

1. **List the Feature's requirements**, `R-` and the `X-` rows that name it, with their priorities.
2. **Group by outcome, not by layer.** Each group is something a named role can do end to end. If a
   group's demo would be "the table exists", it is a layer — regroup
   ([`../anti-patterns/slicing-by-layer.md`](../anti-patterns/slicing-by-layer.md)).
3. **Apply the one-person test** to each group: can one person build, test and demo this in one
   sprint? Too big → split along the next outcome boundary. Too small to demo → merge.
4. **Check the group produces something real**: a workflow, persisted data, enforcement, permission
   behaviour, integration behaviour or a reporting output. Nothing from that list means it is not a
   story.
5. **Decide where failure paths go.** Keep a failure path with its main path when one person can
   build and demo both; split it when its complexity stands alone. This is judgement, and no check
   tests it — so say which way you went.
6. **Honour the priorities.** `P0` and `P1` may share a story, tagged with the highest. A `P2` goes
   in its own story tagged `Stretch`, never mixed with `P0` or `P1`. `P3` is not sliced.
7. **Write each story** ([`../patterns/user-story.md`](../patterns/user-story.md)) with a specific
   role, a need rather than a screen, and a *so that* clause that gives a business reason instead of
   restating the need.
8. **Place every requirement exactly once** across the Feature's stories, and record it in the
   requirement's `coverage` and `stories` ([`../patterns/backlog-notes.md`](../patterns/backlog-notes.md)).

**Done when** every story names a role and an outcome, each would survive a demo, no requirement of
the Feature is unplaced or placed twice, and any failure-path judgement is stated.
