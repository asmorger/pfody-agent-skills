# Copying the system of record

**Smell.** A Context section with the SOW's clauses pasted in. A ledger row holding a connection
string "for the architect's reference". A requirement quoting a customer's name and order number as
an example. A source note recording what a named person said about a colleague.

**Why it is wrong.** A PRD circulates much further than its sources: to a client, into a repository,
to a contractor, into an agent's context window. Each paste multiplies a risk the source system was
holding under access control, and a candid remark about a named person outlives the meeting that
excused it. The copy also goes stale silently — the source gets corrected and the PRD keeps asserting
the old version with a citation that makes it look current.

**Instead.** Link to where it lives and cite it by id. Use roles, not names — "a shipping clerk",
"the operations lead". Quote only where the exact wording is the point, and only as much as
identifies the statement. Leave out credentials, customer records, fee data and personnel comments
entirely, and tell the person when a citation points somewhere only the team can open
([`../principles/link-the-source-never-copy-it.md`](../principles/link-the-source-never-copy-it.md)).
