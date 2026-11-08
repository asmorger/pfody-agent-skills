# One rule, two ideas

**Smell.** `LABEL-1 | A label is created for the order's shipping address when a clerk requests it,
and the carrier's rejection reason is shown to the clerk.` One id, one "and", two behaviours — and
usually two different sources and two different confirmation states.

**Why it is wrong.** The rule stops being testable as a unit, and everything that cites it inherits
the ambiguity: a story's criterion can only test half, and the half nobody tested still looks covered.
Status is the sharper problem. The two halves are rarely confirmed on the same day, so the rule ends
up with a date that is true of one clause and wrong about the other — or with a pending marker that
makes a confirmed behaviour look open.

**Instead.** Split. The original keeps its id and one idea; the second takes the next free number in
the section; the two cross-link. Each then carries its own inline status, its own date and its own
source row. Where the two really are one behaviour, say it as one observable outcome rather than two
verbs joined by "and"
([`../practices/write-a-business-rule.md`](../practices/write-a-business-rule.md),
[`../patterns/business-rules-file.md`](../patterns/business-rules-file.md)).
