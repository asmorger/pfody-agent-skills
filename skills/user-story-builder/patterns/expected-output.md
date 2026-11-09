# Expected Output

**Use when** naming what the story actually delivers. Up to four bullets, one per sourced deliverable.
This is the section that decides whether the story is buildable.

**Skeleton.**

```markdown
**Expected Output**
- A clerk can void a printed label from the order screen.          ← workflow
- The void is recorded against the order with the acting clerk.    ← persisted data
- A voided label is refused by the carrier at collection.          ← integration behaviour
- Voiding is blocked once the parcel is collected.                 ← enforcement
```

A one-bullet story is legitimate:

```markdown
**Expected Output**
- A clerk can void a printed label from the order screen.
```

**Notes.**
- Each bullet is one of: persisted data or configuration · workflow behaviour · user-facing
  visibility · validation or enforcement · API or integration behaviour · audit or history output.
  Nothing from that list means the story is not buildable
  ([`../principles/a-story-produces-something-buildable.md`](../principles/a-story-produces-something-buildable.md)).
- **Do not pad to four.** If the source supports one, write one
  ([`../principles/factuality-over-completeness.md`](../principles/factuality-over-completeness.md)).
- Every bullet must be traceable to a named source. One that is not moves to Assumptions or Open
  Questions, or goes ([`../principles/per-bullet-traceability.md`](../principles/per-bullet-traceability.md)).
- Weak: "Configure label eligibility and constraints" — the output is only rules. Better: "Persist and
  enforce label eligibility settings", with saved settings, evaluation, blocking and admin lockout as
  the bullets.
- Describe the deliverable and where it appears or changes behaviour, not how it is implemented.

**Related.** [`user-story.md`](user-story.md),
[`../anti-patterns/a-business-rule-as-a-story.md`](../anti-patterns/a-business-rule-as-a-story.md).
