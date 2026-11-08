# Coverage check

**Use when** closing out a Feature. The fixed list of behaviours nobody writes a requirement for and
every agent invents. It sits under the Feature's requirement table.

**Skeleton.**

```markdown
**Coverage check.**

| Check | Requirement IDs, or N/A and reason |
|---|---|
| Empty state | N/A — a confirmed order always has at least one line. |
| Loading state | R-007 |
| Error state | R-002, R-008 |
| Permissions | Gap: Q-03 |
| Bad input and boundaries | R-009 |
| Concurrency | R-010 |
| Current records and data migration | N/A — labels did not exist before this release. |
```

**Notes.**
- Three legal values per line: requirement ids, `N/A` plus a reason, or `Gap: Q-xx`. Never blank,
  never removed
  ([`../principles/every-coverage-line-is-answered.md`](../principles/every-coverage-line-is-answered.md)).
- `N/A` with no reason is a blank line wearing a label. The reason is the record that someone thought
  about it.
- `Gap: Q-xx` requires the question to exist in the ledger with an owner and a date
  ([`open-question.md`](open-question.md)).
- The same seven lines appear under every Feature, in this order, whatever the Feature does.
- Filling a line from inference means an `A-xx` row, not a citation.

**Related.** [`requirement-row.md`](requirement-row.md), [`open-question.md`](open-question.md),
[`../anti-patterns/a-blank-coverage-line.md`](../anti-patterns/a-blank-coverage-line.md).
