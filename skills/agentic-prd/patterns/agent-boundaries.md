# Agent boundaries

**Use when** filling section 6. What agents building from this PRD may do alone, must ask about, and
must never do — plus the commands that prove a change works and the conditions that stop a run.

**Skeleton.**

````markdown
## 6. Agent boundaries

**Always.**
- Read this PRD and the assigned User Story before writing code.
- Add or update a test for every acceptance criterion whose requirement verifies `Auto`.
- Run the checks below before opening a pull request.
- Put the User Story id and the requirement ids in the pull request.

**Ask first.**
- Adding a dependency, a service or a data store.
- Changing a schema, a public API or an authentication rule.
- Any behaviour no requirement describes.

**Never.**
- Build a non-goal, or a P3 requirement.
- Fill a gap with a guess. Stop and add an open question.
- Touch production data, secrets or a pipeline.
- Change a test to make it pass, unless the requirement changed first.

**Checks.**

```bash
<build command>
<test command>
<lint command>
```

**Stop conditions.** Stop and report when a requirement conflicts with the code, with another
requirement or with a constraint; or when a check has failed <n> times.
````

**Notes.**
- Delete the lines that do not apply and add the project's own. A boundary list nobody meant is
  ignored wholesale, including the lines that mattered.
- For repo-wide rules, link `AGENTS.md` or `CLAUDE.md` rather than restating them here.
- *Never build a non-goal* is the line that earns its place most often: non-goals are where an agent's
  idea of a complete feature and the project's diverge
  ([`../anti-patterns/plausible-scope.md`](../anti-patterns/plausible-scope.md)).
- The checks block is commands, not descriptions. An agent runs it verbatim.

**Related.** [`prd-hub-note.md`](prd-hub-note.md),
[`../principles/a-gap-is-a-question-not-a-guess.md`](../principles/a-gap-is-a-question-not-a-guess.md).
