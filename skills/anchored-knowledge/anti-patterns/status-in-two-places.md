# Status in two places

**Smell.** `status: draft` in the frontmatter and `(Draft: pending the operations lead)` in the first
sentence. Or `status: confirmed` with a `> [!warning] Draft` callout left over from last month. Or
`tags: [rule/orders, draft]` beside a `status` property. Each one looks like belt and braces.

**Why it is wrong.** One of the two will be updated and the other will not — and there is no rule
about which, so a reader cannot even learn to trust one of them. The duplicate also defeats the point
of the property: Bases and the audit read frontmatter, so a rule whose prose says draft and whose
property says confirmed appears in the confirmed view, silently, and is built from. A status tag is
the worst of the three, because the tag pane then shows a count that disagrees with every query.

**Instead.** The property is the status, always, and the only place it lives. A callout is for what
the property cannot say — which stakeholder, by when, what it replaced, which clause is still open —
and never restates it: `> [!warning] Draft — pending operations lead, as of 2026-11-08` adds the
owner and the date, which is why it is allowed. Tags carry type and topic only. When you catch a
duplicate, delete the prose and keep the property
([`../principles/properties-are-the-query-surface.md`](../principles/properties-are-the-query-surface.md),
[`../patterns/status-callouts.md`](../patterns/status-callouts.md)).
