# Audit the base

**When** asked to health-check a base, after adopting one, or at a handoff. Standing operating
procedure F. The output is a punch list, not a set of edits.

**Why.** The failures that matter are the ones a reader cannot see: a rule nobody anchored, an id
cited from a story that no longer resolves, two files answering the same question. Each is cheap to
fix and silent until something is built on it.

**Steps.** Work the checklist and report each gap as a finding with the item and the action.

1. **Config and locations.** A config exists recording `knowledge_root`, `docs_dir`, the folder map,
   the scope baseline and the id conventions. The workbench is **outside the vault** — or inside
   Obsidian's excluded files — and gitignored or outside the repository. Approved knowledge is
   promoted rather than drafted in place.
2. **Anchoring.** Every durable statement has a non-empty `sources`, or `status: draft` /
   `needs-review` with a dated callout naming who it waits on. Every `sources` entry resolves to a
   source note, and every source note carries an `authority`.
3. **Separation.** Rules, decisions and open questions live in separate homes. Possible added scope is
   separate from confirmed in-scope knowledge. No fact has two homes.
4. **Ids.** Immutable, gap-tolerant, never reused, and present in `aliases` so `[[PREFIX-N]]`
   resolves. Deprecated rules deprecated in place, never deleted. Every wikilink resolves to a real
   note.
5. **Vault shape.** Run `python3 scripts/vault.py lint <vault>`: it reports dangling wikilinks,
   orphans, values outside the vocabularies, a confirmed note with no source, oversized notes and
   duplicate ids. Then check what it cannot — whether each note holds one idea, and whether the
   generated snapshots were regenerated after the last promotion
   ([`regenerate-the-mocs.md`](regenerate-the-mocs.md)).
6. **Change control.** Shifts captured as dated `CH-NNNN`; affected entries carry History notes;
   superseded understanding preserved with anchors.
7. **Authority.** Explicit on every source. Conflicts recorded, not hidden. Note honestly when the
   rule set rests mainly on levels 5 and 6.
8. **Vocabulary.** The glossary is current; retired terms survive as `aliases` so old references
   resolve; no term used two ways.
9. **Delegation.** Transcript ingestion goes through `transcript-knowledge-base`, not re-implemented.
   The transcript index is supplemental and not cited.
10. **Sufficiency.** The Reference Layer alone is enough for a developer or spec author to act without
    reading a raw source. Review cadence and ownership are defined.

**Done when** every line above has a verdict, each gap is a finding naming the item and the action,
and you have said plainly whether the output is an audit, a template set or an applied migration.
