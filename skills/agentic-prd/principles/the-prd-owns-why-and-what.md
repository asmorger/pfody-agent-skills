# The PRD owns why and what

**Rule.** The PRD holds intent, scope, requirements, sources and boundaries. The work tracker holds
state: sprint, assignee, estimate, status. Design, task breakdowns and estimates belong to neither —
they are engineering's at build time. Nothing is duplicated across the line.

**Why.** Two documents holding the same fact means one of them is wrong and nobody knows which. The
split is chosen so each side owns what it is good at: the PRD is reviewable, diffable and cites
sources, which is what *why* and *what* need; the tracker is current, assigned and reportable, which
is what *state* needs. Keeping design out is the same argument one level down — a PRD that specifies
the solution forecloses decisions it has no evidence to make, and it ages the moment engineering
learns something.

**In the PRD.**
- Link to the system of record; never copy its content
  ([`link-the-source-never-copy-it.md`](link-the-source-never-copy-it.md)).
- A tracker link goes in the work item map once the item exists. Sprint and assignee never appear.
- A backlog carries no tasks and no estimates
  ([`../anti-patterns/tasks-and-estimates-in-the-backlog.md`](../anti-patterns/tasks-and-estimates-in-the-backlog.md)).
- *Design* on a Feature is a link, or `None`. A placeholder is `None`, not an invented link.
- Each PRD holds its own copy of the agent protocol, so an agent without this skill can still work
  from it.

**Breaks when.** The PRD starts describing the build →
[`../anti-patterns/tasks-and-estimates-in-the-backlog.md`](../anti-patterns/tasks-and-estimates-in-the-backlog.md).
