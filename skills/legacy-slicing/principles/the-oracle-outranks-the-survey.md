# The oracle outranks the survey

**Rule.** The running legacy system is the specification. Where it and a note about it disagree, the
system is right and the note is a defect to regenerate. Characterisation tests are produced by
driving the old system — its binary, its domain layer, its stored procedures — and never by reading
the survey and writing tests from what it says.

**Why.** A survey is a reading, and a reading can be wrong in ways nobody can see. A test derived by
exercising the system records behaviour that can be re-checked on demand, so a misreading surfaces
the first time the test runs. A test written from the survey instead inherits the misreading, passes
forever, and converts a human error into an automated one. That is the difference between a record
you can trust and a record that merely agrees with itself.

It is also what replaces the on-site customer the old practices assumed. Nobody remembers what the
screen does, but the screen will answer any question that can be phrased as an input, every time,
without a meeting.

**In the slice.**
- Derive every `char/` check by exercising the legacy system, and say in the brief which surface you
  drove ([`../patterns/check-set.md`](../patterns/check-set.md)).
- Record the golden master for the whole population, not only the part the slice touches. It costs
  nothing extra and it protects everything the slice could break.
- A behaviour you cannot reach from outside the system is not yet observed. Tag it `[assumed:]` and
  leave it ([`every-line-carries-its-provenance.md`](every-line-carries-its-provenance.md)).
- When a check disagrees with the new code, the first question is which of the two is wrong. Often
  it is the survey, and the answer is to regenerate the entry rather than to argue
  ([`a-survey-is-derived-and-disposable.md`](a-survey-is-derived-and-disposable.md)).

**Breaks when.** The suite is built from the written record instead of the running one →
[`../anti-patterns/tests-written-from-the-survey.md`](../anti-patterns/tests-written-from-the-survey.md).
