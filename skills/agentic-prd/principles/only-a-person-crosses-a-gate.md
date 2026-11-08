# Only a person crosses a gate

**Rule.** Three gates belong to people: Gate 1 approves intent and scope, Gate 2 approves the Epics,
Features and requirements, Gate 3 approves the backlog. An agent drafts up to a gate, says it is at
one, and stops. It never writes `status: Accepted` unless the approver said so in words, and it never
publishes or pushes without being asked in the current conversation.

**Why.** The gates are where the project's cost is actually set, and the agent is the one participant
who cannot be held to the consequences. Acceptance is also what unlocks the irreversible steps —
decomposition, tracker items, work starting — so an agent that can accept its own draft can start a
build off its own guesses. Keeping the gate human costs one message and removes that whole class of
failure.

**In the PRD.**
- Status moves `Draft` → `In Review` → `Accepted`, by a person, each time.
- Before acceptance, a decomposition is a preview: marked `PREVIEW` at the top, `PROPOSED`
  requirements skipped and reported, never published
  ([`../practices/decompose-a-prd.md`](../practices/decompose-a-prd.md)).
- Warnings may sit in a draft. A person resolves or accepts each one before Gate 2
  ([`../practices/run-the-checks.md`](../practices/run-the-checks.md)).
- End every mode by naming the decisions that are the person's, most consequential first
  ([`../practices/report-the-result.md`](../practices/report-the-result.md)).

**Breaks when.** Items reach a tracker without an explicit yes →
[`../anti-patterns/publishing-without-a-yes.md`](../anti-patterns/publishing-without-a-yes.md).
