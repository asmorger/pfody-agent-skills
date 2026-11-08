# A question is a queue, not a store

**Rule.** The open-questions register holds questions, not knowledge. When one is answered, the
durable part of the answer is promoted into a rule or an ADR, the question links to it, and the
register row closes. The answer never stays in the register as its permanent home.

**Why.** A register that accumulates answers becomes a second rule set — unreconciled, uncited,
read by nobody who was not already looking for an open question. The base then has two places where
behaviour is recorded, and the one everybody cites is missing the answer. Promotion also forces the
reconciliation that a register entry lets you skip: an answer written into `business-rules.md` has to
be checked against the rules around it, which is where contradictions get caught.

**In the base.**
- A question row carries id, status, owner, needed-by, anchor, best current answer, next action, and
  the final answer ([`../patterns/open-question.md`](../patterns/open-question.md)).
- Answering it: record the answer and its source on the row, promote the durable part into a rule or
  ADR, link back, then close
  ([`../practices/answer-an-open-question.md`](../practices/answer-an-open-question.md)).
- An answer that implies scope beyond the baseline opens a `SW-NNNN` as well
  ([`../patterns/scope-watch-item.md`](../patterns/scope-watch-item.md)).
- A question with no owner and no needed-by is an audit finding, not a question.
- The same discipline applies to intake: it is archived once its durable content is promoted, not
  kept as a parallel record.

**Breaks when.** The register becomes where behaviour is looked up →
[`../anti-patterns/the-register-as-a-knowledge-store.md`](../anti-patterns/the-register-as-a-knowledge-store.md).
