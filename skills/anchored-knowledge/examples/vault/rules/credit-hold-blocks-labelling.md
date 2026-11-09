---
id: ORDER-2
aliases: [ORDER-2]
type: business-rule
status: confirmed
topic: orders
authority: 3-client-clarification
sources: ["[[operations-lead-on-credit-holds]]"]
decisions: ["[[ADR-0004]]"]
confirmed: 2026-10-21
created: 2026-10-21
updated: 2026-10-21
tags: [rule/orders]
---

# ORDER-2 — An order on credit hold cannot be labelled

An order with an active credit hold cannot have a label created for it. The check happens at label
creation, not at despatch.

**Also** decided in [[ADR-0004]] · [[credit-hold]] · [[LABEL-1]] enforces it
