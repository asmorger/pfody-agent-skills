---
id: R-012
aliases: [R-012]
type: requirement
status: accepted
topic: labels
prd: "[[shipping-labels-at-order-processing|PRD-001]]"
feature: "[[void-a-label|FEAT-02]]"
priority: P1
verify: Auto
source: SRC-0003 @31:05
coverage: blocked
questions: ["[[who-may-void-a-printed-label|Q-0003]]"]
created: 2026-10-21
updated: 2026-11-05
---

# R-012 — When an authorised user voids a printed label, the system shall return the order to the unlabelled state.

> [!question] Open
> Which role is authorised is unsettled — any clerk, or a supervisor. See [[who-may-void-a-printed-label|Q-0003]].
