# Record a decision

**When** a design or scope decision is settled, or an earlier one is reversed. Standing operating
procedure D.

**Why.** A decision that only exists in a rule row loses its reasoning, and the reasoning is what
stops the question being reopened next quarter. The rejected alternatives are the part that does that
work.

**Steps.**

1. **Check whether it reverses an earlier ADR.** If it does, this is a supersession: write a new ADR
   that names what it supersedes, and change the old one's status. Never overwrite a decision's body
   ([`../principles/deprecate-never-delete.md`](../principles/deprecate-never-delete.md)).
2. **Take the next ADR number** and the project's filename convention — `NNNN-kebab-title.md` in
   `adr/`, sequential, never renumbered
   ([`../patterns/decision-record.md`](../patterns/decision-record.md)).
3. **Fill the frontmatter and every section**: Status, Context, Decision, Rationale, Consequences
   (easier and harder), Alternatives Considered, Assumptions, Future Review, Related. The full set is
   in [`../references/templates.md`](../references/templates.md).
4. **Name how each alternative fails**, not that it lost. An alternative with a verdict and no failure
   is a decision that will be re-argued.
5. **Add the index row**, with the frontmatter `summary` copied as the summary — one wording, two
   places that must match.
6. **Update the rules the decision settles**: cite the ADR inline, date the decided clause, remove any
   pending marker ([`write-a-business-rule.md`](write-a-business-rule.md)).
7. **A refinement that reverses nothing** gets a dated addendum on the existing ADR, not a new one.
8. **Promote and report** the ADR number and every rule id it touched
   ([`promote-to-the-record.md`](promote-to-the-record.md)).

**Done when** the ADR exists with every section filled, each rejected alternative names its failure,
the index has its row, the rules it settles cite it and carry dates, and a reversed ADR's status says
what superseded it.
