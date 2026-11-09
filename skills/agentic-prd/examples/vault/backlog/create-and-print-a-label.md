---
id: FEAT-01
aliases: [FEAT-01]
type: feature
status: accepted
prd: "[[shipping-labels-at-order-processing|PRD-001]]"
parent: "[[carrier-labels-on-the-order-screen|EPIC-01]]"
outcomes: ["[[address-error-rate-on-parcels|OUT-1]]"]
requirements: ["[[create-a-label-on-order-confirmation|R-001]]", "[[show-the-carrier-rejection-reason|R-002]]", "[[refuse-a-label-on-credit-hold|R-003]]"]
checks:
  empty-state: "N/A — a confirmed order always has at least one line."
  loading-state: "[[create-a-label-on-order-confirmation|R-001]]"
  error-state: "[[show-the-carrier-rejection-reason|R-002]]"
  permissions: "[[refuse-a-label-on-credit-hold|R-003]]"
  bad-input-and-boundaries: "[[show-the-carrier-rejection-reason|R-002]]"
  concurrency: "N/A — one clerk owns an order at confirmation; the order system serialises it."
  current-records-and-data-migration: "N/A — labels did not exist before this release."
created: 2026-10-02
updated: 2026-11-05
---

# FEAT-01 — Create and print a label

One job for one role: a clerk turns a confirmed order into a printed carrier label.

**Stories** [[create-a-label-for-a-confirmed-order|US-01]]
