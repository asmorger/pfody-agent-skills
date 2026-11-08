# Propose, then apply

**Rule.** Never edit the Reference Layer without approval. Draft in the working area, present the
proposal — rule id, the current text, the incoming item, the recommended new text — and apply only
what the user approves. Then report exactly which ids changed.

**Why.** The rule set is what a team has agreed to, and an agent is not a party to that agreement. A
silent edit also destroys the one property that makes the base useful under pressure: a reader can
trust that a rule says what someone decided it should say. The reporting half matters just as much —
an approval covering "the new rules" is not an approval of the four existing rules the change also
touched, and naming the ids is what lets the user see that it did.

**In the base.**
- Draft new and edited entries in `working_dir`; leave `docs_dir` and `knowledge_root` untouched
  until approval ([`../practices/reconcile-against-the-rules.md`](../practices/reconcile-against-the-rules.md)).
- Present proposals as a written audit grouped into conflicts, refinements and new rules
  ([`../patterns/reconciliation-audit.md`](../patterns/reconciliation-audit.md)).
- On approval, promote and report the exact ids — added, changed, deprecated
  ([`../practices/promote-to-the-record.md`](../practices/promote-to-the-record.md)).
- Update the Source Register row for each source to name the rule ids it updated. The provenance is
  part of the change, not a follow-up.
- Say which kind of output you produced: an audit, a template set, or an applied migration.

**Breaks when.** The rule set is edited directly because the change looked obviously right →
[`../anti-patterns/auto-editing-the-rule-set.md`](../anti-patterns/auto-editing-the-rule-set.md).
