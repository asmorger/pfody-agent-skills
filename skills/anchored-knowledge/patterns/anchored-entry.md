# Anchored entry

**Use when** a citable fact is not a business rule — a constraint, a requirement detail, a measured
characteristic of the current system. Optional: most bases never need it, and a fact that could be a
rule should be one.

**Skeleton.**

```markdown
## K-0001 - The carrier truncates address line 1 at 35 characters

**Status:** Draft | Confirmed | Needs Review | Superseded | Rejected | Scope Watch
**Type:** Fact | Requirement Detail | Assumption | Constraint
**Confidence:** Low | Medium | High
**Owner:** <role>
**Captured:** 2026-11-08
**Last reviewed:** 2026-11-08
**Applies to:** Label creation
**Anchors:** SRC-0006 carrier API reference p.12
**Related:** LABEL-1, order-data-mapping.md

**Statement**
The carrier silently truncates `AddressLine1` at 35 characters; longer values are accepted and
shortened without an error.

**Implications**
- A label can be created with a wrong address and no failure, so truncation must be caught before the
  request.

**History**
- <YYYY-MM-DD: CH-NNNN refined this because newer source X clarified Y. Prior anchor SRC-NNNN.>
```

**Notes.**
- Use it for facts about the world that rules depend on, where turning the fact into a rule would
  state a behaviour nobody decided.
- `Confidence` is not a substitute for a status marker. A low-confidence fact is still `Draft` or
  `Needs Review` ([`../principles/anchor-or-flag.md`](../principles/anchor-or-flag.md)).
- *Implications* is what makes the entry worth keeping. A fact with no implications is a note.
- `K-NNNN` entries are Reference Layer and citable; they carry a `Status:` field rather than inline
  markers, because they are not table rows.
- If two entries start overlapping, one of them wanted to be a rule
  ([`../principles/one-home-per-fact.md`](../principles/one-home-per-fact.md)).

**Related.** [`business-rules-file.md`](business-rules-file.md), [`convention-doc.md`](convention-doc.md).
