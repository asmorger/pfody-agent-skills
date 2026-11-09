# Vault convention

What this skill writes: **one note per story**, in a flat `backlog/` folder, with the story's labels
as the body and everything a tracker or a query needs as frontmatter. No single backlog file.

If you have `anchored-knowledge` installed, its `references/vault-convention.md` is the canonical
contract for the shared parts: frontmatter as the query surface, wikilinks as the structure, the
callout vocabulary, the MOC's `<!-- generated -->` markers. If you have `agentic-prd` installed,
these are **the same story notes it writes** — same folder, same type, same properties. The two
skills differ in what they take as input, not in what they emit.

**Every type, id pattern, status vocabulary and grouping key in this file is declared once in**
[`vault-taxonomy.json`](vault-taxonomy.json), which this skill's scripts read and which the repo's
`check-taxonomy.py` compares against this file, against every skeleton in `patterns/`, and against
the worked example. The copy here is byte-identical to the repo's canonical one, so the skill still
installs on its own. Before it existed the same three shared types carried two id widths and two
status casings across two skills, each documented in prose, each checker seeing only its own.

That is also what makes the sentence above checkable rather than hopeful: a story is
`type: user-story`, `status: draft | ready | published | retired`, `id: US-NN` and a `topic`
whichever skill wrote it, and `check-taxonomy.py` fails if the two skills' worked examples disagree.
**Where a story and the requirement it covers want the same title, the story takes the `-story`
suffix** — `backlog/void-a-printed-label-story.md` beside `requirements/void-a-printed-label.md` —
because the file name is the link target and the record layer keeps the plain one (section 3 of
`anchored-knowledge`'s convention).


## 1. Folder map

    <stories_dir>/                     default `docs/backlog/`
      <kebab-title>.md                 one note per story, Epic and Feature; level in `type`
    <docs_dir>/moc/backlog.md          the index: prose, a Bases embed, a generated table
    <docs_dir>/bases/backlog.base      the Bases definition the MOC embeds

Every path is declared in the config and the config wins. A project with no vault at all still gets
notes; it just gets them wherever its config says
([`../patterns/knowledge-config.md`](../patterns/knowledge-config.md)).

**The index's table is generated, and it says so.** `story.py moc` rewrites the block between the
`<!-- generated -->` markers from the story notes' front matter and stamps `generator`,
`generated`, `input-paths`, `input-manifest-sha256` and `managed-block-sha256`, so "is this index
current?" has a mechanical answer and a hand edit between the markers is reported rather than
thrown away. `moc/backlog.md` used to be the one generated block in the repo with no generator
behind it: this skill wrote the table by hand while the repo's own rule said a generated note
carries its provenance.

**`agentic-prd` can own that same file**, because it writes story notes too when a whole backlog is
decomposed at once. Both generators read the `snapshot` spec from the note and produce the same
block byte for byte, so a project with both installed does not get a different index depending on
which tool ran last — the repo's `check-vault-tools.py` asserts each one reports the other's block
as current. Outside a `user-story` snapshot each keeps its own: `story.py moc` leaves the coverage
table and the grouped requirement views alone and says which generator owns them.

## 2. The story note

```markdown
---
id: US-03
aliases: [US-03]
type: user-story
status: draft                  # draft | ready | published | retired
topic: labels
parent: "[[void-a-label|FEAT-02]]"          # the Feature; copied, never invented
source-mode: A                 # A | B | C — and the note says so when it is not A
sources: ["[[a-printed-label-may-be-voided|LABEL-2]]", "[[bulk-printing-across-orders|LABEL-3]]", "[[enforce-credit-hold-at-label-creation|ADR-0004]]"]
requirements: []               # R- ids when built from a PRD
testing-complexity: Medium     # High | Medium | Low
tracker-id:                    # filled by the publish step, never by hand
tracker-url:
created: 2026-11-08
updated: 2026-11-08
review-required: true
---

# US-03 — Void a printed label

As a shipping clerk, I want to void a label I have already printed, so that a cancelled order is not
collected by the carrier.

**Expected Output** · **Details** · **Assumptions** · **Testing Strategy** · **Open Questions** ·
**Technical Notes** · **Acceptance Criteria**
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
in `aliases` too, so searching the id finds the story however the title is later reworded — the id is
what was cited, not the wording.

Cite a story as `[[void-a-printed-label|US-03]]`: the filename is the link target and the id is the
display text. A bare `[[void-a-printed-label-story|US-03]]` resolves to nothing, because Obsidian matches a wikilink against
filenames and paths and never against `aliases`.

A story's id is unique across the backlog. An Epic or a Feature is a note of the same shape with
`type: epic` or `type: feature`, written only when the source has one.

## 4. Publishing writes back

After a successful publish, the note gains `tracker-id` and `tracker-url` and `status: published`.
That is what makes the link bidirectional: the vault can answer "which tracker item is this story?"
and a reviewer can get from the tracker back to the sourced note. Never fill them by hand — an id
that was not returned by the tracker is a claim that something was published when it was not
([`../practices/publish-to-a-tracker.md`](../practices/publish-to-a-tracker.md)).

**Wikilinks do not survive the trip.** Before converting to the tracker's markup, strip the brackets:
`[[a-printed-label-may-be-voided|LABEL-2]]` becomes `LABEL-2`, and `[[order-address-frozen-on-confirmation|the address freeze]]` becomes `the address freeze`.
A tracker that renders `[[a-printed-label-may-be-voided|LABEL-2]]` literally is showing a reader a link that goes nowhere, and the
ASCII normalisation runs after this, not before
([`../principles/tracker-text-is-ascii.md`](../principles/tracker-text-is-ascii.md)).

## 5. Status and mode honesty

`status: draft` until a person has read it; `ready` once they have; `published` only after the
tracker returned an id. `source-mode` records which mode produced it, so a Mode B or Mode C story is
visibly not Mode A in every view — not only in the sentence that announced it at the time
([`../principles/mode-honesty.md`](../principles/mode-honesty.md)).

A story needing review carries `review-required: true` — a property, not a tag, so it is read by
the same query surface as everything else and cannot drift from a second copy. It is what makes
"what still needs a person?" a query rather than a reading job.
