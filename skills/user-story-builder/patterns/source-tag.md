# Source tag

**Use when** citing a criterion. The form depends on the source mode, and the mode is declared in the
config.

**Skeleton.**

    Mode A   a rule id from an authoritative source
             AC-1 [LABEL-2] Given a printed label, when a clerk voids it, then …
             AC-2 [ADR-0004] Given an order on credit hold, when a clerk requests a label, then …

    Mode B   the source name and section — never an invented id
             AC-1 [SOW 3.2] Given a confirmed order, when a clerk requests a label, then …
             AC-2 [Carrier integration notes, p.4] Given a rejected address, when …, then …

    Mode C   the user's request
             AC-1 [Request] Given a printed label, when a clerk voids it, then …

    From a PRD, one PRD in play     [R-001]
    From a PRD, several in play     [PRD-001 R-001]

**Notes.**
- One tag per criterion and **nothing else in it**. No ADR plus rule plus file
  ([`../principles/cite-once-per-story.md`](../principles/cite-once-per-story.md)).
- Mode A: only authoritative ids are legal as source of record. A supplemental id may appear solely
  under the config's discrepancy protocol
  ([`../practices/gather-and-rank-sources.md`](../practices/gather-and-rank-sources.md)).
- Mode B: **never invent an id scheme.** A name and a section is a complete citation.
- Mode C: do not attach source ids at all — there are none to attach.
- Every Mode A id must resolve to a real file. An id that does not is an audit finding, not a typo to
  leave in place ([`../practices/diagnose-a-failed-run.md`](../practices/diagnose-a-failed-run.md)).
- A tracker number is not a source tag.

**Related.** [`acceptance-criterion.md`](acceptance-criterion.md), [`knowledge-config.md`](knowledge-config.md).
