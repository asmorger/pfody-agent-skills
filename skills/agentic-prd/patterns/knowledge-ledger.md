# Knowledge ledger

**Use when** recording where anything in the PRD came from. Section 7's three registers: sources,
decisions, and assumptions. Open questions are the fourth and have their own shape.

**Skeleton.**

```markdown
**Sources.**

| ID | Source | Type | Link | Date |
|---|---|---|---|---|
| SRC-01 | Warehouse discovery call | Verified | <link to the recording> | 2026-10-02 |
| SRC-02 | Statement of work, rev C | Verified | <link to the contract system> | 2026-09-11 |
| SRC-03 | Operations lead, notes on label voiding | Stakeholder | <link> | 2026-10-21 |

**Decisions.**

| ID | Decision | Owner | Date | Reason | Rejected options | Revisit when |
|---|---|---|---|---|---|---|
| DEC-02 | An order on credit hold cannot be labelled. | Operations lead | 2026-10-21 | A labelled parcel is treated as committed stock; holds exist to stop that. | Label but suppress printing — the parcel still leaves the pick face. | Credit holds move into the order system. |

**Assumptions and inferences.**

| ID | Statement | Type | Basis | What makes it false | Affects |
|---|---|---|---|---|---|
| A-01 | Bulk printing is wanted but not required for the first release. | Inference | SRC-01 @41:20 raises it; no source commits to it. | A clerk shows that single printing cannot keep up with a peak day. | R-004 |
```

**Notes.**
- Type on a source is `Verified` (a document or recording that exists) or `Stakeholder` (what a person
  said). The distinction is what a reviewer needs to weigh a conflict.
- A decision row carries its own source in *Reason*, which is why a requirement citing `DEC-xx` needs
  no locator.
- *Rejected options* is the row's most valuable field: it is what stops the option being re-proposed
  next quarter. Each one names how it fails, not that it lost.
- *What makes it false* turns an assumption into something testable. An assumption nothing could
  falsify is a guess
  ([`../principles/implied-is-not-stated.md`](../principles/implied-is-not-stated.md)).
- Link to the system of record; copy nothing out of it
  ([`../principles/link-the-source-never-copy-it.md`](../principles/link-the-source-never-copy-it.md)).

**Related.** [`open-question.md`](open-question.md), [`requirement-row.md`](requirement-row.md),
[`../practices/cite-a-source.md`](../practices/cite-a-source.md).
