# Knowledge in two places

**Smell.** A rule note summarising what `order-data-mapping` spells out. A glossary definition that
restates its governing rule. A decision's wording copied into the rule note as a paragraph. A MOC
whose prose lists the rules its own table already lists.

**Why it is wrong.** Two copies are one rule and one bug waiting for the next correction. The
correction reaches one copy, and nothing announces that the other has gone stale — so the base starts
answering the same question two ways, and the reader who finds the wrong copy has no signal that a
right one exists. Duplication also silently doubles the reconciliation cost: a new source now
contradicts two entries, and an audit that checks one passes.

**Instead.** One home, and links everywhere else. The rule states the behaviour; mechanics go in a
reference note it links to; a glossary note says what a word means and links to the governing rule;
the decision holds the reasoning and the rule cites it. Where a reader genuinely needs the other
note's words in place, **embed** it — `![[ORDER-1]]` resolves to whatever that note says now, which
is the opposite of a copy. When a statement seems to belong in two notes it is usually two statements
— a *what* and a *how* — and they get split, not copied
([`../principles/one-home-per-fact.md`](../principles/one-home-per-fact.md),
[`../patterns/reference-note.md`](../patterns/reference-note.md)).
