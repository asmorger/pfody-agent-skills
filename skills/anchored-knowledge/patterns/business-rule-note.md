# Business rule note

**Use when** writing or keeping a rule. One note per rule in `rules/`, named for what it says,
carrying its id in frontmatter. The core of the record, and the thing every story, criterion and test
ultimately cites.

**Skeleton.** `rules/order-address-frozen-on-confirmation.md`

```markdown
---
id: ORDER-1
aliases: [ORDER-1]
type: business-rule
status: confirmed
topic: orders
authority: 1-contractual
sources: ["[[order-fulfilment-sow-v3]]"]
confirmed: 2026-10-02
created: 2026-10-02
updated: 2026-10-02
---

# ORDER-1 — Order address frozen on confirmation

A confirmed order cannot change its `shippingAddress`. After a split, the address is frozen per
parcel (see [[confirmed-order-may-split-across-parcels|ORDER-5]]).

**Also** [[one-label-per-parcel|LABEL-1]] creates the label from this address · [[parcel]]
```

A rule that is not simply confirmed carries one callout and nothing else extra —
`status: out-of-scope`, `scope-watch: ["[[order-splitting-across-parcels|SW-0002]]"]`, then:

```markdown
# LABEL-3 — Bulk printing across orders

Printing one batch of labels for several orders at once.

> [!failure] Out of scope — Phase 1
> Discussed in discovery and deferred. Baseline: [[order-fulfilment-sow-v3]] §4.5. If it returns, it
> arrives through [[order-splitting-across-parcels|SW-0002]].
```

**Notes.**
- **One testable idea, self-contained.** A reader should not need a second note to know whether the
  system obeys it. Two ideas means two notes
  ([`../anti-patterns/one-rule-two-ideas.md`](../anti-patterns/one-rule-two-ideas.md)).
- The statement is one or two sentences of prose — not a table row, and never a restatement of the
  frontmatter. A confirmed rule needs no callout, which is what keeps the note short.
- Long mechanics go in a reference note the rule links to
  ([`reference-note.md`](reference-note.md)).
- Field and entity names in backticks, cross-links as wikilinks, and an **Also** line carrying the
  related rules and terms a reader of this rule will want next.
- `topic` sets the MOC's grouping and the Bases views' `groupBy`. A new topic is a config decision, not
  a free choice ([`../practices/write-a-business-rule.md`](../practices/write-a-business-rule.md)).

**Related.** [`note-frontmatter.md`](note-frontmatter.md), [`status-callouts.md`](status-callouts.md),
[`glossary-term-note.md`](glossary-term-note.md).
