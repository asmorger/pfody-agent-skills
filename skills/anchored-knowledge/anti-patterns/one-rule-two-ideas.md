# One rule, two ideas

**Smell.** One note, titled "Label creation and rejection handling": *A label is created for the
order's shipping address when a clerk requests it, and the carrier's rejection reason is shown to the
clerk.* One id, one "and", two behaviours — and usually two sources and two confirmation states.

**Why it is wrong.** The rule stops being testable as a unit, and everything that cites it inherits
the ambiguity: a story's criterion can only test half, and the half nobody tested still looks covered.
Status is the sharper problem. A note has **one** `status`, one `confirmed` date and one `sources`
list, and the two halves are rarely confirmed on the same day by the same source — so the note ends
up asserting a date that is true of one clause and wrong about the other. Backlinks blur the same
way: "what depends on the rejection-reason behaviour?" has no answer when both live in one note.

**Instead.** Split. The original keeps its id and one idea; the second takes the next free number for
its topic; the two cross-link. Each then carries its own status, dates, `sources` and backlinks.
Where the two really are one behaviour, say it as one observable outcome rather than two verbs joined
by "and"
([`../practices/write-a-business-rule.md`](../practices/write-a-business-rule.md),
[`../patterns/business-rule-note.md`](../patterns/business-rule-note.md)).
