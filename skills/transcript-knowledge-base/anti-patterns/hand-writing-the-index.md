# Hand-writing the index

**Smell.** `knowledge-index.md` written directly, because there were only three transcripts and the
rules were obvious. Or the briefs skipped and the transcripts read straight. Or a missing item typed
into the rendered table after the fact.

**Why it is wrong.** Every guarantee the output carries comes from the steps that were skipped. The
hashes are what make the next run incremental; the parsers handle three different Copilot layouts and
malformed input without guessing; the merge refuses an item with no provenance and reports what it
dropped; the render escapes markdown in the statements. A hand-made file has none of that and looks
exactly the same, so nobody downstream can tell which kind they are holding — and the next incremental
run has no state to build on, so it reprocesses everything and duplicates what was typed in.

**Instead.** Run the four steps, even for three transcripts. The deterministic ones are idempotent, so
a mistake is fixed by re-running rather than by editing output: wrong wording means fixing the
extraction and merging again, not touching the index
([`../principles/the-tool-does-the-mechanics.md`](../principles/the-tool-does-the-mechanics.md),
[`../practices/merge-the-items.md`](../practices/merge-the-items.md)).
