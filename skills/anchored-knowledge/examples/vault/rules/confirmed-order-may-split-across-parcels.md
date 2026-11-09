---
id: ORDER-5
aliases: [ORDER-5]
type: business-rule
status: draft
topic: orders
authority: 3-client-clarification
sources: ["[[operations-lead-on-split-orders]]"]
pending-on: operations lead
questions: ["[[partial-despatch-of-a-split-order|Q-0004]]"]
scope-watch: ["[[order-splitting-across-parcels|SW-0002]]"]
created: 2026-11-08
updated: 2026-11-08
---

# ORDER-5 — A confirmed order may split across parcels

A confirmed order may be split across several parcels. Each parcel is labelled separately
([[one-label-per-parcel|LABEL-1]]).

> [!warning] Draft — pending operations lead, as of 2026-11-08
> Confirmation expected at the 2026-11-18 review. Partial despatch of a split order is unanswered:
> [[partial-despatch-of-a-split-order|Q-0004]]. Splitting may exceed the baseline: [[order-splitting-across-parcels|SW-0002]].

**Also** [[parcel]] · [[order-address-frozen-on-confirmation|ORDER-1]] freezes the address per parcel after a split
