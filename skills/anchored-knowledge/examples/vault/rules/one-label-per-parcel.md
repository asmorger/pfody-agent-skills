---
id: LABEL-1
aliases: [LABEL-1]
type: business-rule
status: confirmed
topic: labels
authority: 3-client-clarification
sources: ["[[order-fulfilment-sow-v3]]", "[[operations-lead-on-split-orders]]"]
supersedes: ["[[one-label-per-order|LABEL-4]]"]
facts: ["[[carrier-truncates-address-line-1|K-0001]]"]
confirmed: 2026-11-08
created: 2026-10-02
updated: 2026-11-08
---

# LABEL-1 — One label per parcel

A label is created per parcel, for the order's `shippingAddress` at the moment a clerk requests it. A
split order produces one label per parcel ([[confirmed-order-may-split-across-parcels|ORDER-5]]).

> [!abstract] Supersedes [[one-label-per-order|LABEL-4]] — 2026-11-08
> Earlier understanding: one label per order, anchored at [[order-fulfilment-sow-v3]] §4.2. It held
> because splitting did not exist. See [[one-label-per-parcel-not-per-order|CH-0003]].

**Also** address validation: [[carrier-truncates-address-line-1|K-0001]] · mechanics: [[order-data-mapping]] · [[credit-hold-blocks-labelling|ORDER-2]] blocks held
orders · in scope per [[label-creation-included]]
