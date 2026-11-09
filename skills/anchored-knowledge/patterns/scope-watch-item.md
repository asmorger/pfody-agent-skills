# Scope watch note

**Use when** knowledge is valid but may exceed the scope baseline. Not a conflict and not a question
— a flag that something real may cost more than was agreed. One note per item in `scope-watch/`.

**Skeleton.** `scope-watch/order-splitting-across-parcels.md`

```markdown
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
---

# SW-0002 — Order splitting across parcels

**Agreed.** [[order-fulfilment-sow-v3]] §4.5 scopes one parcel per order.

**Asked for.** Splitting a confirmed order across parcels
([[operations-lead-on-split-orders]], 2026-11-08).

**Why it may cost more.** Splitting changes label creation, the carrier request and the despatch
flow — three surfaces the baseline priced as one.

**Recommendation.** Clarify with the client before building. If confirmed, route to change control.
```

**Notes.**
- **The two anchors are the item.** What was agreed, and what is now being asked for. Without both it
  is an opinion about scope.
- The recommendation is one of four — in scope, clarify, defer, change control — and it stays a
  recommendation. `disposition` is filled by a person, with a date and a source
  ([`../principles/propose-then-apply.md`](../principles/propose-then-apply.md)).
- A scope-watch note is **not** a contradiction. A contradiction is a change note; added scope is
  this ([`knowledge-change-entry.md`](knowledge-change-entry.md)).
- Deferred items keep their rule, deprecated in place with the phase named, and the rule's
  `scope-watch` property points back here
  ([`../principles/deprecate-never-delete.md`](../principles/deprecate-never-delete.md)).
- Possible added scope stays out of the scope boundaries, which hold what is *decided*. The
  separation is what makes the boundaries usable in a commercial conversation
  ([`scope-boundary-note.md`](scope-boundary-note.md)).

**Related.** [`authority-ladder.md`](authority-ladder.md),
[`../practices/reconcile-against-the-rules.md`](../practices/reconcile-against-the-rules.md).
