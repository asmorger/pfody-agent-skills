---
id: SW-0002
aliases: [SW-0002]
type: scope-watch
status: clarify
owner: delivery lead
baseline: ["[[order-fulfilment-sow-v3]]"]
requested: ["[[operations-lead-on-split-orders]]"]
affects: ["[[confirmed-order-may-split-across-parcels|ORDER-5]]", "[[bulk-printing-across-orders|LABEL-3]]"]
questions: ["[[partial-despatch-of-a-split-order|Q-0004]]"]
disposition:
created: 2026-11-08
updated: 2026-11-08
tags: [scope-watch]
---

# SW-0002 — Order splitting across parcels

**Agreed.** [[order-fulfilment-sow-v3]] §4.5 scopes one parcel per order.

**Asked for.** Splitting a confirmed order across parcels ([[operations-lead-on-split-orders]],
2026-11-08).

**Why it may cost more.** Splitting changes label creation, the carrier request and the despatch flow
— three surfaces the baseline priced as one.

**Recommendation.** Clarify with the client before building. If confirmed, route to change control.
