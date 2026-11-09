---
id: FEAT-02
aliases: [FEAT-02]
type: feature
status: accepted
prd: "[[PRD-001]]"
parent: "[[EPIC-01]]"
requirements: ["[[R-012]]", "[[R-014]]"]
checks:
  empty-state: "N/A — voiding is only reachable from a labelled order."
  loading-state: "[[R-012]]"
  error-state: "[[R-012]]"
  permissions: "Gap: [[Q-03]]"
  bad-input-and-boundaries: "[[R-012]]"
  concurrency: "Gap: [[Q-03]]"
  current-records-and-data-migration: "N/A — no labels predate this release."
created: 2026-10-21
updated: 2026-11-05
tags: [backlog/feature]
---

# FEAT-02 — Void a label

A label that should not have been printed is cancelled, and the order goes back to unlabelled.

> [!question] Open
> Two coverage lines are gaps pending [[Q-03]]. The Feature is not decomposable until it closes.
