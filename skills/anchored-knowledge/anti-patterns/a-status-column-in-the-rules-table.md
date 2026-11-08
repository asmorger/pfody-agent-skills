# A status column in the rules table

**Smell.** `| ID | Rule | Status | Anchors | Owner |`. It looks more rigorous than two columns, and
the first few rows are tidy.

**Why it is wrong.** The columns run to paragraphs, and then they fight the table. An anchor cell
cannot hold a link with a pipe in it, a list of sources, or a history. A status cell cannot say *which
clause* of the rule is still open, which is the usual case — half a rule confirmed and half pending.
So the detail migrates into the rule text anyway and the columns go stale beside it, giving a reader
two answers about the same rule. Wide tables also stop being readable in a diff, which is where
knowledge changes get reviewed.

**Instead.** Two columns, `| ID | Rule |`. Status goes inline, with its date, and can therefore attach
to a single clause. Provenance goes in the Source Register, whose row names the rule ids that source
updated, with the rule's inline date as the pointer. Owner belongs to the question or the ADR, not to
every rule ([`../patterns/business-rules-file.md`](../patterns/business-rules-file.md),
[`../patterns/inline-status-markers.md`](../patterns/inline-status-markers.md)).
