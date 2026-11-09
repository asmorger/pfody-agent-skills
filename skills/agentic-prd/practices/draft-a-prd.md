# Draft a PRD

**When** a person wants a PRD, product brief or functional spec written from sources — a SOW,
transcripts, emails, notes — or from a conversation. Mode `DRAFT`.

**Why.** The draft is where every later cost is set. A requirement written without its locator will
not get one afterwards, and a gap papered over here reaches a build as a confident guess.

**Steps.**

1. **Ask only for what you cannot find**: the sources, the owner, and where the file goes. Default
   `docs/prd/PRD-NNN-<slug>.md`.
2. **Obey any limit on sources.** State the limit at the top of the PRD and report what you did not
   read. An excluded file is exactly where a settling decision tends to live, so the person must know
   it was excluded.
3. **Read every allowed source, whole.** Use
   [`read-a-binary-source.md`](read-a-binary-source.md) for `.docx`, `.pdf`, `.vtt` and `.srt`. Read
   long transcripts completely — a later meeting reversing an earlier one is the normal case. Build
   the decision list from the newest source backwards.
4. **Choose the size** ([`choose-the-prd-size.md`](choose-the-prd-size.md)): the smallest that
   removes guesswork.
5. **Copy [`../assets/prd-template.md`](../assets/prd-template.md) and fill it.** Group the work into
   Epics and Features and list them in the work item map
   ([`../patterns/prd-hub-note.md`](../patterns/prd-hub-note.md)). Delete the guidance blocks. Keep
   the agent protocol section.
6. **Cite every requirement with a locator**, compared against the source as you write it
   ([`cite-a-source.md`](cite-a-source.md)).
7. **Answer every coverage line** — ids, `N/A` with a reason, or `Gap: Q-xx`
   ([`../patterns/coverage-check.md`](../patterns/coverage-check.md)).
8. **Record each inference as an inference**: a priority nobody assigned, a behaviour only implied, a
   metric field nobody gave you
   ([`../principles/implied-is-not-stated.md`](../principles/implied-is-not-stated.md)).
9. **Run the checks** ([`run-the-checks.md`](run-the-checks.md)), report
   ([`report-the-result.md`](report-the-result.md)), then offer `REVIEW`.

**Done when** every requirement carries a source or is visibly `PROPOSED`, every unknown is a
question with an owner and a date, no coverage line is blank, the check passes, and the person knows
which decisions are theirs and what you were not able to read.
