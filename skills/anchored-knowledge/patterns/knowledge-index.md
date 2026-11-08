# Knowledge index

**Use when** a reader arrives at the base for the first time, or needs to know what changed lately.
One orientation document in the record: what to use, what the baseline is, what is open.

**Skeleton.**

```markdown
# Knowledge Index

## How to Use This Knowledge System
- **Reference Layer** (source of record, in `docs/`): glossary, business-rules, assumptions, adr/,
  convention docs, domain reference docs. Only these may be cited by stories, specs and tests.
- **Supplemental:** the transcript index, intake, raw sources. Evidence, not record.
- **Governance Layer:** source register, open questions, scope watch, change log.

## Project Baseline
- Contract / SOW: SRC-0001 Order Fulfilment SOW v3
- Approved requirements: <link>
- Delivery baseline: Phase 1, labels at order processing

## Current Priorities
- High-impact decisions: ADR-0004 credit hold
- Open questions needing answers: Q-0003 (needed 2026-11-20), Q-0004
- Scope-watch items: SW-0002 order splitting
- Ingestion backlog: 2 transcripts from the November reviews

## Recently Changed Knowledge
- 2026-11-08: CH-0003 — one label per parcel, not per order

## Review Cadence
Weekly during discovery; on-change during implementation; full audit at handoff.
Owner: <role>.
```

**Notes.**
- It is an orientation doc, not a second rule set. Everything here is a pointer
  ([`../principles/one-home-per-fact.md`](../principles/one-home-per-fact.md)).
- Keep the layer explanation at the top. It is the only place a newcomer learns which files they are
  allowed to cite.
- *Current Priorities* is what makes the index worth reopening. Stale priorities are the usual reason
  nobody reads it.
- Its filename must not collide with the transcript index
  ([`../anti-patterns/the-transcript-index-overwriting-the-index.md`](../anti-patterns/the-transcript-index-overwriting-the-index.md)).
- Review cadence and ownership are defined here or in the config, and the audit checks that they are
  defined somewhere ([`../practices/audit-the-base.md`](../practices/audit-the-base.md)).

**Related.** [`the-two-trees.md`](the-two-trees.md), [`knowledge-config.md`](knowledge-config.md).
