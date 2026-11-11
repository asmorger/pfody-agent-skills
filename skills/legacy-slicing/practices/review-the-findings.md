# Review the findings

**When** a survey is `surveyed` and rulings are needed before a slice can be shaped. Thirty minutes
with a person, not an interview and not a workshop.

**Why.** Nobody can fill a blank page, and asking a product owner to describe a system they have
never read produces invented requirements with a confident tone. Everybody can tell you that item
four is wrong, that nobody has used the batch export since 2019, and that the discount rule applies
to one customer who is leaving. Marking up a concrete list is a different and far more accurate task
than authoring one, and it is the task this skill exists to hand them.

**Steps.**

1. **Send only the business list.** A specialist's question in a product owner's markup session is
   what turns thirty minutes back into six weeks
   ([`../patterns/survey-note.md`](../patterns/survey-note.md)).
2. **Bring the counts.** Every question that has a usage number carries it. "This has never fired in
   24 months" converts a risk assessment into a thirty-second answer.
3. **Offer choices, not a blank.** Two or three concrete options per question, with the one you
   believe most likely first. They are allowed to reject all of them.
4. **Show the provenance in plain words.** "We read this in the code", "someone told us this", "this
   is a guess" — so they spend their attention on the weak lines rather than evenly.
5. **Record each answer as a ruling with a name and a date**, in the brief, never back in the survey
   ([`../anti-patterns/a-survey-edited-to-record-a-ruling.md`](../anti-patterns/a-survey-edited-to-record-a-ruling.md)).
6. **Take `DEFER` as a real answer** when it comes with a reason. Push back when it comes without
   one, or when it is the answer to everything
   ([`../principles/decisions-outstanding-must-read-zero.md`](../principles/decisions-outstanding-must-read-zero.md)).
7. **Route what they cannot answer.** A question that needed a specialist gets moved to that list
   with a name against it, and the slice is shaped around it rather than waiting.
8. **Set `status: reviewed`.**

**Done when** every business question has a ruling, a deferral with a reason, or a named specialist
against it; every ruling has a decider and a date; the survey itself is unedited apart from its
`status`; and nothing is waiting on a person who was never asked.
