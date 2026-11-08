# A number without a denominator

**Smell.** "Reduce address errors by 50%." "Labels printed in under a minute." "Improve clerk
throughput by a third." An Outcomes table with Metric and Target filled and Baseline, Population,
Denominator, Source system or Window left blank or filled with something plausible.

**Why it is wrong.** None of those can be passed or failed, so none of them will be — the measurement
conversation happens after the work, and whoever wants the project to have succeeded wins it. The
denominator and population are the two that decide the answer and the two that get dropped: errors
per order and errors per parcel move in opposite directions as soon as parcels per order changes. A
guessed baseline is worse than a blank one, because the target was computed from it.

**Instead.** Fill all nine fields or write `Unknown` with an open question against it. `Unknown` in a
draft is honest and routine; a person closes it before Gate 2. Name the source system the value can
actually be read from, and where no such system exists yet, add the telemetry row instead of a
target ([`../principles/a-metric-needs-every-field.md`](../principles/a-metric-needs-every-field.md),
[`../patterns/outcome-metric.md`](../patterns/outcome-metric.md)).
