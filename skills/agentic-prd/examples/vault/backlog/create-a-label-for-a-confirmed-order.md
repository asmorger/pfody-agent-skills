---
id: US-01
aliases: [US-01]
type: user-story
status: accepted
prd: "[[PRD-001]]"
parent: "[[FEAT-01]]"
requirements: ["[[R-001]]", "[[R-002]]", "[[R-003]]", "[[X-002]]"]
testing-complexity: Medium
created: 2026-10-02
updated: 2026-11-05
tags: [backlog/user-story]
---

# US-01 — Create a label for a confirmed order

As a warehouse clerk, I want to create a carrier label from the order screen, so that a parcel
leaves without the address being typed again.

**Expected Output**
- A clerk can create a carrier label for a confirmed order from the order screen.
- The carrier's rejection reason is shown when the address is refused.
- An order on credit hold cannot be labelled.

**Details**
- The address comes from the order at confirmation ([[R-001]]).
- Source grounding: [[R-001]], [[R-002]], [[R-003]], [[X-002]].

**Assumptions**
- None identified.

**Testing Strategy**
- **Testing Complexity**: Medium
- **UAT Approach**: Confirm an order, create a label, check the carrier portal shows it; repeat with
  a bad address and with an order on credit hold.

**Open Questions**
- None identified.

**Technical Notes**
- **Permission**: Create label
- **Feature flag**: To be determined by engineering
- **Design assets**: None

**Acceptance Criteria**
1. AC-1 [R-001] Given a confirmed order, when a clerk creates a label, then a carrier label exists
   for the order's shipping address.
2. AC-2 [R-002] Given an address the carrier refuses, when a clerk creates a label, then the
   carrier's reason is shown and the order stays unlabelled.
3. AC-3 [R-003] Given an order on credit hold, when a clerk creates a label, then the system refuses
   and says why.
4. AC-4 [X-002] Given any label action, when it completes, then the order records the acting user
   and a timestamp.

**Tags**
- EPIC-01, FEAT-01
