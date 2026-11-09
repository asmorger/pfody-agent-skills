# Publishing Adapter — Azure DevOps

Maps the portable story schema to Azure DevOps work-item fields and publishes via the `az` CLI. Field reference names, the story work-item *type*, and custom fields vary per org/project, so this adapter **resolves the field map once per project and saves it to the config**, then reuses it. Load this only when `publishing.target: azure-devops` and the user asked to publish.

## Phase 1 — Resolve the field map (detect → confirm → save)

Run this when **any** of these is true; otherwise skip straight to Phase 2:
- `publishing.fields_resolved` is missing or `false`.
- `publishing.fields_resolved_for` does not equal the current `<organization>/<project>`.
- The user asks to "re-detect fields" / "reconfigure publishing".

### 1a. Detect available work-item types and fields
Use the org/project from the config. Prefer the REST endpoints (they list *all* available fields, including custom ones, not just populated ones):

```bash
# Work-item types available in the project (finds "User Story" vs "Product Backlog Item", etc.)
az rest --method get \
  --url "{organization}/{project}/_apis/wit/workitemtypes?api-version=7.1" -o json

# Fields defined on the chosen story type (reference names + friendly names)
az rest --method get \
  --url "{organization}/{project}/_apis/wit/workitemtypes/{type}/fields?api-version=7.1" -o json
```

Fallback if `az rest` is unavailable or permissions are limited — inspect a real item of the target type to read its `.fields` reference names:
```bash
az boards work-item show --id <existing-story-id> --org {organization} -o json
```

Collect, for the story type: every field's **reference name** (e.g. `System.Title`, `Custom.BlockedReason`) and **friendly name**, and whether it is HTML/long-text (matters for Description and Acceptance Criteria).

### 1b. Match against the fields this skill needs
For each logical field below, check whether its **expected** reference name is present in the detected set:

| Logical field | Expected reference name | If missing |
|---|---|---|
| `work_item_type` | `User Story` | Prompt: pick the type that represents a user story (e.g. `Product Backlog Item`, `Issue`). |
| `title` | `System.Title` | Standard — effectively always present. If truly absent, stop and report. |
| `description` | `System.Description` | Prompt: pick the HTML/long-text field to hold the story body. |
| `acceptance_criteria` | `Microsoft.VSTS.Common.AcceptanceCriteria` | Prompt: pick an alternative field, or choose to fold AC into `description`. |
| `tags` | `System.Tags` | Standard. If absent, mark `unavailable` and skip tag application. |
| `blocked_reason` | `Custom.BlockedReason` | Optional. If absent, mark `unavailable`; do not block publishing. |

Only prompt for the fields that **don't** resolve automatically. For each unresolved field, present the detected candidate fields (filtered to sensible types — HTML/long-text for description and AC) and let the user pick one, or choose "not available → skip / fold in." Keep it to the gaps; don't re-ask what matched cleanly.

### 1c. Save the resolved map to the config
Write the confirmed values back into the config's `publishing` block and set the markers so this never re-runs unnecessarily:

```
publishing:
  target: azure-devops
  organization: {organization}
  project: {project}
  work_item_type: <resolved type>
  fields_resolved: true
  fields_resolved_for: {organization}/{project}
  field_mappings:
    title:               System.Title
    description:         System.Description
    acceptance_criteria: Microsoft.VSTS.Common.AcceptanceCriteria   # or the chosen field, or "fold-into-description"
    tags:                System.Tags                                # or "unavailable"
    blocked_reason:      Custom.BlockedReason                       # or "unavailable"
  parent_link: link each story under the provided Feature
```

Tell the user what was auto-detected vs. what they chose, and that the map is saved for future runs.

## Phase 2 — Publish using the resolved map

Use **only** the reference names from `field_mappings`. Never hardcode `Custom.BlockedReason` or assume `Microsoft.VSTS.Common.AcceptanceCriteria` — read them from the config.

### 2a0. Strip wikilink brackets (before anything else)
The story notes use wikilinks — `[[a-printed-label-may-be-voided|LABEL-2]]`, `[[order-address-frozen-on-confirmation|the address freeze]]`, `![[create-a-label-on-order-confirmation]]`. Azure
DevOps has no idea what those are and renders the brackets literally, so a reader sees a link that
goes nowhere. Before any other transformation:

| In the note | Sent to the tracker |
|---|---|
| `[[a-printed-label-may-be-voided|LABEL-2]]` | `LABEL-2` |
| `[[ORDER-1\|the address freeze]]` | `the address freeze` |
| `![[create-a-label-on-order-confirmation]]` | the embedded note's own text, inlined |

Do this **first**, because an embed pulls in text that then needs the same ASCII normalization as
everything else. A criterion's `[LABEL-2]` source tag is already a bare id and is sent verbatim.

### 2a. Normalize rich-text content to pure ASCII (mandatory)
Everything bound for a rich-text field (description, acceptance criteria, or AC folded into description) **must be pure ASCII** — printable characters 0x20–0x7E plus newlines — before it is sent. This is not stylistic. On Windows the content crosses several encoding boundaries (UTF-8 file → Git Bash → cp1252 console → `az` CLI → ADO REST), and `az` silently **discards** characters it can't map to the console codepage instead of failing (`WARNING: Unable to encode the output with cp1252 encoding. Unsupported characters are discarded.`). Corruption is intermittent — a character can survive creation and then degrade on a later update — and non-ASCII content also makes read-back verification unreliable.

Replace before sending:

| Character | Replace with |
|---|---|
| em/en dash (`—`, `–`) | `-` |
| curly quotes (`“ ” ‘ ’`) | straight `"` / `'` |
| arrows (`→ ← ⇒`) | `->`, `<-`, `=>` |
| section sign (`§8.1`) | `Section 8.1` |
| ellipsis (`…`) | `...` |
| bullet (`•`) | `-` (or a real `<li>`) |
| non-breaking space | regular space |
| multiplication sign (`×`) | `x` |
| any other non-ASCII | closest ASCII spelling |

**Do not use HTML entities as a workaround.** Sending `&mdash;` and friends does not help: ADO's rich-text sanitizer decodes entities server-side into real Unicode characters on save, so the stored value is non-ASCII again and every later read or update re-exposes it to the same hazards. The structural entities `&lt;`, `&gt;`, `&amp;`, `&quot;` remain fine — they decode to ASCII.

**Updating existing items:** if a rich-text field already contains non-ASCII characters (e.g., the item was created before this rule), normalize the **entire field** to ASCII as part of the update. Never round-trip existing non-ASCII content through `az` — that is exactly the path that corrupts it.

### 2b. Convert markdown → HTML
Azure DevOps stores markdown values in a way that forces users into "Edit markdown" mode, so convert the rich-text sections to HTML before sending. Apply HTML to the `description` and `acceptance_criteria` fields:
- `description`: `<p>` for the user-story sentence, `<p><strong>Label</strong></p>` for each section header, `<ul><li>` for bullets.
- `acceptance_criteria`: `<ol><li>` (order = priority). Keep the `AC-1 [source tag]` text in each item, so that each test still traces to its source.

If `acceptance_criteria` resolved to `fold-into-description`, append the AC as an ordered list inside the description HTML instead of a separate field.

### 2c. Create and populate
```powershell
# Create under the resolved type
# Put the US ID at the start of the title: "US-01 <title>"
az boards work-item create --type "<work_item_type>" --title "<US-ID> <title>" --org <organization> --project <project>

# Rich-text fields (use the mapped reference names)
az boards work-item update --id <id> --fields "<description_ref>=<html>"
az boards work-item update --id <id> --fields "<acceptance_criteria_ref>=<html>"   # skip if folded in

# Tags (only if tags mapping is a real field)
az boards work-item update --id <id> --fields "System.Tags=<required tags from config>; <PRD, EPIC, FEAT, and priority tags from the story>"

# Parent link under the Feature. Find the tracker ID in the PRD work item map, or ask the user. Never guess it.
az boards work-item relation add --id <id> --relation-type parent --target-id <feature-id>
```
Do **not** touch `blocked_reason` during normal creation unless the user explicitly asks.

Create an Epic or a Feature only when the user asks. Use the same title form (`EPIC-01 <name>`, `FEAT-01 <name>`), and create the parent first. Do not publish a story from an output marked `PREVIEW`. Record each new tracker ID where the user keeps the work item map.

### 2d. Verify (required before considering done)
```bash
az boards work-item show --id <id> --output json
```
Because the sent content was pure ASCII (2a), read-back through the cp1252 console is trustworthy. Two checks on the returned rich-text values:
1. **ASCII check** — scan for any character outside printable ASCII. If one appears, or `az` prints the cp1252 discard warning during read-back, something non-ASCII slipped through normalization: fix the source text and re-send the whole field.
2. **Format check** — confirm the rich-text fields report `html`, not `markdown`:
```json
{ "<description_ref>": "html", "<acceptance_criteria_ref>": "html" }
```
- If a **newly created** story reports `markdown` on a rich-text field, stop the batch immediately and report which field was affected. Do not update further rich-text fields until corrected.
- If an **existing** story was already markdown-backed and still reports `markdown` after a safe HTML update, continue and add a `Markdown` tag for later manual repair.

Also confirm `title`, description body, acceptance criteria, tags, and the parent relation all saved.

### 2e. Write the tracker ID back into the note (required)
Once an item is verified, update its note:

```yaml
status: published
tracker-id: 12345
tracker-url: https://dev.azure.com/{organization}/{project}/_workitems/edit/12345
```

This is what makes the link bidirectional: the vault can answer "which work item is this story?" and
a reviewer in ADO can get back to the sourced note. It is also how a later run knows what is already
published — a story with a `tracker-id` is not created again, it is updated. Never write these by
hand: an id that the tracker did not return is a claim that something was published when it was not.

## Batch discipline
- Normalize to pure ASCII (2a) on **every** publish and every update — including edits to items created before this rule whose stored fields still contain em-dashes or other non-ASCII characters.
- Use the validated HTML update pattern only; don't mix experimental markdown updates with production items.
- Don't update a second story's rich-text fields until the first is verified.
- Prefer separating rich-text updates from metadata updates (title, tags, state, parent, estimates) during validation.
