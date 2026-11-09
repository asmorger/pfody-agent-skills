---
type: moc
updated: 2026-11-05
snapshot:
  type: requirement
  columns: [id, title, priority, verify, source, coverage]
  group-by: feature
  group-fallback: Cross-cutting
  exclude-status: [retired]
generator: prd.py moc
generated: 2026-11-09
input-paths: [requirements/]
input-manifest-sha256: bad215fc0e64001c16338fa88cde0d13b21f4435b565ed29b70d17a1e64f50fe
managed-block-sha256: ea6d4fb3ba923e486baf734c55f5922ee72fb617dc14aec331ca03f6b19fde5f
---

# Requirements

Every behaviour [[shipping-labels-at-order-processing|PRD-001]] commits to, one note each. A requirement is cited by its id from a
story's acceptance criteria, a commit and a test — which is why the id is immutable and a retired
requirement keeps its note.

![[requirements.base]]

<!-- generated: do not edit -->
### [[create-and-print-a-label|FEAT-01]]

| ID | Title | Priority | Verify | Source | Coverage |
|---|---|---|---|---|---|
| [[create-a-label-on-order-confirmation\|R-001]] | When a clerk confirms an order, the system shall create a carrier label for the order's shipping address. | P0 | Auto | SRC-01 @12:04 | covered |
| [[show-the-carrier-rejection-reason\|R-002]] | If the carrier rejects the address, then the system shall show the carrier's reason and leave the order unlabelled. | P0 | Auto | SRC-01 @18:30 | covered |
| [[refuse-a-label-on-credit-hold\|R-003]] | While an order is on credit hold, the system shall refuse to create a label. | P1 | Auto | DEC-02 | covered |

### [[void-a-label|FEAT-02]]

| ID | Title | Priority | Verify | Source | Coverage |
|---|---|---|---|---|---|
| [[void-a-printed-label\|R-012]] | When an authorised user voids a printed label, the system shall return the order to the unlabelled state. | P1 | Auto | SRC-04 @31:05 | blocked |
| [[print-labels-in-one-job\|R-014]] | Where bulk printing is enabled, the system shall print the labels of a selected set of orders in one job. | P3 | Manual | A-01 | skipped-p3 |

### Cross-cutting

| ID | Title | Priority | Verify | Source | Coverage |
|---|---|---|---|---|---|
| [[record-every-label-action\|X-002]] | The system shall record every label action against the order with the acting user and a timestamp. | P0 | Manual | DEC-02 | covered |
<!-- /generated -->
