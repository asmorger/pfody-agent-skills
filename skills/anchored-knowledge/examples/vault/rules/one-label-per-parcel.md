---
id: LABEL-1
aliases: [LABEL-1]
type: business-rule
status: confirmed
topic: labels
authority: 3-client-clarification
sources: ["[[order-fulfilment-sow-v3]]", "[[operations-lead-on-split-orders]]"]
supersedes: ["[[LABEL-4]]"]
facts: ["[[K-0001]]"]
confirmed: 2026-11-08
created: 2026-10-02
updated: 2026-11-08
tags: [rule/labels]
---

# LABEL-1 — One label per parcel

A label is created per parcel, for the order's `shippingAddress` at the moment a clerk requests it. A
split order produces one label per parcel ([[ORDER-5]]).

> [!abstract] Supersedes [[LABEL-4]] — 2026-11-08
> Earlier understanding: one label per order, anchored at [[order-fulfilment-sow-v3]] §4.2. It held
> because splitting did not exist. See [[CH-0003]].

**Also** address validation: [[K-0001]] · mechanics: [[order-data-mapping]] · [[ORDER-2]] blocks held
orders · in scope per [[label-creation-included]]
