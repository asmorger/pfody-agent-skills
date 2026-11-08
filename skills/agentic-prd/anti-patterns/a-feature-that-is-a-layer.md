# A Feature that is a layer

**Smell.** `FEAT-03: Carrier integration`. `FEAT-04: Database changes`. `FEAT-05: Reporting
infrastructure`. Or an Epic with one Feature whose name is the Epic's name, because the level was
filled in to satisfy the template.

**Why it is wrong.** A Feature is "one job for one role", and the test exists because the Feature is
what a person approves at Gate 2 and what becomes a tracker item with stories under it. A layer has
no role and no job, so nothing can be sliced from it that passes the one-person demo test — the
layer's stories come out as layers too. It also makes the coverage check meaningless: permissions and
empty state have no answer for "database changes", so the lines get `N/A` with no real reason.

**Instead.** Name the job and the role: "Create and print a label" (a shipping clerk), "Void a label"
(a shipping clerk), "See label costs by week" (an operations lead). The carrier integration is work
inside those Features, not a Feature. An Epic with exactly one Feature is usually a Feature that
wanted its own PRD, or two Features that have not been separated yet
([`../principles/one-name-and-one-id-per-level.md`](../principles/one-name-and-one-id-per-level.md)).
