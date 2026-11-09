# The tool does the mechanics; you do the synthesis

**Rule.** Never hand-write the index, and never hand-write any part the tool produces. Run `prepare`,
`merge` and `render`. Your work is the middle step: reading briefs and writing clean statements.

**Why.** The deterministic steps are exactly the steps that make the output trustworthy. The content
hashes are what make a re-run incremental; the parsers handle three different Copilot layouts and
malformed input without guessing; the merge enforces that no item exists without provenance and
reports what it dropped; the render escapes the markdown. A hand-built index has none of those
guarantees and looks identical, so nobody can tell which one they are reading. The division also
plays to what each side is good at — a parser cannot judge whether a sentence is a durable rule, and
a model cannot reliably compute a hash over forty files.

**In the index.**
- Four steps, in order, every time: prepare → extract → merge → render
  ([`../practices/prepare-the-briefs.md`](../practices/prepare-the-briefs.md)).
- `prepare` is both the initial and the incremental run. There is no separate first-time path
  ([`../practices/run-an-incremental-update.md`](../practices/run-an-incremental-update.md)).
- The deterministic steps are idempotent. Re-running them cannot corrupt the index, so re-run rather
  than patching output.
- Your output is one file, `items.json`, in the documented shape
  ([`../patterns/items-json.md`](../patterns/items-json.md)). Nothing else you write enters the index.

**Breaks when.** The index is written directly because it was only a few rules →
[`../anti-patterns/hand-writing-the-index.md`](../anti-patterns/hand-writing-the-index.md).
