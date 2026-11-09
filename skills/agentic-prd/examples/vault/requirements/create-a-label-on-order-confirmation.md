---
id: R-001
aliases: [R-001]
type: requirement
status: accepted
prd: "[[shipping-labels-at-order-processing|PRD-001]]"
feature: "[[create-and-print-a-label|FEAT-01]]"
priority: P0
verify: Auto
source: SRC-01 @12:04
outcomes: ["[[address-error-rate-on-parcels|OUT-1]]"]
coverage: covered
stories: ["[[create-a-label-for-a-confirmed-order|US-01]]"]
created: 2026-10-02
updated: 2026-11-05
---

# R-001 — When a clerk confirms an order, the system shall create a carrier label for the order's shipping address.

The address is taken from the order at the moment of confirmation, not re-entered.
