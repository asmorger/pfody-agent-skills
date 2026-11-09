---
type: moc
updated: 2026-11-08
snapshot:
  type: open-question
  columns: [id, title, status, owner, needed-by]
  exclude-status: [dropped]
generator: vault.py moc
generated: 2026-11-09
input-paths: [questions/]
input-manifest-sha256: 5de0ad2750e7fbd6e8202bff8bd75f05f52a0e083fb55b6434107d8f62131dcf
managed-block-sha256: ce036c33b904fab846fb0569270d6c49f625cd075e4f1764244b00ff690855ae
---

# Open Questions

A queue, not a store. An answered question keeps no answer: the durable part is promoted into a rule
or a decision and `answered-by` points at it. A question with no owner and no needed-by cannot close,
so it is an audit finding rather than a question.

![[open-questions.base]]

<!-- generated: do not edit · 2026-11-09 -->
| ID | Title | Status | Owner | Needed by |
|---|---|---|---|---|
| [[who-may-void-a-printed-label\|Q-0003]] | Who may void a printed label? | open | operations lead | 2026-11-20 |
| [[partial-despatch-of-a-split-order\|Q-0004]] | Can a split order be despatched partially? | blocked | delivery lead | 2026-11-30 |
<!-- /generated -->
