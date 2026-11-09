# Links are the structure

**Rule.** Every reference between notes is a wikilink: `[[ORDER-1]]` by id, `[[ORDER-1|the address
freeze]]` when the sentence needs words, `![[ORDER-1]]` to embed. Never a relative path, never a
copied sentence, never a bare id in prose. A link that resolves to nothing is a finding. Every note
has at least one inbound link and is reachable from the home note.

**Why.** In a graph of small notes the links are the only structure there is — there is no document
order to carry meaning, so an unlinked note is unreachable knowledge and a dangling link is a
citation to nothing. Wikilinks also buy the thing that makes the vault worth the conversion:
**backlinks are free and always current.** A source note does not list the rules it updated; the
rules link to it, and its backlinks pane is that list. A rule does not track what cites it; the
graph does. Every list a person would otherwise maintain by hand, and let rot, is derived from links
instead.

**In the base.**
- Cite by id; the id is an alias on the note, so `[[ORDER-1]]` resolves however the title is worded
  ([`../patterns/note-frontmatter.md`](../patterns/note-frontmatter.md)).
- Wikilinks in frontmatter are Link objects to Obsidian, so a property link is a graph edge too.
  Quote them: `sources: ["[[order-fulfilment-sow-v3]]"]`.
- Embed with `![[…]]` where a reader needs the other note's words in place. Embedding is not copying
  — it resolves to whatever that note says now
  ([`one-home-per-fact.md`](one-home-per-fact.md)).
- Retired glossary names stay as aliases, so old references keep resolving
  ([`../patterns/glossary-term-note.md`](../patterns/glossary-term-note.md)).
- Drafts in the workbench use plain text, not wikilinks to notes that do not exist yet
  ([`../patterns/intake-entry.md`](../patterns/intake-entry.md)).

**Breaks when.** A citation points at no note →
[`../anti-patterns/a-dangling-citation.md`](../anti-patterns/a-dangling-citation.md). Nothing points
at a note → [`../anti-patterns/an-orphan-note.md`](../anti-patterns/an-orphan-note.md).
