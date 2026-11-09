# Render a narrative

**When** somebody needs to *read* the vault rather than query it: an onboarding summary, a design
story, "explain the why". Also after a decision, a scope change or a batch of new rules, because a
narrative that describes an older vault is worse than none.

**Why.** A graph of atomic notes is excellent for citation and poor for reading end to end. The
honest answer is not to grow the notes into documents, and not to forbid documents either — it is a
**derived** document: readable prose that owns nothing, where every statement summarises a note and
links it. The checks make the derivation enforceable
([`../patterns/narrative-note.md`](../patterns/narrative-note.md)), which is the whole difference
between this and the hand-written summary that goes stale
([`../anti-patterns/a-note-that-grew-into-a-document.md`](../anti-patterns/a-note-that-grew-into-a-document.md)).

**Steps.**

1. **Name the inputs.** Set `derived-from` to the folders whose notes the story is built from —
   typically `[rules, scope, decisions, questions]`. Evidence folders are not inputs: the narrative
   reaches a source only through the note that cites it.
2. **Write section by section, link as you go.** Each statement is one line and carries the link to
   the note that holds it. If you want to restate a number, a date or a status, link or embed instead
   ([`../principles/one-home-per-fact.md`](../principles/one-home-per-fact.md)).
3. **Carry status with every claim.** A draft rule is described as draft and a proposed decision as
   proposed, in the sentence. A narrative that flattens status reads as agreement the vault never
   recorded.
4. **Record gaps; never fill them.** When the story needs a fact, a decision or a reason no note
   holds, write it under `## Gaps found while deriving` with the note it belongs in — then stop. The
   fix is to record it in its own home, through its own practice, and regenerate.
5. **Stamp it:** `python3 scripts/vault.py narrative <vault>` writes `covers-through` and
   `input-manifest-sha256`. Never type either by hand, and write no other date.
6. **Check it:** `python3 scripts/vault.py lint <vault>` holds every section to a citation, every
   claim to a link, and the note to having a gaps section.
   `python3 scripts/vault.py narrative <vault> --check` fails once the notes move on.

**Done when** `lint` is clean, `narrative --check` exits 0, every gap is listed with its intended
home, and your report says plainly which gaps a person now has to resolve. **A narrative is never
cited** — it is a reading surface, and the Reference Layer is what anything downstream may cite
([`../principles/only-the-reference-layer-is-citable.md`](../principles/only-the-reference-layer-is-citable.md)).
