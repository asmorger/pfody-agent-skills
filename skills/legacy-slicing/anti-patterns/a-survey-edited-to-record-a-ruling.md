# A survey edited to record a ruling

**Smell.** A behaviour line reads "B03 Negative lines are dropped — **we decided to reject these
instead**", or a tag has quietly become `[code: LabelSvc.cls:112 — confirmed with the ops lead,
keeping as-is]`. The `status` is still `surveyed`. Somewhere in the file, a sentence describes the
future.

**Why it is wrong.** It destroys the one property that made the survey worth writing. Every tag in
the file becomes a claim nobody can check, because a reader can no longer tell which lines were read
out of the running system and which were negotiated into it — and the lines that were negotiated are
exactly the ones that look most authoritative. The file stops being regenerable, too: the next sweep
would wipe the decision, so now it must be hand-merged forever, and a derived note that cannot be
regenerated is just a document with a misleading header.

It also creates a second record of the decision. The brief says `CHANGE`, the survey says "keeping
as-is", both have dates, and in four months nobody will know which won. That is the specific failure
the two-artifact split exists to prevent.

**Instead.** The ruling goes in the brief's keep/change/drop table, citing the survey's behaviour id,
with a decider and a date. The survey's only permitted edit is its `status`, and at the flip the file
is deleted rather than reconciled
([`../principles/a-survey-is-derived-and-disposable.md`](../principles/a-survey-is-derived-and-disposable.md),
[`../patterns/slice-brief.md`](../patterns/slice-brief.md)).

If the survey line is *wrong* rather than undecided, that is a different fix: regenerate the entry
and file a finding ([`../practices/file-a-finding.md`](../practices/file-a-finding.md)).
