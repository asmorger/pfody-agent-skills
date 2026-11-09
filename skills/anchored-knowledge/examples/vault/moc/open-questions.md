---
type: moc
updated: 2026-11-08
snapshot:
  type: open-question
  columns: [id, title, status, owner, needed-by]
  exclude-status: [dropped]
tags: [moc]
---

# Open Questions

A queue, not a store. An answered question keeps no answer: the durable part is promoted into a rule
or a decision and `answered-by` points at it. A question with no owner and no needed-by cannot close,
so it is an audit finding rather than a question.

![[open-questions.base]]

<!-- generated: do not edit · 2026-11-08 -->
| ID | Title | Status | Owner | Needed by |
|---|---|---|---|---|
| [[Q-0003]] | Who may void a printed label? | open | operations lead | 2026-11-20 |
| [[Q-0004]] | Can a split order be despatched partially? | blocked | delivery lead | 2026-11-30 |
<!-- /generated -->
