# Backlog notes

**Use when** writing more than one story. One note per story, Epic and Feature in the config's
stories folder, plus a MOC that indexes them. Never invent an Epic or a Feature to fill a level the
source does not have.

**Skeleton.** `moc/backlog.md`

```markdown
---
type: moc
updated: 2026-11-08
snapshot:
  type: user-story
  columns: [id, title, parent, source-mode, status, tracker-id]
---

# Backlog

Stories for [[shipping-labels-at-order-processing|PRD-001]], one note each in `backlog/`. Source mode A throughout; nothing here was
pattern-matched.

> [!warning] PREVIEW — do not publish
> The source PRD is not Accepted. (Only while that is true.)

**Epics** [[carrier-labels-on-the-order-screen|EPIC-01]] · **Features** [[void-a-label|FEAT-02]]

## Definition of Done for all User Stories

1. DoD-1 [X-002] Every label action is recorded against the order with the acting clerk and a
   timestamp.

![[backlog.base]]

<!-- generated: do not edit -->
| ID | Title | Parent | Source mode | Status | Tracker id |
|---|---|---|---|---|---|
| [[void-a-printed-label-story|US-03]] | Void a printed label | [[void-a-label|FEAT-02]] | A | draft | — |
<!-- /generated -->
```

**Notes.**
- **Coverage is not here.** In Mode A from a PRD, `agentic-prd` owns the coverage table and generates
  it from the requirement notes. In Mode B and Mode C there are no requirement ids to trace, so there
  is nothing to generate ([`../principles/mode-honesty.md`](../principles/mode-honesty.md)).
- Keep the Epic and Feature names exactly as the source has them, and their ids with them
  ([`../principles/one-name-and-one-id-per-level.md`](../principles/one-name-and-one-id-per-level.md)).
- The definition of done carries the requirements that apply to `All`, stated once here rather than
  repeated in every story.
- **`PREVIEW` is a hard gate, not a label**: a preview is not published, and the callout belongs on
  the MOC and in each story's first lines
  ([`../practices/build-from-a-prd.md`](../practices/build-from-a-prd.md)).
- The `tracker-id` column is empty until a publish returns one, which makes "what is still
  unpublished?" a query ([`../practices/publish-to-a-tracker.md`](../practices/publish-to-a-tracker.md)).
- Leave out a heading with no content. A MOC with an empty Epics line is a MOC claiming a level the
  source does not have.

**Related.** [`user-story.md`](user-story.md),
[`../references/vault-convention.md`](../references/vault-convention.md).
