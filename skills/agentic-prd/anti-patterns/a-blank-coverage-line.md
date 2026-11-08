# A blank coverage line

**Smell.** A coverage check with Permissions, Concurrency or Empty state left empty — or, worse, the
row deleted because it obviously did not apply. Sometimes `N/A` with no reason, which is the same
thing wearing a label.

**Why it is wrong.** These are the behaviours nobody writes a requirement for and every agent
invents: no requirement describes the empty list, so the agent designs one, and the design ships. A
blank line records nothing about whether anyone thought about it; a deleted line hides that the
question was ever asked, so the next reviewer cannot tell a considered omission from an oversight.
`N/A` without a reason is unfalsifiable — the reason is the whole content.

**Instead.** Answer every line, every time: requirement ids, `N/A` plus the reason it cannot arise
("a confirmed order always has at least one line"), or `Gap: Q-xx` with the question in the ledger.
Keep all seven lines under every Feature in the same order, whatever the Feature does
([`../principles/every-coverage-line-is-answered.md`](../principles/every-coverage-line-is-answered.md),
[`../patterns/coverage-check.md`](../patterns/coverage-check.md)).
