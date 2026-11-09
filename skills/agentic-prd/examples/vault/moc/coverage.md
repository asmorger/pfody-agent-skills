---
type: moc
updated: 2026-11-05
snapshot:
  type: coverage
generator: prd.py moc
generated: 2026-11-09
input-paths: [requirements/]
input-manifest-sha256: e077957d63e98eaf33f94bbd16d2def0bd217ee4d0dc671f447f7c9d04c99d84
managed-block-sha256: eaf4f8b93378000e3e44e8641fc3b04520592df896124088f0ae4b25b6070e46
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
| [[one-label-per-order\|R-005]] | P1 | Auto | None | retired |
| [[void-a-printed-label\|R-012]] | P1 | Auto | [[who-may-void-a-printed-label\|Q-03]] | blocked |
| [[print-labels-in-one-job\|R-014]] | P3 | Manual | None | skipped-p3 |
| [[record-every-label-action\|X-002]] | P0 | Manual | [[create-a-label-for-a-confirmed-order\|US-01]] | covered |

**Counts.** Requirements: 7 · blocked: 1 · covered: 4 · retired: 1 · skipped-p3: 1
<!-- /generated -->
