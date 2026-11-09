# Untestable acceptance criteria

**Smell.** "The label should be secure." "Voiding works correctly." "The system handles errors
appropriately." "Performance is acceptable." Or a criterion that restates its rule — "Given LABEL-2,
then LABEL-2 applies" — without naming an observable result.

**Why it is wrong.** QA cannot write a pass or fail test, so the criterion cannot be used for the one
thing criteria are for. In practice it is marked satisfied by whoever implemented it, against their
own reading, which means the story is accepted without the behaviour being checked. The hedging verbs
are the tell: "should" invites an argument about intent, where "is" and "can" invite a test.

**Instead.** Make each criterion specific and measurable, independently testable, about *what* rather
than *how*, falsifiable, and a proof of the expected output rather than a restatement of a rule.
"Password requires a minimum of 8 characters with mixed case", not "password is secure". "The user
receives an email within 5 minutes", not "the system uses SendGrid". Where the threshold is not in a
source, that is an Open Question — never a word standing in for a number
([`../patterns/acceptance-criterion.md`](../patterns/acceptance-criterion.md),
[`../practices/review-an-existing-story.md`](../practices/review-an-existing-story.md)).
