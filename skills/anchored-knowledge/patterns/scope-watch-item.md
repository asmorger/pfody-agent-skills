# Scope watch item

**Use when** knowledge is valid but may exceed the scope baseline. Not a conflict and not a question
— a flag that something real may cost more than was agreed.

**Skeleton.**

```markdown
## SW-0002 - Order splitting across parcels

**Status:** Watch | Clarify | In Scope | Deferred | Change Request | Closed
**Owner:** <role>
**Baseline anchor:** SRC-0001 Order Fulfilment SOW v3 §4.5 — one parcel per order
**New/requested behavior anchor:** SRC-0009, operations lead call 2026-11-08
**Related:** ORDER-5, Q-0004

**Why this may be added scope**
The SOW scopes one parcel per order. Splitting changes label creation, the carrier request and the
despatch flow.

**Recommendation**
Clarify with the client before building. If confirmed, route to change control.

**Disposition**
<outcome, date, source>
```

**Notes.**
- The two anchors are the whole item: what was agreed, and what is now being asked for. Without both,
  it is an opinion about scope.
- The recommendation is one of four — in scope, clarify, defer, change control — and it is a
  recommendation. The disposition is a person's
  ([`../principles/propose-then-apply.md`](../principles/propose-then-apply.md)).
- A scope-watch item is *not* a contradiction. A contradiction is a change-log entry; added scope is
  this ([`knowledge-change-entry.md`](knowledge-change-entry.md)).
- Deferred items keep their rule, deprecated in place, with the phase named
  ([`../principles/deprecate-never-delete.md`](../principles/deprecate-never-delete.md)).
- Possible added scope is kept separate from confirmed in-scope knowledge in the ledger. That
  separation is what makes the ledger usable in a commercial conversation.

**Related.** [`assumptions-ledger.md`](assumptions-ledger.md), [`authority-ladder.md`](authority-ladder.md).
