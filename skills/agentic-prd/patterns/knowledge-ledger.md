# Knowledge ledger

**Use when** recording where anything in the PRD came from. Sources, decisions and assumptions are
**notes in `sources/`**; open questions have their own shape. Section 7 of the hub links them rather
than tabulating them.

**Skeleton.** A source, `sources/warehouse-discovery-call.md`:

```markdown
---
id: SRC-01
aliases: [SRC-01]
type: source
source-type: transcript        # transcript | sow | requirements | stakeholder-answer | vendor-doc
authority: 3-client-clarification
provider: Operations lead
source-date: 2026-10-02
location: <link to the system of record>
citable: false
tags: [source/transcript]
---

# Warehouse discovery call

**Does not cover** who may void a label, or bulk printing. A statement about either does not come
from here.
```

A decision, `sources/credit-hold-blocks-labelling.md`, is `type: decision` with `summary`,
`decided`, `deciders`, `requirements`, and an `## Alternatives` section naming **how each rejected
option fails**. An assumption is `type: source` with `source-type: inference`, `authority:
5-internal-interpretation`, and a body saying **what would make it false**.

**Notes.**
- **A source note never lists what it supports.** Each requirement names its source, so the source
  note's backlinks are that list, always current.
- `authority` replaces the old Verified/Stakeholder column and carries more: it is what a reviewer
  weighs a conflict with ([`../practices/cite-a-source.md`](../practices/cite-a-source.md)).
- A requirement citing `DEC-nn` needs no locator, because the decision note carries its own reasoning.
- **Rejected options are the most valuable part of a decision note.** Each names how it fails, not
  that it lost — which is what stops it being re-proposed next quarter.
- "What makes it false" turns an assumption into something testable. An assumption nothing could
  falsify is a guess ([`../principles/implied-is-not-stated.md`](../principles/implied-is-not-stated.md)).
- Link the system of record; copy nothing out of it
  ([`../principles/link-the-source-never-copy-it.md`](../principles/link-the-source-never-copy-it.md)).
- When `anchored-knowledge` is installed these are its notes too, in its folder, with its ids.

**Related.** [`open-question.md`](open-question.md), [`requirement-note.md`](requirement-note.md).
