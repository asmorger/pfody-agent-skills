# One name and one id per level

**Rule.** Five levels, five names, five id formats, used everywhere without synonyms. A level's size
test decides what it is; nothing else does.

| Level | Id | What it is | Size test | Lives in |
|---|---|---|---|---|
| Epic | `EPIC-01` | A business outcome needing one or more Features | Serves a PRD outcome; takes more than one sprint | PRD section 4 |
| Feature | `FEAT-01` | One capability: one job for one role | Delivers one job; needs one or more User Stories | PRD section 4 |
| User Story | `US-01` | A vertical slice of one Feature | One person builds, tests and demos it in one sprint | Backlog file |
| Requirement | `R-001` | One testable behaviour | States one behaviour; belongs to one Feature | PRD section 4 |
| Acceptance criterion | `AC-1` | One Given/When/Then test of a requirement | Numbering restarts in each User Story | Backlog file |

**Why.** "Epic", "feature", "initiative" and "story" mean different things at every company, and a
PRD read by agents cannot carry that ambiguity: the level decides which tracker item gets created,
what gets a parent, and what a person is asked to approve. Fixing the names is cheap; a backlog whose
Features are really Epics has to be rebuilt.

**In the PRD.**
- An Epic, a Feature and a User Story each become one tracker item of the same level. A requirement
  and an acceptance criterion never do — they are text inside a story.
- A PRD is not an Epic. One PRD contains one or more Epics.
- A person decides the Epics and Features at Gate 2; an agent generates the User Stories from them
  ([`only-a-person-crosses-a-gate.md`](only-a-person-crosses-a-gate.md)).
- Give an Epic its own PRD when it can ship alone.

**Breaks when.** A Feature names a technical layer rather than a job →
[`../anti-patterns/a-feature-that-is-a-layer.md`](../anti-patterns/a-feature-that-is-a-layer.md).
