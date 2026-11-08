# Audit the base

**When** asked to health-check a base, after adopting one, or at a handoff. Standing operating
procedure F. The output is a punch list, not a set of edits.

**Why.** The failures that matter are the ones a reader cannot see: a rule nobody anchored, an id
cited from a story that no longer resolves, two files answering the same question. Each is cheap to
fix and silent until something is built on it.

**Steps.** Work the checklist and report each gap as a finding with the item and the action.

1. **Config and locations.** A config exists recording `knowledge_root`, `docs_dir`, the file map, the
   scope baseline and the id conventions. The working area is gitignored or outside the repository.
   Approved knowledge is promoted rather than drafted in place.
2. **Anchoring.** Every durable statement is anchored or marked `Draft`/`Needs Review`. Every marker
   carries a date. Every Source Register row names the rule ids it updated.
3. **Separation.** Rules, decisions and open questions live in separate homes. Possible added scope is
   separate from confirmed in-scope knowledge. No fact has two homes.
4. **Ids.** Immutable, gap-tolerant, never reused. Deprecated rules deprecated in place. Every
   `(see PREFIX-N)` and every `ADR-NNNN` resolves to a real entry. Every ADR has an index row.
5. **Format.** `business-rules.md` uses `## N. Topic` sections and two-column `| ID | Rule |` tables,
   one unique prefix per section, no Status or Anchors column
   ([`../patterns/business-rules-file.md`](../patterns/business-rules-file.md)).
6. **Change control.** Shifts captured as dated `CH-NNNN`; affected entries carry History notes;
   superseded understanding preserved with anchors.
7. **Authority.** Explicit on every source. Conflicts recorded, not hidden. Note honestly when the
   rule set rests mainly on levels 5 and 6.
8. **Vocabulary.** The glossary is current; aliases and retired terms reconciled; no term used two
   ways.
9. **Delegation.** Transcript ingestion goes through `transcript-knowledge-base`, not re-implemented.
   The transcript index is supplemental and not cited.
10. **Sufficiency.** The Reference Layer alone is enough for a developer or spec author to act without
    reading a raw source. Review cadence and ownership are defined.

**Done when** every line above has a verdict, each gap is a finding naming the item and the action,
and you have said plainly whether the output is an audit, a template set or an applied migration.
