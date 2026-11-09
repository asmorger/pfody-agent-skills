---
type: reference
topic: api
status: confirmed
governs: ["[[a-printed-label-may-be-voided|LABEL-2]]"]
sources: ["[[carrier-api-reference]]"]
created: 2026-10-02
updated: 2026-11-08
tags: [reference/api]
---

# API Conventions

How this project shapes its HTTP surface, so a reviewer and an agent reach the same answer.

## Resources

Resources are plural nouns; actions are verbs on a sub-path. `POST /orders/{id}/labels` creates a
label; `DELETE /labels/{id}` is not used, because voiding is an action with its own semantics
([[a-printed-label-may-be-voided|LABEL-2]]).

## Error responses

Every failure returns a problem document with a machine-readable `code` and a human `detail`. Where
the carrier supplies its own reason text, `detail` is that text verbatim rather than a translation —
the clerk needs the carrier's words to act on ([[a-printed-label-may-be-voided|LABEL-2]]).

## Idempotency

Label creation takes an `Idempotency-Key`. A retry with the same key returns the original label
rather than creating a second one for the same parcel ([[one-label-per-parcel|LABEL-1]]).
