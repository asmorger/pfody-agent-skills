# The register as a knowledge store

**Smell.** An open-questions file where half the rows say `Answered` and hold two paragraphs of
behaviour in their *Final answer* field. Nothing in `business-rules.md` reflects any of it. The same
shape in intake: a long file of durable knowledge, triage status `Untriaged`, six weeks old.

**Why it is wrong.** It becomes a second rule set — unreconciled, uncited, read only by people already
looking for an open question. The base then has two places where behaviour is recorded and the one
everybody cites is missing the answer, so stories get built from the older understanding while the
answer sits in a file marked closed. Promotion is also what forces reconciliation: an answer written
into the rules has to be checked against the rules around it, which is where contradictions get
caught. Left in the register, nothing checks it.

**Instead.** Treat both files as queues. An answered question's durable part is promoted into a rule
or an ADR, the question links to it and closes; an intake entry is archived once its content is
promoted. The register keeps the question, the owner, the date and the trail — not the behaviour
([`../principles/a-question-is-a-queue-not-a-store.md`](../principles/a-question-is-a-queue-not-a-store.md),
[`../practices/answer-an-open-question.md`](../practices/answer-an-open-question.md)).
