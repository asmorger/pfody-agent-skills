# One rule per item

**Rule.** Keep statements atomic. One item, one rule. A statement joining two behaviours with "and"
is two items, each with its own id, status and sources.

**Why.** The id is what everything downstream cites, and a compound item cannot be cited precisely:
half of it may be confirmed and half deferred, so any status the item carries is wrong about one
half. Deduplication suffers too — the merge compares statements lexically, so a compound statement
matches nothing cleanly and the same rule said plainly in another meeting becomes a second item
instead of a second source. Splitting costs one line and makes both halves mergeable, citable and
individually falsifiable.

**In the index.**
- Split on "and" whenever the two clauses could be true independently.
- Each half keeps the sources that support it. A source supporting only one half does not travel to
  the other ([`every-item-carries-a-source.md`](every-item-carries-a-source.md)).
- Two items that genuinely always travel together can cross-reference through `related`.
- A statement needing a subordinate clause to be true — "unless the order is on hold" — is usually one
  rule, not two. The test is whether each clause stands as a sentence a test could check.
- Atomic items are what let one topic's rules be read as a list in the rendered table
  ([`../patterns/rendered-index.md`](../patterns/rendered-index.md)).

**Breaks when.** Two behaviours share an item →
[`../anti-patterns/a-compound-statement.md`](../anti-patterns/a-compound-statement.md).
