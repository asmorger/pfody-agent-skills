# Decompose a PRD

**When** a person wants Epics, Features, User Stories and acceptance criteria out of a PRD. Mode
`DECOMPOSE`.

**Why.** This is the step that converts a contract into work. Every behaviour added here is behaviour
nobody sourced, and every requirement dropped here is a behaviour that silently will not be built —
so the coverage table, not the stories, is the deliverable that proves the run.

**Steps.**

1. **Read [`../references/backlog-format.md`](../references/backlog-format.md).**
2. **Check the status.** Not `Accepted` → stop and ask whether the person wants a preview. A preview
   is marked `PREVIEW` at the top, skips `PROPOSED` requirements and reports them, and is never
   published ([`../principles/only-a-person-crosses-a-gate.md`](../principles/only-a-person-crosses-a-gate.md)).
3. **Carry the Epics and Features across unchanged** — same ids, same names. Never create, merge or
   rename one in this mode. A Feature that does not fit is reported, not fixed.
4. **Slice each Feature into stories** ([`slice-a-feature.md`](slice-a-feature.md)), `US-01` upward,
   unique in the backlog.
5. **Place every in-scope `R-` requirement in exactly one story** of its own Feature. Put each `X-`
   requirement in each story of the Features it names whose behaviour it changes; the ones marked
   `All` go in the definition of done, once.
6. **Skip `P3`, and skip anything an open question blocks.** Report both — a skipped requirement is a
   result, not an omission.
7. **Write the criteria**: `AC-n [R-xxx] Given … when … then …`
   ([`../patterns/acceptance-criterion.md`](../patterns/acceptance-criterion.md)).
8. **Add no behaviour.** A gap you find stays out of the story and goes in the report; the person
   decides whether to run `CHANGE`. Add no tasks and no estimates — those are engineering's at build
   time.
9. **Write `<prd-name>.backlog.md`** beside the PRD
   ([`../patterns/backlog-file.md`](../patterns/backlog-file.md)), ending in the coverage table and
   the counts.
10. **Run `check_prd.py --backlog`** and do not report success until it passes
    ([`run-the-checks.md`](run-the-checks.md)).

**Done when** every requirement has a coverage row with one of the four statuses, the ids in each
story's *Source grounding* are exactly the ids its criteria cite, the PRD is unchanged, and the
counts of Epics, Features, stories, covered, blocked and skipped are reported.
