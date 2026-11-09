---
type: moc
updated: 2026-11-08
snapshot:
  type: decision
  columns: [id, title, status, decided, summary]
generator: vault.py moc
generated: 2026-11-09
input-paths: [decisions/]
input-manifest-sha256: 80908e892e91a4f5b5a86d1801a00a2cdea745c9b993d7896d46323a1c7333c1
managed-block-sha256: 0d3a3d2e0276c20e2c09d299ec0cda872dc2c73a8b901389875f3aa2150e2e88
---

# Decisions

One note per decision, with the reasoning and the rejected alternatives. A reversal is a new note
that names what it supersedes; a decision's body is never overwritten.

![[decisions.base]]

<!-- generated: do not edit · 2026-11-09 -->
| ID | Title | Status | Decided | Summary |
|---|---|---|---|---|
| [[enforce-credit-hold-at-label-creation\|ADR-0004]] | A credit hold blocks labelling | accepted | 2026-10-21 | An order on credit hold cannot be labelled; the hold is enforced at label creation. |
<!-- /generated -->
