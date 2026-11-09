# A business rule as a story

**Smell.** "US-04 Associate label terms and conditions." "US-07 Configure label eligibility and
constraints." "US-09 Confirm the voiding rules." The story restates rules, groups requirements, or
prepares for a UX story that comes later. Expected Output lists rules rather than deliverables.

**Why it is wrong.** It cannot be demonstrated, so it cannot be accepted or refused, and the feedback
the sprint exists to produce never arrives. It also cannot be finished: there is no observable state
in which "the eligibility rules are associated" is done, so it gets marked complete on someone's
judgement and the behaviour surfaces as missing two sprints later. Rule round-ups are the most common
version, and preparation stories the most seductive.

**Instead.** Pair the rules with a system output. Weak: "Configure label eligibility and
constraints." Better: "Persist and enforce label eligibility settings" — saved settings, eligibility
evaluation, access blocking, admin edit lockout after the cut-off. The rules still appear, in `Details`
and the criteria, where they belong. If no buildable output can be named from the source, the story
should not exist yet
([`../principles/a-story-produces-something-buildable.md`](../principles/a-story-produces-something-buildable.md),
[`../patterns/expected-output.md`](../patterns/expected-output.md)).
