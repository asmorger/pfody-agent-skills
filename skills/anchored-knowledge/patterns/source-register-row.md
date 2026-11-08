# Source register row

**Use when** registering any source. One row per artifact, carrying its authority level and — in the
Notes column — the rule ids it updated. That Notes column is how a rule's inline date traces back.

**Skeleton.**

```markdown
| Source ID | Source Name | Type | Date | Owner/Provider | Location | Authority Level | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-0001 | Order Fulfilment SOW v3 | SOW | 2026-09-11 | Client | ../sow/order-fulfilment-sow-v3.docx | 1 - Contractual baseline | Seeded ORDER-1, ORDER-2, LABEL-1; assumptions.md "Label creation". |
| SRC-0004 | Operations lead, label voiding | Stakeholder answer | 2026-10-21 | Operations lead | <link> | 3 - Client clarification | Updated LABEL-2; opened Q-0003. Who may void is still open. |
| SRC-0007 | Transcript index (transcript-knowledge-base) | Transcript index | 2026-11-08 | Team | <working_dir>/transcript-knowledge.md | 4 - Source artifact | Supplemental. Reconciled into ORDER-5; not citable as record. |
```

**Notes.**
- Always name the rule ids, ADRs and glossary terms a source updated. A row that says only what the
  source is leaves every rule's date pointing at nothing
  ([`../principles/anchor-or-flag.md`](../principles/anchor-or-flag.md)).
- The authority level comes from the project's ladder and is recorded at registration, not judged
  later ([`authority-ladder.md`](authority-ladder.md)).
- Register the original artifact, not an extraction of it. The location points at the system of
  record.
- Register supporting folders and the transcript index too, marked supplemental — being registered is
  not the same as being citable
  ([`../principles/only-the-reference-layer-is-citable.md`](../principles/only-the-reference-layer-is-citable.md)).
- Caveats belong in Notes: what the source does not cover, where it is known to be stale.

**Related.** [`intake-entry.md`](intake-entry.md), [`inline-status-markers.md`](inline-status-markers.md),
[`../practices/ingest-a-source.md`](../practices/ingest-a-source.md).
