# PRD hub note

**Use when** starting a PRD. The hub keeps the prose a reader needs end to end and **embeds** the
notes that are cited individually. Copy [`../assets/prd-template.md`](../assets/prd-template.md) and
fill it — do not retype it from here.

**Skeleton.** `prd/shipping-labels-at-order-processing.md`

```markdown
---
id: PRD-001
aliases: [PRD-001]
type: prd
status: accepted           # draft | in-review | accepted | superseded
topic: labels
size: Standard             # Small | Standard | Large
owner: <role>
approvers: [<business approver>, <architect>, <QA lead>]
version: 1.0
epics: ["[[carrier-labels-on-the-order-screen|EPIC-01]]"]
outcomes: ["[[address-error-rate-on-parcels|OUT-1]]"]
updated: 2026-11-05
---

# PRD-001 — Shipping labels at order processing

## 1. Intent      narrative, problem with evidence, users, then ![[address-error-rate-on-parcels]]
## 2. Scope       in scope; non-goals with a reason and a revisit-when
## 3. Context     current behaviour, constraints, dependencies
## 4. Epics, Features and requirements      ![[carrier-labels-on-the-order-screen]], then [[requirements]] and [[coverage]]
## 5. Cross-cutting requirements            ![[record-every-label-action]]
## 6. Agent boundaries                      always / ask first / never / stop conditions
## 7. Knowledge ledger                      sources, decisions, [[who-may-void-a-printed-label|Q-0003]]
## 8. Rollout and measurement               flags, phases, rollback, telemetry
## Agent protocol                           kept verbatim in every PRD
```

**Notes.**
- **Embed, do not summarise.** `![[address-error-rate-on-parcels]]` resolves to whatever that note says now, so the hub
  cannot go stale; a summary beside the note is two answers to one question
  ([`../principles/the-prd-owns-why-and-what.md`](../principles/the-prd-owns-why-and-what.md)).
- The size decides which sections are required, and the check enforces it
  ([`../practices/choose-the-prd-size.md`](../practices/choose-the-prd-size.md)).
- **Keep the agent protocol and sections 1, 2 and 6 as prose.** A PRD is read cold by agents that
  have never loaded this skill, and that prose is what makes it usable
  ([`agent-boundaries.md`](agent-boundaries.md)).
- Section 4 holds the Epic embed and links to the two MOCs. It does not hold a requirement table —
  that table is generated ([`coverage-moc.md`](coverage-moc.md)).
- State any limit on sources at the top, and report what you did not read.
- One PRD holds one or more Epics; it is not itself an Epic.

**Related.** [`requirement-note.md`](requirement-note.md),
[`knowledge-ledger.md`](knowledge-ledger.md),
[`../references/vault-convention.md`](../references/vault-convention.md),
[`../practices/draft-a-prd.md`](../practices/draft-a-prd.md).
