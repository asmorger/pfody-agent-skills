---
id: R-003
aliases: [R-003]
type: requirement
status: accepted
prd: "[[shipping-labels-at-order-processing|PRD-001]]"
feature: "[[create-and-print-a-label|FEAT-01]]"
priority: P1
verify: Auto
source: DEC-02
coverage: covered
stories: ["[[create-a-label-for-a-confirmed-order|US-01]]"]
created: 2026-10-21
updated: 2026-11-05
tags: [requirement/orders]
---

# R-003 — While an order is on credit hold, the system shall refuse to create a label.

The hold is read from finance at label creation, not from a cached order field.
