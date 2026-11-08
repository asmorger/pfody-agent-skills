# Glossary

**Use when** the project needs a word to mean one thing. Write it first; consult it first. It is the
cheapest file in the base and the one that prevents the most rework.

**Skeleton.**

```markdown
# Glossary

## Core Concepts

| Term | Definition |
| --- | --- |
| **Order** | A customer's confirmed request for goods. Governed by ORDER-1. |
| **Parcel** (Shipment) | One physical box leaving the warehouse. "Shipment" is retired — it meant both this and a carrier collection. |
| **Label** | A carrier-issued document attached to one parcel. Created per LABEL-1; voiding is LABEL-2. |

## Systems & Integration

| Term | Definition |
| --- | --- |
| **Carrier portal** | The carrier's own web system, the source of record for label status. See [ADR-0003](adr/0003-carrier-rest-api.md). |
```

**Notes.**
- Grouped under `## <Category>` headings; one row per term in a two-column table.
- Write the term as `**Term** (Alias)`. Retired aliases and the reason they were retired go in the
  definition, not in a separate list
  ([`../principles/deprecate-never-delete.md`](../principles/deprecate-never-delete.md)).
- Link the governing rule or ADR from the definition. The glossary says what a word means; it does
  not restate the rule ([`../principles/one-home-per-fact.md`](../principles/one-home-per-fact.md)).
- Two terms for one meaning, and one term used two ways, are both audit findings. Reconcile them in
  the glossary rather than picking a winner in prose.
- Adopt the team's word even when a better one exists. A glossary that argues with its readers is not
  consulted ([`../principles/match-the-projects-voice.md`](../principles/match-the-projects-voice.md)).

**Related.** [`business-rules-file.md`](business-rules-file.md),
[`../practices/audit-the-base.md`](../practices/audit-the-base.md).
