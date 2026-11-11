---
id: SL-007
aliases: [SL-007]
type: slice-brief
status: frozen
area: label-printing
demo: A clerk reprints a label and the superseded one is voided, with the new
      path serving the reprint button.
appetite: 9 judgment-hours · ~2 wks wall clock · tokens order 10^1 USD
toggle: slice.label-reprint.v2   (legacy path stays hot)
blast: one additive nullable column (LABEL.SUPERSEDED_BY); no schema migration;
       no shared-code refactor; no change to label creation; no change to the
       void-reason vocabulary; no change to the four reports
frozen: 2026-11-13
---

# SL-007 — Reprint a label

> Invented content. See [`../README.md`](../README.md).

> DECIDED. Frozen at build start. New learning is appended under Amendments with a date and a
> decider. Nothing above the freeze line is rewritten.

## Keep / change / drop

B01 confirmed-order gate   KEEP    as observed             [survey B01 · PM 11-11]
B02 reprint leaves two     CHANGE  void the superseded one
                                   with reason RP          [survey B02 · PM 11-11]
B04 audit weight floor     DROP    always write the row    [survey B04 · ops 11-11]
B07 8 unreferenced reasons DEFER   safe: this slice writes RP, which is one of
                                   the three in use, and reads no other reason
                                                           [survey B07 · PM 11-11]
B05 rush repricing         DEFER   safe: the reprint path does not price
                                                           [survey B05 · no owner yet]
B03 hidden rejection text  DEFER   safe: creation path only, not reprint
                                                           [survey B03 · carrier owner]

## What this slice deliberately does not decide

Whether the 11 void reasons are still meaningful. The slice writes one existing reason and reads
none, so Q02 and S01 can stay open for as long as they need to.

## Checks

char/label_reprint_*.approved
    Golden master, recorded by driving LabelSvc over all 94,120 orders, not by
    reading the survey. Must not change.
char/label_create_*.approved
    Unchanged creation path, recorded for the same population.
new/reprint_voids_the_superseded_label        new behaviour (B02)
new/audit_row_written_at_zero_weight          new behaviour (B04)
parallel-run
    5 working days. Every reprint resolves both paths and logs a label-row diff.
    Flip required 0 diffs over at least 500 reprints. Actual: 0 over 612.

## No-gos

The price table. The void-reason vocabulary. The four reports. Any migration.

## Decisions outstanding: 0

## Amendments

- **2026-11-19** — B01 was wrong. The confirmed-order gate also admits orders in `PENDING_HOLD`,
  which the golden master caught on its first run; 41 of 94,120 take that path. Survey entry
  regenerated, tag stayed `[code:]`, finding filed. No ruling changed: `KEEP` still means match the
  old system, and the old system admits both. *PM, 11-19.*
- **2026-11-24** — Appetite was 9 judgment-hours, actual 14, driven almost entirely by standing up
  the golden-master harness for the first time. Finding filed; it sizes the next slice, not this
  one. *Tech lead, 11-24.*
