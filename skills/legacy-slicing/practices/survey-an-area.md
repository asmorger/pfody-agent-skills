# Survey an area

**When** the next slice is about to be shaped and nobody can describe what the old system does
there. One area, one slice ahead — never the whole application.

**Why.** Most of what gets called a requirements gap is not one. It is archaeology, and it does not
need a person's memory or a decision: the behaviour is recorded in the code, the schema and the logs,
and it can be read out. Separating that from the genuinely open questions is what shrinks the list a
person has to rule on from a specification to about a dozen rows.

**Steps.**

1. **Find the entry points first.** The screen or form, the service class behind it, the stored
   procedures and triggers it reaches. Record them in `entry:` so the note can be reproduced.
2. **Read the behaviour out, one line per behaviour**, each with its provenance tag and a stable id
   ([`../patterns/provenance-tag.md`](../patterns/provenance-tag.md)). Write the weakest honest tag;
   a confident sentence over a guess is the defect that ships.
3. **Sweep exhaustively for anything you intend to call dead.** Client code, reports, stored
   procedures, scheduled jobs and integration configuration are five corpora, and a ranked search
   over one of them cannot support an absence claim
   ([`../principles/absence-needs-an-exhaustive-sweep.md`](../principles/absence-needs-an-exhaustive-sweep.md)).
4. **Get counts from production.** How often each behaviour fires, over what window, against what
   denominator. This is the cheapest scope-deletion tool available and it costs one query.
5. **Look for the three landmines** every legacy area hides: accounts or jobs that authenticate as a
   user, identifiers referenced as foreign keys across many tables, and credentials or names embedded
   in printed output. Each one constrains later slices and none of them is visible from the screens.
6. **Split what is left into three question lists** — for the business, for a named specialist, and
   still ours to verify. The third list is work you owe, not a blocker on anyone else
   ([`../patterns/survey-note.md`](../patterns/survey-note.md)).
7. **Leave `status: surveyed`.** It becomes `reviewed` only after a person has marked it up.

**Done when** every behaviour line carries a tag, every absence claim names the corpora swept, the
usage block has counts with denominators, the questions are split by who can answer them, nothing in
the file records a decision, and `status` is `surveyed`.
