# Knowledge config

**Use when** provisioning or reading a project's config. It is the whole of this skill's
project-specific knowledge. The full template, with every field and what a blank one changes, is
[`../references/knowledge-config.template.md`](../references/knowledge-config.template.md).

**Skeleton.**

```
config_version: 1
mode: A                       # A curated corpus | B sparse source | C conversational

authoritative_sources:        # source of record — only these are citable in Mode A
  - docs/business-rules.md
  - docs/adr/
supplemental_sources:         # inform scope, never cited as record
  - knowledge-working/transcript-knowledge.md

rule_id_scheme:  PREFIX-N     # e.g. ORDER-3, LABEL-1; PRD requirement ids count
adr_convention:  ADR-NNNN
discrepancy_protocol: true    # supplemental contradicts authoritative on a material point ->
                              # state both, name the supplemental source, add an Open Question

sow_present: true
sow_location: ../sow/order-fulfilment-sow-v3.docx
estimate_present: false

roles: [shipping clerk, support agent, operations lead]
tenancy_term: None            # omit tenancy bullets entirely when None
permission_model: conceptual  # or the exact source of permission names
entity_base_options: [auditable, soft-delete, concurrency-tracked]
pm_has_repo_access: false     # false -> behavioural language only, no class or table names

tags_required: [Review Required]
design_asset_source: None

publishing:
  target: azure-devops
  org: <from `az devops configure -l`>
  project: <from `az devops configure -l`>
  fields_resolved: false      # set true by the adapter's first publish
```

**Notes.**
- Saved at `Knowledge/user-story-builder.config.md`, or `.claude/…` as a fallback. Provisioned once
  by intake and hand-editable afterwards
  ([`../practices/load-or-provision-the-config.md`](../practices/load-or-provision-the-config.md)).
- A blank field changes behaviour — the skill asks, or drops the step. It never silently guesses
  ([`../principles/vocabulary-comes-from-the-config.md`](../principles/vocabulary-comes-from-the-config.md)).
- The source lists are what `anchored-knowledge`'s authority ladder maps onto: levels 1–3 authoritative,
  4–6 supplemental
  ([`../principles/delegation-not-inclusion.md`](../principles/delegation-not-inclusion.md)).
- `fields_resolved` and the saved field map make publishing a one-time setup
  ([`tracker-field-map.md`](tracker-field-map.md)).

**Related.** [`source-tag.md`](source-tag.md),
[`../practices/determine-the-source-mode.md`](../practices/determine-the-source-mode.md).
