# Every line carries its provenance

**Rule.** Every observed behaviour in a survey carries a tag naming where it came from: `[code:]`
with a file and line, `[db:]` with the object, `[logs:]` with the measurement, `[told:]` with who
said it and when, `[assumed:]` where it is a guess. A line with no tag is not an observation and does
not belong in the file.

**Why.** This is the one rule that makes a wide document safe to hand to anybody, model or person. An
unsourced assumption on page thirty reads exactly like a verified fact, and whoever reads next will
implement both with the same confidence. The tag is what lets a reader spend their scepticism where
it is warranted instead of spreading it evenly and trusting nothing.

It also changes what a review is for. Without tags, reviewing a survey means re-deriving all of it.
With tags, the reader goes straight to the `[told:]` and `[assumed:]` lines, which is where the
errors actually are, and leaves the `[code:]` lines alone.

**In the slice.**
- Write the weakest tag that is honest. A behaviour you inferred from two sources is `[assumed:]`,
  and its sentence says "suspected", not "does"
  ([`../patterns/provenance-tag.md`](../patterns/provenance-tag.md)).
- `[logs:]` is the tag that deletes scope. A behaviour that has not fired in two years is a
  candidate for `DROP`, and the count is what makes that a short conversation.
- An absence claim needs its own discipline and its own tag
  ([`absence-needs-an-exhaustive-sweep.md`](absence-needs-an-exhaustive-sweep.md)).
- Never upgrade a tag to make a line look better. Downgrading one is a finding
  ([`../practices/file-a-finding.md`](../practices/file-a-finding.md)).

**Breaks when.** A guess and a verified reading sit in the same list wearing the same clothes, and
the brief rules on both →
[`../anti-patterns/a-survey-edited-to-record-a-ruling.md`](../anti-patterns/a-survey-edited-to-record-a-ruling.md).
