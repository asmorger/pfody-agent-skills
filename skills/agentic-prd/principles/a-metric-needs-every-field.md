# A metric needs every field

**Rule.** An outcome is a metric only with all of it: id, metric, baseline, target, owner, source
system, population, denominator and window. A missing field is the word `Unknown` plus an open
question. A number with fields missing is not a target and is never written as one.

**Why.** "Cut label errors by half" cannot be passed or failed. Half of what, measured where, over
which orders, against what starting point, by when — each missing field is a later argument, and the
argument happens after the work is done. The denominator and population are the two that get dropped
and the two that decide the answer: errors per order and errors per parcel move in opposite
directions when parcels per order changes. Naming the source system matters just as much: a target
nobody can query is a target nobody will check.

**In the PRD.**
- One row per outcome ([`../patterns/outcome-metric.md`](../patterns/outcome-metric.md)); every Epic
  and Feature names the outcomes it serves.
- `Unknown` is honest and belongs in a draft. It must be gone, or accepted, before Gate 2.
- The check script warns when an outcome has an `Unknown`; the warning is for a person, not for you
  to fill in ([`a-gap-is-a-question-not-a-guess.md`](a-gap-is-a-question-not-a-guess.md)).
- An outcome needing an event that does not exist yet gets a telemetry row in section 8.
- An outcome no requirement serves, and a requirement serving no outcome, are both review findings.

**Breaks when.** A plausible baseline or target is supplied to fill the field →
[`../anti-patterns/a-number-without-a-denominator.md`](../anti-patterns/a-number-without-a-denominator.md).
