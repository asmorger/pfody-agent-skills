# A compound statement

**Smell.** One item, one "and": "A label is created for the order's shipping address, and the
carrier's rejection reason is shown to the clerk." Often the two halves came from different turns,
sometimes from different meetings.

**Why it is wrong.** The item cannot be cited precisely, and the id is what everything downstream
cites. Status is the sharper problem: the two halves are rarely confirmed together, so whatever status
the item carries is wrong about one of them — a `confirmed` that covers a deferred behaviour, or a
`draft` that hides a settled one. The dedup suffers too. It compares statements lexically, so a
compound matches nothing cleanly, and the same rule said plainly in a later meeting becomes a second
item instead of a second source.

**Instead.** Split on "and" whenever the two clauses could be true independently, and give each its
own sources — a source supporting one half does not travel to the other. Items that genuinely always
travel together can point at each other through `related`. A subordinate clause that narrows one
behaviour — "unless the order is on hold" — is one rule, not two; the test is whether each clause
stands alone as something a test could check
([`../principles/one-rule-per-item.md`](../principles/one-rule-per-item.md)).
