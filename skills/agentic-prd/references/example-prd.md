---
prd_id: PRD-001
title: Shipping Labels at Order Processing
status: Accepted
size: Standard
owner: Example TPO
approvers: [Example Operations Lead, Example Architect, Example QA Lead]
version: 1.0
updated: 2026-11-05
---

# Shipping Labels at Order Processing

> **Illustrative example only.** This PRD shows the format. The company, the sources, the numbers, and the decisions are invented. Do not use them as evidence.

## How this document works

This PRD is the source of record for **why** and **what**. Azure DevOps (ADO) is the source of record for **state**. The agent protocol is in the PRD template.

**Work item levels.** Each level has one ID format. Do not use another name for a level.

| Level | ID | What it is | Size test | Where it lives |
|---|---|---|---|---|
| Epic | `EPIC-01` | A business outcome that needs one or more Features | It serves an outcome in Section 1, and it can take more than one sprint | This PRD, Section 4 |
| Feature | `FEAT-01` | One capability: one job for one role | It delivers one job, and it needs one or more User Stories | This PRD, Section 4 |
| User Story | `US-01` | A vertical slice of one Feature | One person can build, test, and demo it in one sprint | The backlog file |
| Requirement | `R-001` | One testable behavior. It is not a tracker item. | It states one behavior, and it belongs to one Feature | This PRD, Section 4 |
| Acceptance criterion | `AC-1` | One Given/When/Then test of a Requirement | Its number restarts in each User Story | The backlog file |

---

## 1. Intent

**Narrative.** Warehouse clerks create a carrier label from the order screen. They do not enter the address again. Parcels leave faster and with fewer address errors.

**Problem.** Clerks copy each address from the order system to the carrier website. This step is slow and causes address errors. Evidence: SRC-01

**Users.**

| User | Need | Notes |
|---|---|---|
| Warehouse clerk | Create and print a label during order processing | Primary user. Uses a keyboard and a scanner. |
| Warehouse supervisor | Void a label when an order changes | Approves exceptions |

**Outcomes.**

| ID | Metric | Baseline | Target | Owner | Source system | Population | Denominator | Window |
|---|---|---|---|---|---|---|---|---|
| OUT-1 | Median label creation time | 240 s | 30 s or less | Operations Lead | `label_created` event | Domestic orders that clerks process | Not applicable (median) | First 30 days after release |
| OUT-2 | Label reprint rate from address errors | 3.0% | 1.0% or less | Operations Lead | Carrier invoice | Domestic labels | All domestic labels | First 30 days after release |

## 2. Scope

**In scope.**
- Create and print a domestic label from a paid order, with one carrier.
- Void an active label.

**Non-goals.**

| Non-goal | Reason | Revisit when |
|---|---|---|
| International labels | Customs data is not in the order system | OUT-1 meets its target |
| Compare carrier rates | The contract has one carrier | The contract changes |
| Create labels in a batch | Volume does not justify it in this release | Daily volume is more than 500 labels |

## 3. Context

**Current behavior.** A clerk opens the carrier website, copies the address, and prints the label. The clerk then enters the tracking number on the order.

**Team and links.**

| Discipline | Name | Team | Links |
|---|---|---|---|
| TPM/TPO | Example TPO | Delivery | Backlog link |
| Architect | Example Architect | Delivery | Architecture link, ADR link |
| Design | Example Designer | Delivery | Design link |
| Quality Assurance | Example QA Lead | Delivery | Test plan link |

**Constraints.** The order system stays the system of record for orders. The contract permits one carrier.

**Dependencies.**

| ID | Dependency | Details | Contact |
|---|---|---|---|
| DEP-01 | Carrier API | Creates and voids labels. A sandbox is available. | Carrier account manager |
| DEP-02 | Order system API | Supplies the address, the weight, and the payment status | Example Architect |

**Glossary.**

| Term | Meaning | Do not use |
|---|---|---|
| Label | The carrier document that a clerk prints for one parcel | Waybill, sticker |
| Active label | A label that the carrier issued and that nobody has voided | Live label |
| Void | Cancel a label with the carrier | Delete, remove |

## 4. Epics, Features, and requirements

**Work item map.** User Stories are in the backlog file, because agents generate them.

| ID | Level | Name | Parent | Tracker item |
|---|---|---|---|---|
| EPIC-01 | Epic | Shipping Labels at Order Processing | PRD-001 | none |
| FEAT-01 | Feature | Create and print a label | EPIC-01 | none |
| FEAT-02 | Feature | Void a label | EPIC-01 | none |

### EPIC-01: Shipping Labels at Order Processing

**Outcome.** Clerks create labels from the order screen, with fewer address errors.

**Outcomes served.** OUT-1, OUT-2

#### FEAT-01: Create and print a label

**Job.** As a warehouse clerk, I can create a shipping label when I process the order, so that I do not enter the address again.

**Outcomes served.** OUT-1, OUT-2

**Design.** Design link

| ID | Requirement | Pri | Source | Verify |
|---|---|---|---|---|
| R-001 | When the clerk selects Create label on a paid order, the system shall request a label from the carrier with the ship-to address and the package weight of the order. | P0 | SRC-02 | Auto |
| R-002 | When the carrier returns a label, the system shall store the tracking number on the order and show the label for print. | P0 | SRC-02 | Auto |
| R-003 | While a label request is in progress, the system shall disable Create label and show a progress indicator. | P1 | DEC-01 | Auto |
| R-004 | If the order is not paid, then the system shall block label creation and show "Payment is not complete." | P0 | SRC-02 | Auto |
| R-005 | If the carrier rejects the ship-to address, then the system shall show the reason from the carrier and keep the current order status. | P0 | SRC-03 | Auto |
| R-006 | If the carrier does not respond in 10 seconds, then the system shall show a Retry action. | P0 | SRC-03 | Auto |
| R-007 | When the clerk selects Retry, the system shall not create a second label for the same parcel. | P0 | SRC-03 | Auto |
| R-008 | While an order has an active label, the system shall show that label and hide Create label. | P1 | SRC-02 | Auto |

**Coverage check.**

| Check | Requirement IDs, or N/A and reason |
|---|---|
| Empty state | N/A. The action starts from one order. There is no list. |
| Loading state | R-003 |
| Error state | R-005, R-006 |
| Permissions | N/A. All warehouse roles can create labels. SRC-02 |
| Bad input and boundaries | R-004, R-005 |
| Concurrency | R-007, R-008 |
| Current records and data migration | N/A. Current orders keep their tracking numbers. No migration. DEC-02 |

#### FEAT-02: Void a label

**Job.** As a warehouse supervisor, I can void a label when an order changes, so that the business does not pay for an unused label.

**Outcomes served.** None. This capability is a control for FEAT-01. DEC-03

**Design.** Design link

| ID | Requirement | Pri | Source | Verify |
|---|---|---|---|---|
| R-009 | When the supervisor selects Void on an active label, the system shall send a void request to the carrier and mark the label as Void. | P1 | SRC-02 | Auto |
| R-010 | If a user without the Supervisor role requests a void, then the system shall deny the request. | P1 | SRC-02 | Auto |
| R-011 | If the carrier has scanned the parcel, then the system shall <behavior not known>. | P1 | SRC-02 | Manual |

**Coverage check.**

| Check | Requirement IDs, or N/A and reason |
|---|---|
| Empty state | N/A. The action starts from one label. |
| Loading state | N/A. The workshop did not request an indicator for a void. SRC-02 |
| Error state | R-011 |
| Permissions | R-010 |
| Bad input and boundaries | R-011 |
| Concurrency | N/A. One supervisor works on each shift. SRC-02 |
| Current records and data migration | N/A. Current labels stay outside this system. DEC-02 |

## 5. Cross-cutting requirements

| ID | Applies to | Requirement | Pri | Source | Verify |
|---|---|---|---|---|---|
| X-001 | FEAT-01 | The system shall let the clerk create and print a label with the keyboard only. | P1 | SRC-02 | Manual |
| X-002 | FEAT-01 | When the carrier returns a label, the system shall record the `label_created` event. | P0 | DEC-01 | Telemetry |

## 6. Agent boundaries

**Always.**
- Read this PRD and the assigned User Story before you write code.
- Add or update a test for each acceptance criterion with `Verify: Auto`.
- Use the carrier sandbox for all tests.
- Put the User Story ID and the requirement IDs in the pull request.

**Ask first.**
- Add a dependency, a service, or a data store.
- Change the order schema.
- Change behavior that a requirement does not describe.

**Never.**
- Do not build a non-goal or a P3 requirement.
- Do not fill a gap with a guess. Stop. Add an open question.
- Do not call the production carrier API.
- Do not change a test to make it pass unless the requirement changed.

**Checks.**

```bash
dotnet build
dotnet test
npm run lint
```

**Stop conditions.** Stop and report when a requirement conflicts with code, another requirement, or a constraint. Stop when a check fails after 3 attempts.

## 7. Knowledge ledger

**Sources.**

| ID | Source | Type | Link | Date |
|---|---|---|---|---|
| SRC-01 | Time study of label creation (invented) | Verified | SharePoint link | 2026-09-14 |
| SRC-02 | Operations workshop summary (invented) | Stakeholder: Operations Lead | ADO wiki link | 2026-09-22 |
| SRC-03 | Carrier API guide (invented) | Verified | Carrier docs link | 2026-09-25 |

**Decisions.**

| ID | Decision | Owner | Date | Reason | Rejected options | Revisit when |
|---|---|---|---|---|---|---|
| DEC-01 | Accept the agent proposals R-003 and X-002 | Operations Lead | 2026-10-01 | R-003 prevents double requests. X-002 supplies OUT-1. | Measure OUT-1 with a new time study | Not applicable |
| DEC-02 | Do not migrate current labels | Operations Lead | 2026-10-01 | Current labels finish in the carrier website | Import open labels | Support reports a problem |
| DEC-03 | Keep FEAT-02 in this release with no outcome | Operations Lead | 2026-10-01 | Clerks need a safe way to correct an error | Void with the carrier website | Not applicable |

**Assumptions and inferences.**

| ID | Statement | Type | Basis | What makes it false | Affects |
|---|---|---|---|---|---|
| A-01 | The order record contains a correct package weight | Assumption | Workshop statement. No data check. | More than 2% of sampled orders have no weight | R-001 |

**Open questions.**

| ID | Question | Owner | Needed by | Blocks | Status |
|---|---|---|---|---|---|
| Q-01 | Does the carrier permit a void after the first parcel scan? If it does, what is the fee? | Example TPO | 2026-11-20 | R-011 | Open |

## 8. Rollout and measurement

**Rollout.** Release behind the `shipping-labels` flag. Start with one warehouse for two weeks. Then release to all warehouses. To roll back, turn off the flag. Clerks then use the carrier website.

**Telemetry.**

| Event | Dimensions | Data type | Serves | Requirement |
|---|---|---|---|---|
| `label_created` | order_id, warehouse_id, duration_ms | string, string, integer | OUT-1 | X-002 |
