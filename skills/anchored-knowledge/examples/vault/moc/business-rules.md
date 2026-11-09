---
type: moc
updated: 2026-11-08
snapshot:
  type: business-rule
  columns: [id, title, status, sources]
  exclude-status: [superseded, rejected]
  group-by: topic
tags: [moc]
---

# Business Rules

What this system does, as agreed. Each rule is a note in `rules/`; this note indexes them. Baseline:
[[order-fulfilment-sow-v3]]. Superseded and deprecated rules are in the third view of the embed —
they keep their notes and their ids, they just stay out of the way.

![[business-rules.base]]

<!-- generated: do not edit · 2026-11-08 -->
### labels

| ID | Title | Status | Sources |
|---|---|---|---|
| [[LABEL-1]] | One label per parcel | confirmed | [[order-fulfilment-sow-v3]] · [[operations-lead-on-split-orders]] |
| [[LABEL-2]] | A printed label may be voided | confirmed | [[operations-lead-on-label-voiding]] |
| [[LABEL-3]] | Bulk printing across orders | out-of-scope | [[order-fulfilment-sow-v3]] |

### orders

| ID | Title | Status | Sources |
|---|---|---|---|
| [[ORDER-1]] | Order address frozen on confirmation | confirmed | [[order-fulfilment-sow-v3]] |
| [[ORDER-2]] | An order on credit hold cannot be labelled | confirmed | [[operations-lead-on-credit-holds]] |
| [[ORDER-5]] | A confirmed order may split across parcels | draft | [[operations-lead-on-split-orders]] |
<!-- /generated -->
