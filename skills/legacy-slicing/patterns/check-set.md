# Check set

**Use when** writing a brief's `## Checks`. Three kinds, and a slice needs all three. Together they
are what lets the switch be a setting rather than an event.

**Skeleton.** Three entries, each naming what it proves.

```markdown
## Checks
char/label_reprint_*.approved
    Golden master. Recorded by driving the legacy domain layer over every
    order, not by reading the survey. Must not change.
new/reprint_voids_the_first
    The one behaviour this slice deliberately changes (B02).
parallel-run
    5 working days. Every reprint resolves both paths and logs a diff.
    Flip requires 0 diffs and at least 500 reprints.
```

**Notes.**
- **`char/` is the oracle's output.** Derived by exercising the old system; a characterisation test
  written from the survey encodes the misreading and passes
  ([`../principles/the-oracle-outranks-the-survey.md`](../principles/the-oracle-outranks-the-survey.md)).
- **Record the golden master for the whole population**, even when the slice touches part of it. It
  costs nothing extra and it protects everything the slice could break.
- **`new/` has an entry per `CHANGE` and per `DROP` ruling.** A drop alters behaviour as much as a
  change does, and a `new/` check with no ruling behind it is scope that arrived without a decision.
- **`parallel-run` needs a threshold and a volume**, both stated. "Looks fine" is not a criterion,
  and a diff of zero over four reprints proves nothing.
- A `KEEP` ruling needs no new check — it is covered by the golden master, which is the point of
  recording one.
- The suite is never pruned. It outlives the brief, the survey and usually the slice's author
  ([`../practices/flip-a-slice.md`](../practices/flip-a-slice.md)).

**Related.** [`slice-brief.md`](slice-brief.md),
[`../practices/flip-a-slice.md`](../practices/flip-a-slice.md),
[`../anti-patterns/tests-written-from-the-survey.md`](../anti-patterns/tests-written-from-the-survey.md).
