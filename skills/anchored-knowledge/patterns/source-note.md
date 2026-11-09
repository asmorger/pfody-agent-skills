# Source note

**Use when** registering any source: a SOW, an email, a stakeholder answer, a sample file, a meeting.
One note per source in `sources/`, carrying its authority level and what it does **not** cover.

**Skeleton.** `sources/order-fulfilment-sow-v3.md`

```markdown
---
id: SRC-0001
aliases: [SRC-0001]
type: source
status: registered
source-type: sow
authority: 1-contractual
provider: Client
source-date: 2026-09-11
location: ../sow/order-fulfilment-sow-v3.docx
citable: false
created: 2026-09-12
updated: 2026-09-12
tags: [source/sow]
---

# Order Fulfilment SOW v3

The contractual baseline for Phase 1. Signed 2026-09-11.

**Does not cover** order splitting, partial despatch, or negotiated carrier rates. A statement about
any of those does not come from here.
```

A meeting note from the transcript index adds `participants: [Dana Lee, Priya N.]` and
`source-type: transcript`, and is named for its date: `sources/2026-01-21-order-fulfilment-scope-call.md`.

**Notes.**
- **Never list what this source updated.** Each rule names its source, so this note's **backlinks**
  are that list, and they are always current. That is the Source Register's Notes column, replaced by
  something that cannot go stale
  ([`../principles/properties-are-the-query-surface.md`](../principles/properties-are-the-query-surface.md)).
- `citable: false` on every source note. A source is evidence; only the record is citable
  ([`../principles/only-the-reference-layer-is-citable.md`](../principles/only-the-reference-layer-is-citable.md)).
- The authority level is recorded at registration, not judged later when a conflict makes it
  convenient ([`authority-ladder.md`](authority-ladder.md)).
- `location` points at the system of record. Register the original artifact, never an extraction of
  it, and never copy credentials, customer data or named remarks into the note.
- **"Does not cover" is the line that earns the note.** The gaps are what reconciliation needs, and
  the only place anybody records them.
- Register the transcript index and supporting folders too. Being registered is not being citable
  ([`../practices/ingest-transcripts.md`](../practices/ingest-transcripts.md)).
- A source that has gone stale keeps its note and takes `status: stale` with a dated callout; it is
  never deleted, because statements still point at it.

**Related.** [`intake-entry.md`](intake-entry.md), [`status-callouts.md`](status-callouts.md),
[`../practices/ingest-a-source.md`](../practices/ingest-a-source.md).
