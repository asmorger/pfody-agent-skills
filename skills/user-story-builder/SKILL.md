---
name: user-story-builder
description: >
  Write developer-ready user stories as Obsidian notes — one small linked note per story, with its
  id, parent, sources and tracker id in front matter — by factually transcribing sourced scope, never
  inventing requirements, and optionally publish them to a work tracker such as Azure DevOps or Jira.
  Use it whenever a knowledge base, SOW, requirements document, accepted PRD or feature request must
  become stories with acceptance criteria grounded in named sources; whenever an existing story needs
  auditing for unsourced or pattern-matched scope; whenever stories must be pushed to a tracker with
  their parents and tags intact; and whenever someone asks "are these acceptance criteria actually
  sourced?" Works on any project: a per-project config says where the sources live, what id
  conventions exist and where to publish, and the skill degrades honestly to sparse-source or
  conversational mode. Not for the PRD itself, which `agentic-prd` does, nor for the knowledge base,
  which `anchored-knowledge` does.
allowed-tools: Read, Write, Edit, Glob, Grep, Skill, Bash(python3 *), Bash(az *)
metadata:
  requires: []
  related: [anchored-knowledge, agentic-prd]
---

# user-story-builder

Sourced scope in, developer-ready stories out. The governing rule is **factuality over
completeness**: a short, sourced story beats a complete-looking story with invented requirements, and
every other rule here yields to it.

The output is **one note per story**, in a flat folder, with the labels as the body and everything a
tracker or a query needs in front matter — including the `tracker-id` the publish step writes back,
which is what makes the vault and the tracker point at each other
([`references/vault-convention.md`](references/vault-convention.md)).

This skill is portable. Roles, id schemes, tenancy terms, permission models, source locations, the
vault's folders and the publishing target all live in a per-project config the skill provisions once
and reuses. Three **detect → confirm → save** loops keep it that way: the knowledge config, the
tracker field map, and the handoff when a project has no corpus at all.

## How to use this skill

Run [`practices/load-or-provision-the-config.md`](practices/load-or-provision-the-config.md) first,
every time. Then find your task below and read only the files it names. The story craft itself lives
in [`references/portable-core.md`](references/portable-core.md), which the patterns point into.

## Non-negotiables

1. Factuality over completeness. A rule that seems to demand unsourced content loses to this one → `principles/factuality-over-completeness.md`
2. Pattern-matching to similar features is not a source → `principles/pattern-matching-is-not-a-source.md`
3. Every Expected Output bullet and every criterion traces to a named source, or it is moved → `principles/per-bullet-traceability.md`
4. A gap has three options — assumption, open question, omit. There is no fourth → `principles/a-gap-has-three-options.md`
5. Cite once per story; the criterion's source tag is the only other citation → `principles/cite-once-per-story.md`
6. A story produces something buildable, demonstrable and refusable → `principles/a-story-produces-something-buildable.md`
7. Each level has one name and one id format; `parent` is copied, never invented → `principles/one-name-and-one-id-per-level.md`
8. Vocabulary comes from the config, never from this skill's examples → `principles/vocabulary-comes-from-the-config.md`
9. Say when you dropped to a lower source mode, and record it in `source-mode` → `principles/mode-honesty.md`
10. Detect, confirm, save — once. Never re-run intake on a configured project → `principles/detect-confirm-save.md`
11. Drafting and publishing are separate; never publish unasked, and strip wikilink brackets before normalising tracker text to ASCII → `principles/drafting-and-publishing-are-separate.md`, `principles/tracker-text-is-ascii.md`
12. Delegate to the knowledge builder; never embed its work here → `principles/delegation-not-inclusion.md`

## Task → read

| You are… | Read |
|---|---|
| Starting any run | `practices/load-or-provision-the-config.md`, `patterns/knowledge-config.md` |
| Writing your first note, or checking a note's shape | `references/vault-convention.md` |
| A project with no sourced knowledge at all | `practices/offer-to-build-knowledge-first.md` |
| Working out which source mode applies, and ranking the sources | `practices/determine-the-source-mode.md`, `practices/gather-and-rank-sources.md` |
| Writing a story | `practices/write-a-story.md`, `patterns/user-story.md` |
| Writing the *As a / I want / So that* sentence, Expected Output or Technical Notes | `patterns/as-a-i-want-so-that.md`, `patterns/expected-output.md`, `patterns/technical-notes.md` |
| Writing or citing acceptance criteria | `patterns/acceptance-criterion.md`, `patterns/source-tag.md` |
| Deciding how many stories a Feature needs | `practices/slice-a-feature-into-stories.md` |
| Working from an accepted PRD | `practices/build-from-a-prd.md` |
| Writing more than one story | `patterns/backlog-notes.md` |
| Auditing a story — "are these criteria sourced?" | `practices/review-an-existing-story.md` |
| Publishing to a tracker | `practices/publish-to-a-tracker.md`, `references/adapters/azure-devops.md` |
| Publishing for the first time, or adding a tracker with no adapter | `practices/resolve-the-tracker-fields.md`, `patterns/tracker-field-map.md`, `practices/add-a-tracker-adapter.md` |
| Running the checks on a backlog, or regenerating its index | `practices/run-the-checks.md` |
| Looking at a failed publish or a surprising run | `practices/diagnose-a-failed-run.md` |
| Reviewing a story, or your own draft | `anti-patterns/` — scan the names; open what matches |

## Folders

    principles/     the rules and why each one holds
    patterns/       the note shapes, as fill-in skeletons (neutral Order / shipping-label domain)
    practices/      step-by-step procedures with a done-when checklist
    anti-patterns/  stories that fail — what they look like, why, what to do instead
    references/     the portable core, the vault convention, the config template, the adapters
    scripts/        `story.py check`, `story.py moc` — the backlog's checker and its index
    examples/ evals/   a Mode A and a Mode C story in a vault, and the trigger prompts

## Conventions this skill assumes

    Knowledge/user-story-builder.config.md   the per-project config · `.claude/…` as fallback
    docs/backlog/<kebab-title>.md            one note per story; `stories_dir` in the config
    docs/moc/backlog.md                      the index, when there is more than one story

Everything else — source paths, id schemes, roles, tenancy term, the vault's folders and property
names, the publishing target — is declared in that config and the config wins. `story.py` needs
Python 3.10+; publishing to Azure DevOps needs `az` with the `azure-devops` extension; the MOC's
Bases embed needs Obsidian 1.9+, and a vault without it reads the generated snapshot.

## Related skills

`anchored-knowledge` produces the corpus this skill consumes; they are a producer–consumer pair
coupled by delegation. `agentic-prd` writes the PRD whose requirement ids become Mode A rule ids
here, and owns the decomposition — and the coverage table — when the whole backlog is generated at
once. Where it is installed, these are **the same story notes it writes**: same folder, same type,
same properties. The two skills differ in what they take as input, not in what they emit.
