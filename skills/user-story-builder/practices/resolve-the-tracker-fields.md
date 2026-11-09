# Resolve the tracker fields

**When** publishing for the first time, when `fields_resolved` is false, or when the org or project
has changed. The adapter's phase 1 — detect, confirm, save.

**Why.** Work-item types and field names differ per process template and per project: "User Story"
against "Product Backlog Item", a custom acceptance field, a missing one. Guessing produces a publish
that half-works, and the half that failed is silent.

**Steps.**

1. **Read the target from the tool's own configuration** — `az devops configure -l` for Azure DevOps.
   **Never assume an organisation or a project**
   ([`../patterns/tracker-field-map.md`](../patterns/tracker-field-map.md)).
2. **Detect the available work-item types** in the project, so you pick the one that exists rather
   than the one you expected.
3. **Detect the fields** defined on that type — reference names and friendly names both.
4. **Match them against what this skill needs**: title, description, acceptance criteria, tags, and
   any the config adds. Follow the adapter's matching table
   ([`../references/adapters/azure-devops.md`](../references/adapters/azure-devops.md)).
5. **Prompt only for what did not match.** A field that matched its expected name needs no question —
   that is what keeps this loop short
   ([`../principles/detect-confirm-save.md`](../principles/detect-confirm-save.md)).
6. **Mark a field that does not exist as `unavailable`.** Do not hand-map it onto a different field to
   make the publish succeed.
7. **Save the map back into the config**, with `fields_resolved: true` and `fields_resolved_for` set
   to the current org and project. Later runs reuse it.
8. **Re-run this loop when `fields_resolved_for` does not match** the current target, rather than
   reusing a map from a different project.

**Done when** the work-item type and every needed field are resolved against the real project,
unavailable fields are marked as such, and the map is saved with the org and project it applies to.
