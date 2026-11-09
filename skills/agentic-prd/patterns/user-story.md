# User story note

**Use when** writing any story. One note per story in `backlog/`. Every label appears, in this
order, even when a section is empty — `- None identified`. The check reports a missing label.

**Skeleton.** `backlog/void-a-printed-label.md`

```markdown
---
id: US-03
aliases: [US-03]
type: user-story
status: accepted
prd: "[[PRD-001]]"
parent: "[[FEAT-02]]"
requirements: ["[[R-012]]", "[[X-002]]"]
testing-complexity: Medium
tags: [backlog/user-story]
---

# US-03 — Void a printed label

As a shipping clerk, I want to void a label I have already printed, so that a cancelled order is not
collected by the carrier.

**Expected Output**
- A clerk can void a printed label from the order screen.
- The order returns to the unlabelled state and can be labelled again.

**Details**
- Source grounding: [[R-012]], [[X-002]]. A label may be voided only until collection.

**Assumptions** · **Testing Strategy** · **Open Questions** · **Technical Notes**
- `- None identified.` where a section is empty; Testing Complexity and a UAT approach; [[Q-03]]
  under Open Questions; permission, feature flag and design assets under Technical Notes.

**Acceptance Criteria**
1. AC-1 [R-012] Given a printed label on an uncollected parcel, when an authorised user voids it,
   then the order returns to the unlabelled state.
2. AC-2 [X-002] Given any label action, when it completes, then the order records the acting user
   and a timestamp.

**Tags**
- EPIC-01, FEAT-02
```

Each label is its own `**Label**` line in a real note; four are run together above only to keep this
skeleton short.

**Notes.**
- **`parent` and `requirements` are the traceability**, not the heading level. Every requirement a
  story covers must belong to its parent Feature or be cross-cutting; the check enforces it
  ([`backlog-notes.md`](backlog-notes.md)).
- A criterion's `[R-012]` tag is read by the check and must name a real requirement note. One tag per
  criterion; nothing else ([`acceptance-criterion.md`](acceptance-criterion.md)).
- A publishing adapter maps these labels to tracker fields; do not embed tracker field names here
  ([`tracker-item.md`](tracker-item.md)). While the PRD is not `Accepted`, the note says `PREVIEW` in
  its first lines ([`../principles/only-a-person-crosses-a-gate.md`](../principles/only-a-person-crosses-a-gate.md)).

**Related.** [`requirement-note.md`](requirement-note.md), [`coverage-moc.md`](coverage-moc.md).
