# Outcome metric

**Use when** writing section 1's outcomes, or checking one. Nine fields; a row missing any of them is
not yet a metric.

**Skeleton.**

```markdown
**Outcomes.**

| ID | Metric | Baseline | Target | Owner | Source system | Population | Denominator | Window |
|---|---|---|---|---|---|---|---|---|
| OUT-1 | Address-error rate on parcels | 4.1% | 1.5% | Operations lead | Carrier returns report | Parcels shipped from the main warehouse | Parcels shipped | Rolling 30 days |
| OUT-2 | Minutes from order confirmation to label printed | Unknown | Unknown | Operations lead | Order system audit log | Confirmed orders | Confirmed orders | Rolling 7 days |
```

**Notes.**
- `OUT-2` above is honest and incomplete: both unknowns carry an open question, and neither is
  guessed at ([`../principles/a-metric-needs-every-field.md`](../principles/a-metric-needs-every-field.md)).
- Population is *who is counted*; denominator is *what the rate is per*. They differ more often than
  they look like they will, and when they differ the number changes.
- Source system names where the value can actually be read. "We'll need telemetry for this" is a row
  in section 8, not a source system.
- Every Epic and Feature names the outcomes it serves. An outcome no requirement serves is a review
  finding, as is a requirement serving no outcome.

**Related.** [`prd-document.md`](prd-document.md), [`open-question.md`](open-question.md),
[`../anti-patterns/a-number-without-a-denominator.md`](../anti-patterns/a-number-without-a-denominator.md).
