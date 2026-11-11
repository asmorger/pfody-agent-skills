---
type: survey
status: reviewed           # surveyed | reviewed | sliced | replaced
area: label-printing
entry: frmLabelPrint.vb:1-980; LabelSvc.cls:1-420; usp_CreateLabel; tr_label_post
generated: 2026-11-10 from legacy@a3f91c2
---

# Label printing

> Invented content. See [`../README.md`](../README.md).

> DERIVED. Regenerate this file; never hand-edit it to record a decision. `[code:]` means we read
> it. `[db:]` means we queried it. `[logs:]` means we measured it. `[told:]` means a person said so
> and we have not checked. `[assumed:]` means we are guessing, and the reader should trust us least.

## Observed behaviours

B01  A label is created only for a confirmed order.        [code: LabelSvc.cls:112]
B02  Reprint writes a second label row and voids neither, so two labels are
     live for one order.                                   [code: frmLabelPrint.vb:604]
B03  Carrier rejection text is written to the log and never shown on the
     screen; the clerk sees "Label failed".                [code: LabelSvc.cls:288]
B04  The audit row is written only when weight > 0.        [db: trigger tr_label_post]
B05  Rush orders reprice from a fixed table of 14 prices.  [told: ops lead, 2026-10-14]
B06  Credit hold appears to be bypassed for account class 7; we could not
     reach the branch from the screen.                     [assumed: unverified]
B07  8 of the 11 void reasons are referenced nowhere: not in the client, not
     in the four reports, not in any stored procedure.
                 [code: exhaustive sweep of client, reports, stored procedures]

## Data touched

ORDER_HDR, LABEL, LABEL_VOID, AUDIT_POST
usp_CreateLabel, tr_label_post

## Usage (prod logs and database, 24 months)

labels 94,120 · reprints 1,308 · orders with two live labels 1,308
void reasons defined 11 · referenced in code 3 · rows holding an unreferenced
reason 2,904 · rush flag used 118 of 94,120 · negative weight 0

## Questions for the business

Q01 (B02) Every reprint leaves two live labels, 1,308 times in two years. Bug,
    or does the warehouse rely on the first one staying valid?
Q02 (B07) 8 of the 11 void reasons are referenced nowhere in the software, but
    2,904 rows still carry one. Retire them, or do they mean something to you
    outside the app?
Q03 (B04) The audit row is skipped below zero weight. Intended, or an accident?

## Questions for a named specialist

S01 (B05) Which of the 14 rush prices are still correct? → the operations lead
S02 (B03) Should the carrier's rejection text be shown to a clerk, or is it
    deliberately hidden? → the carrier-integration owner

## Still ours to verify

V01 Whether any of the four reports reads LABEL_VOID directly, which would make
    B07's sweep an undercount.
V02 Whether usp_CreateLabel is called by anything other than the desktop client.
