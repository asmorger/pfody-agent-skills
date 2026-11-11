# Slice brief

**Use when** rulings exist and work is about to start. One note per slice: the demo sentence, the
appetite, the blast radius, the rulings against a survey's behaviour ids, and the checks that must
pass before the switch.

**Skeleton.** `slices/reprint-a-label.md`

```markdown
---
id: SL-007
aliases: [SL-007]
type: slice-brief
status: frozen             # shaping | frozen | flipped | abandoned
area: label-printing
demo: A clerk reprints a label and the superseded one is voided, with the
      new path serving the screen.
appetite: 9 judgment-hours · ~2 wks wall clock
toggle: slice.label-reprint.v2   (legacy path stays hot)
blast: one additive nullable column; no schema migration; no shared-code
       refactor; no change to label creation; no change to the void screen
frozen: 2026-11-13
---

# SL-007 — Reprint a label

## Keep / change / drop
B01 confirmed-order gate   KEEP    as observed      [survey B01 · PM 11-11]
B02 reprint leaves two     CHANGE  void the first   [survey B02 · PM 11-11]
B04 audit weight floor     DROP    always write     [survey B04 · ops 11-11]
B05 rush repricing         DEFER   not this slice; the slice does not read
                                   the price table  [survey B05 · no owner yet]

## What this slice deliberately does not decide
Whether the 11 void reasons are still meaningful. The slice writes one of the
three in use and leaves the vocabulary alone, so Q02 can stay open.

## Checks
char/label_reprint_*.approved      golden master, all orders, must not change
new/reprint_voids_the_first        new behaviour (B02)
parallel-run: label-row diff = 0 over 500 reprints before the flip

## No-gos
The price table. The void-reason vocabulary. Any migration.

## Decisions outstanding: 0
```

**Notes.**
- One demo sentence in the user's words. If it needs a conjunction, it is two slices.
- Every ruling row carries a survey id, a decider and a date. A row without all three is not a
  ruling ([`../principles/decisions-outstanding-must-read-zero.md`](../principles/decisions-outstanding-must-read-zero.md)).
- `blast:` is written as negatives, because a list of what is untouched is what a reviewer can argue
  with ([`../principles/blast-radius-not-size.md`](../principles/blast-radius-not-size.md)).
- The *does not decide* section is the seam; naming it is what keeps the count at zero.
- After the freeze the body gains only a dated `## Amendments` section
  ([`../principles/a-frozen-brief-is-appended-never-rewritten.md`](../principles/a-frozen-brief-is-appended-never-rewritten.md)).

**Related.** [`check-set.md`](check-set.md), [`survey-note.md`](survey-note.md),
[`../practices/shape-a-slice.md`](../practices/shape-a-slice.md).
