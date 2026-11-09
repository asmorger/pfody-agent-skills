# Review findings

**Use when** writing the output of `REVIEW`. One note beside the hub, `prd/<prd-slug>.review.md`,
`type: prd-review`: the check result, findings in three groups, a readiness verdict, and the
questions to ask in order. Findings cite notes by id, so each is one click from its subject.

**Skeleton.**

```markdown
---
type: prd-review
prd: "[[PRD-001]]"
version: 0.4
checked: 2026-11-08
errors: 0           # and warnings: 4
verdict: not-ready
tags: [prd-review]
---
# Review of [[PRD-001]], version 0.4

**Check.** `prd.py check` — 0 errors, 4 warnings. The script does not judge whether a citation
supports its requirement, whether a slice is sound, or whether a criterion is faithful.

## Conflicts
- **[[R-003]] against [[DEC-02]].** R-003 refuses a label on credit hold; DEC-02 says the hold is
  advisory. Neither source settles precedence. → Raise as an open question; do not pick a side.
- **Scope against the SOW.** [[FEAT-02]] is not in [[SRC-02]] rev C. → Confirm: in scope, or a
  change request?

## Requirement quality

- **[[R-006]]** states two behaviours. → Split; R-006 keeps printing.
- **[[R-011]]** is `PROPOSED`. An Accepted PRD cannot hold one. → Source it, or retire it in place.

## Coverage

- **[[FEAT-01]]** `checks.permissions` is blank. → Answer with requirement links, `N/A` with a
  reason, or `Gap:` naming a question note. **[[OUT-2]]** has no requirement serving it.

## Readiness

Not ready for Gate 2: one conflict, one `PROPOSED` requirement, one blank coverage line.

## Questions, in order

1. Is voiding a label in scope? (Changes one Feature and three stories.)
2. Does a credit hold block labelling? (Changes [[R-003]] and its coverage.)
```

**Notes.**
- `REVIEW` changes nothing, ever — not even to fix a failing check
  ([`../principles/the-prd-changes-before-the-backlog.md`](../principles/the-prd-changes-before-the-backlog.md)).
- Three groups, always the same, conflicts first because they can invalidate the others.
- **Every finding names the note and the action**, citing it by id. "Section 4 is weak" is not a
  finding ([`../anti-patterns/a-green-check-as-approval.md`](../anti-patterns/a-green-check-as-approval.md)).
- Compare against the contract: scope drift against a SOW is routinely the largest finding, and the
  one nobody is looking for. Order the questions by how much scope the answer can move.

**Related.** [`../practices/review-a-prd.md`](../practices/review-a-prd.md),
[`coverage-moc.md`](coverage-moc.md).
