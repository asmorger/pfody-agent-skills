---
id: DEC-02
aliases: [DEC-02]
type: decision
status: accepted
summary: An order on credit hold cannot be labelled; the hold is enforced at label creation.
decided: 2026-10-21
deciders: [Example Operations Lead, Example Architect]
prd: "[[PRD-001]]"
requirements: ["[[R-003]]", "[[X-002]]"]
created: 2026-10-21
updated: 2026-10-21
tags: [decision]
---

# DEC-02 — A credit hold blocks labelling

**Illustrative example only.** Invented.

## Context
A labelled parcel is treated as committed stock, so a held order was leaving before finance resolved
payment.

## Decision
The hold is checked at label creation, read live from finance ([[R-003]]).

## Alternatives
**Nightly reconciliation.** Rejected: a parcel can leave before the sweep runs.
