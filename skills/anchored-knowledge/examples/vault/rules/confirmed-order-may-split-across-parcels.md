---
id: ORDER-5
aliases: [ORDER-5]
type: business-rule
status: draft
topic: orders
authority: 3-client-clarification
sources: ["[[operations-lead-on-split-orders]]"]
pending-on: operations lead
questions: ["[[Q-0004]]"]
scope-watch: ["[[SW-0002]]"]
created: 2026-11-08
updated: 2026-11-08
tags: [rule/orders]
---

# ORDER-5 — A confirmed order may split across parcels

A confirmed order may be split across several parcels. Each parcel is labelled separately
([[LABEL-1]]).

> [!warning] Draft — pending operations lead, as of 2026-11-08
> Confirmation expected at the 2026-11-18 review. Partial despatch of a split order is unanswered:
> [[Q-0004]]. Splitting may exceed the baseline: [[SW-0002]].

**Also** [[parcel]] · [[ORDER-1]] freezes the address per parcel after a split
