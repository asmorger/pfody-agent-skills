# Errata register

**Use when** the transcription service misheard a word, or labelled a speaker only `@N`. The
transcript and its archived original are never edited, so the correction lives in a register and the
quote carries it as a visible annotation.

**Skeleton.** `errata.md`, at the vault root

```markdown
---
type: errata
---

# Transcript errata

| Transcript | Cue | Speaker | Transcript says | Correction | State | Evidence |
|---|---|---|---|---|---|---|
| 2026-01-21-order-fulfilment-scope-call | 0:14:22 | Priya | get live tracking | lot | candidate | "live" makes no sense of the sentence; the topic is lot control |
| 2026-01-21-order-fulfilment-scope-call | 0:31:05 | @1 | @1 | Devin Alvarez | confirmed | self-introduces at 0:30:58; confirmed 2026-02-02 by Maya, attended |
```

A quote then reads `get live [lot] tracking`, or the citation reads
`— Devin Alvarez [unlabeled @1] (0:31:05)`.

**Notes.**
- **The bracket is skipped when matching and required to be registered.** `verify` fails a bracket
  with no row, *and* fails a quote that contains a registered span without its annotation — so a
  correction cannot be applied in one note and quietly forgotten in the next
  ([`../practices/verify-the-quotes.md`](../practices/verify-the-quotes.md)).
- **Two states, and only one of them an agent may set.** `candidate` is an inference — from an agent,
  or from somebody who was not in the room — and must cite the evidence inside the transcript that
  supports it. `confirmed` means a named person vouched for it, and records who, on what basis, and
  when. **An agent never writes `confirmed`.** Keep the earlier state in the evidence text when a row
  is upgraded, so the history of the claim survives.
- **The span must be unique in that turn.** `what are you`, not `you`.
- **A correction is for a mishearing, not a rewording.** If the speaker said something unclear, quote
  it as transcribed and say so in the item's `note`
  ([`../principles/status-is-a-field-not-a-sentence.md`](../principles/status-is-a-field-not-a-sentence.md)).
- The register is the one hand-maintained file in the vault. Every other file is generated, so keep
  it at the root where the renderer does not reach
  ([`../references/vault-convention.md`](../references/vault-convention.md)).

**Related.** [`../principles/a-quote-is-checked-not-trusted.md`](../principles/a-quote-is-checked-not-trusted.md),
[`knowledge-item.md`](knowledge-item.md),
[`../anti-patterns/an-invented-citation.md`](../anti-patterns/an-invented-citation.md).
