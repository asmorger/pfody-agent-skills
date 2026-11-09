---
id: CH-0003
aliases: [CH-0003]
type: knowledge-change
status: accepted
change-type: scope-refinement
identified: 2026-11-08
older: ["[[order-fulfilment-sow-v3]]", "[[one-label-per-order|LABEL-4]]"]
newer: ["[[operations-lead-on-split-orders]]"]
affects: ["[[one-label-per-parcel|LABEL-1]]", "[[one-label-per-order|LABEL-4]]", "[[confirmed-order-may-split-across-parcels|ORDER-5]]", "[[order-splitting-across-parcels|SW-0002]]", "[[parcel]]"]
owner: delivery lead
created: 2026-11-08
updated: 2026-11-08
tags: [change]
---

# CH-0003 — One label per parcel, not per order

**Previously.** One label per order ([[one-label-per-order|LABEL-4]]), from [[order-fulfilment-sow-v3]] §4.2, which
assumed one parcel per order.

**Now.** The carrier counts per parcel, so a split order needs one label per parcel.
[[operations-lead-on-split-orders]] states it directly; the SOW does not contemplate splitting.

**Interpretation.** A refinement of [[one-label-per-order|LABEL-4]], not a contradiction — the SOW's wording held because
splitting did not exist. Splitting itself is added scope: [[order-splitting-across-parcels|SW-0002]].

**Done.** [[one-label-per-parcel|LABEL-1]] written per parcel · [[one-label-per-order|LABEL-4]] superseded in place · [[confirmed-order-may-split-across-parcels|ORDER-5]] added, draft
· "Shipment" retired on [[parcel]] · [[partial-despatch-of-a-split-order|Q-0004]] opened.
