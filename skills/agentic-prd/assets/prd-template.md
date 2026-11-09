---
id: PRD-000
aliases: [PRD-000]
type: prd
status: Draft            # Draft | In Review | Accepted | Superseded
size: Standard           # Small | Standard | Large
owner: <TPO or TPM>
approvers: [<business approver>, <architect>, <QA lead>]
version: 0.1
epics: []
outcomes: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [prd]
---

# PRD-000 — <Project or feature name>

> **Template use.** Copy this file into the vault at `docs/prd/<slug>.md`.
> Delete the guidance blocks that start with "Guidance". Keep the section numbers and all ID formats.
>
> **This is the hub.** It keeps prose a reader needs end to end, and **embeds** the notes that are
> cited individually: `![[OUT-1]]` for each outcome, `![[EPIC-01]]` in section 4, `![[X-002]]` in
> section 5. Requirements, questions, metrics, decisions and work items are their own notes, in
> `requirements/`, `questions/`, `metrics/`, `sources/` and `backlog/`. The full contract is in the
> skill's `references/vault-convention.md`.

## How this document works

This PRD is the source of record for **why** and **what**. Azure DevOps (ADO) is the source of record for **state**: sprint, assignee, estimate, and status. The PRD does not contain design, tasks, or estimates.

**Work item levels.** Each level has one ID format. Do not use another name for a level.

| Level | ID | What it is | Size test | Where it lives |
|---|---|---|---|---|
| Epic | `EPIC-01` | A business outcome that needs one or more Features | It serves an outcome in Section 1, and it can take more than one sprint | `backlog/`, embedded here |
| Feature | `FEAT-01` | One capability: one job for one role | It delivers one job, and it needs one or more User Stories | `backlog/` |
| User Story | `US-01` | A vertical slice of one Feature | One person can build, test, and demo it in one sprint | The backlog file |
| Requirement | `R-001` | One testable behavior. It is not a tracker item. | It states one behavior, and it belongs to one Feature | `requirements/`, one note each |
| Acceptance criterion | `AC-1` | One Given/When/Then test of a Requirement | Its number restarts in each User Story | The backlog file |

**Select the size first. Use the smallest size that removes guesswork.**

| Size | Use for | Required sections |
|---|---|---|
| No PRD | A bug, or a change with one clear behavior | None. Write one User Story. |
| Small | One Feature under one Epic. Put constraints at the end of Section 2. | 1, 2, 4, 6, 7 |
| Standard | One Epic in one release | 1 to 8 |
| Large | Several Epics, or work across several releases | 1 to 8, and the modules that apply. Give an Epic its own PRD when it can ship alone. |

**Humans decide. Agents draft and check.**

| Section | Human job | Agent job |
|---|---|---|
| 1 Intent, 2 Scope | Write or approve. **Gate 1.** | Draft from sources. Challenge weak evidence. |
| 3 Context | Confirm | Collect links. Summarize current behavior. |
| 4 and 5 Epics, Features, and requirements | Decide. Approve. **Gate 2.** | Draft. Find gaps and conflicts. |
| 6 Agent boundaries | Set | Obey |
| 7 Ledger | Answer. Decide. | Record every source, gap, and assumption. |
| Backlog (derived file) | Review the diff. **Gate 3.** | Generate. Prove coverage. |

---

## 1. Intent

**Narrative.** <Three sentences or fewer. Who gets what outcome, and why it matters.>

**Problem.** <The user or business problem. Do not name a solution.> Evidence: <SRC-xx>

**Users.**

| User | Need | Notes |
|---|---|---|
| <Primary role> | | |
| <Admin, internal, or support role> | | |

**Outcomes.** Guidance: A number without all of these fields is not a metric. Use "Unknown" and add an open question when a value is not known.

| ID | Metric | Baseline | Target | Owner | Source system | Population | Denominator | Window |
|---|---|---|---|---|---|---|---|---|
| OUT-1 | | | | | | | | |

## 2. Scope

**In scope.**
- <Outcome-level item>

**Non-goals.** Guidance: Agents add plausible scope when a boundary is not stated. Write down each item that a reader can assume is in scope.

| Non-goal | Reason | Revisit when |
|---|---|---|
| | | |

## 3. Context

**Current behavior.** <What happens today. Link to the code or the system of record.>

**Team and links.** Guidance: Link. Do not copy content from a system of record.

| Discipline | Name | Team | Links |
|---|---|---|---|
| TPM/TPO | | | Backlog, SOW |
| Architect | | | Architecture docs, ADRs, repo conventions |
| Design | | | Designs |
| Quality Assurance | | | Test plan |

**Constraints.** <Fixed technology, contract, compliance, budget, or date limits. State only real limits.>

**Dependencies.**

| ID | Dependency | Details | Contact |
|---|---|---|---|
| DEP-01 | | | |

**Glossary.** Guidance: Use one term for one meaning. Agents copy your words into code and tests.

| Term | Meaning | Do not use |
|---|---|---|
| | | |

## 4. Epics, Features, and requirements

**Work item map.** Guidance: List each Epic and Feature. A Feature ID is unique in the PRD. Add the tracker link when the item exists. User Stories stay in the backlog file, because agents generate them.

| ID | Level | Name | Parent | Tracker item |
|---|---|---|---|---|
| EPIC-01 | Epic | <Epic name> | PRD-000 | <link, or none> |
| FEAT-01 | Feature | <Feature name> | EPIC-01 | <link, or none> |

**Priority.**
- **P0:** Must have in MVP. Without this, there is no project.
- **P1:** Must have for a functional release.
- **P2:** Nice to have for MVP. User Stories get the `Stretch` tag.
- **P3:** Include in a later release. Do not generate User Stories.

If no stakeholder assigned a priority, record the priority as an inference in Section 7.

**Requirement format.** Write one behavior in each requirement. Start each requirement with a pattern below, because the check script looks for these words. Describe observable behavior. Do not name a technology unless a constraint requires it.

| Type | Pattern |
|---|---|
| Always | The system shall <behavior>. |
| Event | When <trigger>, the system shall <behavior>. |
| State | While <state>, the system shall <behavior>. |
| Unwanted | If <bad condition>, then the system shall <behavior>. |
| Optional | Where <option is on>, the system shall <behavior>. |

**Source column.** Every requirement has one value:
- `SRC-xx`: verified evidence or stakeholder input in the source register. Add a locator: a time (`SRC-xx @12:34`), a page (`SRC-xx p.4`), or a line in plain notes (`SRC-xx L12`).
- `DEC-xx`: a recorded decision. The decision row cites its source, so do not repeat the source here.
- `A-xx`: an inference or assumption. The approver accepts the risk.
- `PROPOSED`: no source. An agent or a person suggested it. **An Accepted PRD has no `PROPOSED` values.**

**Verify column.** `Auto` (a test that a build can run), `Manual` (UAT or exploratory test), `Eval` (a scored data set, Module M1), or `Telemetry`.

### EPIC-01: <Epic name>

**Outcome.** <The business change that this Epic delivers.>

**Outcomes served.** OUT-1

#### FEAT-01: <Feature name>

**Job.** As a <specific role>, I can <need> when <situation>, so that <business result>.

**Outcomes served.** OUT-1

**Design.** <Link, or none>

| ID | Requirement | Pri | Source | Verify |
|---|---|---|---|---|
| R-001 | | P0 | | Auto |

**Coverage check.** Guidance: For each line, give the requirement IDs. If a line does not apply, write "N/A" and the reason. If the sources do not answer, write "Gap: Q-xx" and add the open question. Do not delete a line.

| Check | Requirement IDs, or N/A and reason |
|---|---|
| Empty state | |
| Loading state | |
| Error state | |
| Permissions | |
| Bad input and boundaries | |
| Concurrency | |
| Current records and data migration | |

<Copy the FEAT block for each Feature. Copy the EPIC block for each Epic. Each Epic, Feature, and User Story becomes one tracker item of the same level.>

## 5. Cross-cutting requirements

Guidance: Use this section for behavior that applies to more than one Feature. In Applies to, write `All` or FEAT IDs. A requirement that applies to "All" goes to the Definition of Done in the backlog. It does not repeat in each User Story.

| ID | Applies to | Requirement | Pri | Source | Verify |
|---|---|---|---|---|---|
| X-001 | FEAT-01 | <Accessibility: keyboard, contrast, screen reader> | | | |
| X-002 | All | <Security, privacy, or performance> | | | |

## 6. Agent boundaries

Guidance: Remove the examples that do not apply. Add project rules. Link to `AGENTS.md` or `CLAUDE.md` for rules that apply to the full repo.

**Always.**
- Read this PRD and the assigned User Story before you write code.
- Add or update a test for each acceptance criterion with `Verify: Auto`.
- Run the checks below before you open a pull request.
- Put the User Story ID and the requirement IDs in the pull request.

**Ask first.**
- Add a dependency, a service, or a data store.
- Change a schema, a public API, or an authentication rule.
- Change behavior that a requirement does not describe.

**Never.**
- Do not build a non-goal or a P3 requirement.
- Do not fill a gap with a guess. Stop. Add an open question.
- Do not change production data, secrets, or a pipeline.
- Do not change a test to make it pass unless the requirement changed.

**Checks.**

```bash
<build command>
<test command>
<lint command>
```

**Stop conditions.** Stop and report when a requirement conflicts with code, another requirement, or a constraint. Stop when a check fails after <n> attempts.

## 7. Knowledge ledger

**Sources.** Guidance: A newer decision replaces an older statement. If two sources conflict and no decision settles it, add an open question. Do not select a side.

| ID | Source | Type | Link | Date |
|---|---|---|---|---|
| SRC-01 | | Verified or Stakeholder | | |

**Decisions.**

| ID | Decision | Owner | Date | Reason | Rejected options | Revisit when |
|---|---|---|---|---|---|---|
| DEC-01 | | | | | | |

**Assumptions and inferences.**

| ID | Statement | Type | Basis | What makes it false | Affects |
|---|---|---|---|---|---|
| A-01 | | Assumption or Inference | | | |

**Open questions.** Guidance: An open question blocks its requirements. Decomposition skips blocked requirements and reports them. A blocked requirement can state `<behavior not known>`. Use a date for Needed by. A draft can use a gate name until the schedule is known.

| ID | Question | Owner | Needed by | Blocks | Status |
|---|---|---|---|---|---|
| Q-01 | | | | | Open |

## 8. Rollout and measurement

**Rollout.** <Feature flags, phases, migration, communication, and rollback.>

**Telemetry.** Guidance: Each outcome needs a data source. List only events that do not exist today.

| Event | Dimensions | Data type | Serves | Requirement |
|---|---|---|---|---|
| | | | OUT-1 | |

---

## Optional modules

### M1. AI behavior

Guidance: Use this module when the product itself contains a model or an agent. The same input can give different outputs, so pass or fail tests are not sufficient.

| Item | Definition |
|---|---|
| Tools and permissions | <What the agent can read, write, and call> |
| Autonomy limits | <What it does alone. What needs human approval.> |
| Eval set | <Data set link, size, owner, and refresh rule> |
| Pass thresholds | <Metric, threshold, and sample size> |
| Failure behavior | <Low confidence, refusal, timeout, and fallback> |
| Retries and limits | <Attempts, cost limit, and latency limit> |
| Audit | <What the system records for human review> |
| Prohibited behavior | <What the agent must never do> |

Write the behavior in these items as requirement notes with `verify: Eval`.

### M2. Data migration

| Item | Definition |
|---|---|
| Records in scope | |
| Rules for each record state | |
| Validation and reconciliation | |
| Rollback | |

---

## Agent protocol

Guidance: Keep this section in each PRD. It gives each agent the same rules.

**Use one mode at a time. The person who asks names the mode. Do not publish or push unless that person asks.**

### Mode: DRAFT

1. Read the named sources. Fill this template.
2. Record each source in Section 7.
3. Mark each statement that has no source as `PROPOSED`, an assumption, or an open question.
4. Do not invent a metric, a date, a customer need, or a behavior. Write "Unknown".

### Mode: REVIEW

Report findings as a list. Do not change the PRD. Find these items:

1. A requirement with more than one behavior, or a behavior that a test cannot check.
2. A vague word with no threshold, such as "fast", "simple", or "appropriate".
3. A requirement that serves no outcome, or an outcome with no requirement.
4. A blank line in a coverage check.
5. A conflict between requirements, non-goals, constraints, or the current code.
6. A term that the glossary does not define, or two terms for one meaning.
7. A `PROPOSED` value, or an open question without an owner and a date.
8. An Epic with no Feature, a Feature that delivers more than one job, or a Feature that is only a technical layer.
9. The questions that a developer must ask before the build can start. List them in the order to ask.

### Mode: DECOMPOSE

**Preconditions.** The status is Accepted. No `PROPOSED` value remains.

**Preview.** A person can ask for a preview before acceptance. Say PREVIEW in the first lines of every User Story note. Skip each `PROPOSED` requirement and report it. Do not publish a preview.

1. Keep each Epic and Feature with its ID and name. Do not create, merge, or rename them in this mode.
2. Slice each Feature into User Stories with the IDs US-01, US-02, and so on. An ID is unique in the backlog. Each User Story is a vertical slice that one person can build, test, and demo in one sprint. Slice by outcome. Do not slice by layer.
3. Assign each in-scope `R-` requirement to exactly one User Story in its own Feature.
4. Assign each `X-` requirement to each User Story that it changes, in the Features that it names. Put each "All" requirement in a Definition of Done at the top of the backlog.
5. Skip P3 requirements. Skip requirements that an open question blocks. Report both.
6. Convert each requirement to one or more acceptance criteria in this form: `AC-n [R-001] Given <precondition>, when <trigger>, then <result>.`
7. Do not add behavior. Leave a new gap out of the User Story and report it. A person decides whether to use Mode: CHANGE.
8. Do not add tasks or estimates.
9. Write one note per work item in `backlog/`. Each has `type` (epic, feature or user-story), an `id`, a matching `aliases`, and a `parent` wikilink: an Epic's parent is the PRD, a Feature's is an Epic, a User Story's is a Feature. Each User Story has these labels in this order: the "As a" sentence, Expected Output, Details (with `Source grounding:`), Assumptions, Testing Strategy, Open Questions, Technical Notes, Acceptance Criteria, Tags. Put each "All" requirement in a Definition of Done in `moc/backlog.md`.
10. Set each requirement note's `coverage` to covered, blocked, skipped-proposed, skipped-p3 or retired, and its `stories` or `questions` to match. Do not write a coverage table: run `python3 scripts/prd.py moc <vault>` and it is generated from the notes. Report the counts of Epics, Features and User Stories.

### Mode: CHANGE

1. Change the PRD first. Add the new source or decision. Increase the version.
2. Do not reuse an ID. Keep the current EPIC, FEAT, US, and R IDs. Mark a removed requirement with `status: retired`, `coverage: retired` and a `superseded-by` link. Never delete a note: deleting it dangles every wikilink that cited it.
3. List the Epics, Features, User Stories, and tests that the change affects.
4. Regenerate only the User Stories that the change affects. Show the diff.
5. Do not change acceptance criteria in ADO unless the PRD changed first.
