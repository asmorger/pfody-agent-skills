---
id: R-002
aliases: [R-002]
type: requirement
status: accepted
prd: "[[shipping-labels-at-order-processing|PRD-001]]"
feature: "[[create-and-print-a-label|FEAT-01]]"
priority: P0
verify: Auto
source: SRC-01 @18:30
outcomes: ["[[address-error-rate-on-parcels|OUT-1]]"]
coverage: covered
stories: ["[[create-a-label-for-a-confirmed-order|US-01]]"]
created: 2026-10-02
updated: 2026-11-05
---

# R-002 — If the carrier rejects the address, then the system shall show the carrier's reason and leave the order unlabelled.

The carrier's own wording is shown verbatim, because the clerk needs it to act.
