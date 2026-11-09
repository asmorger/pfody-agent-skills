# Per-bullet traceability

**Rule.** Before output, for every Expected Output bullet and every acceptance criterion, name the
specific source to yourself — a SOW deliverable, a rule id, an ADR, a file, an estimate line, the
user's request. If you cannot name it, that bullet does not belong there: move it to Assumptions,
move it to Open Questions, or delete it.

**Why.** This is the check that makes every other rule enforceable, because it is applied per line
rather than per story. A story reviewed as a whole reads as sourced if most of it is; reviewed bullet
by bullet, the two or three invented lines are obvious. It is also what makes the story auditable
later by someone who was not involved — the same pass run against an existing story is exactly the
audit this skill offers
([`../practices/review-an-existing-story.md`](../practices/review-an-existing-story.md)).

**In the story.**
- The check is silent and per line. It does not produce a citation per bullet — citation is
  consolidated ([`cite-once-per-story.md`](cite-once-per-story.md)).
- Three legal destinations for an untraceable bullet, and deletion is one of them. There is no
  "probably fine" ([`a-gap-has-three-options.md`](a-gap-has-three-options.md)).
- Apply it to Technical Notes too. The optional bullets — entity base, tenancy, resource-scoped
  authorization, validation highlights — are where unsourced detail hides most comfortably.
- An Assumption must still be an *explicit unconfirmed assumption*, not a requirement in disguise.

**Breaks when.** A bullet survives because it seemed obviously right →
[`../anti-patterns/pattern-matched-scope.md`](../anti-patterns/pattern-matched-scope.md).
