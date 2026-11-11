# Flip a slice

**When** the checks pass and the parallel run has met its threshold. Switches one slice on and
retires its paperwork.

**Why.** Going live is a setting, not an event. The reason it can be is that by this point three
things are already true: the old system's behaviour is recorded as tests that pass, the new path has
run on real traffic beside the old one with the differences counted, and the old path is still
serving. The flip is the cheapest step in the whole practice, and the cleanup after it is what stops
the record rotting.

**Steps.**

1. **Check the parallel-run threshold literally.** Zero diffs over the stated volume, not zero diffs
   over however many happened to occur. A clean diff on four transactions proves nothing
   ([`../patterns/check-set.md`](../patterns/check-set.md)).
2. **Confirm the golden master is unchanged.** A `char/` check that was edited during the slice is a
   finding, not a pass — the suite records the old system, and the old system did not change
   ([`../principles/the-oracle-outranks-the-survey.md`](../principles/the-oracle-outranks-the-survey.md)).
3. **Flip the toggle, leaving the old path hot.** Removing it is the next slice, not this one.
4. **Set the brief to `flipped`.** Its rulings are now history; the suite is the live record.
5. **Delete the survey entry.** Not archive — delete. Its content lives in the suite now, and keeping
   a prose copy beside an executable one guarantees they will disagree and nobody will know which to
   believe ([`../principles/a-survey-is-derived-and-disposable.md`](../principles/a-survey-is-derived-and-disposable.md)).
6. **File one finding.** At minimum, appetite against actual. This is the only moment the comparison
   is cheap to make ([`file-a-finding.md`](file-a-finding.md)).
7. **Check the two health signals.** `survey/` should be smaller than last slice and the suite
   larger. If neither moved across several slices, the loop is not running and the practice has
   become paperwork.

**Done when** the threshold was met as written, no `char/` check was weakened, the toggle is on with
the old path still available, the brief reads `flipped`, the survey entry is gone, a finding is
filed, and the two signals have been looked at rather than assumed.
