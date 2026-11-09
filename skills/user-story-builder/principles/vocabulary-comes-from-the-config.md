# Vocabulary comes from the config

**Rule.** Every project-specific word comes from the per-project config: roles and personas, the
tenancy term, the permission model, entity base options, id and ADR conventions, tag policy, design
asset locations, the publishing target. Any role, class, permission or term appearing in this skill's
examples is illustrative only, and substitutes for a `{{placeholder}}` are taken from the config.

**Why.** It is what makes the skill portable. A rule that names a real project's `TenantId` or
`AuditableEntity` stops being a rule and becomes that project's leaked detail, and the next project
inherits vocabulary nobody there uses — which is worse than no guidance, because it reads as
authoritative. Keeping the vocabulary in one declared file also means a project can change its own
terms in one place rather than across every story written since.

**In the story.**
- Roles come from the config's persona list, and distinguish external users from internal staff
  ([`../anti-patterns/a-vague-role.md`](../anti-patterns/a-vague-role.md)).
- Omit a tenancy bullet entirely when the config's `tenancy_term` is `None`. Do not substitute a
  generic one.
- Where the config lists `entity_base_options`, engineering selects among them — describe the need
  behaviourally and assert nothing
  ([`../patterns/technical-notes.md`](../patterns/technical-notes.md)).
- Where a value would need code access and the config says you have none, use the conceptual
  capability name or "To be determined by engineering".
- A config path that no longer resolves is flagged to the user, never silently cited as nothing
  ([`../practices/load-or-provision-the-config.md`](../practices/load-or-provision-the-config.md)).

**Breaks when.** An example's vocabulary is used as though it were the project's →
[`../anti-patterns/vocabulary-from-the-skill-not-the-config.md`](../anti-patterns/vocabulary-from-the-skill-not-the-config.md).
