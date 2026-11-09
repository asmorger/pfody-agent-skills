# Tracker field map

**Use when** publishing, or resolving fields for the first time. The map lives in the config, written
back by the adapter's detect-confirm-save loop, so later runs do not re-prompt.

**Skeleton.** In the config, under `publishing`:

```
publishing:
  target: azure-devops
  org: <from `az devops configure -l`>
  project: <from `az devops configure -l`>
  work_item_type: User Story          # or Product Backlog Item, per the process template
  fields_resolved: true
  fields_resolved_for: <org>/<project>
  fields:
    title:             System.Title
    description:       System.Description
    acceptance:        Microsoft.VSTS.Common.AcceptanceCriteria
    tags:              System.Tags
    blocked_reason:    unavailable    # field does not exist in this project
```

**Notes.**
- `fields_resolved_for` is what makes the cache safe: a different org or project re-runs resolution
  rather than reusing a map that does not apply
  ([`../practices/resolve-the-tracker-fields.md`](../practices/resolve-the-tracker-fields.md)).
- Read `org` and `project` from the tool's own configuration — `az devops configure -l`. **Never
  assume a project.**
- A field that does not exist in the project is marked `unavailable` by the resolution loop. Do not
  hand-map it to something else
  ([`../practices/diagnose-a-failed-run.md`](../practices/diagnose-a-failed-run.md)).
- The story's markdown labels map to these fields at publish time. The markdown itself never names a
  tracker field ([`user-story.md`](user-story.md)).
- A tracker id is a separate value and does not replace `US-01`
  ([`../principles/one-name-and-one-id-per-level.md`](../principles/one-name-and-one-id-per-level.md)).

**Related.** [`knowledge-config.md`](knowledge-config.md),
[`../references/adapters/azure-devops.md`](../references/adapters/azure-devops.md).
