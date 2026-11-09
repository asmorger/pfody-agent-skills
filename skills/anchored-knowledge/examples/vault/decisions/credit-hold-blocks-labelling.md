---
id: ADR-0004
aliases: [ADR-0004]
type: decision
status: accepted
summary: An order on credit hold cannot be labelled; the hold is enforced at label creation.
decided: 2026-10-21
deciders: [operations lead, architect]
confidence: high
rules: ["[[ORDER-2]]"]
sources: ["[[operations-lead-on-credit-holds]]"]
supersedes: []
review-when: when the finance system exposes a hard-hold flag
created: 2026-10-21
updated: 2026-10-21
tags: [decision]
---

# ADR-0004 — A credit hold blocks labelling

## Context

Credit holds live in the finance system and are advisory there. Clerks were labelling held orders,
and a labelled parcel is treated as committed stock by the warehouse — so a held order was leaving
with the carrier before finance had resolved payment.

## Decision

An order on credit hold cannot be labelled. The check happens at label creation ([[ORDER-2]]),
reading the hold flag live from finance rather than from a cached order field.

## Consequences

**Easier.** A held order cannot physically leave. One enforcement point, so one place to test.

**Harder.** Label creation now depends on the finance system being reachable; an outage blocks
labelling entirely. The fallback is unaddressed and no question has been raised for it yet.

## Alternatives

**Nightly reconciliation.** Rejected: a parcel can leave the warehouse before the sweep runs, which
is the failure we are fixing.

**Blocking at despatch instead.** Rejected: the label is what the warehouse treats as the commitment,
so the parcel is already picked and packed by then.

## Assumptions

The finance hold flag is authoritative and available synchronously.

## Related

[[ORDER-2]] · [[credit-hold]] · [[operations-lead-on-credit-holds]]
