# User story

**Use when** writing a story in the backlog. Every label appears, in this order, even when a section
is empty — an empty section reads `None identified`.

**Skeleton.**

```markdown
### User Story: US-03 Void a printed label

As a shipping clerk, I want to void a label I have already printed, so that the parcel is not
collected against a cancelled order.

**Expected Output**
- A clerk can void a printed label from the order screen.
- A voided label is refused by the carrier at collection.
- The order returns to the unlabelled state and can be labelled again.

**Details**
- Source grounding: PRD-001 R-012, R-013, X-002.

**Assumptions**
- A-01 Bulk printing is not required for the first release.

**Testing Strategy**
- **Testing Complexity**: Medium
- **UAT Approach**: Print a label, void it, confirm the order is unlabelled and the carrier portal
  shows the label cancelled.

**Open Questions**
- Q-03 Who may void a printed label — any clerk, or a supervisor?

**Technical Notes**
- **Permission**: Void label
- **Feature flag**: labels.void
- **Design assets**: None

**Acceptance Criteria**
1. AC-1 [R-012] Given a printed label on a confirmed order, when a clerk voids it, then the order
   returns to the unlabelled state.
2. AC-2 [R-013] Given a voided label, when the carrier scans it at collection, then the carrier
   rejects the parcel.

**Tags**
- PRD-001, EPIC-01, FEAT-02, P0
```

**Notes.**
- *Source grounding* lists exactly the requirement ids the criteria cite; the check script compares
  the two sets. Up to four Expected Output bullets, each nameable to a source; Open Questions lists
  every question that could change the story, including one blocking a related requirement.
- A specific role, a need and a business reason; the *so that* clause does not restate the need
  ([`../principles/slice-by-outcome-not-by-layer.md`](../principles/slice-by-outcome-not-by-layer.md)).
- Testing Complexity: `High` for money, security, multi-system integration, migration or
  concurrency · `Medium` for business rules or one integration · `Low` for display or configuration.
- Permission is a capability name, or `None`. Feature flag is the name from section 8, `None`, or
  `To be determined by engineering`. Design assets is a real link or `None` — never a placeholder.

**Related.** [`acceptance-criterion.md`](acceptance-criterion.md), [`backlog-file.md`](backlog-file.md),
[`../practices/slice-a-feature.md`](../practices/slice-a-feature.md), [`../references/backlog-format.md`](../references/backlog-format.md).
