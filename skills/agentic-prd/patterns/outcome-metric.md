# Outcome metric

**Use when** writing the PRD's outcomes, or checking one. One note per metric in `metrics/`, with
every field a property. A metric missing any of them is not yet a metric, and the check says so.

**Skeleton.** `metrics/address-error-rate-on-parcels.md`

```markdown
---
id: OUT-1
aliases: [OUT-1]
type: outcome-metric
status: accepted
prd: "[[PRD-001]]"
baseline: 4.1%
target: 1.5%
owner: Operations lead
source-system: Carrier returns report
population: Parcels shipped from the main warehouse
denominator: Parcels shipped
window: Rolling 30 days
tags: [metric]
---

# OUT-1 — Address-error rate on parcels

The rate this PRD exists to move. Served by [[R-001]] and [[R-002]].
```

The hub embeds it: `![[OUT-1]]` in section 1, so a cold reader sees the whole metric without
following a link.

**Notes.**
- A field reading `Unknown` is honest and incomplete: the check warns, and the unknown carries an
  open question rather than a guess
  ([`../principles/a-metric-needs-every-field.md`](../principles/a-metric-needs-every-field.md)).
- An empty field is an **error**, not a warning. `Unknown` is a statement about the world; blank is a
  statement about nobody having looked.
- Population is *who is counted*; denominator is *what the rate is per*. They differ more often than
  they look like they will, and when they differ the number changes.
- Source system names where the value can actually be read. "We'll need telemetry for this" is a row
  in section 8, not a source system.
- Every Epic and Feature names the outcomes it serves. An outcome no requirement serves is a review
  finding, as is a requirement serving no outcome.

**Related.** [`prd-hub-note.md`](prd-hub-note.md), [`open-question.md`](open-question.md),
[`../anti-patterns/a-number-without-a-denominator.md`](../anti-patterns/a-number-without-a-denominator.md).
