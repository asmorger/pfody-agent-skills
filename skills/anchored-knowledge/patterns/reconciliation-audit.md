# Reconciliation audit

**Use when** presenting what an incoming source means for the base. The written proposal that stands
between a new source and the Reference Layer — three groups, each row carrying the current text and
the recommended text.

**Skeleton.**

```markdown
# Reconciliation — SRC-0009, operations lead call 2026-11-08

## Conflicts
| Rule | Current text | Incoming item | Recommended |
|---|---|---|---|
| LABEL-1 | A label is created per order (confirmed 2026-10-02). | The carrier counts per parcel. | Rewrite per parcel; log CH-0003; preserve the prior assumption with its SOW anchor. |

## Refinements
| Rule | Current text | Incoming item | Recommended |
|---|---|---|---|
| ORDER-1 | A confirmed order cannot change its shipping address. | Address is frozen at confirmation, per parcel after a split. | Add "per parcel after a split (see ORDER-5)"; same id. |

## New rules
| Proposed id | Rule | Basis | Status |
|---|---|---|---|
| ORDER-5 | A confirmed order may be split across parcels. | SRC-0009 | Draft: pending operations lead as of 2026-11-08. |

## Also opening
- SW-0002 — splitting may exceed SOW §4.5.
- Q-0004 — partial despatch of a split order is unaddressed.

## Already covered
- "One label per parcel" for unsplit orders — LABEL-1 already says it.
```

**Notes.**
- Every incoming item lands in exactly one of five places: already covered, conflicts, refines, new
  rule, or a governance entry. An item that lands nowhere was not durable knowledge
  ([`../practices/reconcile-against-the-rules.md`](../practices/reconcile-against-the-rules.md)).
- Current text is quoted, not summarised. The user is approving a diff, and a summary hides what the
  change costs.
- *Already covered* is worth writing. It is the evidence that the base was read end to end rather
  than appended to.
- Nothing is applied from this document until it is approved, and then the exact ids are reported
  ([`../principles/propose-then-apply.md`](../principles/propose-then-apply.md)).
- Draft the changed entries in the working area alongside the audit, so approval is one step from
  promotion ([`../practices/promote-to-the-record.md`](../practices/promote-to-the-record.md)).

**Related.** [`knowledge-change-entry.md`](knowledge-change-entry.md), [`intake-entry.md`](intake-entry.md).
