# Links are the structure

**Rule.** Every reference between notes is a wikilink, and **its target is always a filename**:
`[[order-address-frozen-on-confirmation|ORDER-1]]` to cite by id,
`[[order-address-frozen-on-confirmation|the address freeze]]` when the sentence needs words,
`![[order-address-frozen-on-confirmation]]` to embed. Never a relative path, never a copied
sentence, and never a bare `[[ORDER-1]]`, which resolves to nothing
([`a-link-targets-a-filename.md`](a-link-targets-a-filename.md)). A link that resolves to nothing is
a finding. Every note has at least one inbound link and is reachable from the home note.

**Why.** In a graph of small notes the links are the only structure there is — there is no document
order to carry meaning, so an unlinked note is unreachable knowledge and a dangling link is a
citation to nothing. Wikilinks also buy the thing that makes the vault worth the conversion:
**backlinks are free and always current.** A source note does not list the rules it updated; the
rules link to it, and its backlinks pane is that list. A rule does not track what cites it; the
graph does. Every list a person would otherwise maintain by hand, and let rot, is derived from links
instead.

**In the base.**
- Cite by id in the display text and by filename in the target. Obsidian rewrites the target when
  the note is retitled, so the citation survives every rewording
  ([`a-link-targets-a-filename.md`](a-link-targets-a-filename.md),
  [`../patterns/note-frontmatter.md`](../patterns/note-frontmatter.md)).
- Wikilinks in frontmatter are Link objects to Obsidian, so a property link is a graph edge too.
  Quote them: `sources: ["[[order-fulfilment-sow-v3]]"]`.
- Embed with `![[…]]` where a reader needs the other note's words in place. Embedding is not copying
  — it resolves to whatever that note says now
  ([`one-home-per-fact.md`](one-home-per-fact.md)).
- Retired glossary names stay as aliases, so the old word still finds the note in search. It does
  not make a link to the old name resolve — renaming the file is what repairs existing links
  ([`../patterns/glossary-term-note.md`](../patterns/glossary-term-note.md)).
- Drafts in the workbench use plain text, not wikilinks to notes that do not exist yet
  ([`../patterns/intake-entry.md`](../patterns/intake-entry.md)).

**Breaks when.** A citation points at no note →
[`../anti-patterns/a-dangling-citation.md`](../anti-patterns/a-dangling-citation.md). Nothing points
at a note → [`../anti-patterns/an-orphan-note.md`](../anti-patterns/an-orphan-note.md).
