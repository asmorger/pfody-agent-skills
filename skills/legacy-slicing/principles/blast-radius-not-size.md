# Blast radius, not size

**Rule.** What makes a slice cheap to be wrong about is reversibility, not hours. Every brief states
its blast radius as a list of what the slice does **not** touch, and a slice whose list cannot be
written is not yet a slice.

**Why.** Hours are the wrong unit because they measure the cost of doing the work, not the cost of
having been wrong about it. A two-hour change that alters a shared table is expensive to reverse at
any size; a two-week change behind a toggle, with the old path still serving traffic, can be undone
in an afternoon. Estimating the first as small because it is short is how a sprint-sized task becomes
a weekend outage.

Writing the radius as negatives is deliberate. "Adds a nullable column" invites nothing; "no schema
migration, no shared-code refactor, no change to the permission check, no change to external
sign-in" is a list a reviewer can argue with, and each line is a commitment that can be checked
against the diff afterwards.

**In the slice.**
- Additive-only schema changes. A nullable column is in radius; a migration, a rename or a
  constraint is its own slice
  ([`../anti-patterns/a-slice-with-a-migration-in-it.md`](../anti-patterns/a-slice-with-a-migration-in-it.md)).
- The old path stays hot. A slice that removes the thing it replaces is two slices, and the removal
  is the second one.
- Where every workflow depends on the area — sign-in, tenancy, audit — slice by **population**
  instead of by workflow, smallest and most tolerant first
  ([`../practices/shape-a-slice.md`](../practices/shape-a-slice.md)).
- A useful calibration: a slice is sized right when being completely wrong about it costs less than
  the meeting it would take to be sure.

**Breaks when.** An irreversible change rides along inside a slice that looked small →
[`../anti-patterns/a-slice-with-a-migration-in-it.md`](../anti-patterns/a-slice-with-a-migration-in-it.md).
