# A link targets a filename

**Rule.** A wikilink's target is a **filename or a path** — never an id, and never an alias. Cite as
`[[order-address-frozen-on-confirmation|ORDER-1]]`: filename as the target, id as the display text.
Inside a table cell the pipe is escaped, `[[one-label-per-parcel\|LABEL-1]]`. A bare `[[ORDER-1]]`
is a dangling link. Filenames are therefore vault-unique, and display text shaped like an id must
be the id of the note the link opens.

**Why.** Obsidian resolves a wikilink by matching the target against file names and paths. An
`aliases` entry powers autocomplete and search and **takes no part in resolution**, so `[[ORDER-1]]`
does not open the rule — it offers to create a new empty note of that name. Watch Obsidian's own
autocomplete: pick a note by its alias and it inserts
`[[order-address-frozen-on-confirmation|ORDER-1]]`, the target spelled out and the alias left as
display text. That is this convention, and the editor writes it for you.

The cost of getting this wrong is specific and total. Citation by id is the whole mechanism by which
a story, a spec or a test reaches the record, so a vault that cites bare ids has no working
citations at all — several hundred of them — while every note looks correct, the graph looks
plausible because frontmatter links resolve by filename, and nobody notices until someone clicks one
and is offered an empty note. **A linter that accepts the alias cannot distinguish the two cases**,
which is how the mistake survives being checked.

**In the base.**
- `lint` resolves links exactly as Obsidian does, and reports a bare id with the form to use instead
  ([`../references/vault-convention.md`](../references/vault-convention.md) §6).
- It also checks `#heading` and `#^block` against the target's real headings and block ids, and
  compares id-shaped display text with the target's `id`. `[[one-label-per-order|LABEL-9]]` opens
  the right note under the wrong name: the link works, so only a checker sees it.
- Two notes may not share a basename. Obsidian would pick between them by proximity — the same link
  text resolving differently depending on where it is written — and under this rule one of the two
  becomes uncitable.
- The generators emit this form too. A MOC that wrote `[[ORDER-1]]` once per row would plant the one
  link form Obsidian cannot follow, at scale, and call it an index
  ([`../patterns/moc-note.md`](../patterns/moc-note.md)).
- Keep the id in `aliases` regardless: searching `ORDER-1` should find the note, and autocomplete
  should offer it ([`../patterns/note-frontmatter.md`](../patterns/note-frontmatter.md)).

**Breaks when.** A citation points at no note →
[`../anti-patterns/a-dangling-citation.md`](../anti-patterns/a-dangling-citation.md). A title is
reworded and someone "fixes" the id instead →
[`../anti-patterns/renumbered-rule-ids.md`](../anti-patterns/renumbered-rule-ids.md).
