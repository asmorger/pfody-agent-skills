# Hand-writing the index

**Smell.** The notes written directly, because there were only three transcripts and the rules were
obvious. Or the briefs skipped and the transcripts read straight. Or a missing statement typed into
the MOC's generated table after the fact.

**Why it is wrong.** Every guarantee the output carries comes from the steps that were skipped. The
hashes are what make the next run incremental; the parsers handle three different Copilot layouts and
malformed input without guessing; the merge refuses an item with no provenance and reports what it
dropped; the render escapes pipes in the table, keeps ids stable, and writes the wikilinks that make
the graph work. A hand-made note has none of that and looks exactly the same, so nobody downstream
can tell which kind they are holding — and the next incremental run has no state to build on, so it
reprocesses everything and duplicates what was typed in. A hand-typed MOC row is worse: it names an
id with no note behind it, which is a dangling citation the moment anybody follows it.

**Instead.** Run the four steps, even for three transcripts. The deterministic ones are idempotent, so
a mistake is fixed by re-running rather than by editing output: wrong wording means fixing the
extraction and merging again, not touching a note
([`editing-a-generated-note.md`](editing-a-generated-note.md)
([`../principles/the-tool-does-the-mechanics.md`](../principles/the-tool-does-the-mechanics.md),
[`../practices/merge-the-items.md`](../practices/merge-the-items.md)).
