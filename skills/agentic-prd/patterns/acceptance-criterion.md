# Acceptance criterion

**Use when** turning a requirement into tests. One or more criteria per requirement, each carrying
its requirement's id.

**Skeleton.**

```markdown
1. AC-1 [R-001] Given a confirmed order with a shipping address, when a clerk requests a label, then
   the system creates a carrier label for that address.
2. AC-2 [R-002] Given an address the carrier rejects, when a clerk requests a label, then the system
   shows the carrier's reason and the order stays unlabelled.
3. AC-3 [R-003] Given an order on credit hold, when a clerk requests a label, then the system refuses
   and says why.
```

**Notes.**
- `AC-n [R-xxx] Given … when … then …`. The bracketed id is the machine-readable link from test to
  source; put no other citation in a criterion.
- Numbering restarts in each story. The requirement id carries the identity, so there is nothing to
  collide ([`../principles/ids-are-never-reused.md`](../principles/ids-are-never-reused.md)).
- Converting each requirement pattern:

      When X, the system shall Y    Given the precondition, when X, then Y
      While S, the system shall Y   Given S, when the person views or acts, then Y
      If X, then the system shall Y Given a state where X can occur, when X occurs, then Y
      The system shall Y            Given the related screen or data, when it is used, then Y

- The verify method shapes the criterion: `Manual` is named in the UAT approach; `Telemetry` names
  the event and its fields; `Eval` names the data set and the threshold.
- Order from the main output outward to the edges. Never add a criterion to reach a count
  ([`../anti-patterns/criteria-padded-to-a-count.md`](../anti-patterns/criteria-padded-to-a-count.md)).
- A criterion may not test behaviour its requirement does not state. If it needs to, the requirement
  changes first ([`../principles/the-prd-changes-before-the-backlog.md`](../principles/the-prd-changes-before-the-backlog.md)).

**Related.** [`user-story.md`](user-story.md), [`requirement-row.md`](requirement-row.md).
