# Knowledge config

**Use when** provisioning or reading a project's config. It is the whole of this skill's
project-specific knowledge. The full template, with every field and what a blank one changes, is
[`../references/knowledge-config.template.md`](../references/knowledge-config.template.md).

**Skeleton.**

```
config_version: 2
mode: A                       # A curated corpus | B sparse source | C conversational

authoritative_sources:        # source of record — only these are citable in Mode A
  - docs/rules/
  - docs/decisions/
supplemental_sources:         # inform scope, never cited as record
  - knowledge-working/transcript-knowledge/

# where the stories go — an existing vault's real folders and property names win
stories_dir:     docs/backlog/        # one note per story, Epic and Feature
moc:             docs/moc/backlog.md  # the index, with a generated snapshot
link_style:      wikilink             # wikilink | markdown

rule_id_scheme:  PREFIX-N     # e.g. ORDER-3, LABEL-1; PRD requirement ids count
adr_convention:  ADR-NNNN
discrepancy_protocol: true    # supplemental contradicts authoritative -> state both, name the
                              # supplemental source, add an Open Question

sow_present: true
sow_location: ../sow/order-fulfilment-sow-v3.docx

roles: [shipping clerk, support agent, operations lead]
tenancy_term: None            # omit tenancy bullets entirely when None
permission_model: conceptual  # or the exact source of permission names
pm_has_repo_access: false     # false -> behavioural language only, no class or table names
tags_required: [Review Required]
design_asset_source: None

publishing:
  target: azure-devops
  org: <from `az devops configure -l`>
  project: <from `az devops configure -l`>
  fields_resolved: false      # set true by the adapter's first publish
  write_back: true            # write tracker-id/url into each note after a verified create
```

**Notes.**
- Saved at `Knowledge/user-story-builder.config.md`, or `.claude/…` as a fallback; provisioned once
  by intake ([`../practices/load-or-provision-the-config.md`](../practices/load-or-provision-the-config.md)).
- A blank field changes behaviour — the skill asks, or drops the step. It never silently guesses
  ([`../principles/vocabulary-comes-from-the-config.md`](../principles/vocabulary-comes-from-the-config.md)).
- The source lists are what `anchored-knowledge`'s authority ladder maps onto: levels 1–3
  authoritative, 4–6 supplemental
  ([`../principles/delegation-not-inclusion.md`](../principles/delegation-not-inclusion.md)).
- `fields_resolved` plus the saved field map make publishing a one-time setup, and `write_back`
  controls whether the tracker id returns to the note
  ([`tracker-field-map.md`](tracker-field-map.md)).

**Related.** [`source-tag.md`](source-tag.md),
[`../references/vault-convention.md`](../references/vault-convention.md).
