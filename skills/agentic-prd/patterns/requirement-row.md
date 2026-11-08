# Requirement row

**Use when** writing or fixing any requirement. One row, one behaviour, one of five patterns, a
source, a priority and a verify method.

**Skeleton.**

```markdown
| ID | Requirement | Pri | Source | Verify |
|---|---|---|---|---|
| R-001 | When a clerk confirms an order, the system shall create a carrier label for the order's shipping address. | P0 | SRC-01 @12:04 | Auto |
| R-002 | If the carrier rejects the address, then the system shall show the carrier's reason and leave the order unlabelled. | P0 | SRC-01 @18:30 | Auto |
| R-003 | While an order is on credit hold, the system shall refuse to create a label. | P1 | DEC-02 | Auto |
| R-004 | Where bulk printing is enabled, the system shall print the labels of a selected set of orders in one job. | P2 | A-01 | Manual |
| R-005 | Retired. Superseded by R-011. | P1 | SRC-01 @18:30 | Auto |
```

**Notes.**
- The five patterns, whose opening words the check script looks for:

      Always    The system shall <behaviour>.
      Event     When <trigger>, the system shall <behaviour>.
      State     While <state>, the system shall <behaviour>.
      Unwanted  If <bad condition>, then the system shall <behaviour>.
      Optional  Where <option is on>, the system shall <behaviour>.

- Source is one of `SRC-xx` with a locator, `DEC-xx`, `A-xx`, or `PROPOSED`
  ([`../principles/every-requirement-cites-a-source.md`](../principles/every-requirement-cites-a-source.md)).
- Verify is `Auto` (a build can run it), `Manual` (UAT or exploratory), `Eval` (a scored data set,
  module M1) or `Telemetry`.
- Priorities: `P0` no project without it · `P1` needed for a functional release · `P2` nice to have,
  tagged `Stretch` · `P3` a later release, not decomposed. A priority nobody assigned is recorded as
  an inference.
- `X-001`-style rows live in section 5 and name what they apply to: `All`, or specific `FEAT` ids.
- Retire in place; never reuse the number
  ([`../principles/ids-are-never-reused.md`](../principles/ids-are-never-reused.md)).

**Related.** [`coverage-check.md`](coverage-check.md),
[`acceptance-criterion.md`](acceptance-criterion.md),
[`../principles/one-behaviour-per-requirement.md`](../principles/one-behaviour-per-requirement.md),
[`../anti-patterns/vague-requirement.md`](../anti-patterns/vague-requirement.md).
