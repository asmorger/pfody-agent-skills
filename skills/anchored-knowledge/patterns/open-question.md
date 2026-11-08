# Open question

**Use when** the sources do not answer something the base needs. A queue entry — not a place to store
the answer once it arrives.

**Skeleton.**

```markdown
## Q-0003 - Who may void a printed label?

**Status:** Open | Partial | Answered | Blocked | No Longer Needed
**Owner:** Operations lead
**Needed by:** 2026-11-20
**Source/anchor:** SRC-0004; LABEL-2
**Related:** LABEL-2, SW-0002

**Question**
Can any shipping clerk void a printed label, or does it need a supervisor?

**Current best answer**
SRC-0004 says voiding exists but not who may do it. The carrier portal allows it for any authenticated
account, which is not an authority statement about our users.

**Next action**
Operations lead to confirm in the 2026-11-18 review; record as a rule on LABEL-2.

**Final answer**
<answer, date, source. Promote the durable part into a rule or ADR and link it here.>
```

**Notes.**
- Owner and needed-by are mandatory. A question with neither cannot close, so it is an audit finding
  rather than a question ([`../practices/audit-the-base.md`](../practices/audit-the-base.md)).
- *Current best answer* is where an honest partial goes — including evidence that does not settle it,
  labelled as not settling it.
- Answering it means promoting the durable part into a rule or ADR and linking back; the register row
  closes ([`../practices/answer-an-open-question.md`](../practices/answer-an-open-question.md)).
- An answer that implies scope beyond the baseline opens a scope-watch item too
  ([`scope-watch-item.md`](scope-watch-item.md)).
- The affected rule carries the open part inline — `**pending final operations lead confirmation**`
  with the question id ([`inline-status-markers.md`](inline-status-markers.md)).

**Related.** [`../principles/a-question-is-a-queue-not-a-store.md`](../principles/a-question-is-a-queue-not-a-store.md),
[`assumptions-ledger.md`](assumptions-ledger.md).
