# Knowledge change entry

**Use when** a newer source refines, contradicts or supersedes what the base already says. `CH-NNNN`
in the change log, plus a dated note on every entry it touches.

**Skeleton.**

```markdown
## CH-0003 - One label per parcel, not per order

**Date identified:** 2026-11-08
**Change type:** Contradiction | Scope Refinement | Terminology Shift | Decision Update | Requirement Update | Source Correction
**Status:** Proposed | Accepted | Needs Review | Closed
**Owner:** <role>
**Older anchors:** SRC-0001 SOW v3 §4.2; LABEL-1 (confirmed 2026-10-02)
**Newer anchors:** SRC-0009, operations lead call 2026-11-08
**Affected entries:** LABEL-1, ORDER-5, SW-0002

**Previous understanding**
One label per order, from SOW v3 §4.2, which assumed one parcel per order.

**New understanding**
The carrier counts per parcel, so a split order needs one label per parcel. SRC-0009 states it
directly; the SOW does not contemplate splitting.

**Interpretation**
Refinement of LABEL-1, not a contradiction of it — the SOW's wording held because splitting did not
exist. Splitting itself is added scope: SW-0002.

**Action taken**
- LABEL-1 rewritten per parcel, with a dated supersession note.
- ORDER-5 added for splitting, marked Draft pending the operations lead.
- Prior assumption preserved in assumptions.md with its SOW anchor.
- SW-0002 opened; Q-0004 opened for partial despatch.
```

**Notes.**
- The interpretation line is the one that does the work: contradiction, refinement, terminology shift
  or correction get different treatment, and naming which stops a refinement being logged as a
  reversal ([`../principles/conflicts-are-recorded-not-resolved.md`](../principles/conflicts-are-recorded-not-resolved.md)).
- Both anchor sets are mandatory. An entry with only the newer anchor cannot be audited.
- Every affected entry gets a dated History or amendment note; the superseded understanding is
  preserved with its anchors, not edited away
  ([`../principles/deprecate-never-delete.md`](../principles/deprecate-never-delete.md)).
- Where authority does not settle it, the entry opens a question rather than choosing.

**Related.** [`scope-watch-item.md`](scope-watch-item.md), [`authority-ladder.md`](authority-ladder.md),
[`../practices/log-a-knowledge-shift.md`](../practices/log-a-knowledge-shift.md).
