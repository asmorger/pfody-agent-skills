# Knowledge config

**Use when** provisioning or reading a project's config. It declares everything this skill would
otherwise have to guess. The full template, with every field and what a blank one changes, is
[`../references/knowledge-config.template.md`](../references/knowledge-config.template.md).

**Skeleton.**

```
config_version: 2

# 1 locations
knowledge_root:   docs/                  # committed record; Knowledge/ without a repo
docs_dir:         docs/                  # the Obsidian vault; Knowledge/Docs/ without a repo
working_dir:      knowledge-working/     # the workbench; NEVER committed, OUTSIDE the vault
storage_mode:     repo-docs              # repo-docs | project-knowledge
git_managed:      true
working_dir_gitignored: true

# 2 vault layout — an existing vault's real names win over these defaults
vault:            true
link_style:       wikilink               # wikilink | markdown
query_engine:     bases                  # bases | dataview | none
home_note:        moc/knowledge.md
folders:          moc/ rules/ glossary/ scope/ decisions/ questions/ changes/
                  scope-watch/ sources/ facts/ reference/ bases/

# 3 scope baseline
sow_present:      true
sow_name:         "<Client> Order Fulfilment SOW v3"
sow_location:     ../sow/order-fulfilment-sow-v3.docx

# 4 ids
rule_id_prefixes: ORDER, LABEL, AUTH     # or "emerge" to derive per topic
topics:           orders, labels, auth   # one prefix per topic
adr_convention:   ADR-NNNN

# 5 transcripts (delegated) — index path is in the workbench, never the vault
transcripts_present: true
transcripts_folder:  ../transcripts/
transcript_index:    knowledge-working/transcript-knowledge/transcript-knowledge.md
```

**Notes.**
- A blank field changes behaviour — the skill asks, or drops the step. It never makes the skill guess
  ([`../principles/config-before-anything.md`](../principles/config-before-anything.md)).
- Record the project's real folders, filenames **and property names**, not the defaults. Nothing is
  renamed to match this file, and renaming a property silently empties every Bases view the team had
  ([`../principles/match-the-projects-voice.md`](../principles/match-the-projects-voice.md)).
- `query_engine: none` for a vault without Bases: the MOCs then carry the generated snapshot alone,
  which still reads correctly everywhere ([`moc-note.md`](moc-note.md)).
- `transcript_index` points into the workbench. The transcript skill's defaults would otherwise
  write into the vault
  ([`../anti-patterns/the-transcript-index-overwriting-the-index.md`](../anti-patterns/the-transcript-index-overwriting-the-index.md)).
- The template's later sections hold the authority ladder, the review cadence and the owner.

**Related.** [`the-two-trees.md`](the-two-trees.md), [`authority-ladder.md`](authority-ladder.md),
[`../practices/locate-the-base.md`](../practices/locate-the-base.md).
