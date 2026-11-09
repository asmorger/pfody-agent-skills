# Detect, confirm, save — once

**Rule.** Everything project-specific is provisioned by a loop that detects what it can, confirms
only what it cannot infer, and saves the result. Three such loops: the knowledge config, the tracker
field map, and the handoff when no corpus exists. Each persists, so each runs **once** — not on every
invocation.

**Why.** A skill that interrogates the user at the start of every run gets abandoned, and the usual
alternative — hand-authored configuration — never gets written. Detecting first is what keeps the
confirmation short: the user approves a draft instead of answering a questionnaire. Persisting is what
keeps it honest across sessions, because the second run reaches the same sources and the same tracker
fields rather than rediscovering them differently.

**In the story.**
- Config found → validate and proceed. Do **not** re-run intake. The only exceptions are an explicit
  "reconfigure" and a `config_version` older than the template's
  ([`../practices/load-or-provision-the-config.md`](../practices/load-or-provision-the-config.md)).
- Discover before asking: scan for `Knowledge/`, `Docs/`, a SOW, an ADR directory, a requirements
  doc, existing stories. Draft a proposed config from what you find.
- Confirm only the uninferable: source mode, which sources are authoritative, persona vocabulary, tag
  policy, publishing target. Short — confirm a draft, do not interrogate.
- Tracker fields resolve on first publish and write back to the config; later runs reuse the saved map
  ([`../practices/resolve-the-tracker-fields.md`](../practices/resolve-the-tracker-fields.md)).
- Intake is a means, not the deliverable. Save, show the path, then answer the original request in the
  same turn.

**Breaks when.** A configured project is interrogated again →
[`../anti-patterns/re-running-intake-every-time.md`](../anti-patterns/re-running-intake-every-time.md).
