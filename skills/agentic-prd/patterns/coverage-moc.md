# Coverage MOC

**Use when** reporting what the backlog covers, or checking it. `moc/coverage.md` — a Bases view and
a generated table, both derived from the requirement notes. **Nobody maintains it.**

**Skeleton.**

```markdown
---
type: moc
updated: 2026-11-05
snapshot:
  type: coverage
tags: [moc]
---

# Coverage

One row per requirement, built from the requirement notes themselves. `blocked` and `skipped` are
results, not failures.

![[coverage.base]]

<!-- generated: do not edit -->
| Requirement | Pri | Verify | Story | Coverage |
|---|---|---|---|---|
| [[R-001]] | P0 | Auto | [[US-01]] | covered |
| [[R-012]] | P1 | Auto | [[Q-03]] | blocked |
| [[R-014]] | P3 | Manual | None | skipped-p3 |
| [[X-002]] | P0 | Manual | [[US-01]] | covered |

**Counts.** Requirements: 7 · blocked: 1 · covered: 4 · retired: 1 · skipped-p3: 1
<!-- /generated -->
```

**Notes.**
- Run `python3 scripts/prd.py moc <vault>` to fill it. It reads each requirement's `coverage` and
  `stories`, so **the table cannot disagree with the notes** — which is the whole reason the
  hand-kept version is gone ([`../practices/run-the-checks.md`](../practices/run-the-checks.md)).
- Every requirement gets a row, `X-` rows included. There is no blank cell: a requirement with no
  story shows the question blocking it, or `None` with a `skipped` coverage naming why
  ([`../principles/every-coverage-line-is-answered.md`](../principles/every-coverage-line-is-answered.md)).
- **Change a requirement to change the table.** An edit between the markers is discarded by the next
  regeneration, silently.
- The counts are the honest summary of the run; report them rather than a single "done"
  ([`../practices/report-the-result.md`](../practices/report-the-result.md)).
- This is coverage of *requirements by stories*. The seven per-Feature coverage lines are a different
  thing and live on the Feature note ([`coverage-check.md`](coverage-check.md)).

**Related.** [`requirement-note.md`](requirement-note.md), [`backlog-notes.md`](backlog-notes.md),
[`../references/vault-convention.md`](../references/vault-convention.md).
