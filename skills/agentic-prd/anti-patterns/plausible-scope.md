# Plausible scope

**Smell.** Requirements nobody asked for, each of which any product like this would have: an audit
trail, soft delete, a permissions matrix, validation messages, retries, notifications, an export, a
reporting screen, "standard CRUD". No source names them. They arrived because a feature of this shape
usually has them.

**Why it is wrong.** Pattern-matching is not a source, and these are expensive items — the audit
trail and the permission model are often larger than the feature they were added around. Because each
one is defensible in isolation, review approves them individually and the release misses its date
collectively. The deeper cost is that the PRD stops being evidence of what was agreed, so it can no
longer settle an argument about scope, which was its job.

**Instead.** Write only what a source states, and make the Non-goals table carry the rest explicitly:
each item a reader would otherwise assume is in scope, with a reason and a revisit-when. Where the
behaviour is genuinely needed and nobody has specified it, that is an open question, not a
requirement ([`../principles/a-gap-is-a-question-not-a-guess.md`](../principles/a-gap-is-a-question-not-a-guess.md),
[`../patterns/agent-boundaries.md`](../patterns/agent-boundaries.md)).
