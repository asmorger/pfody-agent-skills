# Survey note

**Use when** starting on a legacy area nobody can describe. One note per area, derived from the
code, the database and the logs, holding observed behaviours with their provenance and the questions
they raise. Never a record of what anyone decided.

**Skeleton.** `survey/label-printing.md`

```markdown
---
type: survey
status: surveyed           # surveyed | reviewed | sliced | replaced
area: label-printing
entry: frmLabelPrint.vb:1-980; LabelSvc.cls:1-420; usp_CreateLabel
generated: 2026-11-10 from legacy@a3f91c2
---

# Label printing

## Observed behaviours

B01  A label is created only for a confirmed order.      [code: LabelSvc.cls:112]
B02  Reprint writes a second label row and voids neither. [code: frmLabelPrint.vb:604]
B03  Carrier rejection text is logged, never shown.      [code: LabelSvc.cls:288]
B04  Audit row written only when weight > 0.             [db: trigger tr_label_post]
B05  Rush orders reprice from a fixed table.             [told: ops lead, 2026-10-14]
B06  Credit hold is bypassed for account class 7.        [assumed: unverified]

## Data touched
ORDER_HDR, LABEL, LABEL_VOID, AUDIT_POST
usp_CreateLabel, tr_label_post

## Usage (prod logs, 24 months)
labels 94,120 · reprints 1,308 · rush used 118 · negative weight 0
void reasons in use 3 of 11 defined

## Questions for the business
Q01 (B02) A reprint leaves two live labels. Bug, or relied on?
Q02 (B04) 8 of the 11 void reasons are referenced nowhere. Retire them?

## Questions for a named specialist
S01 (B05) Which rush prices are still correct? → the operations lead

## Still ours to verify
V01 Whether any report reads LABEL_VOID directly.
```

**Notes.**
- Behaviour ids are stable and never reused. A brief's rulings cite them, and a finding filed months
  later still has to resolve ([`slice-brief.md`](slice-brief.md)).
- Sort the three question lists by **who can answer**, not by importance. Sending a specialist's
  question to a product owner is how a markup session becomes a requirements meeting
  ([`../practices/review-the-findings.md`](../practices/review-the-findings.md)).
- The usage block exists to delete scope. Pair every count with its denominator.
- `generated:` names the commit so the note can be reproduced rather than trusted.

**Related.** [`provenance-tag.md`](provenance-tag.md),
[`../principles/a-survey-is-derived-and-disposable.md`](../principles/a-survey-is-derived-and-disposable.md),
[`../practices/survey-an-area.md`](../practices/survey-an-area.md).
