---
type: moc
updated: 2026-11-08
snapshot:
  type: decision
  columns: [id, title, status, decided, summary]
tags: [moc]
generator: vault.py moc
generated: 2026-11-09
input-paths: [decisions/]
input-manifest-sha256: 2bd94c687bf4a485b52ecb8de8f99dcf4715102d09c4f003a1ed5cc4f8f9ca5b
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
