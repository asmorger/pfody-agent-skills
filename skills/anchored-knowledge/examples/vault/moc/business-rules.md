---
type: moc
updated: 2026-11-08
snapshot:
  type: business-rule
  columns: [id, title, status, sources]
  exclude-status: [superseded, rejected]
  group-by: topic
generator: vault.py moc
generated: 2026-11-09
input-paths: [rules/]
input-manifest-sha256: ff78154ec54bad33f6bea242a9b4b42960792bbdc2a7bb866c5687a2184332df
managed-block-sha256: fde7322a1820c7bec08e3cfa341e5172838dce15ca6c91f4164a6a2a8d52bde5
---

# Business Rules

What this system does, as agreed. Each rule is a note in `rules/`; this note indexes them. Baseline:
[[order-fulfilment-sow-v3]]. Superseded and deprecated rules are in the third view of the embed —
they keep their notes and their ids, they just stay out of the way.

![[business-rules.base]]

<!-- generated: do not edit · 2026-11-09 -->
### labels

| ID | Title | Status | Sources |
|---|---|---|---|
| [[one-label-per-parcel\|LABEL-1]] | One label per parcel | confirmed | [[order-fulfilment-sow-v3]] · [[operations-lead-on-split-orders]] |
| [[a-printed-label-may-be-voided\|LABEL-2]] | A printed label may be voided | confirmed | [[operations-lead-on-label-voiding]] |
| [[bulk-printing-across-orders\|LABEL-3]] | Bulk printing across orders | out-of-scope | [[order-fulfilment-sow-v3]] |

### orders

| ID | Title | Status | Sources |
|---|---|---|---|
| [[order-address-frozen-on-confirmation\|ORDER-1]] | Order address frozen on confirmation | confirmed | [[order-fulfilment-sow-v3]] |
| [[credit-hold-blocks-labelling\|ORDER-2]] | An order on credit hold cannot be labelled | confirmed | [[operations-lead-on-credit-holds]] |
| [[confirmed-order-may-split-across-parcels\|ORDER-5]] | A confirmed order may split across parcels | draft | [[operations-lead-on-split-orders]] |
<!-- /generated -->
