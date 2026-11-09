# Rendered index

**Use when** you need to say what the deliverable looks like, or to check that a render came out
right. One markdown file: per-category tables, then an evidence appendix.

**Skeleton.**

```markdown
# Knowledge Index

Durable rules and decisions distilled from project transcripts, each cited to its source meeting.

## Orders
| ID | Rule | Sources |
|----|------|---------|
| ORDER-1 | An order's shipping address is frozen once the order is submitted. | Order Fulfilment Scope Call (2026-01-21; Dana Lee) |
| ORDER-2 | *(deferred)* A submitted order may be split across parcels. | November Review (2026-11-08; Dana Lee) |

## Labels
| ID | Rule | Sources |
|----|------|---------|
| LABEL-1 | *(superseded)* One label is created per order. | Order Fulfilment Scope Call (2026-01-21; Dana Lee) |
| LABEL-2 | One label is created per parcel; a split order produces several labels. | November Review (2026-11-08; Dana Lee); Carrier Sync (2026-11-15; Priya N.) |
```

**Notes.**
- Status is folded inline on the rule, the way a curated document flags drafts and out-of-scope items.
  The statement itself stays clean
  ([`../principles/status-is-a-field-not-a-sentence.md`](../principles/status-is-a-field-not-a-sentence.md)).
- The Sources cell names meeting, date and speaker. **The verbatim quote and timestamp stay in the
  state file**, so the document stays compact as the corpus grows
  ([`state-file.md`](state-file.md)).
- `LABEL-2` with two sources is the output working as intended: one rule, cited to two meetings months
  apart ([`../principles/evidence-is-never-discarded.md`](../principles/evidence-is-never-discarded.md)).
- Category order and id prefixes come from the seeded taxonomy; `title` and `intro` come from the
  config ([`tool-config.md`](tool-config.md)).
- The render escapes markdown in statements, which is one of several reasons not to write this file by
  hand ([`../anti-patterns/hand-writing-the-index.md`](../anti-patterns/hand-writing-the-index.md)).

**Related.** [`state-file.md`](state-file.md),
[`../practices/render-the-index.md`](../practices/render-the-index.md).
