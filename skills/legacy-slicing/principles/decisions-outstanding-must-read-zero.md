# Decisions outstanding must read zero

**Rule.** A brief states a `Decisions outstanding` count, and it reads `0` before building starts.
The way it gets there is `DEFER`: every question nobody has answered becomes a deferral row carrying
a reason and either an owner or an explicit "no owner yet". A deferral is not a dependency.

**Why.** This single line is what separates deferring from stalling. Both look like not deciding, but
a deferral moves the question out of the slice and lets the work start this week, while a dependency
holds the slice hostage to a person who is on leave. Most legacy projects stall because every
unanswered question was treated as the second kind.

The count also makes the gate mechanical rather than a judgement call. Eight of twenty questions
unanswered and a brief that still reads `0` is a healthy slice. A brief that reads `3` is not ready,
and nobody has to argue about whether it feels ready.

**In the slice.**
- A `DEFER` row names what is deferred and why it is safe to defer — usually that the slice does not
  touch the thing the question is about
  ([`../patterns/slice-brief.md`](../patterns/slice-brief.md)).
- The deferral device that does the most work is a seam: move one concern and leave the other in
  place, so the open question sits entirely on the side you did not touch
  ([`../practices/shape-a-slice.md`](../practices/shape-a-slice.md)).
- A question that cannot be deferred without making the slice useless is a real dependency. Say so,
  name who owes the answer, and shape a different slice meanwhile.
- Guard against the opposite failure. More than two or three deferrals in one slice usually means the
  area is not understood well enough to slice yet, and the honest move is another survey pass.

**Breaks when.** A row says `DEFER` with no reason and no owner, so nobody can tell a decision from
an evasion →
[`../anti-patterns/a-deferral-with-no-reason.md`](../anti-patterns/a-deferral-with-no-reason.md).
