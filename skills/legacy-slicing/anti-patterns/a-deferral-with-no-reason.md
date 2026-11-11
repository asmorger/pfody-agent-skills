# A deferral with no reason

**Smell.** The rulings table is mostly `DEFER`, and the rows read `DEFER — TBD`, `DEFER — needs
discussion`, `DEFER — pending`. `Decisions outstanding` reads 0 because every unanswered question
was deferred. Nobody can say what the slice actually decided.

**Why it is wrong.** `DEFER` is the mechanism that lets work start without every answer, and a
deferral with no reason converts it into the opposite: a way to record having not decided, while
reporting a clean gate. The count still reads zero, so the check that was supposed to catch an
unready slice passes, and the slice starts without anyone noticing that its scope is undefined rather
than deliberately narrow.

A legitimate deferral always has the same shape: *this question is safe to leave open because the
slice does not touch the thing it is about.* That sentence is checkable, and writing it is what
forces the seam to exist. "Needs discussion" is not that sentence; it is an admission that the slice
and the question overlap and nobody has worked out how.

**Instead.** Every `DEFER` row names why it is safe to defer and either an owner or an explicit "no
owner yet". Where the reason cannot be written, the question is a real dependency: say so, name who
owes the answer, and shape a different slice meanwhile. And treat volume as its own signal — more
than two or three deferrals in one slice usually means the area is not understood well enough to
slice, and another survey pass is the honest move rather than a brief full of placeholders
([`../principles/decisions-outstanding-must-read-zero.md`](../principles/decisions-outstanding-must-read-zero.md),
[`../practices/shape-a-slice.md`](../practices/shape-a-slice.md)).
