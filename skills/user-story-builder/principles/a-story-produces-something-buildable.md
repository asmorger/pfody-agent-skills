# A story produces something buildable

**Rule.** Every story describes a concrete implementable output a developer can build, test and demo.
A valid story produces at least one of: a user-visible workflow, persisted data or configuration,
validation or enforcement behaviour, permission or eligibility behaviour, integration or API
behaviour, or reporting or audit output. Business rules belong in `Details` and the criteria — a rule
alone is not a story.

**Why.** A story that documents a rule cannot be demonstrated, so it cannot be accepted or refused,
and the feedback the sprint exists to produce never arrives. It also cannot be finished: there is no
state in which "the eligibility rules are associated" is observably done. The buildable-output test is
what converts a list of agreed rules into work, and it is the test that catches the two most common
non-stories — the rule round-up and the preparation story for a future one.

**In the story.**
- Reject a story whose primary output is documenting a rule, confirming scope, preparing for a later
  UX story, describing policy without system behaviour, or grouping requirements with no deliverable.
- Weak: "Configure label eligibility and constraints." Better: "Persist and enforce label eligibility
  settings" — saved settings, evaluation, blocking, admin lockout after cut-off.
- Self-check: could a developer implement **what is sourced** without asking for more? A missing piece
  is an Open Question, never an inferred requirement.
- Each Expected Output bullet names one sourced deliverable
  ([`../patterns/expected-output.md`](../patterns/expected-output.md)).
- One person, one sprint, build-test-demo. Larger means slicing
  ([`../practices/slice-a-feature-into-stories.md`](../practices/slice-a-feature-into-stories.md)).

**Breaks when.** The story only restates rules →
[`../anti-patterns/a-business-rule-as-a-story.md`](../anti-patterns/a-business-rule-as-a-story.md).
