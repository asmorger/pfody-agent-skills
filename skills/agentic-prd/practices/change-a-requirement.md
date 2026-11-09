# Change a requirement

**When** behaviour changes in a PRD that already has a backlog. Mode `CHANGE`.

**Why.** A change applied to the backlog first turns the PRD into a stale summary of the work, and
the trail from behaviour back to the source that asked for it is the only thing the document was
for.

**Steps.**

1. **Change the PRD first.** Add the new source or the decision that caused the change, then raise
   the version ([`../principles/the-prd-changes-before-the-backlog.md`](../principles/the-prd-changes-before-the-backlog.md)).
2. **Keep every id.** `EPIC`, `FEAT`, `US` and `R` ids all stay. A requirement that is going away is
   marked `Retired` in its Requirement column and keeps its number
   ([`../principles/ids-are-never-reused.md`](../principles/ids-are-never-reused.md)).
3. **List the blast radius** before touching anything downstream: the Epics, Features, stories and
   tests the change reaches.
4. **Regenerate only the affected stories**, and show the diff of each one. A story the change does
   not reach is not rewritten, even if you would write it differently today.
5. **Run `prd.py check`** ([`run-the-checks.md`](run-the-checks.md)).
6. **Leave the tracker alone** until the person asks. Criteria already published change only after
   the PRD has, and only through `PUBLISH`
   ([`publish-a-backlog.md`](publish-a-backlog.md)).

**Done when** the PRD states the new behaviour with its source, the version is raised, every id is
intact, each affected story shows its diff, unaffected stories are byte-identical, and the check
passes.
