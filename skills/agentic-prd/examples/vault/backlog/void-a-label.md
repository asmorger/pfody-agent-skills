---
id: FEAT-02
aliases: [FEAT-02]
type: feature
status: accepted
prd: "[[shipping-labels-at-order-processing|PRD-001]]"
parent: "[[carrier-labels-on-the-order-screen|EPIC-01]]"
requirements: ["[[void-a-printed-label|R-012]]", "[[print-labels-in-one-job|R-014]]"]
checks:
  empty-state: "N/A — voiding is only reachable from a labelled order."
  loading-state: "[[void-a-printed-label|R-012]]"
  error-state: "[[void-a-printed-label|R-012]]"
  permissions: "Gap: [[who-may-void-a-printed-label|Q-03]]"
  bad-input-and-boundaries: "[[void-a-printed-label|R-012]]"
  concurrency: "Gap: [[who-may-void-a-printed-label|Q-03]]"
  current-records-and-data-migration: "N/A — no labels predate this release."
created: 2026-10-21
updated: 2026-11-05
tags: [backlog/feature]
---

# FEAT-02 — Void a label

A label that should not have been printed is cancelled, and the order goes back to unlabelled.

> [!question] Open
> Two coverage lines are gaps pending [[who-may-void-a-printed-label|Q-03]]. The Feature is not decomposable until it closes.
