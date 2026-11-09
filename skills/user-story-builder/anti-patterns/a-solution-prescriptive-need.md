# A solution-prescriptive need

**Smell.** "I want a table with filters showing label data." "I want a modal that confirms the void."
"I want an endpoint that returns the label status." The *I want to* describes the implementation, or
the screen, rather than the need.

**Why it is wrong.** It forecloses a decision the story has no evidence to make. A table may be the
wrong answer — a count, an alert or a different workflow may serve the same need better — and the
developer who sees it is the one best placed to know, now told not to think about it. Prescribed
solutions also hide the need, so the acceptance criteria end up testing the widget instead of the
outcome, and a correct implementation that looks different fails them.

**Instead.** Describe the need and let the criteria pin the observable outcome: "I want to review
pending labels before they print". Avoid the vague verbs that often accompany the problem — `manage`,
`handle`, `deal with` — and prefer `view`, `submit`, `approve`, `configure`, `filter`, `receive`.
Where a source genuinely fixes the mechanism, it goes in `Details` as a sourced constraint, not into
the opening sentence ([`../patterns/as-a-i-want-so-that.md`](../patterns/as-a-i-want-so-that.md)).
