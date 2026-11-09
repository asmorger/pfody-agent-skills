# Fact note

**Use when** a citable fact is not a business rule — a constraint, a measured characteristic of the
current system, a requirement detail. One note per fact in `facts/`. Optional: most records never
need one, and a fact that could be a rule should be one.

**Skeleton.** `facts/carrier-truncates-address-line-1.md`

```markdown
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
rules: ["[[one-label-per-parcel|LABEL-1]]"]
created: 2026-11-08
updated: 2026-11-08
---

# K-0001 — The carrier truncates address line 1 at 35 characters

The carrier silently truncates `AddressLine1` at 35 characters. Longer values are accepted and
shortened without an error.

**So.** A label can be created with a wrong address and no failure, which is why [[one-label-per-parcel|LABEL-1]] must
validate length before the request. Mechanics: [[order-data-mapping]].
```

**Notes.**
- Use it for facts about the world that rules depend on, where turning the fact into a rule would
  state a behaviour nobody decided.
- **The "So." line is what earns the note.** A fact with no consequence is a note nobody needs; the
  consequence is why a rule links to it.
- `confidence` is not a substitute for `status`. A low-confidence fact is still `draft` or
  `needs-review` ([`../principles/anchor-or-flag.md`](../principles/anchor-or-flag.md)).
- Facts are Reference Layer and citable by id, like rules
  ([`../principles/only-the-reference-layer-is-citable.md`](../principles/only-the-reference-layer-is-citable.md)).
- If two facts start overlapping, one of them wanted to be a rule
  ([`../principles/facts-are-never-copied.md`](../principles/facts-are-never-copied.md)).

**Related.** [`business-rule-note.md`](business-rule-note.md),
[`reference-note.md`](reference-note.md).
