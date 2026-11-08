# Open question

**Use when** the sources do not answer something the PRD needs. The one shape a gap is allowed to
take.

**Skeleton.**

```markdown
**Open questions.**

| ID | Question | Owner | Needed by | Blocks | Status |
|---|---|---|---|---|---|
| Q-03 | Who may void a printed label — any clerk, or a supervisor? | Operations lead | 2026-11-20 | R-012, FEAT-02 coverage: permissions | Open |
| Q-04 | What is today's address-error rate, and where is it read from? | Operations lead | Gate 2 | OUT-1 baseline | Open |
| Q-05 | Does the carrier charge for a voided label? | Account manager | 2026-11-20 | R-014 | Answered — see DEC-05 |
```

**Notes.**
- *Blocks* is what makes a question operational: decomposition skips a blocked requirement and
  reports it, so the gap reaches the person who can close it rather than becoming an invented
  behaviour ([`../practices/decompose-a-prd.md`](../practices/decompose-a-prd.md)).
- A blocked requirement may read `<behaviour not known>` and keep its id, priority and verify method.
- *Needed by* is a date. A draft may use a gate name until there is a schedule — `Gate 2` above —
  but never nothing.
- Answering a question does not leave the answer here. Promote it into a requirement or a `DEC-xx`
  row and point back, so the ledger stays a queue rather than a second place to look for behaviour.
- A question with no owner is a review finding, not a question.

**Related.** [`knowledge-ledger.md`](knowledge-ledger.md), [`coverage-check.md`](coverage-check.md),
[`../principles/a-gap-is-a-question-not-a-guess.md`](../principles/a-gap-is-a-question-not-a-guess.md).
