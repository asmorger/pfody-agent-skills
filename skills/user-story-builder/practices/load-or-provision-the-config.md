# Load or provision the config

**When** at the start of every run, before anything is written. Step 0.

**Why.** Every project-specific word this skill uses comes from the config. Without it the skill
either interrogates the user on every invocation, or guesses — and a guessed role or id scheme reads
as authoritative in the finished story.

**Steps.**

1. **Detect**, first found wins: a path the user named · `Knowledge/user-story-builder.config.md`
   (primary) · `.claude/user-story-builder.config.md` (fallback).
2. **Found → validate and proceed.** Read it fully and go to
   [`determine-the-source-mode.md`](determine-the-source-mode.md). **Do not re-run intake.** The only
   exceptions: the user says "reconfigure", or `config_version` is older than the template's
   ([`../principles/detect-confirm-save.md`](../principles/detect-confirm-save.md)).
3. **Not found → discover before asking.** Scan for a `Knowledge/`, `Docs/` or `docs/` folder, a SOW,
   an ADR directory, a requirements or spec doc, existing stories. Draft a proposed config against
   [`../references/knowledge-config.template.md`](../references/knowledge-config.template.md),
   pre-filling source lists, the likely mode and any id or ADR convention you detected.
4. **No usable corpus at all → offer the fork** before settling for a lower mode
   ([`offer-to-build-knowledge-first.md`](offer-to-build-knowledge-first.md)).
5. **Confirm only what you could not infer**: source mode, which sources are authoritative against
   supplemental, persona vocabulary, tag policy, publishing target. Structured questions for the
   categorical choices, free text for paths. Confirm a draft — do not interrogate.
6. **Save** to `Knowledge/user-story-builder.config.md`, creating `Knowledge/` if needed, with the
   `config_version` stamp. Show the saved path and say it is reusable and hand-editable.
7. **Validate on load, every time.** Check the source paths still resolve. A moved or renamed file is
   flagged — offer to update the config — never silently cited as nothing.
8. **Continue with the original request in the same turn.** Intake is a means, not the deliverable.

**Done when** a config exists at a detected path with its version stamp, its source paths resolve, the
user confirmed anything you could not infer, and the thing they asked for is underway.
