# Pattern-matched scope

**Smell.** Expected Output bullets and criteria nobody sourced, each of which any feature like this
would have: an audit trail, soft delete, a permissions matrix, validation messages, retries,
notifications, an export, tenant scoping, "standard CRUD". The story reads complete. No source names
any of it.

**Why it is wrong.** Pattern-matching to similar features is not a source, and that list is not
arbitrary — it is what gets added every time. Each item is individually defensible, so review approves
them one at a time and the release misses its date collectively; several are larger than the behaviour
they were attached to. The deeper cost is that the story stops being evidence of what was agreed, so
it can no longer settle a scope argument, which is the job it existed to do.

**Instead.** Apply the named-source test per bullet: can you point at a rule id, a SOW section, a
file, the request? If not, the bullet has three destinations and only three — an explicit Assumption,
an Open Question, or deletion. A narrower story that is entirely sourced is the correct output from a
thin source, and it is visibly incomplete, which is what makes it safe
([`../principles/pattern-matching-is-not-a-source.md`](../principles/pattern-matching-is-not-a-source.md),
[`../principles/a-gap-has-three-options.md`](../principles/a-gap-has-three-options.md)).
