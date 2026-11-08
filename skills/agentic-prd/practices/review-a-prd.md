# Review a PRD

**When** a person asks whether a PRD is ready, where its gaps are, or whether an agent could build
from it. Mode `REVIEW`.

**Why.** The defects that matter are the ones that still look like a finished spec: a quietly
resolved conflict, a requirement with two behaviours, scope that drifted past the contract. Each is
cheap now and expensive once code exists.

**Steps.**

1. **Run the checks** and put the result in the review, including what the script cannot judge
   ([`run-the-checks.md`](run-the-checks.md)). **Change nothing**, even if a check fails — not one
   word of the PRD ([`../principles/the-prd-changes-before-the-backlog.md`](../principles/the-prd-changes-before-the-backlog.md)).
2. **Write to `<prd-name>.review.md`**, in the shape of
   [`../patterns/review-findings.md`](../patterns/review-findings.md).
3. **Compare against the contract** and any earlier requirements, where they exist. Scope drift
   against a SOW is routinely the largest finding, and nobody is looking for it.
4. **Work the checklist**, hunting for: a requirement with more than one behaviour or no checkable
   test; a vague word with no threshold; a requirement serving no outcome, or an outcome with no
   requirement; a blank coverage line; a conflict between requirements, non-goals, constraints or the
   current code; a term the glossary does not define, or two terms for one meaning; a `PROPOSED`
   value, or a question with no owner and date; an Epic with no Feature, a Feature doing more than one
   job, or a Feature that is only a technical layer.
5. **Group the findings** as conflicts, requirement quality, coverage. Each one names the item and
   the action.
6. **State readiness** for the next gate, plainly, with the reasons that decided it.
7. **End with the questions to ask**, ordered by how much scope the answer can move. Scan
   [`../anti-patterns/`](../anti-patterns/) by file name and open any that match what you found.

**Done when** the PRD is untouched, every finding names an item and an action, the readiness verdict
is stated either way, and the first question on the list is the one that could make the others moot.
