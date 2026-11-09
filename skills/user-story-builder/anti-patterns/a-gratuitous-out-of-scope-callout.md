# A gratuitous out-of-scope callout

**Smell.** A Technical Notes bullet listing what the story does not do: "no bulk voiding", "no
reporting", "no mobile support", "no integration with the finance system". None of it was ever in
scope. Sometimes a criterion asserting the absence.

**Why it is wrong.** Restating known exclusions is noise, and noise has a cost: the list grows with
every story, so the one exclusion that genuinely resolves an ambiguity is buried among six that do
not. Worse, naming a capability implies it was considered and rejected, which is a scope conversation
nobody had — a client reading "no mobile support" reasonably asks when mobile is coming. An exclusion
is a claim about a decision, and most of these record no decision.

**Instead.** Omit silently, unless one of three things is true: a prior version of this work item
included the capability and the rewrite removes it — state it once in `Details`, plus one criterion if
user-visible behaviour changes; a stakeholder explicitly asked for the exclusion to be visible; or the
exclusion resolves an ambiguity a developer or QA could reasonably read as in scope. Otherwise the
story's silence is the correct statement
([`../patterns/technical-notes.md`](../patterns/technical-notes.md),
[`../practices/review-an-existing-story.md`](../practices/review-an-existing-story.md)).
