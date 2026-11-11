# A slice with a migration in it

**Smell.** The appetite says six judgment-hours and the brief is short, so the slice reads as small.
Buried in it: a column rename, a backfill, a new constraint, a type widened, or a shared service
refactored "while we are in there". The blast radius section says "small" or is missing.

**Why it is wrong.** Size and reversibility are different properties, and only one of them decides
what being wrong costs. A short change that rewrites rows cannot be undone by flipping a toggle —
the old path now reads a schema it was not written against, so the fallback that makes every other
slice safe has quietly stopped existing. The slice is not cheap to be wrong about at any hour count,
and the estimate is measuring the wrong thing with real confidence.

The shared-code version is the same failure with a longer fuse. A refactor touching code outside the
slice means the toggle no longer isolates anything: turning the new path off leaves the refactor in
place, serving every other workflow.

**Instead.** Additive-only inside a slice — a nullable column, a new table nothing yet reads, a
parallel code path. Migrations, backfills, renames, constraints and shared refactors get their own
slices, each with its own backout, and they are usually sequenced *after* the behaviour they support
has been proven on real traffic. Write the radius as a list of negatives so a reviewer can argue
with it before the work starts, and check that list against the diff afterwards
([`../principles/blast-radius-not-size.md`](../principles/blast-radius-not-size.md),
[`../practices/shape-a-slice.md`](../practices/shape-a-slice.md)).
