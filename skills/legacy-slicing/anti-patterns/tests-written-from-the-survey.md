# Tests written from the survey

**Smell.** The characterisation suite was produced quickly and cleanly, every test passes first run,
and no test ever disagreed with anybody's expectation. Asked where a `char/` test came from, the
answer is the survey — "B01 says a label is only created for a confirmed order, so that is what the
test asserts." Nobody drove the old system to get it.

**Why it is wrong.** This is the quietest fatal defect in the practice, because its symptom is
everything working. A survey line is a *reading*, and a reading can be wrong. A test written from
that reading inherits the error, passes forever, and converts one person's misunderstanding into an
automated guarantee that the new system reproduces it. The whole value of a golden master is that it
was recorded from the thing itself and can therefore contradict you — a suite derived from the
written record cannot contradict anything, because it only ever agreed with itself.

The failure surfaces, if it ever does, long after the flip: the new system matches the tests, the
tests match the survey, and production matches neither. By then the legacy path has usually been
removed, so the evidence that would settle it is gone.

**Instead.** Derive every `char/` check by exercising the legacy system — its binary, its domain
layer, its stored procedures — and record what it actually returns, including behaviour nobody
described and behaviour that looks wrong. Say in the brief which surface was driven. A test that
disagrees with the survey on its first run is the practice working: regenerate the survey entry and
file a finding
([`../principles/the-oracle-outranks-the-survey.md`](../principles/the-oracle-outranks-the-survey.md),
[`../patterns/check-set.md`](../patterns/check-set.md)).
