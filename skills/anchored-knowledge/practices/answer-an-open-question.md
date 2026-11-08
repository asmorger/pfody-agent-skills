# Answer an open question

**When** somebody answers a question the register is holding. Standing operating procedure C.

**Why.** An answer left in the register is behaviour recorded where nobody cites it. The base then has
the answer and the rule set does not, and every story built from the rule set is built from the older
understanding.

**Steps.**

1. **Record the answer and its source on the question row**, with the date and who gave it
   ([`../patterns/open-question.md`](../patterns/open-question.md)).
2. **Reconcile it before promoting it.** An answer is an incoming item like any other, and it may
   conflict with a rule that was written while the question was open
   ([`reconcile-against-the-rules.md`](reconcile-against-the-rules.md)).
3. **Promote the durable part** into a rule or an ADR — not the conversation, the behaviour. Remove
   the `**pending …**` marker from the affected rule and date the decided clause
   ([`write-a-business-rule.md`](write-a-business-rule.md)).
4. **Link back** from the question to the rule or ADR that now holds the answer, and set the row's
   status to `Answered`.
5. **Register the source** of the answer if it is new, with its authority level
   ([`../patterns/source-register-row.md`](../patterns/source-register-row.md)).
6. **Open a scope-watch item** if the answer implies work beyond the baseline. An answer is often how
   added scope arrives ([`../patterns/scope-watch-item.md`](../patterns/scope-watch-item.md)).
7. **Log a change entry** if the answer contradicts what the base previously said
   ([`log-a-knowledge-shift.md`](log-a-knowledge-shift.md)).
8. **Close the row**, and report which rule now carries the answer.

**Done when** the durable answer lives in a rule or ADR, the question links to it and is closed, the
affected rule has lost its pending marker and gained a date, and any scope or contradiction the
answer carried has its own entry.
