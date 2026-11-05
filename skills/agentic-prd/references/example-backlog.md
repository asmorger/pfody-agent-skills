# Backlog for PRD-001, version 1.0

> **Illustrative example only.** This file shows the output of Mode: DECOMPOSE. Do not edit behavior here. Change the PRD with Mode: CHANGE, then regenerate.

## Work item summary

| ID | Level | Title | Parent |
|---|---|---|---|
| EPIC-01 | Epic | Shipping Labels at Order Processing | PRD-001 |
| FEAT-01 | Feature | Create and print a label | EPIC-01 |
| US-01 | User Story | Create and print a label for a paid order | FEAT-01 |
| US-02 | User Story | Block a label when the order or the address is not valid | FEAT-01 |
| US-03 | User Story | Recover from a carrier timeout with no duplicate label | FEAT-01 |
| FEAT-02 | Feature | Void a label | EPIC-01 |
| US-04 | User Story | Void an active label as a supervisor | FEAT-02 |

---

# Epic: Shipping Labels at Order Processing (EPIC-01)

## Feature: Create and print a label (FEAT-01)

### User Story: US-01 Create and print a label for a paid order

As a warehouse clerk, I want to create a label from the order, so that I do not enter the address again.

**Expected Output**
- A Create label action on a paid order that returns a printable label
- A tracking number stored on the order

**Details**
- Source grounding: PRD-001 R-001, R-002, R-003, R-008, X-001, X-002.

**Assumptions**
- A-01: The order record contains a correct package weight.

**Testing Strategy**
- **Testing Complexity**: Medium
- **UAT Approach**: Open a paid order in the sandbox. Create a label with the keyboard only. Confirm that the label prints and that the order shows the tracking number.

**Open Questions**
- None identified

**Technical Notes**
- **Permission**: Create label
- **Feature flag**: shipping-labels
- **Design assets**: Design link

**Acceptance Criteria**
1. AC-1 [R-001] Given a paid order, when the clerk selects Create label, then the carrier receives a label request with the order address and weight.
2. AC-2 [R-002] Given a label request, when the carrier returns a label, then the order shows the tracking number and the label can print.
3. AC-3 [R-003] Given a label request in progress, when the clerk views the order, then Create label is disabled and a progress indicator shows.
4. AC-4 [R-008] Given an order with an active label, when the clerk opens the order, then the label shows and Create label does not show.
5. AC-5 [X-001] Given a paid order, when the clerk uses the keyboard only, then the clerk can create and print a label.
6. AC-6 [X-002] Given a label request, when the carrier returns a label, then the system records the `label_created` event with order_id, warehouse_id, and duration_ms.

**Tags**
- PRD-001, EPIC-01, FEAT-01, P0

### User Story: US-02 Block a label when the order or the address is not valid

As a warehouse clerk, I want to see why a label cannot be created, so that I can correct the problem before the pickup.

**Expected Output**
- A block on label creation for an order that is not paid
- A message that shows the carrier reason for a rejected address

**Details**
- Source grounding: PRD-001 R-004, R-005.

**Assumptions**
- None identified

**Testing Strategy**
- **Testing Complexity**: Medium
- **UAT Approach**: Try to create a label for an unpaid order. Then use a sandbox address that the carrier rejects. Confirm each message and that the order status does not change.

**Open Questions**
- None identified

**Technical Notes**
- **Permission**: Create label
- **Feature flag**: shipping-labels
- **Design assets**: Design link

**Acceptance Criteria**
1. AC-1 [R-004] Given an unpaid order, when the clerk selects Create label, then no request occurs and "Payment is not complete." shows.
2. AC-2 [R-005] Given a paid order, when the carrier rejects the ship-to address, then the carrier reason shows and the order status does not change.

**Tags**
- PRD-001, EPIC-01, FEAT-01, P0

### User Story: US-03 Recover from a carrier timeout with no duplicate label

As a warehouse clerk, I want to retry after a carrier timeout, so that the business pays for only one label.

**Expected Output**
- A Retry action after a carrier timeout
- A retry that creates one label for one parcel

**Details**
- Source grounding: PRD-001 R-006, R-007.

**Assumptions**
- None identified

**Testing Strategy**
- **Testing Complexity**: High
- **UAT Approach**: Simulate a carrier timeout in the sandbox. Select Retry. Confirm that the carrier account shows one label for the parcel.

**Open Questions**
- None identified

**Technical Notes**
- **Permission**: Create label
- **Feature flag**: shipping-labels
- **Design assets**: Design link

**Acceptance Criteria**
1. AC-1 [R-006] Given a label request, when the carrier does not respond in 10 seconds, then a Retry action shows.
2. AC-2 [R-007] Given a timed-out label request, when the clerk selects Retry, then the carrier has one label for the parcel.

**Tags**
- PRD-001, EPIC-01, FEAT-01, P0

---

## Feature: Void a label (FEAT-02)

### User Story: US-04 Void an active label as a supervisor

As a warehouse supervisor, I want to void an active label, so that the business does not pay for an unused label.

**Expected Output**
- A Void action on an active label, for supervisors only
- A label status of Void after the carrier accepts the request

**Details**
- Source grounding: PRD-001 R-009, R-010.
- The behavior after a carrier scan is not in this User Story. Q-01 blocks R-011.

**Assumptions**
- None identified

**Testing Strategy**
- **Testing Complexity**: Medium
- **UAT Approach**: Sign in to the sandbox as a supervisor and void an active label. Then try the same action as a clerk. Confirm that the system denies the clerk.

**Open Questions**
- Q-01: Does the carrier permit a void after the first parcel scan? If it does, what is the fee?

**Technical Notes**
- **Permission**: Void label
- **Feature flag**: shipping-labels
- **Design assets**: Design link

**Acceptance Criteria**
1. AC-1 [R-009] Given an active label, when the supervisor selects Void, then the carrier receives a void request and the label status is Void.
2. AC-2 [R-010] Given an active label, when a non-supervisor requests a void, then the system denies the request and the label stays active.

**Tags**
- PRD-001, EPIC-01, FEAT-02, P1

---

# Coverage

| Requirement | Pri | Verify | User Story | Criterion | Status |
|---|---|---|---|---|---|
| R-001 | P0 | Auto | US-01 | AC-1 | Covered |
| R-002 | P0 | Auto | US-01 | AC-2 | Covered |
| R-003 | P1 | Auto | US-01 | AC-3 | Covered |
| R-004 | P0 | Auto | US-02 | AC-1 | Covered |
| R-005 | P0 | Auto | US-02 | AC-2 | Covered |
| R-006 | P0 | Auto | US-03 | AC-1 | Covered |
| R-007 | P0 | Auto | US-03 | AC-2 | Covered |
| R-008 | P1 | Auto | US-01 | AC-4 | Covered |
| R-009 | P1 | Auto | US-04 | AC-1 | Covered |
| R-010 | P1 | Auto | US-04 | AC-2 | Covered |
| R-011 | P1 | Manual | None | None | Blocked by Q-01 |
| X-001 | P1 | Manual | US-01 | AC-5 | Covered |
| X-002 | P0 | Telemetry | US-01 | AC-6 | Covered |

**Counts.** Requirements: 13. Covered: 12. Blocked: 1. Skipped P3: 0. Epics: 1. Features: 2. User Stories: 4.
