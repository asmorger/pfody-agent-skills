# The agent picks a side

**Smell.** Two sources disagree and the PRD states one of them, with that source's citation and no
mention of the other. Or a conflict is "resolved" in prose — "the later discussion suggests the
supervisor approves voids" — where no decision says so.

**Why it is wrong.** Which statement holds is almost never a question about the statements; it is a
question about who has authority and what has happened since, and the agent has neither fact. A
quietly resolved conflict is the most expensive thing a PRD can carry, because it looks settled: it
passes review, it gets built, and the losing stakeholder finds out at the demo. There is also no
trail — nothing records that a choice was made, so the argument restarts from scratch.

**Instead.** Apply the one resolution that is allowed: a newer *decision* supersedes an older
statement, cited as `ADR-xxxx`. Everything else is recorded — name both sources with their locators and
open a question with an owner and a date. One question now, instead of a release later
([`../principles/a-conflict-is-recorded-not-resolved.md`](../principles/a-conflict-is-recorded-not-resolved.md),
[`../patterns/open-question.md`](../patterns/open-question.md)).
