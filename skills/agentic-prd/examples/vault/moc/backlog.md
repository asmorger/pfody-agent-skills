---
type: moc
updated: 2026-11-05
snapshot:
  type: user-story
  columns: [id, title, parent, testing-complexity]
generator: prd.py moc
generated: 2026-11-09
input-paths: [backlog/]
input-manifest-sha256: cd9e14a8c67ed663dd098c5b27d987fbc4b68f3b41e9cd009f380965155e8fab
managed-block-sha256: 6b33f3ef2485658b147f56f86d9cfd1602cad3772076fde787a4cf83f9210555
---

# Backlog

Epics, Features and User Stories for [[shipping-labels-at-order-processing|PRD-001]], one note each, each naming its parent. The PRD
owns why and what; the tracker owns state. Nothing here carries a task or an estimate.

**Epics** [[carrier-labels-on-the-order-screen|EPIC-01]] · **Features** [[create-and-print-a-label|FEAT-01]], [[void-a-label|FEAT-02]]

## Definition of Done for all User Stories

1. DoD-1 [[record-every-label-action|X-002]] Every label action is recorded against the order with the acting user and a
   timestamp.

![[backlog.base]]

<!-- generated: do not edit -->
| ID | Title | Parent | Testing complexity |
|---|---|---|---|
| [[create-a-label-for-a-confirmed-order\|US-01]] | Create a label for a confirmed order | [[create-and-print-a-label\|FEAT-01]] | Medium |
<!-- /generated -->
