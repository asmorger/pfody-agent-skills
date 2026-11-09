# A question is a queue, not a store

**Rule.** A question note holds a question, not knowledge. When one is answered, the durable part of
the answer is promoted into a rule or a decision, the question note points at it, and the question
closes. The answer never stays in the question as its permanent home.

**Why.** A register that accumulates answers becomes a second rule set — unreconciled, uncited,
read by nobody who was not already looking for an open question. The base then has two places where
behaviour is recorded, and the one everybody cites is missing the answer. Promotion also forces the
reconciliation that a register entry lets you skip: an answer written as a rule note has to be
checked against the rules around it, which is where contradictions get caught.

**In the base.**
- A question note carries `owner`, `needed-by`, `blocks`, the best answer so far and the next action
  ([`../patterns/open-question.md`](../patterns/open-question.md)).
- Answering it: promote the durable part into a rule or decision, point `answered-by` at it, set
  `status: answered`, and keep one line saying who answered and when
  ([`../practices/answer-an-open-question.md`](../practices/answer-an-open-question.md)).
- An answer that implies scope beyond the baseline opens a `SW-NNNN` as well
  ([`../patterns/scope-watch-item.md`](../patterns/scope-watch-item.md)).
- A question with no owner and no needed-by is an audit finding, not a question.
- The same discipline applies to intake: it is archived once its durable content is promoted, not
  kept as a parallel record.

**Breaks when.** The register becomes where behaviour is looked up →
[`../anti-patterns/the-register-as-a-knowledge-store.md`](../anti-patterns/the-register-as-a-knowledge-store.md).
