---
id: ORDER-1
aliases: [ORDER-1]
type: business-rule
status: confirmed
topic: orders
authority: 1-contractual
sources: ["[[order-fulfilment-sow-v3]]"]
confirmed: 2026-10-02
created: 2026-10-02
updated: 2026-11-08
tags: [rule/orders]
---

# ORDER-1 — Order address frozen on confirmation

A confirmed order cannot change its `shippingAddress`. After a split, the address is frozen per
parcel (see [[confirmed-order-may-split-across-parcels|ORDER-5]]).

**Also** [[one-label-per-parcel|LABEL-1]] creates the label from this address · [[parcel]]
