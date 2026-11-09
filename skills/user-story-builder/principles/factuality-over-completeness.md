# Factuality over completeness

**Rule.** A short, sourced story beats a complete-looking story with invented requirements. Where a
formatting or coverage rule appears to demand content the source does not support, this rule wins.
One sourced Expected Output bullet means one bullet. Two sourced criteria mean two criteria.

**Why.** An incomplete story is visibly incomplete: the gaps are in Open Questions, somebody answers
them, and the cost is one conversation. A complete-looking story is invisibly wrong — it gets
estimated, assigned, built and accepted, and the invented requirement is discovered as working
software nobody asked for. The asymmetry is the whole argument. Under-reach is cheap and
self-correcting; over-reach is expensive and self-concealing, and a story's apparent thoroughness is
exactly what stops anyone checking it.

**In the story.**
- Never fill a quota with inference. Not Expected Output bullets, not criteria, not Technical Notes
  ([`../anti-patterns/criteria-padded-to-a-count.md`](../anti-patterns/criteria-padded-to-a-count.md)).
- Three to seven criteria is typical. Fewer is correct when the source specifies fewer.
- Up to four Expected Output bullets. One is a legitimate story
  ([`../patterns/expected-output.md`](../patterns/expected-output.md)).
- A narrower story is the right answer to a thin source. An Open Question is the right answer to a
  gap that needs a decision
  ([`a-gap-has-three-options.md`](a-gap-has-three-options.md)).

**Breaks when.** Scope arrives because features like this usually have it →
[`../anti-patterns/pattern-matched-scope.md`](../anti-patterns/pattern-matched-scope.md).
