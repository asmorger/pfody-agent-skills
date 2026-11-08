# Deprecate, never delete

**Rule.** Knowledge that goes out of scope, gets deferred or is superseded stays in the base, clearly
marked, with its anchors intact and its id unchanged. Rewrite the rule to say what is now true about
it — "**not in Phase 2 scope**. Deferred to a future phase." — and leave it where it is.

**Why.** "Did we ever agree to that?" is the question a knowledge base is most often asked, and a
deleted rule cannot answer it. Worse, deletion loses the anchor: the rule was recorded because a
source said something, and that source is still what it is. Six weeks later the behaviour gets
re-proposed as new, re-argued from scratch, and nobody can show it was considered and dropped. A
deprecated rule answers in one read and costs one line.

**In the base.**
- Out of scope or deferred: keep the id, rewrite the rule text, state the phase.
- A superseded understanding ends with the supersession note and its date:
  `*(Supersedes <earlier understanding>; confirmed 2026-11-08.)*`
  ([`../patterns/inline-status-markers.md`](../patterns/inline-status-markers.md)).
- Superseded assumptions are preserved with their anchors, not edited into the new version
  ([`../patterns/knowledge-change-entry.md`](../patterns/knowledge-change-entry.md)).
- An ADR is superseded by a later ADR, never overwritten. A refinement that reverses nothing gets a
  dated addendum ([`../patterns/decision-record.md`](../patterns/decision-record.md)).
- The glossary keeps retired aliases, in the definition of the term that replaced them.

**Breaks when.** A rule is removed because it is no longer being built →
[`../anti-patterns/deleting-an-out-of-scope-rule.md`](../anti-patterns/deleting-an-out-of-scope-rule.md).
