# Vault convention

What this skill writes: **one note per story**, in a flat `backlog/` folder, with the story's labels
as the body and everything a tracker or a query needs as frontmatter. No single backlog file.

If you have `anchored-knowledge` installed, its `references/vault-convention.md` is the canonical
contract for the shared parts: frontmatter as the query surface, wikilinks as the structure, the
callout vocabulary, the MOC's `<!-- generated -->` markers. If you have `agentic-prd` installed,
these are **the same story notes it writes** — same folder, same type, same properties. The two
skills differ in what they take as input, not in what they emit.

## 1. Folder map

    <stories_dir>/                     default `docs/backlog/`
      <kebab-title>.md                 one note per story, Epic and Feature; level in `type`
    <docs_dir>/moc/backlog.md          the index: prose, a Bases embed, a generated table
    <docs_dir>/bases/backlog.base      the Bases definition the MOC embeds

Every path is declared in the config and the config wins. A project with no vault at all still gets
notes; it just gets them wherever its config says
([`../patterns/knowledge-config.md`](../patterns/knowledge-config.md)).

## 2. The story note

```markdown
---
id: US-03
aliases: [US-03]
type: user-story
status: draft                  # draft | ready | published
parent: "[[FEAT-02]]"          # the Feature; copied, never invented
source-mode: A                 # A | B | C — and the note says so when it is not A
sources: ["[[LABEL-2]]", "[[LABEL-3]]", "[[ADR-0004]]"]
requirements: []               # R- ids when built from a PRD
testing-complexity: Medium     # High | Medium | Low
tracker-id:                    # filled by the publish step, never by hand
tracker-url:
created: 2026-11-08
updated: 2026-11-08
tags: [backlog/user-story, review-required]
---

# US-03 — Void a printed label

As a shipping clerk, I want to void a label I have already printed, so that a cancelled order is not
collected by the carrier.

**Expected Output** · **Details** · **Assumptions** · **Testing Strategy** · **Open Questions** ·
**Technical Notes** · **Acceptance Criteria** · **Tags**
```

Every label appears, in that order, each as its own `**Label**` line, even when empty —
`- None identified`. The labels are the publishing contract: an adapter maps them to tracker fields,
and no tracker field name appears in the note
([`../patterns/user-story.md`](../patterns/user-story.md)).

**`sources` is the property, and `Source grounding:` under Details is the sentence a reader sees.**
They say the same thing on purpose: one is for queries and the publish step, the other is what lands
in the tracker's description. That is the only duplication the shape allows, and the audit checks
they agree ([`../principles/cite-once-per-story.md`](../principles/cite-once-per-story.md)).

## 3. Ids and parents

`parent` is a wikilink to the Feature, copied from the source and never invented
([`../anti-patterns/an-invented-parent-id.md`](../anti-patterns/an-invented-parent-id.md)). `id` goes
in `aliases` too, so `[[US-03]]` resolves however the title is later reworded — the id is what was
cited, not the wording.

A story's id is unique across the backlog. An Epic or a Feature is a note of the same shape with
`type: epic` or `type: feature`, written only when the source has one.

## 4. Publishing writes back

After a successful publish, the note gains `tracker-id` and `tracker-url` and `status: published`.
That is what makes the link bidirectional: the vault can answer "which tracker item is this story?"
and a reviewer can get from the tracker back to the sourced note. Never fill them by hand — an id
that was not returned by the tracker is a claim that something was published when it was not
([`../practices/publish-to-a-tracker.md`](../practices/publish-to-a-tracker.md)).

**Wikilinks do not survive the trip.** Before converting to the tracker's markup, strip the brackets:
`[[LABEL-2]]` becomes `LABEL-2`, and `[[ORDER-1|the address freeze]]` becomes `the address freeze`.
A tracker that renders `[[LABEL-2]]` literally is showing a reader a link that goes nowhere, and the
ASCII normalisation runs after this, not before
([`../principles/tracker-text-is-ascii.md`](../principles/tracker-text-is-ascii.md)).

## 5. Status and mode honesty

`status: draft` until a person has read it; `ready` once they have; `published` only after the
tracker returned an id. `source-mode` records which mode produced it, so a Mode B or Mode C story is
visibly not Mode A in every view — not only in the sentence that announced it at the time
([`../principles/mode-honesty.md`](../principles/mode-honesty.md)).

A story needing review carries a `review-required` tag, which is what makes "what still needs a
person?" a query rather than a reading job.
