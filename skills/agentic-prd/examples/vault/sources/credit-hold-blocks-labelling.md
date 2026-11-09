---
id: DEC-02
aliases: [DEC-02]
type: decision
status: accepted
summary: An order on credit hold cannot be labelled; the hold is enforced at label creation.
decided: 2026-10-21
deciders: [Example Operations Lead, Example Architect]
prd: "[[shipping-labels-at-order-processing|PRD-001]]"
requirements: ["[[refuse-a-label-on-credit-hold|R-003]]", "[[record-every-label-action|X-002]]"]
created: 2026-10-21
updated: 2026-10-21
---

# DEC-02 — A credit hold blocks labelling

**Illustrative example only.** Invented.

## Context
A labelled parcel is treated as committed stock, so a held order was leaving before finance resolved
payment.

## Decision
The hold is checked at label creation, read live from finance ([[refuse-a-label-on-credit-hold|R-003]]).

## Alternatives
**Nightly reconciliation.** Rejected: a parcel can leave before the sweep runs.
