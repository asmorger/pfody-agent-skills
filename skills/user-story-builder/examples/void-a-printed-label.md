---
id: US-03
aliases: [US-03]
type: user-story
status: draft
parent: "[[void-a-label|FEAT-02]]"
source-mode: A
sources: ["[[a-printed-label-may-be-voided|LABEL-2]]", "[[bulk-printing-across-orders|LABEL-3]]", "[[enforce-credit-hold-at-label-creation|ADR-0004]]"]
testing-complexity: Medium
tracker-id:
tracker-url:
created: 2026-11-08
updated: 2026-11-08
tags: [backlog/user-story, review-required]
---

# US-03 — Void a printed label

As a shipping clerk, I want to void a label I have already printed, so that a cancelled order is not
collected by the carrier.

**Expected Output**
- A clerk can void a printed label from the order screen.
- A voided label is refused by the carrier at collection.
- The order returns to the unlabelled state and can be labelled again.

**Details**
- A label may be voided only while the parcel has not been collected ([[bulk-printing-across-orders|LABEL-3]]).
- Source grounding: [[a-printed-label-may-be-voided|LABEL-2]], [[bulk-printing-across-orders|LABEL-3]], [[enforce-credit-hold-at-label-creation|ADR-0004]].

**Assumptions**
- Any shipping clerk may void a label; the source does not restrict it to the creator.

**Testing Strategy**
- **Testing Complexity**: Medium
- **UAT Approach**: Print a label, void it, confirm the order shows unlabelled and the carrier portal
  shows the label cancelled.

**Open Questions**
- Does voiding require supervisor approval, or may any clerk do it?

**Technical Notes**
- **Permission**: Void label
- **Feature flag**: To be determined by engineering
- **Design assets**: None

**Acceptance Criteria**
1. AC-1 [LABEL-2] Given a printed label on an uncollected parcel, when a clerk voids it, then the
   order returns to the unlabelled state.
2. AC-2 [LABEL-3] Given a collected parcel, when a clerk attempts to void its label, then the system
   refuses and says why.

**Tags**
- Review Required, EPIC-01, FEAT-02
