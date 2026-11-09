# Tracker text is ASCII

**Rule.** Normalise every field bound for a tracker's rich-text to pure ASCII before sending:
straight quotes for curly ones, `-` for en and em dashes, `->` for arrows, `"Section"` for `§`,
`...` for an ellipsis. The adapter defines the full step and it is mandatory, not best-effort.

**Why.** On Windows the encoding hops between the CLI, the shell and the tracker's API corrupt
non-ASCII characters silently — nothing errors, and the damage is only visible in the tracker
afterwards, inside a field a developer is about to work from. A mangled acceptance criterion is worse
than a missing one, because it still reads as instructions. The failure is also platform-dependent,
so it passes every test on the author's machine and appears on someone else's.

**In the story.**
- The order is fixed: **strip wikilink brackets, then normalise to ASCII, then convert to the
  tracker's markup.** Stripping first matters because an embed pulls in text that needs normalising
  too, and normalising last would miss it
  ([`../references/adapters/azure-devops.md`](../references/adapters/azure-devops.md)).
- It applies to every rich-text field, not only the description: criteria, notes, assumptions, the
  demo scenario.
- The skill's own prose uses `§` and em dashes freely. Those are for the markdown deliverable — the
  tracker copy is a different artefact with a different constraint.
- Verify by reading the created item back, not by trusting the send
  ([`../practices/publish-to-a-tracker.md`](../practices/publish-to-a-tracker.md)).

**Breaks when.** Rich text goes out unnormalised →
[`../anti-patterns/non-ascii-in-a-tracker-field.md`](../anti-patterns/non-ascii-in-a-tracker-field.md).
