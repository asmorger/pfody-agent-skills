# Open question

**Use when** the sources do not answer something the PRD needs. One note per question in
`questions/` — the one shape a gap is allowed to take. Same note type and folder as
`anchored-knowledge` uses, because a PRD's gap is a question the project needs answered, and two
question registers is the failure the never-copy rule exists to prevent.

**Skeleton.** `questions/who-may-void-a-printed-label.md`

```markdown
---
id: Q-0003
aliases: [Q-0003]
type: open-question
status: open               # open | partial | answered | blocked | dropped
topic: labels
owner: Operations lead     # mandatory
needed-by: 2026-11-20      # mandatory — a date, or a gate name in a draft
blocks: ["[[void-a-printed-label|R-012]]", "[[void-a-label|FEAT-02]]"]
prd: "[[shipping-labels-at-order-processing|PRD-001]]"
answered-by: []
---

# Q-0003 — Who may void a printed label — any clerk, or a supervisor?

**Best answer so far.** [[label-workflow-walkthrough|SRC-0003]] says voiding exists and stops at
collection, but not who may do it. The carrier portal allows any authenticated account, which is not
an authority statement about our users.

**Next.** Operations lead to confirm at the 2026-11-18 review; the answer becomes a clause on
[[void-a-printed-label|R-012]] and closes the `permissions` coverage line on [[void-a-label|FEAT-02]].
```

**Notes.**
- **`blocks` is what makes a question operational**: the blocked requirement names it in
  `questions`, decomposition skips it and reports it, and the gap reaches the person who can close
  it rather than becoming an invented behaviour
  ([`../practices/decompose-a-prd.md`](../practices/decompose-a-prd.md)).
- A blocked requirement may state `<behaviour not known>` and keep its id, priority and verify
  method.
- `needed-by` is a date. A draft may use a gate name until there is a schedule — `Gate 2` — but
  never nothing. The check errors on either field missing, because a question with neither cannot
  close.
- Answering does not leave the answer here. Promote it into a requirement or a decision, point
  `answered-by` at it, and set `status: answered` — so the register stays a queue rather than a
  second place to look for behaviour.
- When `anchored-knowledge` is also installed, this is the same note it writes and audits. The `prd`
  property is what makes it findable from both sides.

**Related.** [`knowledge-ledger.md`](knowledge-ledger.md), [`coverage-check.md`](coverage-check.md),
[`../principles/a-gap-is-a-question-not-a-guess.md`](../principles/a-gap-is-a-question-not-a-guess.md).
