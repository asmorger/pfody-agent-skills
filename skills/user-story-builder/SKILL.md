---
name: user-story-builder
description: >
  Write developer-ready user stories by factually transcribing sourced scope — never inventing
  requirements — and optionally publish them to a work tracker such as Azure DevOps or Jira. Use it
  whenever a knowledge base, SOW, requirements document, accepted PRD or feature request must become
  stories with acceptance criteria grounded in named sources; whenever an existing story needs
  auditing for unsourced or pattern-matched scope; whenever stories must be pushed to a tracker with
  their parents and tags intact; and whenever someone asks "are these acceptance criteria actually
  sourced?" Works on any project: a per-project config declares where the sources live, what id
  conventions exist and where to publish, and the skill degrades honestly to sparse-source or
  conversational mode when little exists. Not for writing the PRD itself, which `agentic-prd` does,
  and not for building the knowledge base, which `anchored-knowledge` does.
---

# user-story-builder

Sourced scope in, developer-ready stories out. The governing rule is **factuality over
completeness**: a short, sourced story beats a complete-looking story with invented requirements, and
every other rule here yields to it.

This skill is portable. Nothing project-specific lives in it — roles, id schemes, tenancy terms,
permission models, source locations and the publishing target all live in a per-project config that
the skill provisions once and reuses. Three **detect → confirm → save** loops keep it that way: the
knowledge config, the tracker field map, and the handoff when a project has no knowledge corpus at
all. Each persists its result, so each runs once rather than every time.

## How to use this skill

Run [`practices/load-or-provision-the-config.md`](practices/load-or-provision-the-config.md) first,
every time. Then find your task below and read only the files it names — each is short and
self-contained. The story craft itself lives in
[`references/portable-core.md`](references/portable-core.md), which the patterns point into.

## Non-negotiables

1. Factuality over completeness. A rule that seems to demand unsourced content loses to this one → `principles/factuality-over-completeness.md`
2. Pattern-matching to similar features is not a source → `principles/pattern-matching-is-not-a-source.md`
3. Every Expected Output bullet and every criterion can be traced to a named source, or it is moved → `principles/per-bullet-traceability.md`
4. A gap has three options — assumption, open question, omit. There is no fourth → `principles/a-gap-has-three-options.md`
5. Cite once per story; the criterion's source tag is the only other citation → `principles/cite-once-per-story.md`
6. A story produces something buildable, demonstrable and refusable → `principles/a-story-produces-something-buildable.md`
7. Each level has one name and one id format; copy parent ids, never invent them → `principles/one-name-and-one-id-per-level.md`
8. Vocabulary comes from the config, never from this skill's examples → `principles/vocabulary-comes-from-the-config.md`
9. Say when you dropped to a lower source mode, and show what it cost → `principles/mode-honesty.md`
10. Detect, confirm, save — once. Never re-run intake on a configured project → `principles/detect-confirm-save.md`
11. Drafting and publishing are separate actions; never publish unasked → `principles/drafting-and-publishing-are-separate.md`
12. All tracker rich-text is normalised to pure ASCII before sending → `principles/tracker-text-is-ascii.md`
13. Delegate to the knowledge builder; never embed its work here → `principles/delegation-not-inclusion.md`

## Task → read

| You are… | Read |
|---|---|
| Starting any run | `practices/load-or-provision-the-config.md`, `patterns/knowledge-config.md` |
| Finding a project with no sourced knowledge at all | `practices/offer-to-build-knowledge-first.md` |
| Working out which source mode applies | `practices/determine-the-source-mode.md` |
| Ranking authoritative against supplemental sources | `practices/gather-and-rank-sources.md` |
| Writing a story | `practices/write-a-story.md`, `patterns/user-story.md` |
| Writing the *As a / I want / So that* sentence | `patterns/as-a-i-want-so-that.md` |
| Writing Expected Output or Technical Notes | `patterns/expected-output.md`, `patterns/technical-notes.md` |
| Writing or citing acceptance criteria | `patterns/acceptance-criterion.md`, `patterns/source-tag.md` |
| Deciding how many stories a Feature needs | `practices/slice-a-feature-into-stories.md` |
| Working from an accepted PRD | `practices/build-from-a-prd.md` |
| Writing more than one story to a file | `patterns/backlog-file.md` |
| Auditing a story — "are these criteria sourced?" | `practices/review-an-existing-story.md` |
| Publishing to a tracker | `practices/publish-to-a-tracker.md`, `references/adapters/azure-devops.md` |
| Publishing for the first time, or to a new project | `practices/resolve-the-tracker-fields.md`, `patterns/tracker-field-map.md` |
| Adding support for a tracker with no adapter | `practices/add-a-tracker-adapter.md` |
| Looking at a failed publish or a surprising run | `practices/diagnose-a-failed-run.md` |
| Reviewing a story, or your own draft | `anti-patterns/` — scan the names; open what matches |

## Folders

    principles/     the rules and why each one holds
    patterns/       the shapes, as fill-in skeletons (neutral Order / shipping-label domain)
    practices/      step-by-step procedures with a done-when checklist
    anti-patterns/  stories that fail — what they look like, why, what to do instead
    references/     the portable core, the config template, and one adapter per tracker
    evals/          prompts that should and should not load this skill

## Conventions this skill assumes

    Knowledge/user-story-builder.config.md     the per-project config — primary location
    .claude/user-story-builder.config.md       fallback, when the project has no Knowledge folder

Everything else — source paths, id schemes, roles, tenancy term, tags, publishing target — is
declared in that config and the config wins. Publishing to Azure DevOps needs `az` with the
`azure-devops` extension.

## Related skills

`anchored-knowledge` produces the corpus this skill consumes; they are a producer–consumer pair
coupled by delegation. `agentic-prd` writes the PRD whose requirement ids become Mode A rule ids
here, and owns the decomposition when the whole backlog is generated at once.
