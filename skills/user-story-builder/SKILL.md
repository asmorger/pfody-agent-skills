---
name: user-story-builder
description: >-
  Write sourced, source-traceable user stories by factually transcribing a project's scope — never inventing requirements — and optionally publish them to a work tracker (Azure DevOps, Jira, etc.). Use when the user wants to turn a knowledge base, SOW, requirements docs, or a feature request into developer-ready user stories with acceptance criteria that are grounded in named sources, or wants an existing story audited for unsourced/pattern-matched scope. Works on ANY project: it reads a per-project knowledge-config to learn where the sources live, what ID conventions exist, and where to publish. If no config exists, it degrades to sparse-source or conversational mode. Best suited when factual traceability to named sources and/or tracker publishing is the point. Trigger even if the user just says "write a story for X from these docs" or "are these AC actually sourced?"
---

# User Story Builder

Turn sourced project scope into developer-ready user stories, with **factuality over completeness** as the governing rule. A short, sourced story beats a complete-looking story with invented requirements. This skill is portable across projects — everything project-specific lives in a **knowledge-config**, not in the skill.

## Operating procedure

### Step 0 — Load or provision the project knowledge-config
Every project stores its config once and reuses it. On each invocation:

**0a. Detect.** Look for the config, in this order, and use the first found:
1. A path the user named in their request.
2. `./Knowledge/user-story-builder.config.md`  ← **primary/default location**
3. `./.claude/user-story-builder.config.md`  (fallback)

**If found:** validate it (0e), then read it fully and proceed to Step 1. Do **not** re-run intake. The only exceptions: the user explicitly asks to "reconfigure," or the config's `config_version` is older than the template's — then re-run intake to update it.

**If not found → run first-run intake (0b–0d).** Do not silently drop to a lower mode and do not invent a config; provision one with the user, once.

**0b. Discover.** Scan the project before asking anything. Look for: a `Knowledge/`, `Docs/`, or `docs/` folder; a SOW or statement-of-work document; an ADR directory; a requirements/spec doc; any existing user stories. From what you find, draft a proposed config against `reference/knowledge-config.template.md` — pre-filling source lists, likely mode, and any ID/ADR convention you can detect.

**0b-2. If no usable knowledge corpus exists — offer to build one (don't force it).** When discovery turns up no sourced knowledge base (no `Knowledge/`/`Docs/` corpus, no SOW, no requirements docs — only raw notes or the user's request), present a fork before settling for a lower mode:
- **Build sourced knowledge first (→ Mode A).** If an `anchored-knowledge` skill — or an equivalent knowledge-building / "developer knowledge" skill — is available, offer to delegate to it to stand up a proper anchored knowledge system (source register, anchored entries, IDs, open questions). When it finishes, re-enter Step 0 from 0b: discovery now finds that corpus and drafts a Mode A config whose `authoritative_sources`, `rule_id_scheme`, and `supplemental_sources` map onto what the builder produced.
- **Proceed now (→ Mode B/C).** If the user just wants a story from what exists, skip the build and continue in the appropriate lower mode.

Only surface this when the corpus is genuinely absent, and never build a knowledge system without the user's yes. If no builder skill is available, offer instead to scaffold a minimal source file and proceed in Mode B/C. This is a one-way handoff — this skill invokes the builder; it never contains it.

**0c. Confirm.** Present the draft and ask the user only about what you could not infer or must confirm: source mode (A/B/C), which sources are authoritative vs. supplemental, persona/role vocabulary, tag policy, and the publishing target. Use structured questions for the categorical choices and free text for paths/lists. Keep it short — confirm a draft, don't interrogate.

**0d. Save.** Write the finished config to `./Knowledge/user-story-builder.config.md` (create `Knowledge/` if absent, unless the user chose the `.claude/` fallback). Include the `config_version` stamp. Show the user the saved path and state that it is now reusable and hand-editable. Then continue with their original request in the same turn — intake is a means, not the deliverable.

**0e. Validate on load.** When loading an existing config, sanity-check that the source paths it names still exist. If a referenced folder/file is missing (renamed or moved), flag it to the user rather than silently citing nothing — offer to update the config.

The config supplies: source mode, source lists, ID/ADR conventions, scope-guard artifacts (SOW/estimate), persona vocabulary, codebase architecture vocabulary, tenancy term, tag policy, and the publishing target.

### Step 1 — Determine the source mode
The config declares a `mode`, or you infer it from what's actually available:

- **Mode A — Curated corpus.** A defined set of authoritative, ID-bearing source docs exists (e.g., a `Docs/` folder with rule IDs and ADRs, or an approved PRD with requirement IDs). Enforce strict citation: every cited ID must resolve to a real file; use the two-tier authoritative-vs-supplemental discrepancy protocol if the config enables it.
- **Mode B — Sparse source.** A SOW, ticket, requirements doc, or notes exist but there is no curated ID scheme. Same anti-inference discipline, but cite sources by **name/section**, never invent IDs, and lean harder on Assumptions and Open Questions.
- **Mode C — Conversational only.** The only source is the user's request. Transcribe exactly what they said; everything beyond it becomes an Assumption or Open Question, and the story stays deliberately narrow.

Factuality > Completeness governs all three modes.

### Step 2 — Gather and rank sources
Pull scope from the sources the config names. Treat authoritative sources as the source of record; treat supplemental sources as *informing* scope but not citable as record (unless the config's discrepancy rule applies). If the config marks a SOW or estimate as present, use them as the scope guard; if absent, do not reference them.

### Step 3 — Apply the portable core
Follow `reference/portable-core.md` for the story-writing craft and all anti-inference rules. That file is domain-agnostic; substitute the project's own vocabulary from the config wherever it shows a `{{placeholder}}` or a generic role.

### Step 4 — Produce the output
Emit the tracker-agnostic markdown schema defined in `reference/portable-core.md` (§ Output Format). Give each story a `US-01` ID, and tag each acceptance criterion with its source (`reference/portable-core.md` § Work Item Levels and IDs). When you write more than one story to a file, use § Backlog File Layout. Preserve every section label even when empty. Return markdown only — no commentary before or after — unless the user asked for an audit rather than a draft.

### Step 5 — Publish (only if asked and configured)
If the user wants the story pushed to a tracker AND the config names a `publishing` target, load the matching adapter under `reference/adapters/` (e.g., `azure-devops.md`). The adapter runs its own **detect → confirm → save** loop for tracker fields: on first publish (or when `fields_resolved` is false / the org·project changed), it scans the tracker for the available work-item type and fields, prompts you only for the ones that don't match the expected names, and writes the resolved map back into the config. On later runs it reuses that saved map. Then it publishes and verifies per the adapter's steps. **All content bound for tracker rich-text fields must be normalized to pure ASCII before sending** (straight quotes, `-` for dashes, `->` for arrows, "Section" for `§`) — on Windows, the encoding hops between the CLI and the tracker silently corrupt non-ASCII characters; the adapter defines the full normalization step. If no adapter matches the configured target, produce the portable markdown and tell the user which adapter is missing. **Never publish without an explicit request** — drafting and publishing are separate actions.

## Guardrails (always in force)
- **No invention.** Do not create audit trails, soft delete, concurrency, validation rules, permissions, error/notification behavior, integrations, tenancy, export/reporting requirements, or "standard CRUD" expectations unless a named source supports them. Pattern-matching to similar features is not a source.
- **Per-bullet traceability.** For every Expected Output bullet and every Acceptance Criterion, you must be able to name the specific source. If you cannot, move it to Assumptions/Open Questions or delete it.
- **Levels stay separate.** Use `EPIC-01`, `FEAT-01`, and `US-01`. Copy Epic and Feature IDs from the source. Never invent or rename them.
- **Vocabulary comes from the config, not from this skill.** Any role, entity base class, permission model, tenancy term, or ID scheme mentioned in examples here is illustrative only.
- **Mode honesty.** If you dropped to Mode B or C because sources were thin, say so and make the resulting Assumptions/Open Questions visible rather than papering the gap with plausible content.

## Auditing an existing story
When asked "is this sourced?" / "review these AC," run the Pre-Finalization Review Checklist in `reference/portable-core.md` against the story, flag each unsourced or pattern-matched bullet with the specific pitfall, and propose the corrected version (move to Assumptions/Open Questions, or delete). Do not rewrite scope in — only remove what isn't sourced and surface the gaps.
