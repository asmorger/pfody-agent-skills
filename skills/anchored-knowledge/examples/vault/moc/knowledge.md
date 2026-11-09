---
type: moc
updated: 2026-11-08
review-cadence: weekly during discovery; on-change in build; full audit at handoff
owner: delivery lead
---

# Knowledge

## What you may cite

The **record** is this vault: [[business-rules|Business Rules]], [[glossary|Glossary]],
[[scope|Scope]], [[decisions|Decisions]] and the notes in `reference/`. A story, spec, criterion or
test may cite these and nothing else.

**Governance** — [[sources|Sources]], [[open-questions|Open Questions]],
[[scope-watch|Scope Watch]], [[changes|Changes]] — records where statements came from and what
changed them. Not citable as record. The **workbench** at `knowledge-working/` holds intake, drafts
and the transcript index: evidence, not record.

## Baseline

- Contract: [[order-fulfilment-sow-v3]] (Phase 1, labels at order processing)
- Rules rest on it plus three operations-lead clarifications; nothing here is level 5 or 6 except
  [[scope/negotiated-carrier-rates-excluded|negotiated carrier rates]], which needs review.

## Now

- Questions needing answers: [[who-may-void-a-printed-label|Q-0003]] (needed 2026-11-20), [[partial-despatch-of-a-split-order|Q-0004]] (blocked on [[order-splitting-across-parcels|SW-0002]])
- Scope watch: [[order-splitting-across-parcels|SW-0002]] order splitting — recommendation is clarify before building
- Decisions in flight: none; [[enforce-credit-hold-at-label-creation|ADR-0004]] accepted 2026-10-21
- Ingestion backlog: none

## Recently changed

- 2026-11-08 — [[one-label-per-parcel-not-per-order|CH-0003]] one label per parcel, not per order. [[one-label-per-order|LABEL-4]] superseded,
  [[confirmed-order-may-split-across-parcels|ORDER-5]] added as draft, "Shipment" retired on [[parcel]].
