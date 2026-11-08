# Inline status markers

**Use when** a rule is anything other than confirmed. The Docs format carries status inside the rule
text, so the table stays two columns — which means the marker has to be unambiguous and dated.

**Skeleton.**

    no marker       ORDER-1 | A confirmed order cannot change its shipping address.

    draft           ORDER-3 | (Draft: pending operations lead confirmation as of 2026-11-08.) A
                              confirmed order may be split across parcels.

    decided clause  LABEL-1 | A label is created for the order's shipping address (confirmed
                              2026-10-02).

    open part       LABEL-2 | A printed label may be voided; who may void it is **pending final
                              operations lead confirmation** (see Q-0003).

    superseded      ORDER-5 | A split order produces one label per parcel. *(Supersedes one-label-per-
                              order; confirmed 2026-11-08.)*

    out of scope    LABEL-3 | Bulk printing is **not in Phase 1 scope**. Deferred to a future phase.

**Notes.**
- A rule with no marker is confirmed. Every other state carries a marker, and **every marker carries
  a date** ([`../principles/anchor-or-flag.md`](../principles/anchor-or-flag.md)).
- A draft names the stakeholder it is pending on. "Pending confirmation" with nobody named is not a
  marker, because nothing can close it.
- Out of scope keeps the id and rewrites the rule to say so — it is never deleted
  ([`../principles/deprecate-never-delete.md`](../principles/deprecate-never-delete.md)).
- The inline date is what points at the Source Register row that updated the rule. Add an explicit
  `SRC-…` only when two or more sources share that date
  ([`source-register-row.md`](source-register-row.md)).
- Reading an existing file, accept an em-dash or a colon after `Draft`. Write the colon form in new
  text ([`../principles/match-the-projects-voice.md`](../principles/match-the-projects-voice.md)).

**Related.** [`business-rules-file.md`](business-rules-file.md),
[`../anti-patterns/a-draft-with-no-date.md`](../anti-patterns/a-draft-with-no-date.md).
