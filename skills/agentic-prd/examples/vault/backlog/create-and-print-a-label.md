---
id: FEAT-01
aliases: [FEAT-01]
type: feature
status: accepted
prd: "[[PRD-001]]"
parent: "[[EPIC-01]]"
outcomes: ["[[OUT-1]]"]
requirements: ["[[R-001]]", "[[R-002]]", "[[R-003]]"]
checks:
  empty-state: "N/A — a confirmed order always has at least one line."
  loading-state: "[[R-001]]"
  error-state: "[[R-002]]"
  permissions: "[[R-003]]"
  bad-input-and-boundaries: "[[R-002]]"
  concurrency: "N/A — one clerk owns an order at confirmation; the order system serialises it."
  current-records-and-data-migration: "N/A — labels did not exist before this release."
created: 2026-10-02
updated: 2026-11-05
tags: [backlog/feature]
---

# FEAT-01 — Create and print a label

One job for one role: a clerk turns a confirmed order into a printed carrier label.

**Stories** [[US-01]]
