# Shape a slice

**When** a survey is `reviewed` and rulings exist. Produces one brief, frozen, with a zero count.

**Why.** A slice is the unit of being wrong cheaply. Getting it wrong in the other direction — too
big, or irreversible — is what turns a two-week rhythm into a six-month rewrite with no feedback in
the middle. Most of the work here is subtraction: finding the version of the slice that leaves the
hardest question untouched.

**Steps.**

1. **Write the demo sentence first**, in the user's words, present tense. If it needs a conjunction,
   you have two slices. If you cannot write it, you do not have a slice yet.
2. **Write the blast radius as negatives** — what the slice does not touch. Additive schema changes
   only, the old path stays hot, no shared-code refactor
   ([`../principles/blast-radius-not-size.md`](../principles/blast-radius-not-size.md)).
3. **Where every workflow depends on the area, slice by population instead.** Sign-in, tenancy and
   audit cannot be sliced by workflow because there is no vertical slice of a bit of authentication.
   There is a perfectly good slice of six people, by explicit allow-list, with the old path live.
4. **Look for the seam.** The deferral device that does the most work is splitting two concerns and
   moving only one, so the open question sits entirely on the side you did not touch — move
   authentication and leave authorisation, move the read path and leave the writes. This is usually
   what takes the count to zero
   ([`../principles/decisions-outstanding-must-read-zero.md`](../principles/decisions-outstanding-must-read-zero.md)).
5. **Write the rulings table** from the review, one row per behaviour id, each with a decider and a
   date. Unanswered questions become `DEFER` rows with a reason
   ([`../patterns/slice-brief.md`](../patterns/slice-brief.md)).
6. **Name what the slice deliberately does not decide**, in its own section. This is the seam written
   down, and it is what stops a later reader thinking the question was missed.
7. **Write the three checks** — golden master, one per `CHANGE`, and a parallel-run threshold with a
   volume ([`../patterns/check-set.md`](../patterns/check-set.md)).
8. **State the appetite in judgment-hours**, with a wall-clock and a cost order of magnitude beside
   it, so the estimate can be compared against what it actually took.
9. **Freeze it.** `status: frozen`, a date, and nothing above that line changes again
   ([`../principles/a-frozen-brief-is-appended-never-rewritten.md`](../principles/a-frozen-brief-is-appended-never-rewritten.md)).

**Done when** the demo sentence has no conjunction, the blast radius is a list of negatives with no
migration in it, every ruling has an id and a decider, every deferral has a reason, the checks name
a threshold and a volume, `Decisions outstanding` reads 0, and the brief is frozen with a date.
