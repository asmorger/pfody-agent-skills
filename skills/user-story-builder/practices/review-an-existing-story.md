# Review an existing story

**When** asked "is this sourced?", "review these acceptance criteria", or before handing over
anything you wrote. The same checklist either way.

**Why.** The defects that matter look like a finished story. An unsourced criterion is formatted
identically to a sourced one, so only a per-line pass finds it.

**Steps.** Work the fifteen checks. Each finding names the item and the correction.

1. **Circular *so that*** — does it restate the *I want to*?
2. **Vague role** — is it specific enough to imply context and goals?
3. **Solution-prescriptive need** — does it describe a UI or implementation instead of a need?
4. **Untestable criterion** — can QA write a pass/fail test for every one?
5. **Story too large** — realistically built and demoed in one sprint?
6. **Missing business rationale** — is there a real *why* anywhere?
7. **Criteria missing edge cases** — only the happy path, *where a source specifies more*?
8. **Business-rule-only story** — does it produce a buildable output, or only document rules?
9. **Hidden prerequisite** — would a developer need another story first?
10. **Gratuitous out-of-scope callout** — excluding something that was never in scope here?
11. **Citation repetition** — the same rule cited across several sections? Consolidate.
12. **Criterion form or citation noise** — `AC-n [tag] Given, when, then`? Remove any other citation.
13. **Unsourced bullet or criterion** — for each, can you name the specific source? If not, move it to
    Assumptions or Open Questions, or delete it.
14. **Pattern-matched scope** — audit, soft delete, validation, error handling, permissions or
    notifications the source never requested? Remove them.
15. **Wrong level or id** — a free `US-` id; every `EPIC-` and `FEAT-` id copied from the source, with
    no invented or renamed parent?

**Then.** Propose the corrected version. **Do not rewrite scope in** — only remove what is not sourced
and surface the gaps. Do not raise these as Open Questions unless they genuinely need a stakeholder
decision.

**Done when** every check has a verdict, each finding names the item and the correction, nothing was
added to the story, and the gaps are visible rather than filled.
