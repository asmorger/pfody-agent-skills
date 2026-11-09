# Cite once per story

**Rule.** One consolidated `Source grounding` bullet in `Details` — the developer's reading list. One
source tag on each acceptance criterion, and nothing else in it. Never cite in the opening *As a*
sentence. Never restate the same rule, ADR, file or workstream across sections.

**Why.** Repeated citation is noise that costs comprehension: when every bullet carries an id, the
reader stops seeing ids, and the one that mattered — a rule that marks a workstream boundary, say —
reads like the rest. The consolidated list has a different job from the criterion tag, which is why
both exist: the list tells a developer what to read before starting, and the tag is the machine-
readable link from one test back to one rule. Mixing them turns both into decoration.

**In the story.**
- `Details`: `Source grounding: [[one-label-per-parcel|LABEL-1]], [[bulk-printing-across-orders|LABEL-3]], [[enforce-credit-hold-at-label-creation|ADR-0004]].`
- The same ids go in the `sources` property as wikilinks. That is the one sanctioned duplication:
  the property is what queries and the publish step read, the sentence is what reaches the tracker's
  description, and the audit checks they agree
  ([`../references/vault-convention.md`](../references/vault-convention.md)).
- Criterion: `AC-1 [LABEL-1] Given …, when …, then …` — the behaviour is embedded, so the criterion
  reads correctly with the source closed
  ([`../patterns/acceptance-criterion.md`](../patterns/acceptance-criterion.md)).
- Inline citations elsewhere are allowed only where the rule is non-obvious, marks a workstream
  boundary, explains terminology, or identifies a gap or conflict.
- The tag's form depends on the mode: a rule id, a source name and section, or `[Request]`
  ([`../patterns/source-tag.md`](../patterns/source-tag.md)).

**Breaks when.** The same rule is cited in three sections →
[`../anti-patterns/citation-repetition.md`](../anti-patterns/citation-repetition.md).
