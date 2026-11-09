---
id: US-07
aliases: [US-07]
type: user-story
status: draft
parent:
source-mode: C
sources: []
testing-complexity: Low
tracker-id:
tracker-url:
created: 2026-11-08
updated: 2026-11-08
review-required: true
---

# US-07 — Export the day's labels as a CSV

As a warehouse supervisor, I want to export the labels created today as a CSV, so that I can
reconcile them against the carrier's collection manifest.

> [!warning] Mode C — no sourced corpus
> Everything here is a transcription of what was asked for in conversation on 2026-11-08. No rule,
> ADR or requirement backs it, so no criterion carries a source id and `sources` is empty. It is not
> ready to build from until somebody confirms the scope it implies.

**Expected Output**
- A supervisor can download a CSV of the labels created on a chosen day.

**Details**
- Source grounding: None — Mode C. The request named the export and the reconciliation purpose, and
  nothing else.
- No parent Feature exists for this; one is **not** invented
  ([[an-invented-parent-id]]).

**Assumptions**
- "Today" means the warehouse's local calendar day. The request did not say.
- The CSV holds one row per label. The request did not name the columns.

**Testing Strategy**
- **Testing Complexity**: Low
- **UAT Approach**: Create three labels, export the day, confirm three rows.

**Open Questions**
- Which columns does the carrier's manifest need to reconcile against?
- Does a voided label appear in the export, and if so how is it marked?
- Who may export — any supervisor, or a named role?

**Technical Notes**
- **Permission**: To be determined by engineering
- **Feature flag**: To be determined by engineering
- **Design assets**: None

**Acceptance Criteria**
1. AC-1 [Request] Given labels created on a chosen day, when a supervisor exports that day, then a
   CSV downloads containing one row per label.

**Tags**
- Review Required
