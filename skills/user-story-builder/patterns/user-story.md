# User story note

**Use when** writing any story. One note per story in the config's stories folder. Every label
appears, in this order, even when empty — `- None identified`. Return the note only, no commentary.

**Skeleton.** `backlog/void-a-printed-label.md`

```markdown
---
id: US-03
aliases: [US-03]
type: user-story
status: draft                  # draft | ready | published
parent: "[[void-a-label|FEAT-02]]"          # copied from the source, never invented
source-mode: A
sources: ["[[a-printed-label-may-be-voided|LABEL-2]]", "[[bulk-printing-across-orders|LABEL-3]]", "[[enforce-credit-hold-at-label-creation|ADR-0004]]"]
testing-complexity: Medium
tracker-id:                    # filled by the publish step, never by hand
review-required: true
---

# US-03 — Void a printed label

As a shipping clerk, I want to void a label I have already printed, so that a cancelled order is not
collected by the carrier.

**Expected Output**
- A clerk can void a printed label from the order screen.
- The order returns to the unlabelled state and can be labelled again.

**Details**
- Source grounding: [[a-printed-label-may-be-voided|LABEL-2]], [[bulk-printing-across-orders|LABEL-3]], [[enforce-credit-hold-at-label-creation|ADR-0004]]. Voiding stops at collection.

**Assumptions** · **Testing Strategy** · **Open Questions** · **Technical Notes**
- "Any shipping clerk may void a label; the source does not restrict it to the creator."; Testing
  Complexity and a UAT approach; the supervisor-approval question; permission, flag and design
  assets. Each is its own `**Label**` line in a real note.

**Acceptance Criteria**
1. AC-1 [LABEL-2] Given a printed label on an uncollected parcel, when a clerk voids it, then the
   order returns to the unlabelled state.
2. AC-2 [LABEL-3] Given a collected parcel, when a clerk attempts to void it, then the system
   refuses and says why.

```

**Notes.**
- `sources` and the `Source grounding:` line say the same thing: one for queries and the publish
  step, one for the tracker's description — the only duplication the shape allows
  ([`../principles/cite-once-per-story.md`](../principles/cite-once-per-story.md)).
- A criterion's `[LABEL-2]` tag stays a bare id, not a wikilink: it is a **source tag**, sent to the
  tracker verbatim ([`source-tag.md`](source-tag.md)).
- A publishing adapter maps these labels to tracker fields, strips the wikilink brackets and
  normalises to ASCII ([`tracker-field-map.md`](tracker-field-map.md)).
- The Assumption above is the right move for an unsourced restriction, and the Open Question is its
  pair ([`../principles/a-gap-has-three-options.md`](../principles/a-gap-has-three-options.md)).
- Testing Complexity: `High` for money, security, integration, migration, complex state or
  concurrency · `Medium` for CRUD with rules or one integration · `Low` for display or config.

**Related.** [`as-a-i-want-so-that.md`](as-a-i-want-so-that.md), [`source-tag.md`](source-tag.md).
