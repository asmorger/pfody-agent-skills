# Note frontmatter

**Use when** writing any note, or checking one. The frontmatter is the query surface: Bases, the
MOC snapshots and the audit all read it, and nothing in the prose restates it. The full schema and
both closed vocabularies are in
[`../references/vault-convention.md`](../references/vault-convention.md) §4–5.

**Skeleton.** Every note carries these six, plus `id` and `aliases` wherever there is an id:

```yaml
---
id: ORDER-1                 # immutable; omit on MOC and reference notes
aliases: [ORDER-1]          # makes [[ORDER-1]] resolve; omit where there is no id
type: business-rule         # closed vocabulary
status: confirmed           # closed vocabulary, per type
created: 2026-10-02
updated: 2026-11-08
tags: [rule/orders]         # <type-tag>/<topic>, derived from type and topic
---
```

A rule, filled:

```yaml
---
id: LABEL-2
aliases: [LABEL-2]
type: business-rule
status: draft
topic: labels
authority: 3-client-clarification
sources: ["[[operations-lead-on-label-voiding]]"]
pending-on: operations lead
questions: ["[[Q-0003]]"]
decisions: ["[[ADR-0004]]"]
supersedes: []
created: 2026-10-21
updated: 2026-11-08
tags: [rule/labels]
---
```

**Notes.**
- **Quote wikilinks in properties.** `sources: ["[[x]]"]` — unquoted, YAML reads `[[` as a nested
  sequence. Quoted, Obsidian reads it as a Link and gives you the backlink and the graph edge.
- A list property is a list even with one entry, and `[]` when empty. A Bases filter on a scalar
  that is sometimes a list silently matches nothing.
- `tags` duplicates `type` and `topic` on purpose, and is the only duplication allowed. The
  properties win; the tag is derived
  ([`../principles/properties-are-the-query-surface.md`](../principles/properties-are-the-query-surface.md)).
- **Status is never a tag and never prose.** One home, one answer
  ([`../anti-patterns/status-in-two-places.md`](../anti-patterns/status-in-two-places.md)).
- `updated` moves on every edit; `created` never does. `confirmed`, `decided`, `identified` and
  `needed-by` are the dates that mean something to a reader, and the audit reads them
  ([`../anti-patterns/a-draft-with-no-date.md`](../anti-patterns/a-draft-with-no-date.md)).
- A value outside the closed vocabulary is an audit finding, not a local improvement. Widening a
  vocabulary is a decision to raise.

**Related.** [`business-rule-note.md`](business-rule-note.md), [`status-callouts.md`](status-callouts.md),
[`moc-note.md`](moc-note.md).
