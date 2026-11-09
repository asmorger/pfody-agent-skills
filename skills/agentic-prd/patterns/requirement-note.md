# Requirement note

**Use when** writing or fixing any requirement. One note, one behaviour, one of five patterns, with
its source, priority, verify method and coverage in frontmatter.

**Skeleton.** `requirements/create-a-label-on-order-confirmation.md`

```markdown
---
id: R-001
aliases: [R-001]
type: requirement
status: accepted           # draft | accepted | retired
prd: "[[shipping-labels-at-order-processing|PRD-001]]"
feature: "[[create-and-print-a-label|FEAT-01]]"
priority: P0               # P0 | P1 | P2 | P3
verify: Auto               # Auto | Manual | Eval | Telemetry
source: SRC-01 @12:04      # SRC-nn + locator | DEC-nn | A-nn | PROPOSED
outcomes: ["[[address-error-rate-on-parcels|OUT-1]]"]
coverage: covered          # covered | blocked | skipped-proposed | skipped-p3 | retired
stories: ["[[create-a-label-for-a-confirmed-order|US-01]]"]
---

# R-001 — When a clerk confirms an order, the system shall create a carrier label for the order's shipping address.

The address is taken from the order at confirmation, not re-entered.
```

**Notes.**
- **The statement is the H1**, and the five patterns are what the check looks for:

      Always    The system shall <behaviour>.
      Event     When <trigger>, the system shall <behaviour>.
      State     While <state>, the system shall <behaviour>.
      Unwanted  If <bad condition>, then the system shall <behaviour>.
      Optional  Where <option is on>, the system shall <behaviour>.

- `coverage: covered` requires `stories`; `coverage: blocked` requires `questions`. The check
  enforces both, which is how the coverage table stays derivable
  ([`coverage-moc.md`](coverage-moc.md)).
- Priorities: `P0` no project without it · `P1` needed for a functional release · `P2` nice to have ·
  `P3` a later release, `coverage: skipped-p3`, not decomposed.
- An `X-` requirement has no `feature` and must name `applies-to`: `All`, or the `FEAT` ids whose
  behaviour it changes.
- **Retire in place.** `status: retired`, `coverage: retired`, a `superseded-by` link and an
  `[!abstract]` callout holding what changed. The note and the id stay forever
  ([`../principles/ids-are-never-reused.md`](../principles/ids-are-never-reused.md)).
- A blocked requirement may state `<behaviour not known>` and keep its id, priority and verify
  method ([`open-question.md`](open-question.md)).

**Related.** [`acceptance-criterion.md`](acceptance-criterion.md),
[`../principles/one-behaviour-per-requirement.md`](../principles/one-behaviour-per-requirement.md),
[`../anti-patterns/vague-requirement.md`](../anti-patterns/vague-requirement.md).
