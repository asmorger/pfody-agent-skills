---
id: K-0001
aliases: [K-0001]
type: fact
status: confirmed
topic: labels
applies-to: label creation
confidence: high
authority: 4-source-artifact
sources: ["[[carrier-api-reference]]"]
rules: ["[[LABEL-1]]"]
created: 2026-11-08
updated: 2026-11-08
tags: [fact/labels]
---

# K-0001 — The carrier truncates address line 1 at 35 characters

The carrier silently truncates `AddressLine1` at 35 characters. Longer values are accepted and
shortened without an error.

**So.** A label can be created with a wrong address and no failure, which is why [[LABEL-1]] must
validate length before the request. Mechanics: [[order-data-mapping]].
