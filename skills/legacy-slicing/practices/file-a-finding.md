# File a finding

**When** something died, hurt or surprised you: a check disagreed, an estimate was wrong by a
multiple, a landmine turned up, a slice was too big to be wrong cheaply. Also once at every flip.

**Why.** "Cheap enough to be wrong" is a slogan until every kind of wrongness has somewhere to go. A
loop with no destinations is a meeting; what makes it a loop is that each finding changes a named
thing and nothing else. The routing below is the whole mechanism, and the reason it is written down
is that the tempting response to most findings — quietly fix the brief — is the one that destroys the
evidence.

**Steps.**

1. **Name what was learned in one sentence**, with the evidence that established it. A finding
   without evidence is an opinion with a date on it.
2. **Route it, to exactly one destination:**

       the survey misread the old system   regenerate the entry; the brief is untouched,
                                           because no decision was wrong
       the old behaviour is itself a bug    an amendment on the live brief, dated and signed
       a behaviour nobody surveyed exists   a new survey entry, then a new slice; the current
                                           slice still ships
       appetite wrong by more than 2x       a finding only; it changes how the next slice is
                                           sized, never this one's scope
       the slice was too big to be wrong    a finding, then a new line on the blast-radius list
       the same ruling recurs three times   a decision record; the only way a document here
                                           earns permanence
       something dropped turns out needed   a new slice, never a retro-edit of a shipped brief

3. **Never smooth the record.** An amendment is appended with a date and a decider; the version that
   was wrong stays visible
   ([`../principles/a-frozen-brief-is-appended-never-rewritten.md`](../principles/a-frozen-brief-is-appended-never-rewritten.md)).
4. **Create no new obligations.** A finding records what happened. It does not open work, assign
   anyone, or change a frozen scope — if it needs work, that is a slice and it gets shaped.
5. **Downgrade the tag where provenance was wrong.** A `[code:]` line that turns out to have been
   inferred becomes `[assumed:]`, and that correction is itself the finding
   ([`../patterns/provenance-tag.md`](../patterns/provenance-tag.md)).
6. **Watch for the second amendment.** Two on one slice means the premises were wrong enough that
   reshaping beats patching.

**Done when** the finding names its evidence, has exactly one destination, created no new
obligations, and left the record it came from unsmoothed.
