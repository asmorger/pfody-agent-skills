# Tracker item

**Use when** publishing an approved backlog. The shape of what gets created, so a person can trace
any item back to the requirement that caused it.

**Skeleton.**

    Epic         EPIC-01 Shipping labels at order processing        tag: PRD-001
      Feature    FEAT-01 Create and print a label                   tag: PRD-001
        Story    US-01 Create a label for a confirmed order         tag: PRD-001, P0
        Story    US-02 Reprint a damaged label                      tag: PRD-001, P1
      Feature    FEAT-02 Void a label                                tag: PRD-001
        Story    US-03 Void a printed label                          tag: PRD-001, P0

The story's description carries the backlog's story body verbatim: the *As a* sentence, Expected
Output, Details, Assumptions, Testing Strategy, Open Questions, Technical Notes, Acceptance Criteria,
Tags.

**Notes.**
- The level id opens the title, so the tracker and the backlog can be read against each other with
  no lookup. The `PRD-NNN` id is a tag, so every item of a PRD can be listed at once.
- Parents before children: Epic, then Feature, then Story. A child created first has nowhere to hang.
- Read the organisation and project from the tool's own configuration — `az devops configure -l` for
  Azure DevOps. Never assume a project.
- Normalise tracker text to plain ASCII: straight quotes, `-` for dashes, `->` for arrows, "Section"
  for `§`. On Windows the encoding hops between the CLI and the tracker corrupt the rest silently.
- Read the created items back and record their ids in the PRD's work item map. An unverified create
  is a report, not a fact.
- Nothing is created without an explicit yes in the current conversation
  ([`../principles/only-a-person-crosses-a-gate.md`](../principles/only-a-person-crosses-a-gate.md)).

**Related.** [`backlog-notes.md`](backlog-notes.md),
[`../practices/publish-a-backlog.md`](../practices/publish-a-backlog.md),
[`../anti-patterns/publishing-without-a-yes.md`](../anti-patterns/publishing-without-a-yes.md).
