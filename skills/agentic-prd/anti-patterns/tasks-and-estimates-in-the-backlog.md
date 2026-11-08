# Tasks and estimates in the backlog

**Smell.** A story with a task list under it: "add migration", "write the client", "update the
screen". Story points or day counts in the Technical Notes. A PRD section describing the schema or
naming the library to use, where no constraint requires it.

**Why it is wrong.** Three different owners get confused at once. Tasks and design are engineering's,
decided at build time with information the PRD does not have — written early they are guesses that
constrain the people who will know better. Estimates belong to the estimate process and to the
tracker, where they can be revised without reopening a contract. And the PRD is supposed to be stable
*because* it holds only why and what; the moment it holds how, every implementation discovery becomes
a PRD change.

**Instead.** State the behaviour and stop. Let the story carry Testing Complexity — `Low`, `Medium`,
`High` — which is a property of the behaviour rather than a forecast, and let the tracker carry sprint,
assignee and estimate. Name a technology only where a constraint genuinely fixes it, and say which
constraint ([`../principles/the-prd-owns-why-and-what.md`](../principles/the-prd-owns-why-and-what.md)).
