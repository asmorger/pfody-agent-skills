# Render a readable PRD

**When** the PRD has to be read somewhere that is not Obsidian: a GitHub review, a pull-request
diff, a pasted brief, an agent reading the raw file. Also before sharing it with anybody who does
not have the vault.

**Why.** The hub is the right shape *inside* Obsidian, where `![[address-error-rate-on-parcels]]`
resolves to the whole metric and cannot go stale. Outside Obsidian that line renders as nothing —
so the cold-read property the hub was designed for is exactly what a non-Obsidian reader loses, and
the PRD arrives full of holes where its requirements should be.

The wrong fix is to summarise the notes back into the hub by hand: that is the never-copy rule broken
in the document everybody reads
([`../anti-patterns/a-hub-that-summarises-its-notes.md`](../anti-patterns/a-hub-that-summarises-its-notes.md)).
The right fix is to **derive** the readable version and never retype it.

**Steps.**

1. Render it:

       python3 scripts/prd.py render <vault> --out <path>.md [--prd PRD-001]

   Embeds are resolved from the notes in place, their headings demoted a level, and wikilinks
   flattened to their display text — so `[[create-a-label-on-order-confirmation|R-001]]` reads as
   `R-001`, which is still traceable back to its note.

2. **Put the output where generated things go**, not in the vault beside the notes. It is a
   rendition, not a record: the notes are the record, and two editable copies of one PRD is the
   failure the never-copy rule exists to prevent.

3. **Never edit it.** Every change goes into the note that holds the thing being changed, and you
   re-render. The banner at the top of the file says so.

4. Before relying on one somebody else rendered:

       python3 scripts/prd.py render <vault> --out <path>.md --check

   Exit 1 means the notes have moved since it was written. It fails on a stale rendition rather than
   silently rewriting it, so a stale document in a review is visible
   ([`../principles/the-check-is-not-a-reviewer.md`](../principles/the-check-is-not-a-reviewer.md)).

**Done when** `prd.py check` is clean, the rendition was produced by the script rather than by hand,
`render --check` exits 0, and the document lives outside the vault. Say in your report that the
readable copy is derived and name the file.
