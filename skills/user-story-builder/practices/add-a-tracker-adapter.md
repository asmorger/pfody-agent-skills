# Add a tracker adapter

**When** the configured publishing target has no adapter — Jira, GitHub, Linear — and the user wants
publishing to work.

**Why.** The portable markdown is deliberately tracker-agnostic, so adding a target is a new file
rather than a change to the story craft. Keeping it that way is what stops tracker field names leaking
into the stories themselves.

**Steps.**

1. **Until the adapter exists, do not improvise.** Emit the portable markdown and name the missing
   adapter ([`../principles/drafting-and-publishing-are-separate.md`](../principles/drafting-and-publishing-are-separate.md)).
2. **Create `references/adapters/<target>.md`**, following the Azure DevOps adapter's shape
   ([`../references/adapters/azure-devops.md`](../references/adapters/azure-devops.md)).
3. **Write phase 1 — field resolution.** Detect the available item types and fields, confirm only
   what did not match, and save the resolved map back into the config with `fields_resolved_for`
   ([`resolve-the-tracker-fields.md`](resolve-the-tracker-fields.md)).
4. **Write phase 2 — publish and verify.** Normalise rich text to ASCII, convert the markdown to the
   tracker's markup, create parents before children, open each title with its level id, apply the
   tags, link the parent, then read the items back
   ([`publish-to-a-tracker.md`](publish-to-a-tracker.md)).
5. **Define the batch discipline** explicitly: how many creates at once, and what happens on a
   partial failure.
6. **Map this skill's markdown labels to the target's fields in the adapter**, never in the story
   ([`../patterns/user-story.md`](../patterns/user-story.md)).
7. **Set `publishing.target`** in the config to the new name.
8. **Bump `config_version`** if the adapter needed new config fields, so existing projects re-run
   intake to pick them up.

**Done when** the adapter has both phases, resolves and saves its own field map, normalises and
verifies, names its batch discipline, and the stories themselves still contain no tracker field names.
