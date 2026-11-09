---
id: X-002
aliases: [X-002]
type: requirement
status: accepted
topic: labels
prd: "[[shipping-labels-at-order-processing|PRD-001]]"
applies-to: [All]
priority: P0
verify: Manual
source: ADR-0004
coverage: covered
stories: ["[[create-a-label-for-a-confirmed-order|US-01]]"]
created: 2026-10-21
updated: 2026-11-05
---

# X-002 — The system shall record every label action against the order with the acting user and a timestamp.

Cross-cutting: it applies to every Feature, and it is stated once in the definition of done rather
than repeated in every story.
