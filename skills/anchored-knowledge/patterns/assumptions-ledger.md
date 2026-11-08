# Assumptions ledger

**Use when** recording what is in and out of scope. `assumptions.md` makes "we never agreed to that"
provable, by area, with the deciding source named.

**Skeleton.**

```markdown
# Assumptions

## Label creation

1. **Included**
   1. Creating and printing a label for a confirmed order (SOW v3 §4.2).
   2. Showing the carrier's rejection reason to the clerk (SRC-0004, 2026-10-21).
2. **Not Included**
   1. Bulk printing across several orders — deferred to a future phase (SW-0002).
   2. Negotiated carrier rates. No source addresses them.

## Order splitting

1. **Included**
   1. Splitting a confirmed order across parcels (Draft: pending operations lead, 2026-11-08).
2. **Not Included**
   1. Partial despatch of a split order (SOW v3 §4.5 excludes it).
```

**Notes.**
- A nested numbered outline per area, with **Included** and **Not Included** branches. The outline
  shape matters: it is what makes the ledger quotable in a scope conversation.
- Name the deciding source whenever it is known. "No source addresses them" is an honest and useful
  entry — it says the boundary was considered.
- Unknowns do not go here. They go in the open-questions register
  ([`open-question.md`](open-question.md)).
- Knowledge that may push past the baseline goes to scope watch, and the ledger links it
  ([`scope-watch-item.md`](scope-watch-item.md)).
- Superseded assumptions stay, with their anchors, when a change entry revises them
  ([`knowledge-change-entry.md`](knowledge-change-entry.md)).

**Related.** [`authority-ladder.md`](authority-ladder.md),
[`../practices/bootstrap-a-base.md`](../practices/bootstrap-a-base.md).
