# A gap has three options

**Rule.** When source coverage runs out there are exactly three moves: state it as an explicit
unconfirmed **Assumption**; raise it as an **Open Question** when it needs a stakeholder decision; or
**omit** it and leave the story narrower. There is no fourth option.

**Why.** Naming the options closes the escape route. Without them, the reflex at the edge of a source
is to write the plausible behaviour and hope — and the hope is invisible in the output, because an
invented requirement is formatted identically to a sourced one. All three legal moves keep the gap
visible to the person who can close it, which is the only thing that makes a thin source safe to work
from.

**In the story.**
- Assumption: "Only the clerk who created the label may void it." Unconfirmed, and labelled so.
- Open Question: decision-oriented, answerable by product, business or architecture. Not "any
  concerns?" ([`../patterns/user-story.md`](../patterns/user-story.md)).
- Omit: the story is smaller and entirely sourced. Usually the right answer.
- Do not use Open Questions to dodge a story-quality problem you could resolve from the context you
  already have ([`../practices/review-an-existing-story.md`](../practices/review-an-existing-story.md)).
- Add questions when confidence is medium or low, or when an assumption signals uncertainty.

**Breaks when.** Unsourced behaviour is written into Expected Output or the criteria →
[`../anti-patterns/pattern-matched-scope.md`](../anti-patterns/pattern-matched-scope.md).
