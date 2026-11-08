# Reconcile against the rules

**When** an incoming item — from any source — must be checked against what the base already says.
This is the step that makes a knowledge base a base rather than an archive.

**Why.** Appending is what produces a base that answers the same question two ways. Reconciliation is
also the only point where a contradiction is cheap to catch: before the rule is cited by a story, a
test and a tracker item.

**Steps.**

1. **Read `business-rules.md` end to end**, with the glossary and the scope ledger. Not a search —
   the whole file. A contradiction you did not read is a contradiction you will not find.
2. **Classify every incoming item** into exactly one of five: already covered · conflicts (name the
   rule id) · refines · new rule · a governance entry only. An item that lands nowhere was not durable
   knowledge.
3. **For a conflict, compare authority** before anything else
   ([`../patterns/authority-ladder.md`](../patterns/authority-ladder.md)). Equal levels settle
   nothing — that is a question
   ([`../patterns/open-question.md`](../patterns/open-question.md)).
4. **Write the audit**, grouped into conflicts, refinements and new rules, each row giving the rule
   id, the **quoted** current text, the incoming item, and the recommended new text or id
   ([`../patterns/reconciliation-audit.md`](../patterns/reconciliation-audit.md)).
5. **Draft `CH-NNNN` for a genuine shift** and `SW-NNNN` for anything that may exceed the baseline
   ([`../patterns/knowledge-change-entry.md`](../patterns/knowledge-change-entry.md),
   [`../patterns/scope-watch-item.md`](../patterns/scope-watch-item.md)).
6. **Propose ids for new rules** — the next free number in the owning section, or a new section and
   prefix per the config ([`write-a-business-rule.md`](write-a-business-rule.md)).
7. **Draft everything in the working area.** Do not touch the Docs folder or the record yet
   ([`../principles/propose-then-apply.md`](../principles/propose-then-apply.md)).
8. **Present the audit and stop.** Approval is the user's.

**Done when** every incoming item is classified, every conflict names the rule it conflicts with and
the authority on each side, the current text is quoted rather than summarised, and nothing has been
written to the record.
