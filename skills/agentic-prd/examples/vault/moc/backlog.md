---
type: moc
updated: 2026-11-05
snapshot:
  type: user-story
  columns: [id, title, parent, source-mode, status, testing-complexity, tracker-id]
generator: prd.py moc
generated: 2026-11-09
input-paths: [backlog/]
input-manifest-sha256: 6a7428016d4e5d39ef0801f79268c4ba07895c6223566b75e3e4e2408e3bb4cf
managed-block-sha256: 5b5ce9b258eafe6b91aa6562e8954eb0d53068020d3f1ea66214dcf3d37a057f
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
| ID | Title | Parent | Source mode | Status | Testing complexity | Tracker id |
|---|---|---|---|---|---|---|
| [[create-a-label-for-a-confirmed-order\|US-01]] | Create a label for a confirmed order | [[create-and-print-a-label\|FEAT-01]] | A | ready | Medium | — |
<!-- /generated -->
