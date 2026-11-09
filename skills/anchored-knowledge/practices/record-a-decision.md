# Record a decision

**When** a design or scope decision is settled, or an earlier one is reversed. Standing operating
procedure D.

**Why.** A decision that only exists in a rule note loses its reasoning, and the reasoning is what
stops the question being reopened next quarter. The rejected alternatives are the part that does that
work.

**Steps.**

1. **Check whether it reverses an earlier ADR.** If it does, this is a supersession: write a new ADR
   that names what it supersedes, and change the old one's status. Never overwrite a decision's body
   ([`../principles/deprecate-never-delete.md`](../principles/deprecate-never-delete.md)).
2. **Take the next ADR number** into `id` and `aliases`, and name the note for the decision:
   `decisions/credit-hold-blocks-labelling.md`. Numbers are sequential and never renumbered; a
   project already numbering its filenames keeps that form
   ([`../patterns/decision-record.md`](../patterns/decision-record.md)).
3. **Fill the frontmatter and every section**: Status, Context, Decision, Rationale, Consequences
   (easier and harder), Alternatives Considered, Assumptions, Future Review, Related. The full set is
   in [`../references/templates.md`](../references/templates.md).
4. **Name how each alternative fails**, not that it lost. An alternative with a verdict and no failure
   is a decision that will be re-argued.
5. **Write `summary` once, in the frontmatter.** The decisions MOC reads it from there, so there is
   no index row to keep in step ([`../patterns/moc-note.md`](../patterns/moc-note.md)).
6. **Update the rules the decision settles**: add the ADR to their `decisions`, wikilink it in the
   body, set `confirmed`, and drop any open-question callout it closes
   ([`write-a-business-rule.md`](write-a-business-rule.md)).
7. **Point `rules` at what it settles**, so each rule's backlinks lead here.
8. **A refinement that reverses nothing** gets a dated `[!info]` addendum on the existing note.
9. **Promote and report** the ADR number and every rule id it touched
   ([`promote-to-the-record.md`](promote-to-the-record.md)).

**Done when** the note exists with every section filled, each rejected alternative names its failure,
the rules it settles link to it and carry dates, a reversed decision's `status` and `superseded-by`
say what replaced it, and the decisions MOC has been regenerated.
