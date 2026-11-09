# Open question

**Use when** the sources do not answer something the record needs. One note per question in
`questions/` — a queue entry, not a place to store the answer once it arrives.

**Skeleton.** `questions/who-may-void-a-printed-label.md`

```markdown
---
id: Q-0003
aliases: [Q-0003]
type: open-question
status: open
owner: operations lead
needed-by: 2026-11-20
blocks: ["[[a-printed-label-may-be-voided|LABEL-2]]"]
sources: ["[[operations-lead-on-label-voiding]]"]
scope-watch: []
created: 2026-10-21
updated: 2026-11-08
---

# Q-0003 — Who may void a printed label?

Can any shipping clerk void a printed label, or does it need a supervisor?

**Best answer so far.** [[operations-lead-on-label-voiding]] says voiding exists but not who may do
it. The carrier portal allows it for any authenticated account, which is not an authority statement
about our users.

**Next.** Operations lead to confirm at the 2026-11-18 review; the answer becomes a clause on
[[a-printed-label-may-be-voided|LABEL-2]].
```

Answered, it keeps no answer — `status: answered`, `answered-by: ["[[one-label-per-consignment|LABEL-5]]"]`, and one line:
"Answered 2026-11-19 by the operations lead; the rule is [[one-label-per-consignment|LABEL-5]]."

**Notes.**
- **`owner` and `needed-by` are mandatory.** A question with neither cannot close, so it is an audit
  finding rather than a question. The `Overdue` Bases view is built on `needed-by`
  ([`../references/bases.md`](../references/bases.md)).
- `blocks` is what makes the question findable from the work it holds up: the rule's backlinks show
  it. The rule carries a `[!question] Open` callout naming it
  ([`status-callouts.md`](status-callouts.md)).
- **Best answer so far** is where an honest partial goes — including evidence that does not settle
  it, labelled as not settling it.
- Answering means promoting the durable part into a rule or decision and linking to it from
  `answered-by`; the answer itself lives there
  ([`../principles/a-question-is-a-queue-not-a-store.md`](../principles/a-question-is-a-queue-not-a-store.md)).
- An answer implying work beyond the baseline opens a scope-watch item too
  ([`scope-watch-item.md`](scope-watch-item.md)).

**Related.** [`../practices/answer-an-open-question.md`](../practices/answer-an-open-question.md),
[`scope-boundary-note.md`](scope-boundary-note.md).
