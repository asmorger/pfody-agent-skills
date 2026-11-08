# Accepted with PROPOSED left in

**Smell.** `status: Accepted` in the front matter and `PROPOSED` in a Source column. Or an open
question still `Open` against a `P0` requirement in an accepted PRD. Often the acceptance was verbal
and broad — "yes, looks good" — and the agent wrote the status.

**Why it is wrong.** `Accepted` is what unlocks the irreversible steps: decomposition, tracker items,
work starting. A `PROPOSED` requirement inside an accepted PRD is an unsourced behaviour that now has
a story, a criterion, a test and an assignee, and the fact that nobody sourced it has been erased by
the status line. The approver, meanwhile, approved a document whose gaps they were never shown as
gaps.

**Instead.** Before asking for acceptance, list every `PROPOSED` requirement and every question
blocking a `P0`, and ask about each one. Then let the person set the status in words. If they accept
with known gaps, that is their call — record it as an `A-xx` assumption with the approver named, so
it is visible rather than erased
([`../principles/only-a-person-crosses-a-gate.md`](../principles/only-a-person-crosses-a-gate.md),
[`../principles/every-requirement-cites-a-source.md`](../principles/every-requirement-cites-a-source.md)).
