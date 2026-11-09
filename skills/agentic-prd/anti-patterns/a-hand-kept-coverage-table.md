# A hand-kept coverage table

**Smell.** A coverage row corrected in `moc/coverage.md` between the `<!-- generated -->` markers,
because the requirement is covered now and the table had not caught up. Or a row added there for a
requirement that has no note. Or the table left untouched after `CHANGE` retired a requirement,
because regenerating felt like a formality.

**Why it is wrong.** The table is built from the requirement notes, so the edit is discarded by the
next `prd.py moc` without asking — and that is the lucky outcome. The unlucky one is that nobody
regenerates for a sprint, the table is the only place the correction exists, and the Bases view two
lines above it disagrees with the table underneath. Coverage is the artifact that proves the
decomposition run: a requirement nobody noticed was uncovered is a behaviour that silently will not
be built, and this is precisely the drift that the hand-kept version used to hide.

**Instead.** Change the requirement note. `coverage: covered` with its `stories`, or `blocked` with
its `questions`, or one of the `skipped` values — then run `python3 scripts/prd.py moc <vault>` and
the table follows. There is one place a requirement's coverage lives, and the table is a view of it.
If the table is wrong in a way no requirement note can fix, the `snapshot` spec is wrong; change
that and regenerate ([`../patterns/coverage-moc.md`](../patterns/coverage-moc.md),
[`../practices/run-the-checks.md`](../practices/run-the-checks.md)).
