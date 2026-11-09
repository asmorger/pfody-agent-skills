# Requirement with two behaviours

**Smell.** One id, one "and". "The system shall create the label and email the customer a tracking
link." "When an order is confirmed the system shall print a label and reserve the stock." Often the
second behaviour is the bigger one.

**Why it is wrong.** Everything downstream counts requirements: a criterion cites one, a coverage row
tracks one, a test is named for one, a change regenerates the stories carrying one. Two behaviours
under one id break all four — the criterion tests half, the coverage row is half `Covered`, and a
change to the email forces a rewrite of the labelling story. The half nobody wrote a criterion for is
the half that does not get built, and the generated coverage table still reads complete.

**Instead.** Split into one id per behaviour and let each take its own priority, source and verify
method; they are usually different. Where the two are genuinely one behaviour with a compound
outcome, say it as one observable result rather than two verbs
([`../principles/one-behaviour-per-requirement.md`](../principles/one-behaviour-per-requirement.md)).
