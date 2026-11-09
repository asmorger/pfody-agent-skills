# Acceptance criterion

**Use when** turning sourced behaviour into tests. One form, one tag, no other citation.

**Skeleton.**

```markdown
**Acceptance Criteria**
1. AC-1 [LABEL-2] Given a printed label on an uncollected parcel, when a clerk voids it, then the
   order returns to the unlabelled state.
2. AC-2 [LABEL-2] Given a voided label, when the carrier scans it at collection, then the carrier
   rejects the parcel.
3. AC-3 [LABEL-3] Given a collected parcel, when a clerk attempts to void its label, then the system
   refuses and states that the parcel has been collected.
```

**Notes.**
- `AC-n [source tag] Given <precondition>, when <trigger>, then <observable result>.` Numbering
  restarts in each story ([`source-tag.md`](source-tag.md)).
- Count is whatever the source supports — typically three to seven, fewer where the source specifies
  fewer. Never pad ([`../anti-patterns/criteria-padded-to-a-count.md`](../anti-patterns/criteria-padded-to-a-count.md)).
- Order by implementation and testing priority: the primary output exists · the workflow consumes or
  displays it · core validation or enforcement · permission, role, state or eligibility behaviour ·
  edge cases, errors, audit and explicit exclusions.
- Each one is specific and measurable, independently testable, about *what* not *how*, falsifiable
  (prefer "is" and "can" over "should"), and proves the expected output rather than restating a rule.
- **Embed the behaviour**, so the criterion reads correctly with the source closed. The tag is a link,
  not the content ([`../principles/cite-once-per-story.md`](../principles/cite-once-per-story.md)).
- Add criteria for edge cases, validation, errors or permissions **only** where a source specifies
  them. Silence means an Open Question or nothing.
- If every criterion starts with a rule and none describes observable behaviour, rewrite the story
  ([`../anti-patterns/untestable-acceptance-criteria.md`](../anti-patterns/untestable-acceptance-criteria.md)).

**Related.** [`user-story.md`](user-story.md), [`expected-output.md`](expected-output.md).
