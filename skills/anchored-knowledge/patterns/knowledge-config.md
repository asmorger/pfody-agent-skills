# Knowledge config

**Use when** provisioning or reading a project's config. It declares everything this skill would
otherwise have to guess. The full template, with every field and what a blank one changes, is
[`../references/knowledge-config.template.md`](../references/knowledge-config.template.md).

**Skeleton.**

```
config_version: 1

# 1 locations
knowledge_root:   docs/                  # committed record; Knowledge/ without a repo
docs_dir:         docs/                  # Reference Layer; Knowledge/Docs/ without a repo
working_dir:      knowledge-working/     # local staging; NEVER committed
storage_mode:     repo-docs              # repo-docs | project-knowledge
git_managed:      true
git_host:         github
working_dir_gitignored: true

# 2 file map — the project's real names win over these defaults
business_rules:   business-rules.md
glossary:         glossary.md
assumptions:      assumptions.md
adr_dir:          adr/
source_register:  source-register.md
open_questions:   open-questions.md
scope_watch:      scope-watch.md
change_log:       knowledge-change-log.md
index:            knowledge-index.md
intake:           knowledge-intake.md    # working_dir

# 3 scope baseline
sow_present:      true
sow_name:         "<Client> Order Fulfilment SOW v3"
sow_location:     ../sow/order-fulfilment-sow-v3.docx

# 4 ids
rule_id_prefixes: ORDER, LABEL, AUTH     # or "emerge" to derive per section
adr_convention:   ADR-NNNN

# 5 transcripts (delegated)
transcripts_present: true
transcripts_folder:  ../transcripts/
transcript_index:    transcript-knowledge.md   # working_dir; MUST differ from `index`
```

**Notes.**
- A blank field changes behaviour — the skill asks, or drops the step. It never makes the skill guess
  ([`../principles/config-before-anything.md`](../principles/config-before-anything.md)).
- Record the project's real filenames, not the defaults. Nothing is renamed to match this file
  ([`../principles/match-the-projects-voice.md`](../principles/match-the-projects-voice.md)).
- `transcript_index` must differ from `index`. The transcript skill's default output would otherwise
  overwrite this base's index
  ([`../anti-patterns/the-transcript-index-overwriting-the-index.md`](../anti-patterns/the-transcript-index-overwriting-the-index.md)).
- Sections 6 and 7 of the template hold the authority ladder and the review cadence and owner.

**Related.** [`the-two-trees.md`](the-two-trees.md), [`authority-ladder.md`](authority-ladder.md),
[`../practices/locate-the-base.md`](../practices/locate-the-base.md).
