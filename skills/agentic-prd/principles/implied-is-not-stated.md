# Implied is not stated

**Rule.** A behaviour a source implies but does not state is marked `PROPOSED`, or raised as an open
question. It is never given a `SRC-xx`. The test is mechanical: if you cannot quote the sentence that
says it, the source does not say it.

**Why.** Inference is the step where a spec stops being a record and becomes an argument. Each
inference is individually reasonable, and a page of them is a product nobody agreed to. Marking the
inference keeps it visible to the approver, who is the only person entitled to promote it — and keeps
the honest ones, which are often right, from being thrown away along with the rest.

**In the PRD.**
- "The source mentions a void button, so there is presumably a void permission" → `PROPOSED`, or a
  question.
- An inference the project will rely on gets an `A-xx` row naming its basis and what would make it
  false ([`../patterns/knowledge-ledger.md`](../patterns/knowledge-ledger.md)).
- A priority nobody assigned is recorded as an inference, not as a judgement of yours.
- Say in the review which requirements rest on inference, so the approver sees the stack
  ([`../practices/review-a-prd.md`](../practices/review-a-prd.md)).

**Breaks when.** The inference is dressed as a citation →
[`../anti-patterns/implied-behaviour-as-sourced.md`](../anti-patterns/implied-behaviour-as-sourced.md).
