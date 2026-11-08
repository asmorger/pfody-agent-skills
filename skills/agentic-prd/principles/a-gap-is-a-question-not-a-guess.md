# A gap is a question, not a guess

**Rule.** When the sources do not answer something the PRD needs, write an open question with an id,
an owner and a date. Never fill the hole with a plausible value. A requirement whose behaviour is
unknown may say `<behaviour not known>` and carry the question in its Blocks column; it may not say
what the behaviour probably is.

**Why.** An agent builds whatever the page says, and a plausible guess reads exactly like a decision
somebody made. The cost arrives late: the build is correct against the PRD and wrong against the
business, and the review that would have caught it was a review of the code, not of the spec. A
question is the only form of a gap that survives into the backlog — decomposition skips a blocked
requirement and reports it, so the gap reaches the person who can close it
([`../practices/decompose-a-prd.md`](../practices/decompose-a-prd.md)).

**In the PRD.**
- Unknown metric values are the word `Unknown` plus a question, never an estimate
  ([`a-metric-needs-every-field.md`](a-metric-needs-every-field.md)).
- An unanswered coverage line is `Gap: Q-xx`, never blank and never removed
  ([`every-coverage-line-is-answered.md`](every-coverage-line-is-answered.md)).
- A date is recorded as the source gives it. A source that says "next quarter" does not become a
  date.
- Questions carry an owner and a needed-by ([`../patterns/open-question.md`](../patterns/open-question.md)).

**Breaks when.** Scope nobody asked for appears because it usually comes with a feature like this →
[`../anti-patterns/plausible-scope.md`](../anti-patterns/plausible-scope.md).
