# Curate a large corpus

**When** the corpus runs to dozens of transcripts, or includes standups and status meetings.

**Why.** Both failure modes at this scale are structural: dedup is lexical, so one topic sprawls; and
status sentences are grammatically indistinguishable from rules, so they get extracted. Neither is
fixed by trying harder, and presenting the result as finished transfers confidence it has not earned.

**Steps.**

1. **Say what you are handing over**: a fully-sourced superset to curate, not a finished document
   ([`../principles/a-large-corpus-is-a-superset.md`](../principles/a-large-corpus-is-a-superset.md)).
2. **Prune the status items.** Scan for assignments, progress, flags, dates and sprint talk that
   survived extraction — they come mostly from the standup briefs
   ([`../anti-patterns/status-recorded-as-a-rule.md`](../anti-patterns/status-recorded-as-a-rule.md)).
3. **Find the sprawl.** Read each category's table end to end and look for two or three items that are
   one rule in different words.
4. **Merge them deliberately**: lower `dedup_threshold` and re-merge, or align the statements to the
   best-worded one and re-merge ([`merge-the-items.md`](merge-the-items.md)). Keep the better wording,
   and all the sources.
5. **Mark supersessions the dedup could not see.** A rule overturned in a later meeting rarely matches
   its predecessor lexically ([`../patterns/supersession.md`](../patterns/supersession.md)).
6. **Check the thin citations.** An item with one source from one speaker, in a domain the corpus
   discusses repeatedly, is often a passing remark rather than a rule.
7. **Report the counts before and after**, and name what you pruned and merged. The point is that the
   curation is visible and reversible, since nothing was deleted from the state's evidence.
8. **Consider a dedicated consolidation pass** as a separate run rather than doing it inside
   extraction. The two jobs want different attention.

**Done when** status items are gone, each category reads as a list of distinct rules, supersessions
are marked, and the user knows what was pruned, what was merged and that this was a curation pass.
