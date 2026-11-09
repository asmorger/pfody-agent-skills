# Knowledge change note

**Use when** a newer source refines, contradicts or supersedes what the record already says. One
note per shift in `changes/`, plus a dated callout on every note it touches.

**Skeleton.** `changes/one-label-per-parcel-not-per-order.md`

```markdown
---
id: CH-0003
aliases: [CH-0003]
type: knowledge-change
status: accepted
topic: labels
change-type: scope-refinement
identified: 2026-11-08
older: ["[[order-fulfilment-sow-v3]]", "[[one-label-per-parcel|LABEL-1]]"]
newer: ["[[operations-lead-on-split-orders]]"]
affects: ["[[one-label-per-parcel|LABEL-1]]", "[[confirmed-order-may-split-across-parcels|ORDER-5]]", "[[order-splitting-across-parcels|SW-0002]]"]
owner: delivery lead
created: 2026-11-08
updated: 2026-11-08
---

# CH-0003 — One label per parcel, not per order

**Previously.** One label per order, from [[order-fulfilment-sow-v3]] §4.2, which assumed one parcel
per order.

**Now.** The carrier counts per parcel, so a split order needs one label per parcel.
[[operations-lead-on-split-orders]] states it directly; the SOW does not contemplate splitting.

**Interpretation.** A refinement of [[one-label-per-parcel|LABEL-1]], not a contradiction — the SOW's wording held because
splitting did not exist. Splitting itself is added scope: [[order-splitting-across-parcels|SW-0002]].

**Done.** [[one-label-per-parcel|LABEL-1]] rewritten per parcel with a supersession callout · [[confirmed-order-may-split-across-parcels|ORDER-5]] added, draft ·
the prior boundary preserved in [[scope/one-parcel-per-order]] · [[partial-despatch-of-a-split-order|Q-0004]] opened.
```

**Notes.**
- **The interpretation line does the work.** Contradiction, refinement, terminology shift and
  correction get different treatment, and naming which stops a refinement being logged as a reversal
  ([`../principles/conflicts-are-recorded-not-resolved.md`](../principles/conflicts-are-recorded-not-resolved.md)).
- **Both anchor sets are mandatory.** A note with only `newer` cannot be audited. Both are wikilinks,
  so each source's backlinks show every shift it caused.
- `change-type` is one of: `contradiction` · `scope-refinement` · `terminology-shift` ·
  `decision-update` · `requirement-update` · `source-correction`.
- Every note in `affects` gets its own dated callout. The superseded understanding is preserved with
  its anchors, not edited away
  ([`status-callouts.md`](status-callouts.md)).
- Where authority does not settle it, the note opens a question rather than choosing
  ([`authority-ladder.md`](authority-ladder.md)).
- Add it to the start note's **Recently changed** list, so a reader sees it without searching
  ([`start-note.md`](start-note.md)).

**Related.** [`scope-watch-item.md`](scope-watch-item.md),
[`../practices/log-a-knowledge-shift.md`](../practices/log-a-knowledge-shift.md).
