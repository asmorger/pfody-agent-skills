# Every coverage line is answered

**Rule.** Each Feature carries the same fixed list of coverage checks — empty state, loading, error,
permissions, bad input and boundaries, concurrency, existing records and migration. Every line gets
requirement ids, or `N/A` with a reason, or `Gap: Q-xx`. No line is left blank and no line is deleted,
even when it looks irrelevant.

**Why.** These are the behaviours everyone forgets and an agent invents: nobody writes a requirement
for the empty list, so the agent designs one. A fixed list turns the forgetting into an answerable
question, and `N/A` with a reason is a real answer — it records that someone considered concurrency
and decided it could not arise here. A blank line records nothing, and a deleted line hides that the
question was ever asked.

**In the PRD.**
- The block sits under each Feature, after its requirement table
  ([`../patterns/coverage-check.md`](../patterns/coverage-check.md)).
- `N/A` always comes with its reason: "N/A — the list cannot be empty; every order has one line."
- `Gap: Q-xx` means the question exists in the ledger, with an owner and a date.
- A check filled from inference, not a source, is an `A-xx`, not a citation
  ([`implied-is-not-stated.md`](implied-is-not-stated.md)).

**Breaks when.** A line is left empty or quietly dropped →
[`../anti-patterns/a-blank-coverage-line.md`](../anti-patterns/a-blank-coverage-line.md).
