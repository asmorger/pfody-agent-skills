# Tool config

**Use when** running the tool anywhere other than its defaults — which includes every time this skill
is driven by another skill. Pass `--config config.json`, or YAML with PyYAML installed. Every field is
optional; the full set is in [`../config.example.yaml`](../config.example.yaml).

**Skeleton.**

```yaml
title: "Knowledge Index"
intro: "Durable rules and decisions distilled from project transcripts, each cited to its source meeting."

vault_path:  "transcript-knowledge"
state_path:  "knowledge-index.state.json"
workdir:     ".knowledge-index.work"

supported_extensions: [".docx", ".txt", ".md", ".json", ".vtt", ".srt", ".csv"]
recursive: true

dedup_threshold: 0.6        # Jaccard over keywords; lower merges more aggressively

categories:
  - {name: "Orders", prefix: "ORDER"}
  - {name: "Labels", prefix: "LABEL"}
```

**Notes.**
- **A caller embedding this skill must override `vault_path` and `state_path`**, into the workbench.
  This renderer owns every file in its output folder and deletes what it no longer generates, so the
  one place it must never point is a record vault
  ([`../anti-patterns/overwriting-a-sibling-index.md`](../anti-patterns/overwriting-a-sibling-index.md)).
- `dedup_threshold` is the one dial worth turning on a large corpus. Lower it when one topic has
  sprawled across several items
  ([`../practices/curate-a-large-corpus.md`](../practices/curate-a-large-corpus.md)).
- `.docx` is the primary format — Copilot and Teams exports — and the parser handles all three of
  their layouts with no `python-docx` dependency.
- `title` names the MOC note and the `.base` file as well as heading the index, so changing it moves
  two files. `intro` is the prose above the embed
  ([`vault-notes.md`](vault-notes.md)).
- JSON needs no dependency; YAML needs PyYAML. Prefer JSON when the standard library matters.

**Related.** [`category-taxonomy.md`](category-taxonomy.md), [`state-file.md`](state-file.md).
