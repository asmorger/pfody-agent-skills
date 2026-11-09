---
type: moc
updated: 2026-11-05
snapshot:
  type: coverage
generator: prd.py moc
generated: 2026-11-09
input-paths: [requirements/]
input-manifest-sha256: 5e08599bd14edea30394555db2372a1c918b2cd92aac3ebdd3b4e288dc5276d8
managed-block-sha256: c7fecf60b84127815471e15a37aab9c9dc224d4cb59163331588e2fc024576ee
---

# Coverage

One row per requirement, built from the requirement notes themselves — so it cannot disagree with
them the way a hand-kept table does. `blocked` and `skipped` are results, not failures: a blocked
requirement is a gap that reached the person who can close it instead of becoming an invented
behaviour.

![[coverage.base]]

<!-- generated: do not edit -->
| Requirement | Pri | Verify | Story | Coverage |
|---|---|---|---|---|
| [[create-a-label-on-order-confirmation\|R-001]] | P0 | Auto | [[create-a-label-for-a-confirmed-order\|US-01]] | covered |
| [[show-the-carrier-rejection-reason\|R-002]] | P0 | Auto | [[create-a-label-for-a-confirmed-order\|US-01]] | covered |
| [[refuse-a-label-on-credit-hold\|R-003]] | P1 | Auto | [[create-a-label-for-a-confirmed-order\|US-01]] | covered |
| [[one-label-per-order-requirement\|R-005]] | P1 | Auto | None | retired |
| [[void-a-printed-label\|R-012]] | P1 | Auto | [[who-may-void-a-printed-label\|Q-0003]] | blocked |
| [[print-labels-in-one-job\|R-014]] | P3 | Manual | None | skipped-p3 |
| [[record-every-label-action\|X-002]] | P0 | Manual | [[create-a-label-for-a-confirmed-order\|US-01]] | covered |

**Counts.** Requirements: 7 · blocked: 1 · covered: 4 · retired: 1 · skipped-p3: 1
<!-- /generated -->
