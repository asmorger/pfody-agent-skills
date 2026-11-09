# Vocabulary from the skill, not the config

**Smell.** A story using `AuditableEntity`, `TenantId`, "shipping clerk" or `labels.void` on a project
whose config names none of them — because they appeared in this skill's examples, or in a story written
for a different client. A tenancy bullet on a project whose `tenancy_term` is `None`.

**Why it is wrong.** The borrowed word reads as authoritative, so it propagates: into the tracker, into
code, into the next story. On a project that calls them "despatch operators", "shipping clerk" is a
small, confident error that a developer will reasonably assume came from a source. The class and flag
names are worse, because they assert an implementation choice this skill has no access to — and where
the config says the author has no repository access, they cannot have been verified at all.

**Instead.** Take every project-specific word from the config: roles, tenancy term, permission model,
entity base options, id scheme, flag names, design asset locations. Substitute them wherever the
portable core shows a `{{placeholder}}` or a generic role. Omit a bullet entirely when its config field
is `None` rather than substituting a generic term, and where a value would need code access, use the
conceptual capability name or "To be determined by engineering"
([`../principles/vocabulary-comes-from-the-config.md`](../principles/vocabulary-comes-from-the-config.md),
[`../patterns/knowledge-config.md`](../patterns/knowledge-config.md)).
