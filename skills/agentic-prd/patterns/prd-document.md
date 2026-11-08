# PRD document

**Use when** starting a PRD. The whole-document shape: front matter, eight numbered sections, two
optional modules, and the agent protocol the PRD carries with it. Copy
[`../assets/prd-template.md`](../assets/prd-template.md) and fill it — do not retype it from here.

**Skeleton.**

```markdown
---
prd_id: PRD-001
title: Shipping labels at order processing
status: Draft              # Draft | In Review | Accepted | Superseded
size: Standard             # Small | Standard | Large
owner: <role>
approvers: [<business approver>, <architect>, <QA lead>]
version: 0.1
updated: 2026-11-08
---

# Shipping labels at order processing

## 1. Intent          narrative, problem with evidence, users, outcome metrics
## 2. Scope           in scope; non-goals with a reason and a revisit-when
## 3. Context         current behaviour, team links, constraints, dependencies, glossary
## 4. Epics, Features and requirements    work item map, priorities, requirement tables, coverage
## 5. Cross-cutting requirements          X-001…, each naming what it applies to
## 6. Agent boundaries                    always / ask first / never / checks / stop conditions
## 7. Knowledge ledger                    sources, decisions, assumptions, open questions
## 8. Rollout and measurement             flags, phases, rollback, telemetry

## Optional modules    M1 AI behaviour · M2 data migration
## Agent protocol      kept verbatim in every PRD
```

**Notes.**
- The size decides which sections are required
  ([`../practices/choose-the-prd-size.md`](../practices/choose-the-prd-size.md)). Delete the
  template's guidance blocks; keep the section numbers and every id format.
- Keep the agent protocol section. A PRD is read by agents that have never loaded this skill, and the
  protocol is what makes it usable cold.
- State any limit on sources at the top, and report what you did not read
  ([`../principles/a-conflict-is-recorded-not-resolved.md`](../principles/a-conflict-is-recorded-not-resolved.md)).
- One PRD holds one or more Epics; it is not itself an Epic.

**Related.** [`requirement-row.md`](requirement-row.md), [`knowledge-ledger.md`](knowledge-ledger.md),
[`agent-boundaries.md`](agent-boundaries.md),
[`../practices/draft-a-prd.md`](../practices/draft-a-prd.md),
[`../references/example-prd.md`](../references/example-prd.md).
