# Ids are immutable

**Rule.** An id, once issued, belongs to that note forever: never reused, never renumbered, never
deleted. A new rule takes the next free number for its topic. Gaps in the numbering are normal and
stay. The id lives in frontmatter, with an alias so `[[order-address-frozen-on-confirmation|ORDER-1]]` resolves — which is what frees the
**title and filename** to be reworded whenever a better wording is found.

**Why.** The id is the whole value of the base to everything downstream — a story's source grounding,
an acceptance criterion, a test name, a pull request, a tracker tag, another rule's cross-link.
Renumbering silently re-points every one of those at a different rule, and nothing fails: the test
still passes, against the wrong rule. The immutability is also what lets the base be refined
aggressively. A rule's text can be rewritten freely, because the id is what was cited, not the
wording.

**In the base.**
- `PREFIX-N` per topic, one unique prefix per topic, declared in the config. The topic is a property,
  so moving a rule between topics never changes its id
  ([`../patterns/business-rule-note.md`](../patterns/business-rule-note.md)).
- **Rename a title freely; never touch an `id`.** Obsidian rewrites every wikilink to a renamed
  note, including the filename half of `[[order-address-frozen-on-confirmation|ORDER-1]]`, so the
  citation survives the rewording and still reads as `ORDER-1`
  ([`../patterns/note-frontmatter.md`](../patterns/note-frontmatter.md)).
- Refine a rule in place. Split it when it has grown two ideas — the original keeps its id and one
  idea, the second takes a new number
  ([`../practices/write-a-business-rule.md`](../practices/write-a-business-rule.md)).
- `ADR-NNNN` is sequential and never renumbered; reversal is supersession, not an overwrite
  ([`../patterns/decision-record.md`](../patterns/decision-record.md)).
- **A note is never deleted**, because deleting it dangles every wikilink that cited it
  ([`deprecate-never-delete.md`](deprecate-never-delete.md)).
- Every id cited anywhere resolves to a real note. That is what the audit checks
  ([`../practices/audit-the-base.md`](../practices/audit-the-base.md)).

**Breaks when.** Numbering is tidied after a removal →
[`../anti-patterns/renumbered-rule-ids.md`](../anti-patterns/renumbered-rule-ids.md).
