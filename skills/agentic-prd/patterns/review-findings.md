# Review findings

**Use when** writing the output of `REVIEW`. A file beside the PRD, `<prd-name>.review.md`: the check
result, findings in three groups, a readiness verdict, and the questions to ask in order.

**Skeleton.**

```markdown
# Review of PRD-001, version 0.4

**Check.** `check_prd.py` — 0 errors, 4 warnings. The script does not judge whether a citation
supports its requirement, whether a slice is sound, or whether a criterion is faithful.

## Conflicts

- **R-003 against DEC-02.** R-003 refuses a label on credit hold; DEC-02 says the hold is advisory
  until it moves into the order system. Neither source settles the order of precedence. → Raise as
  an open question; do not pick a side.
- **Scope against the SOW.** FEAT-02 (void a label) is not in SRC-02 rev C. → Confirm whether void
  is in scope or a change request.

## Requirement quality

- **R-006** states two behaviours — printing and reprinting. → Split; R-006 keeps printing.
- **R-009** says "the system shall respond quickly". → Give a threshold, or mark it `PROPOSED`.
- **R-011** is `PROPOSED`. An Accepted PRD cannot hold one. → Source it, or retire it.

## Coverage

- **FEAT-01 permissions** is blank. → Answer, `N/A` with a reason, or `Gap: Q-xx`.
- **OUT-2** has no requirement serving it. → Add one, or drop the outcome.

## Readiness

Not ready for Gate 2: one unsettled conflict, one `PROPOSED` requirement, one blank coverage line.

## Questions, in order

1. Is voiding a label in scope for this release? (Changes one Feature and three stories.)
2. Does a credit hold block labelling? (Changes R-003 and its coverage.)
3. Who may void a label? (Changes one story's permission.)
```

**Notes.**
- `REVIEW` changes nothing, ever — not even to fix a failing check
  ([`../principles/the-prd-changes-before-the-backlog.md`](../principles/the-prd-changes-before-the-backlog.md)).
- Three groups, always the same: conflicts, requirement quality, coverage. Conflicts come first
  because they are the findings that can invalidate the others.
- Every finding names the item and the action. "Section 4 is weak" is not a finding.
- Compare against the contract and any earlier requirements where they exist. Scope drift against a
  SOW is routinely the largest finding and the one nobody is looking for.
- Order the questions by how much scope the answer can move, not by section number. The first
  question is the one that could make the rest moot.

**Related.** [`../practices/review-a-prd.md`](../practices/review-a-prd.md),
[`../anti-patterns/a-green-check-as-approval.md`](../anti-patterns/a-green-check-as-approval.md).
