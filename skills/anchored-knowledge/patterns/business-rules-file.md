# Business rules file

**Use when** writing or keeping `business-rules.md` — the core of the Reference Layer. Numbered topic
sections, each owning one uppercase prefix; one rule per row in a two-column table.

**Skeleton.**

```markdown
# Business Rules

What this system does, as agreed. Baseline sources: the Order Fulfilment SOW v3 and the approved
requirements. Rules with no marker are confirmed.

---

## 1. Orders

| ID | Rule |
| --- | --- |
| ORDER-1 | An order is confirmed when a clerk accepts it; a confirmed order cannot change its shipping address (confirmed 2026-10-02). |
| ORDER-2 | An order on credit hold cannot be labelled (see LABEL-3). Decided in [ADR-0004](adr/0004-credit-hold-blocks-labelling.md). |
| ORDER-3 | (Draft: pending operations lead confirmation as of 2026-11-08.) A confirmed order may be split across parcels. |

## 2. Labels

| ID | Rule |
| --- | --- |
| LABEL-1 | A label is created for the order's shipping address at the moment a clerk requests it (confirmed 2026-10-02). |
| LABEL-2 | A printed label may be voided; who may void it is **pending final operations lead confirmation** (see Q-0003). |
| LABEL-3 | Bulk printing is **not in Phase 1 scope**. Deferred to a future phase. |
```

**Notes.**
- Header: title, one sentence giving the purpose and the baseline sources, then `---`.
- Sections are `## N. Topic`, numbered, Title Case. The prefix appears only in the ids, never in the
  heading, and no two sections share a prefix.
- Two columns, `| ID | Rule |`. Never add a Status or Anchors column — status and provenance live in
  the rule text ([`../anti-patterns/a-status-column-in-the-rules-table.md`](../anti-patterns/a-status-column-in-the-rules-table.md)).
- Each rule is self-contained and testable. State mechanics — fields, formulas, thresholds — once
  they are decided; put long mechanics in a domain reference doc and link to it.
- Field and entity names in backticks; key decisions in bold; cross-links inline.
- A new rule takes the next free number in its section, whatever row it goes in
  ([`../practices/write-a-business-rule.md`](../practices/write-a-business-rule.md)).

**Related.** [`inline-status-markers.md`](inline-status-markers.md), [`glossary.md`](glossary.md),
[`decision-record.md`](decision-record.md).
