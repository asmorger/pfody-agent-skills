# User Story Builder — Documentation

A portable Claude skill that turns **sourced project scope** into **developer-ready user stories** and, optionally, publishes them to a work tracker. Its defining principle is **factuality over completeness**: it transcribes what the sources say and refuses to invent requirements. It adapts to any project by reading a per-project **knowledge-config** rather than hardcoding any one project's sources, conventions, or tracker.

- **Skill name:** `user-story-builder`
- **Created by:** `Paul Foty`
- **Install location:** `~/.claude/skills/user-story-builder/` (user-level → available on every project)
- **Loaded file:** `SKILL.md` (everything else is loaded on demand by reference)

---

## Table of contents
1. [What it does](#1-what-it-does)
2. [Package layout](#2-package-layout)
3. [Core concepts](#3-core-concepts)
4. [The three self-provisioning loops](#4-the-three-self-provisioning-loops)
5. [Knowledge sources & the config](#5-knowledge-sources--the-config)
6. [Interaction: Anchored Knowledge skill](#6-interaction-anchored-knowledge-skill)
7. [Interaction: Azure DevOps & the Azure CLI](#7-interaction-azure-devops--the-azure-cli)
8. [The portable core (story craft)](#8-the-portable-core-story-craft)
9. [End-to-end walkthroughs](#9-end-to-end-walkthroughs)
10. [Prerequisites](#10-prerequisites)
11. [Maintenance & reconfiguration](#11-maintenance--reconfiguration)
12. [Troubleshooting](#12-troubleshooting)
13. [Extending the skill](#13-extending-the-skill)

---

## 1. What it does

Given a feature request or a body of project knowledge, the skill produces user stories in a consistent schema (`US-01` ID and title, user-story sentence, Expected Output, Details, Assumptions, Testing Strategy, Open Questions, Technical Notes, Acceptance Criteria, Tags). Every Expected Output bullet and every Acceptance Criterion must trace to a named source; anything that can't is moved to Assumptions/Open Questions or dropped.

It has two modes of use:
- **Draft** — write new stories from sources.
- **Audit** — review an existing story and flag unsourced or pattern-matched scope, without writing scope back in.

It can also **publish** finished stories to a tracker (currently an Azure DevOps adapter ships with it).

---

## 2. Package layout

```
user-story-builder/
├── SKILL.md                               # Loaded instructions: orchestration, modes, guardrails
├── README.md                              # This file
└── reference/
    ├── knowledge-config.template.md        # Per-project config schema (versioned)
    ├── portable-core.md                    # Domain-agnostic story craft + anti-inference + audit checklist
    └── adapters/
        └── azure-devops.md                 # Tracker adapter: field detection + publish + verify
```

**Why the split matters.** `SKILL.md` is the only file Claude loads up front; the `reference/` files are pulled in when relevant. This keeps the base prompt small and lets project-specific behavior live in a config instead of in the skill. The original monolithic prompt this was derived from welded three concerns together (story craft, one project's knowledge architecture, and one org's Azure DevOps mechanics); the package separates them so the craft is portable, the knowledge architecture is configured per project, and the tracker mechanics are a pluggable adapter.

---

## 3. Core concepts

### Factuality > Completeness (governing rule)
A short, sourced story beats a complete-looking story with invented requirements. This rule overrides every formatting/coverage rule: if a rule seems to demand content the source doesn't support, factuality wins.

### Anti-inference
The skill will not invent audit trails, soft delete, concurrency, validation rules, permissions, error/notification behavior, integrations, tenancy, export/reporting requirements, or "standard CRUD" expectations unless a named source states them. Pattern-matching to similar features is explicitly **not** a source.

### Source modes
The skill operates in one of three modes depending on how much sourced material exists:

| Mode | When | Citation behavior |
|------|------|-------------------|
| **A — Curated corpus** | A defined set of authoritative, ID-bearing docs exists (e.g. a `Docs/` folder with rule IDs and ADRs). | Strict: every cited ID must resolve to a real file. Optional two-tier authoritative-vs-supplemental discrepancy protocol. |
| **B — Sparse source** | A SOW, ticket, or requirements doc exists but no ID scheme. | Cite by source name/section; never invent IDs; lean harder on Assumptions/Open Questions. |
| **C — Conversational only** | The only source is the user's request. | Transcribe the request; everything beyond it becomes an Assumption or Open Question; story stays deliberately narrow. |

Factuality > Completeness governs all three.

---

## 4. The three self-provisioning loops

The skill is designed so a user never has to hand-author configuration. Three independent **detect → confirm → save** loops handle everything project-specific:

1. **Knowledge config** (§5) — on first use, discovers the project's sources, drafts a config, confirms gaps with the user, and saves it to `Knowledge/`.
2. **Tracker fields** (§7) — on first publish, scans the Azure DevOps project's work-item types and fields, prompts for anything that doesn't match expected names, and saves the resolved map back into the config.
3. **Empty-corpus handoff** (§6) — when a project has no knowledge at all, offers to delegate to the Anchored Knowledge skill to build one, then re-enters its own intake.

Each loop persists its result so it runs once, not every time.

---

## 5. Knowledge sources & the config

### The config file
- **Default path:** `Knowledge/user-story-builder.config.md`
- **Fallback path:** `.claude/user-story-builder.config.md`
- **Template/schema:** `reference/knowledge-config.template.md`
- **Version stamp:** `config_version: 1` at the top, so the skill can detect schema drift and refresh intake when the template evolves.

The `Knowledge/` location is deliberate: it's visible to a product manager who has no repository access, and it travels with the source documents.

### What the config captures
| Section | Field(s) | Purpose |
|--------|----------|---------|
| Source mode | `mode` | A / B / C (or inferred) |
| Authoritative sources | `authoritative_root`, `authoritative_sources` | The only sources citable as the record |
| Supplemental sources | `supplemental_sources` | Inform scope but not citable as record (except under the discrepancy rule) |
| ID conventions | `rule_id_scheme`, `adr_convention`, `id_rule` | How rules/decisions are referenced; "don't invent IDs" |
| Two-tier handling | `two_tier_enabled` | Whether to run the authoritative-vs-supplemental discrepancy protocol |
| Scope guards | `sow_present`, `estimate_present` | Whether a SOW / estimate exists to bound scope |
| Personas | `roles`, `pm_has_repo_access` | Project-specific role vocabulary; whether to stay business-facing |
| Codebase vocab | `entity_base_options`, `permission_model`, `tenancy_term` | House architecture terms for Technical Notes (optional) |
| Tags | `required_tags` | Tags every created story must carry (e.g. `Review Required`) |
| Design assets | `design_asset_source` | Figma/wireframe location |
| Publishing | `publishing.*` | Tracker target + resolved field map (see §7) |

### How the config drives behavior
- Missing `authoritative_sources` **and** `rule_id_scheme` ⇒ Mode B (cite by name, no IDs).
- Missing every source ⇒ Mode C (transcribe the request; the rest is Assumptions/Open Questions).
- `sow_present: false` ⇒ the skill never invokes "the SOW" as a scope guard.
- `estimate_present: false` ⇒ Assumptions are not framed as "carried from the estimate."
- Empty codebase vocabulary ⇒ Technical Notes describe behavior generically, no house base-class names.
- `publishing.target: none` ⇒ output stays as portable markdown; nothing is pushed.

### Detection & validation
- **Detect (Step 0a):** looks for the config at a user-named path, then `Knowledge/`, then `.claude/`. If found, it validates and proceeds — no re-prompting.
- **First-run intake (Step 0b–0d):** if absent, the skill scans the project (`Knowledge/`, `Docs/`, SOW, ADRs, existing stories), drafts a config, confirms only the gaps, and saves it.
- **Validate on load (Step 0e):** each run it checks that the source paths still exist. If a referenced folder/file was renamed or moved, it flags this rather than silently producing uncited stories — the worst failure mode for a factuality-first skill.

---

## 6. Interaction: Anchored Knowledge skill

The **Anchored Knowledge** skill is the *producer* of a knowledge corpus; User Story Builder is a *consumer* of it. They are a clean producer→consumer pair, coupled by **delegation, not inclusion** — User Story Builder never embeds Anchored Knowledge's content; it invokes it.

### When the handoff fires
In Step 0b-2, if discovery finds **no usable knowledge corpus** (no `Knowledge/`/`Docs/`, no SOW, no requirements docs — only raw notes or the request), the skill presents a fork:
- **Build sourced knowledge first (→ Mode A):** if an `anchored-knowledge` skill (or an equivalent "developer knowledge" builder) is available, delegate to it to stand up a proper anchored knowledge system, then re-enter Step 0 — discovery now finds the corpus and drafts a **Mode A** config.
- **Proceed now (→ Mode B/C):** skip the build and write from what exists.

The handoff is an **offer**, never forced, and only appears when the corpus is genuinely absent. If no builder skill is installed, the skill instead offers to scaffold a minimal source file and proceeds in Mode B/C.

### Why the config is the contract between them
Anchored Knowledge's outputs map directly onto User Story Builder's config fields, so no translation is needed:

| Anchored Knowledge produces | Maps to config field |
|---|---|
| Source Register + Authority Levels 1–3 (contractual, approved requirements, client clarification) | `authoritative_sources` |
| Authority Levels 4–6 (source artifacts, internal interpretation, unreviewed intake) | `supplemental_sources` |
| Stable IDs (`K-0001`, `ADR-0001`, `Q-0001`) | `rule_id_scheme`, `adr_convention` |
| Open Questions file | feeds each story's Open Questions section |
| `Confirmed` vs `Draft`/`Needs Review` status | Mode A eligibility (only anchored/Confirmed content is citable as record) |

In short: run Anchored Knowledge to reach a citable Mode A corpus; run User Story Builder to convert that corpus into stories.

---

## 7. Interaction: Azure DevOps & the Azure CLI

Publishing is handled by the adapter at `reference/adapters/azure-devops.md`, loaded only when `publishing.target: azure-devops` **and** the user explicitly asks to publish. Drafting and publishing are always separate actions — the skill never pushes to a tracker without an explicit request.

Azure DevOps varies per org/project — field reference names, custom fields (e.g. `Custom.BlockedReason`), and even the work-item *type* (`User Story` on Agile vs. `Product Backlog Item` on Scrum) all differ. So the adapter resolves the field map once, saves it, and reuses it — the same detect→confirm→save pattern as the knowledge config.

### Phase 1 — Resolve the field map (detect → confirm → save)
Runs on first publish, or whenever `publishing.fields_resolved` is false, the `<org>/<project>` changed, or the user asks to "re-detect fields."

**1a. Detect available types and fields** (via the `azure-devops` CLI extension / REST):
```bash
# Work-item types available in the project
az rest --method get \
  --url "{organization}/{project}/_apis/wit/workitemtypes?api-version=7.1" -o json

# Fields defined on the chosen story type (reference names + friendly names)
az rest --method get \
  --url "{organization}/{project}/_apis/wit/workitemtypes/{type}/fields?api-version=7.1" -o json
```
Fallback when `az rest` is unavailable or permissions are limited — read a real item's `.fields`:
```bash
az boards work-item show --id <existing-story-id> --org {organization} -o json
```

**1b. Match against needed fields.** For each logical field, check whether its expected reference name is present:

| Logical field | Expected reference name | If missing |
|---|---|---|
| `work_item_type` | `User Story` | Prompt: pick the type representing a story (e.g. `Product Backlog Item`, `Issue`). |
| `title` | `System.Title` | Standard; if truly absent, stop and report. |
| `description` | `System.Description` | Prompt: pick the HTML/long-text field for the story body. |
| `acceptance_criteria` | `Microsoft.VSTS.Common.AcceptanceCriteria` | Prompt: pick an alternative, or fold AC into `description`. |
| `tags` | `System.Tags` | Standard; if absent, mark `unavailable` and skip tags. |
| `blocked_reason` | `Custom.BlockedReason` | Optional; if absent, mark `unavailable` — never blocks publishing. |

Only the fields that don't auto-resolve are surfaced to the user, with detected candidates to choose from.

**1c. Save the resolved map** back into the config's `publishing` block, setting `fields_resolved: true` and `fields_resolved_for: <org>/<project>` so it won't re-run needlessly:
```
publishing:
  target: azure-devops
  organization: https://dev.azure.com/<org>
  project: <project>
  work_item_type: <resolved type>
  fields_resolved: true
  fields_resolved_for: <org>/<project>
  field_mappings:
    title:               System.Title
    description:         System.Description
    acceptance_criteria: Microsoft.VSTS.Common.AcceptanceCriteria   # or chosen field, or fold-into-description
    tags:                System.Tags                                # or unavailable
    blocked_reason:      Custom.BlockedReason                       # or unavailable
  parent_link: link each story under the provided Feature
```

### Phase 2 — Publish using the resolved map
Uses **only** the reference names from `field_mappings` — nothing is hardcoded.

**2a. Convert markdown → HTML first.** Azure DevOps stores markdown in a way that forces users into "Edit markdown" mode, so rich-text fields are sent as HTML:
- `description`: `<p>` for the user-story sentence, `<p><strong>Label</strong></p>` for section headers, `<ul><li>` for bullets.
- `acceptance_criteria`: `<ol><li>` (order = priority). If AC resolved to `fold-into-description`, it's appended as an ordered list inside the description HTML.

**2b. Create and populate:**
```powershell
az boards work-item create --type "<work_item_type>" --title "<title>" --org <organization> --project <project>
az boards work-item update --id <id> --fields "<description_ref>=<html>"
az boards work-item update --id <id> --fields "<acceptance_criteria_ref>=<html>"   # skip if folded in
az boards work-item update --id <id> --fields "System.Tags=<required tags>"        # if tags mapped
az boards work-item relation add --id <id> --relation-type parent --target-id <feature-id>
```
`blocked_reason` is not touched during normal creation unless explicitly requested.

**2c. Verify (required before "done"):**
```bash
az boards work-item show --id <id> --output json
```
Confirm the rich-text fields report `html`, not `markdown`:
```json
{ "<description_ref>": "html", "<acceptance_criteria_ref>": "html" }
```
- **Newly created** story reporting `markdown` on a rich-text field ⇒ stop the batch immediately and report the affected field.
- **Existing** story that was already markdown-backed and still reports `markdown` after a safe HTML update ⇒ continue and add a `Markdown` tag for later manual repair.

### Batch discipline
- Use the validated HTML update pattern only; don't mix experimental markdown updates with production items.
- Don't update a second story's rich-text fields until the first is verified.
- Prefer separating rich-text updates from metadata updates (title, tags, state, parent, estimates) during validation.

### CLI surface used
| Command | Purpose |
|---|---|
| `az rest --method get --url ".../_apis/wit/workitemtypes..."` | Detect types & fields (Phase 1a) |
| `az boards work-item show --id <id> -o json` | Fallback field inspection; verification (Phase 1a / 2c) |
| `az boards work-item create --type ... --title ...` | Create the story (Phase 2b) |
| `az boards work-item update --id <id> --fields "<ref>=<value>"` | Populate mapped fields (Phase 2b) |
| `az boards work-item relation add --id <id> --relation-type parent --target-id <feature>` | Parent link (Phase 2b) |

---

## 8. The portable core (story craft)

`reference/portable-core.md` holds the domain-agnostic craft rules, applied in Step 3. Highlights:

- **"As a / I want / So that"** discipline — specific contextual roles (from the config's `roles`), a need not a UI, and a non-circular business outcome.
- **Developer-Ready Story Standard** — every story must yield a concrete buildable output (workflow, persisted data, validation, permission, integration, or audit output); a business rule alone is not a story.
- **Expected Output** — up to 4 sourced bullets; never padded to a count.
- **Acceptance Criteria** — typically 3–7, ordered by implementation priority, each specific/testable/falsifiable, behavior-focused, and grounded. Each uses `AC-1 [source tag] Given, when, then`, and the tag is its only citation. Edge-case/validation AC only when a source specifies them.
- **Work item levels** — `EPIC-01`, `FEAT-01`, and `US-01`. Epic and Feature IDs are copied from the source and never invented.
- **Output schema** — a tracker-agnostic markdown block (§ Output Format) with all section labels preserved even when empty. Publishing adapters map these labels to tracker fields; no tracker field names appear in the core.
- **Pre-Finalization Review Checklist** — 15 pitfalls (circular "so that," vague user, untestable AC, business-rule-only story, unsourced bullet, pattern-matched scope, etc.). This same checklist powers the **audit** mode.

Wherever the core shows a `{{placeholder}}` or generic role, the skill substitutes the project's own vocabulary from the config.

---

## 9. End-to-end walkthroughs

### A. First use on a project with a knowledge base
1. User: *"Build a user story for lot eligibility from the docs."*
2. Skill finds no config → scans project → discovers `Knowledge/Docs/` with rule IDs and ADRs → drafts a **Mode A** config.
3. Confirms gaps (personas, tags, publishing target), then saves `Knowledge/user-story-builder.config.md`.
4. Writes the story from the corpus with strict citations, then returns it as portable markdown.

### B. Subsequent use
1. Skill finds the config, validates the paths still exist, and skips intake.
2. Writes/audits immediately using the saved conventions.

### C. Project with no knowledge at all
1. Discovery finds nothing citable.
2. Skill offers the **Anchored Knowledge** handoff. If accepted, that skill builds the corpus; the builder re-enters intake and lands in Mode A. If declined, it proceeds in Mode B/C from the request.

### D. Publishing to Azure DevOps
1. User: *"Publish these to our ADO project."*
2. `publishing.target` is `azure-devops` but `fields_resolved` is false → adapter scans types/fields, prompts for unmatched ones, saves the map.
3. Converts to HTML, creates the work item, links the parent, applies tags, and verifies `multilineFieldsFormat: html`.
4. Later publishes reuse the saved map and skip Phase 1.

---

## 10. Prerequisites

**For drafting/auditing:** none beyond the skill itself and readable project sources.

**For Azure DevOps publishing:**
- **Azure CLI** installed (`az`).
- **Azure DevOps extension:** `az extension add --name azure-devops`.
- **Authentication:** `az login`, or `az devops login` with a Personal Access Token (PAT) that has **Work Items (Read & Write)** scope.
- **Defaults (optional but convenient):**
  ```bash
  az devops configure --defaults organization=https://dev.azure.com/<org> project=<project>
  ```
- The org/project in the config's `publishing` block must match a project the authenticated identity can write to.

**For the Anchored Knowledge handoff:** the `anchored-knowledge` skill (or an equivalent) installed and discoverable. If absent, the skill degrades gracefully (scaffold-and-proceed).

---

## 11. Maintenance & reconfiguration

| Task | How |
|---|---|
| Re-run knowledge intake | Tell the skill to **"reconfigure"**, or delete the config file. |
| Re-detect ADO fields | Set `publishing.fields_resolved: false`, or say **"reconfigure publishing"** (e.g. after a process-template change). |
| Update source lists | Edit `authoritative_sources` / `supplemental_sources` in the config by hand. |
| Change tracker | Edit `publishing.target`; add a matching adapter under `reference/adapters/` if one doesn't exist. |
| Evolve the schema | Bump `config_version` in the template; the skill re-runs intake on projects with an older stamp. |
| Edit skill behavior | Edit the four files in place; changes take effect on the next invocation (no reload step). |

---

## 12. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Skill keeps re-asking intake | Config not saved to a detected path, or `config_version` mismatch | Confirm `Knowledge/user-story-builder.config.md` exists; check the version stamp. |
| Stories cite nothing / drop to Mode B unexpectedly | `authoritative_sources` empty or paths moved | Run validate-on-load flag; update the config's source paths. |
| ADO publish writes markdown, not HTML | Rich-text field sent as markdown | Adapter should convert first; if a **new** story shows `markdown` in `multilineFieldsFormat`, stop and report per Phase 2c. |
| `az boards` not found | DevOps extension missing | `az extension add --name azure-devops`. |
| 401 / permission errors on publish | Not authenticated, or PAT lacks Work Items write | `az login` / `az devops login`; issue a PAT with Work Items (Read & Write). |
| Field prompt appears every publish | `fields_resolved` not persisting, or org/project changed | Ensure Phase 1c wrote back to the config; verify `fields_resolved_for` matches the current org/project. |
| Custom field errors (e.g. `Custom.BlockedReason`) | Field doesn't exist in this project | Let Phase 1 mark it `unavailable`; don't hand-map it. |

---

## 13. Extending the skill

- **New tracker (Jira, GitHub, Linear):** add `reference/adapters/<target>.md` following the Azure DevOps adapter's shape — a Phase 1 field-resolution loop that saves back to the config, and a Phase 2 publish + verify. Set `publishing.target` to the new name. Until an adapter exists, the skill emits portable markdown and names the missing adapter.
- **New source authority model:** extend the config template (§ authoritative/supplemental) and bump `config_version`.
- **Different knowledge builder:** any skill that produces a sourced, ID-bearing corpus can stand in for Anchored Knowledge; the handoff wording already generalizes to "an equivalent developer-knowledge skill."

