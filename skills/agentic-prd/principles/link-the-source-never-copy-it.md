# Link the source, never copy it

**Rule.** Cite a source by id and link to where it lives. Do not copy credentials, customer records,
personnel comments, fee data or candid remarks into the PRD. Name roles, not people. If a citation
points at something only the team can open, say so before the PRD is shared outside it.

**Why.** A PRD circulates further than any of its sources: it goes to a client, into a repository, to
a contractor, into an agent's context window. Each copy of a secret or a customer record multiplies a
risk that the source system was holding under access control, and a copied remark about a named
person outlives the meeting that excused it. Linking keeps one copy under its own controls and keeps
the PRD about behaviour. It is also the only form of citation that stays true — a link follows the
source when it is corrected, and a paste does not.

**In the PRD.**
- Roles: "a shipping clerk", "the support agent on duty" — never a name, in requirements or stories.
- Context links point at the backlog, the SOW, the architecture docs, the designs, the test plan.
- A quote exists to identify a statement, not to reproduce a conversation: short, and only where the
  wording is the point.
- Flag internal-only citations in the report, before anyone shares the document
  ([`../practices/report-the-result.md`](../practices/report-the-result.md)).

**Breaks when.** The ledger becomes a copy of the system of record →
[`../anti-patterns/copying-the-system-of-record.md`](../anti-patterns/copying-the-system-of-record.md).
