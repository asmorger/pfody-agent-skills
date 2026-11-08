# Decision record

**Use when** a design or scope decision is settled, or an earlier one is reversed. One file per
decision in `adr/`, numbered sequentially, plus a row in the index. The full frontmatter and section
set is in [`../references/templates.md`](../references/templates.md).

**Skeleton.** `adr/0004-credit-hold-blocks-labelling.md`

```markdown
---
type: adr
title: A credit hold blocks labelling
status: Accepted
created: 2026-10-21
deciders: [operations lead, architect]
tags: [orders, labels]
relatedTo: [ADR-0003]
supersedes: null
dependsOn: []
confidence: High
summary: An order on credit hold cannot be labelled; the hold is enforced at label creation.
---

## Status
Accepted, 2026-10-21.

## Context
Credit holds live in the finance system and are advisory there. Clerks were labelling held orders,
and a labelled parcel is treated as committed stock.

## Decision
An order on credit hold cannot be labelled. The check happens at label creation (ORDER-2, LABEL-3).

## Rationale · Consequences (Easier / Harder) · Alternatives Considered · Assumptions ·
## Future Review · Related
```

The index row: `| ADR-0004 | A credit hold blocks labelling | Accepted | 2026-10-21 | <summary> |`

**Notes.**
- File name `NNNN-kebab-title.md`, sequential, never renumbered
  ([`../principles/ids-are-immutable.md`](../principles/ids-are-immutable.md)).
- Reversal is **supersession**: a new ADR that names what it supersedes, and the old one's status
  changes. Never overwrite a decision's body.
- A refinement that reverses nothing gets a dated addendum on the existing ADR.
- The index's summary column is the frontmatter `summary`, copied — one home, one wording.
- Every ADR has an index row, and every `ADR-NNNN` cited anywhere resolves to a real file. The audit
  checks both ([`../practices/audit-the-base.md`](../practices/audit-the-base.md)).
- *Alternatives Considered* is the section that earns the file: each alternative names how it fails.

**Related.** [`business-rules-file.md`](business-rules-file.md),
[`../practices/record-a-decision.md`](../practices/record-a-decision.md).
