# Properties are the query surface

**Rule.** Frontmatter carries the state: `type`, `status`, dates, authority, owner, and the links to
related notes. Bases views, the MOC snapshots and the audit all read properties and nothing else. The
prose never restates a property, and no index table is authoritative.

**Why.** Every table a person maintains by hand drifts, and the drift is silent — the table says
`confirmed` for a rule that went back to draft last week, and the reader who believes the table has
no signal that the note disagrees. Derive the table from properties and that failure stops existing:
there is one place to change a status, and everything that displays it is a view. This is also what
makes the record answerable. "What is pending and overdue", "what rests only on internal
interpretation", "what did this meeting change" are queries over properties; in prose they are
reading jobs nobody does.

**In the base.**
- Closed vocabularies for `type`, `status` and `authority`. A value outside them is a finding, not a
  local improvement ([`../references/vault-convention.md`](../references/vault-convention.md) §5).
- A list property is a list even with one entry, and `[]` when empty. A filter on a scalar that is
  sometimes a list matches nothing, quietly.
- `tags` duplicates `type` and `topic` and is the only sanctioned duplication; the properties win and
  the tag is derived from them. **Status is never a tag**
  ([`../anti-patterns/status-in-two-places.md`](../anti-patterns/status-in-two-places.md)).
- A callout says what a property cannot — what would close a draft, what a supersession replaced —
  and never repeats the property itself
  ([`../patterns/status-callouts.md`](../patterns/status-callouts.md)).
- A generated table is refreshed from the notes, never edited
  ([`../practices/regenerate-the-mocs.md`](../practices/regenerate-the-mocs.md)).

**Breaks when.** An index table is corrected instead of the note →
[`../anti-patterns/a-generated-table-edited-by-hand.md`](../anti-patterns/a-generated-table-edited-by-hand.md).
