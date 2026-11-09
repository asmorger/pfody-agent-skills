# Answer an open question

**When** somebody answers a question the register is holding. Standing operating procedure C.

**Why.** An answer left in the register is behaviour recorded where nobody cites it. The base then has
the answer and the rule set does not, and every story built from the rule set is built from the older
understanding.

**Steps.**

1. **Record the answer and its source on the question note**, with the date and who gave it
   ([`../patterns/open-question.md`](../patterns/open-question.md)).
2. **Reconcile it before promoting it.** An answer is an incoming item like any other, and it may
   conflict with a rule that was written while the question was open
   ([`reconcile-against-the-rules.md`](reconcile-against-the-rules.md)).
3. **Promote the durable part** into a rule or a decision note — not the conversation, the
   behaviour. Remove the `[!question] Open` callout from the affected rule and set its `confirmed`
   date ([`write-a-business-rule.md`](write-a-business-rule.md)).
4. **Point `answered-by` at the note that now holds the answer**, set `status: answered`, and leave
   one line saying who answered and when. The answer itself does not stay here
   ([`../principles/a-question-is-a-queue-not-a-store.md`](../principles/a-question-is-a-queue-not-a-store.md)).
5. **Write a source note** for the answer if it is new, with its authority level, and point the
   rule's `sources` at it ([`../patterns/source-note.md`](../patterns/source-note.md)).
6. **Open a scope-watch item** if the answer implies work beyond the baseline. An answer is often how
   added scope arrives ([`../patterns/scope-watch-item.md`](../patterns/scope-watch-item.md)).
7. **Log a change entry** if the answer contradicts what the base previously said
   ([`log-a-knowledge-shift.md`](log-a-knowledge-shift.md)).
8. **Close the question and regenerate**, and report which rule now carries the answer
   ([`regenerate-the-mocs.md`](regenerate-the-mocs.md)).

**Done when** the durable answer lives in a rule or decision note, the question's `answered-by`
points at it and its status is `answered`, the affected rule has lost its open callout and gained a
date, and any scope or contradiction the answer carried has its own note.
