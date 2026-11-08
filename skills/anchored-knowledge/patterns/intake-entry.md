# Intake entry

**Use when** capturing a source before you have triaged it. Fast, in the working area, never in the
record. Its job is to stop knowledge being lost between arriving and being understood.

**Skeleton.**

```markdown
## Intake - 2026-11-08 - Operations lead on split orders

**Captured by:** <role or agent>
**Source:** Call with the operations lead
**Triage status:** Untriaged | Converted | Archived

Raw notes:
- A confirmed order may be split across parcels.
- One label per parcel, not per order — "that's always how the carrier counts it".
- Unclear whether a split order can be despatched partially.

Triage destination:
- Reference Layer: ORDER-5 (new rule), LABEL-1 (refine — per parcel, not per order)
- Open question: partial despatch of a split order
- Scope watch: splitting may exceed SOW §4.5
- Knowledge change: CH-0003 — supersedes one-label-per-order
- Source register: SRC-0009
```

**Notes.**
- Lives in `working_dir` and is archived once its durable content is promoted — never kept as a
  parallel record ([`../principles/a-question-is-a-queue-not-a-store.md`](../principles/a-question-is-a-queue-not-a-store.md)).
- Raw notes stay raw. Do not clean a stakeholder's words into a rule here; that happens at
  reconciliation, against the existing rules
  ([`../practices/reconcile-against-the-rules.md`](../practices/reconcile-against-the-rules.md)).
- The triage destinations are the whole point of the shape: every bullet above routes somewhere, and
  anything that routes nowhere was not durable knowledge.
- Capture is not approval. Nothing here is in the Reference Layer until it is promoted
  ([`../principles/propose-then-apply.md`](../principles/propose-then-apply.md)).

**Related.** [`source-register-row.md`](source-register-row.md),
[`../practices/ingest-a-source.md`](../practices/ingest-a-source.md).
