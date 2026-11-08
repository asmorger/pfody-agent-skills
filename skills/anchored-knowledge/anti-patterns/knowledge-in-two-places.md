# Knowledge in two places

**Smell.** The label rules summarised in `business-rules.md` and spelled out in
`order-data-mapping.md`. A glossary definition that restates the rule. An ADR's decision copied into
the rule row as a paragraph. A convention doc repeating what the API rules already say.

**Why it is wrong.** Two copies are one rule and one bug waiting for the next correction. The
correction reaches one copy, and nothing announces that the other has gone stale — so the base starts
answering the same question two ways, and the reader who finds the wrong copy has no signal that a
right one exists. Duplication also silently doubles the reconciliation cost: a new source now
contradicts two entries, and an audit that checks one passes.

**Instead.** One home, and links everywhere else. The rule states the behaviour; mechanics go in a
reference doc the rule links to; the glossary says what a word means and links to the governing rule;
the ADR holds the reasoning and the rule cites it. When a statement seems to belong in two files, it
is usually two statements — a *what* and a *how* — and they get split, not copied
([`../principles/one-home-per-fact.md`](../principles/one-home-per-fact.md),
[`../patterns/convention-doc.md`](../patterns/convention-doc.md)).
