# Mode honesty

**Rule.** Three source modes: **A** a curated, id-bearing corpus; **B** a sparse source with no id
scheme; **C** the user's request alone. If you are in B or C because the sources were thin, say so,
and make the resulting Assumptions and Open Questions visible rather than papering the gap with
plausible content.

**Why.** The mode tells the reader how much weight the story carries, and that is information they
cannot recover from the story's appearance — a Mode C story and a Mode A story look identical. Naming
the mode is also what makes the thin-source case useful rather than dangerous: a story explicitly
built from one conversation, with four Open Questions, is a good artefact. The same story presented as
grounded is a liability.

**In the story.**
- Mode A: strict citation. Every cited id resolves to a real file; use the config's two-tier
  discrepancy protocol where it is enabled
  ([`../practices/gather-and-rank-sources.md`](../practices/gather-and-rank-sources.md)).
- Mode B: same anti-inference discipline, cite by source name and section, **never invent an id**, and
  lean harder on Assumptions and Open Questions.
- Mode C: transcribe exactly what the user said. Everything beyond it is an Assumption or an Open
  Question, and the story stays deliberately narrow.
- Omit the coverage table in B and C — there are no requirement ids to trace
  ([`../patterns/backlog-file.md`](../patterns/backlog-file.md)).
- Factuality over completeness governs all three equally
  ([`factuality-over-completeness.md`](factuality-over-completeness.md)).

**Breaks when.** The mode drops and nobody is told →
[`../anti-patterns/silent-mode-downgrade.md`](../anti-patterns/silent-mode-downgrade.md).
