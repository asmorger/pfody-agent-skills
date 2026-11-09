# anchored-knowledge config — Order Fulfilment (example)

```
config_version: 2

# 1 locations
knowledge_root:   docs/
docs_dir:         docs/                  # the Obsidian vault
working_dir:      knowledge-working/     # the workbench; NEVER committed, outside the vault
storage_mode:     repo-docs
git_managed:      true
git_host:         github
working_dir_gitignored: true

# 2 vault layout
vault:            true
link_style:       wikilink
note_naming:      title-with-id-alias
folders:
  moc:            moc/
  rules:          rules/
  glossary:       glossary/
  scope:          scope/
  decisions:      decisions/
  questions:      questions/
  scope_watch:    scope-watch/
  changes:        changes/
  sources:        sources/
  facts:          facts/
  reference:      reference/
  bases:          bases/
start_note:        moc/knowledge.md
query_engine:     bases                  # bases | dataview | none
snapshot:         true                   # generated tables beneath each embed

# 3 scope baseline
sow_present:      true
sow_name:         "Order Fulfilment SOW v3"
sow_location:     ../sow/order-fulfilment-sow-v3.docx

# 4 ids
rule_id_prefixes: ORDER, LABEL
topics:           orders, labels
adr_convention:   ADR-NNNN

# 5 transcripts (delegated)
transcripts_present: true
transcripts_folder:  ../transcripts/
transcript_index:    knowledge-working/transcript-knowledge/transcript-knowledge.md
```

Every path above is this example's choice, not a default this skill assumes. The real template is
`references/knowledge-config.template.md`.
