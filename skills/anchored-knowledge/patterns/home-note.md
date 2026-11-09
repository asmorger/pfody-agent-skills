# Home note

**Use when** a reader arrives at the vault for the first time, or needs to know what changed lately.
`moc/knowledge.md` — the one note that orients, and the only place a newcomer learns what they are
allowed to cite.

**Skeleton.**

```markdown
---
type: moc
updated: 2026-11-08
review-cadence: weekly during discovery; on-change in build; full audit at handoff
owner: delivery lead
tags: [moc]
---

# Knowledge

## What you may cite

The **record** is this vault: [[business-rules|Business Rules]], [[glossary|Glossary]],
[[scope|Scope]], [[decisions|Decisions]] and the notes in `reference/`. A story, spec, criterion or
test may cite these and nothing else.

**Governance** — [[sources|Sources]], [[open-questions|Open Questions]],
[[scope-watch|Scope Watch]], [[changes|Changes]] — records where statements came from and what
changed them. Not citable as record. The **workbench** at `knowledge-working/` holds intake, drafts
and the transcript index: evidence, not record.

## Baseline

- Contract: [[order-fulfilment-sow-v3]] · Requirements: [[phase-1-approved-requirements]]
- Delivery baseline: Phase 1, labels at order processing

## Now

- Decisions in flight: [[ADR-0004]] · Scope watch: [[SW-0002]]
- Questions needing answers: [[Q-0003]] (needed 2026-11-20), [[Q-0004]]
- Ingestion backlog: two transcripts from the November reviews

## Recently changed

- 2026-11-08 — [[CH-0003]] one label per parcel, not per order
```

**Notes.**
- **Now** is what makes the home note worth reopening, and the first section to rot. Refresh it on
  every run that touches the record
  ([`../practices/promote-to-the-record.md`](../practices/promote-to-the-record.md)).
- Keep the three-layer explanation. Every other note assumes the reader knows which layer they are
  in, and this is the only place that says so
  ([`../principles/only-the-reference-layer-is-citable.md`](../principles/only-the-reference-layer-is-citable.md)).
- Link the MOCs with a display alias so the prose reads as prose. Everything here is a pointer,
  nothing here is a fact ([`../principles/one-home-per-fact.md`](../principles/one-home-per-fact.md)).
- Review cadence and ownership live here or in the config; the audit checks they exist somewhere
  ([`../practices/audit-the-base.md`](../practices/audit-the-base.md)).
- Make it the vault's start note: a reader who opens the graph first sees hubs and no explanation.

**Related.** [`moc-note.md`](moc-note.md), [`the-two-trees.md`](the-two-trees.md).
