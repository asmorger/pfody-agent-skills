# Pattern-matching is not a source

**Rule.** Do not invent audit trails, soft delete, optimistic concurrency, validation rules,
permission names, error messages, retry behaviour, notifications, entity relationships, integration
behaviour, tenant scoping, export formats, reporting requirements or "standard CRUD" expectations
unless a named source states them. If you catch yourself thinking *this kind of feature usually needs
X*, and X is not in the source, X does not belong in the story.

**Why.** That list is not arbitrary — it is what gets added, every time, and each item is individually
defensible, which is why review approves them one at a time and the release misses its date
collectively. Several of them are also larger than the feature they were added around: a permission
model and an audit trail routinely outweigh the behaviour they were attached to. And the story stops
being evidence of what was agreed, so it can no longer settle a scope argument, which was its job.

**In the story.**
- The named-source test is mechanical: can you point at a rule id, a SOW section, a file, a request?
  No → it is not scope ([`per-bullet-traceability.md`](per-bullet-traceability.md)).
- Do not infer entity behaviour, tenancy or ownership from a feature's name. Where the source is
  silent, write "Not specified in source" or omit the bullet
  ([`../patterns/technical-notes.md`](../patterns/technical-notes.md)).
- Add criteria for edge cases, validation, error states or permissions **only** where a source
  specifies behaviour for them. Silence means an Open Question or nothing.
- Where the config says the author has no repository access, express requirements behaviourally — no
  enum names, class names, flag names, file paths or table names.

**Breaks when.** Plausible scope is written as though it were sourced →
[`../anti-patterns/pattern-matched-scope.md`](../anti-patterns/pattern-matched-scope.md).
