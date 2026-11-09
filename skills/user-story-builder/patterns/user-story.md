# User story

**Use when** writing any story. Every label appears, in this order, even when a section is empty —
`- None identified`. Return markdown only, with no commentary before or after.

**Skeleton.**

```markdown
### User Story: US-03 Void a printed label

As a shipping clerk, I want to void a label I have already printed, so that a cancelled order is not
collected by the carrier.

**Expected Output**
- A clerk can void a printed label from the order screen.
- A voided label is refused by the carrier at collection.
- The order returns to the unlabelled state and can be labelled again.

**Details**
- A label may be voided only while the parcel has not been collected (LABEL-3).
- Source grounding: docs/business-rules.md LABEL-2, LABEL-3; ADR-0004.

**Assumptions**
- Any shipping clerk may void a label; the source does not restrict it to the creator.

**Testing Strategy**
- **Testing Complexity**: Medium
- **UAT Approach**: Print a label, void it, confirm the order shows unlabelled and the carrier portal
  shows the label cancelled.

**Open Questions**
- Does voiding require supervisor approval, or may any clerk do it?

**Technical Notes**
- **Permission**: Void label
- **Feature flag**: To be determined by engineering
- **Design assets**: None

**Acceptance Criteria**
1. AC-1 [LABEL-2] Given a printed label on an uncollected parcel, when a clerk voids it, then the
   order returns to the unlabelled state.
2. AC-2 [LABEL-3] Given a collected parcel, when a clerk attempts to void its label, then the system
   refuses and says why.

**Tags**
- Review Required, EPIC-01, FEAT-02
```

**Notes.**
- A publishing adapter maps these labels to tracker fields. Do not embed tracker field names here
  ([`tracker-field-map.md`](tracker-field-map.md)).
- One consolidated `Source grounding` in `Details`; one tag per criterion; nothing else
  ([`../principles/cite-once-per-story.md`](../principles/cite-once-per-story.md)).
- The Assumption above is the correct move for an unsourced restriction, and the Open Question is its
  pair ([`../principles/a-gap-has-three-options.md`](../principles/a-gap-has-three-options.md)).
- Testing Complexity: `High` for money, security, multi-system integration, migration, complex state
  or concurrency · `Medium` for CRUD with rules or one integration · `Low` for display or config.

**Related.** [`as-a-i-want-so-that.md`](as-a-i-want-so-that.md), [`expected-output.md`](expected-output.md),
[`acceptance-criterion.md`](acceptance-criterion.md), [`technical-notes.md`](technical-notes.md).
