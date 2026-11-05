# Agent Skills

Skills for AI-assisted product management. They turn project sources into cited knowledge, agent-ready PRDs, and traceable work items.

| Skill | What it does | Needs |
|---|---|---|
| [`transcript-knowledge-base`](skills/transcript-knowledge-base) | Builds a sourced knowledge index from meeting transcripts | Python 3 |
| [`anchored-knowledge`](skills/anchored-knowledge) | Creates and audits a citable project knowledge system | Nothing extra |
| [`agentic-prd`](skills/agentic-prd) | Creates and reviews agent-ready PRDs, then generates Epics, Features, and User Stories | Python 3 for its scripts |
| [`user-story-builder`](skills/user-story-builder) | Writes sourced User Stories and can publish them to Azure DevOps | `az` CLI to publish |

## Install

Copy a skill folder to your Claude Code skills folder, then start a new session:

```bash
git clone https://github.com/pfoty/agent-skills.git
cp -r agent-skills/skills/agentic-prd ~/.claude/skills/
```

## Use

Ask in plain language. For example:

- "Build a knowledge index from the transcripts in this folder."
- "Draft a PRD from this SOW and these notes."
- "Break this accepted PRD into Epics, Features, and User Stories."

A person approves scope and publishing. Check the output against its sources before you use it.
