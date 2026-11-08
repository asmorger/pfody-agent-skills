# Auto-editing the rule set

**Smell.** `business-rules.md` edited directly because the incoming source was unambiguous. Four
rules refined "while I was in there". A report that says "updated the business rules" without naming
which ones.

**Why it is wrong.** The rule set is what a team has agreed to, and an agent is not a party to that
agreement — however obviously right the edit is. The silent edit also destroys the property that
makes the base useful under pressure: that a rule says what someone decided it should say. And the
unnamed ids are the practical harm. An approval covering "the new rules" is not an approval of the
four existing rules the change also touched, and without the id list the user cannot see that it did.

**Instead.** Draft in the working area; present an audit with the quoted current text beside the
recommendation; apply only what is approved; then report the exact ids added, changed and deprecated.
Where a refinement is genuinely obvious, it is also obviously cheap to approve — the cost of asking is
one message, and it is the difference between a record and a guess
([`../principles/propose-then-apply.md`](../principles/propose-then-apply.md),
[`../patterns/reconciliation-audit.md`](../patterns/reconciliation-audit.md)).
