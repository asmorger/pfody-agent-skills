# MOC note

**Use when** writing or refreshing an index note. A MOC holds **no knowledge** — an embedded Bases
view that cannot drift, and a generated table beneath it that reads without Obsidian. Both are
derived; the notes are the record.

**Skeleton.** `moc/business-rules.md`

```markdown
---
type: moc
updated: 2026-11-08
snapshot:
  type: business-rule
  columns: [id, title, status, sources]
  exclude-status: [superseded, rejected]
  group-by: topic
tags: [moc]
---

# Business Rules

What this system does, as agreed. Each rule is a note in `rules/`; this note indexes them. Baseline:
[[order-fulfilment-sow-v3]]. Deprecated and superseded rules are in the third view of the embed.

![[business-rules.base]]

<!-- generated: do not edit · 2026-11-08 -->
### orders

| ID | Rule | Status | Sources |
|---|---|---|---|
| [[order-address-frozen-on-confirmation|ORDER-1]] | Order address frozen on confirmation | confirmed | [[order-fulfilment-sow-v3]] |
| [[confirmed-order-may-split-across-parcels|ORDER-5]] | Confirmed order may split across parcels | draft | [[operations-lead-on-split-orders]] |

### labels

| ID | Rule | Status | Sources |
|---|---|---|---|
| [[bulk-printing-across-orders|LABEL-3]] | Bulk printing across orders | out-of-scope | [[order-fulfilment-sow-v3]] |
<!-- /generated -->
```

**Notes.**
- `snapshot` is the generator's input; the two markers are its output boundary. Everything between
  them is overwritten and nothing else in the note is touched
  ([`../practices/regenerate-the-mocs.md`](../practices/regenerate-the-mocs.md)).
- **Change a note to change the table.** An edit between the markers is discarded by the next
  regeneration, silently
  ([`../anti-patterns/a-generated-table-edited-by-hand.md`](../anti-patterns/a-generated-table-edited-by-hand.md)).
- Prose above the embed is not generated, and is where the MOC earns its place: what the baseline is,
  what a reader may cite, what the views are for. Keep it to a few lines
  ([`../principles/one-home-per-fact.md`](../principles/one-home-per-fact.md)).
- The snapshot exists for the readers who are not in Obsidian — a reviewer on GitHub, an agent, a
  diff — and for a vault on a version without Bases. It is not a fallback for a missing query; both
  are written every time.
- One MOC per note type, plus the home note ([`home-note.md`](home-note.md)).

**Related.** [`../references/bases.md`](../references/bases.md),
[`note-frontmatter.md`](note-frontmatter.md), [`the-two-trees.md`](the-two-trees.md).
