# Intake entry

**Use when** capturing a source before you have triaged it. Fast, in the workbench, never in the
vault. Its job is to stop knowledge being lost between arriving and being understood.

**Skeleton.** `knowledge-working/intake/2026-11-08-operations-lead-on-split-orders.md`

```markdown
---
type: intake
status: untriaged        # untriaged | converted | archived
captured-by: delivery lead
captured: 2026-11-08
source: Call with the operations lead
---

# Intake — operations lead on split orders

Raw notes:
- A confirmed order may be split across parcels.
- One label per parcel, not per order — "that's always how the carrier counts it".
- Unclear whether a split order can be despatched partially.

Triage destination:
- Record: new rule for splitting · [[LABEL-1]] refined to per-parcel
- Question: partial despatch of a split order
- Scope watch: splitting may exceed SOW §4.5
- Change: supersedes one-label-per-order
- Source: register the call
```

**Notes.**
- **Lives in the workbench**, outside the vault or inside Obsidian's excluded files, and is archived
  once its durable content is promoted — never kept as a parallel record
  ([`the-two-trees.md`](the-two-trees.md)).
- Plain markdown, no wikilinks to notes that do not exist yet. A dangling link from a draft looks
  identical to a dangling citation in the record
  ([`../anti-patterns/a-dangling-citation.md`](../anti-patterns/a-dangling-citation.md)).
- Raw notes stay raw. Do not clean a stakeholder's words into a rule here; that happens at
  reconciliation, against the existing rules
  ([`../practices/reconcile-against-the-rules.md`](../practices/reconcile-against-the-rules.md)).
- The triage destinations are the whole point of the shape: every bullet routes somewhere, and
  anything that routes nowhere was not durable knowledge.
- Capture is not approval. Nothing here is in the record until it is promoted
  ([`../principles/propose-then-apply.md`](../principles/propose-then-apply.md)).

**Related.** [`source-note.md`](source-note.md),
[`../practices/ingest-a-source.md`](../practices/ingest-a-source.md).
