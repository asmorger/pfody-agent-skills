# Decompose a PRD

**When** a person wants Epics, Features, User Stories and acceptance criteria out of a PRD. Mode
`DECOMPOSE`.

**Why.** This is the step that converts a contract into work. Every behaviour added here is behaviour
nobody sourced, and every requirement dropped here is a behaviour that silently will not be built —
so the coverage table, not the stories, is the deliverable that proves the run.

**Steps.**

1. **Read [`../references/vault-convention.md`](../references/vault-convention.md).**
2. **Check the status.** Not `accepted` → stop and ask whether the person wants a preview. A preview
   says `PREVIEW` in each story note's first lines, skips `PROPOSED` requirements and reports them,
   and is never published; the check enforces the marker
   ([`../principles/only-a-person-crosses-a-gate.md`](../principles/only-a-person-crosses-a-gate.md)).
3. **Carry the Epics and Features across unchanged** — same ids, same names. Never create, merge or
   rename one in this mode. A Feature that does not fit is reported, not fixed.
4. **Slice each Feature into stories** ([`slice-a-feature.md`](slice-a-feature.md)), one note each
   in `backlog/`, `US-01` upward, `parent` pointing at the Feature.
5. **Place every in-scope `R-` requirement in exactly one story** of its own Feature, listed in the
   story's `requirements` and in the requirement's `stories`. The check rejects a story covering
   another Feature's requirement. Put each `X-` requirement in each story of the Features it names;
   the ones marked `All` go in the definition of done, once.
6. **Set each requirement's `coverage`**: `covered` with its story, `blocked` with the question,
   `skipped-p3`, or `skipped-proposed`. This is the whole coverage record — the table is generated
   from it ([`../patterns/coverage-moc.md`](../patterns/coverage-moc.md)).
7. **Write the criteria**: `AC-n [R-xxx] Given … when … then …`
   ([`../patterns/acceptance-criterion.md`](../patterns/acceptance-criterion.md)).
8. **Add no behaviour.** A gap you find stays out of the story and goes in the report; the person
   decides whether to run `CHANGE`. Add no tasks and no estimates — those are engineering's at build
   time.
9. **Write the notes** into `backlog/`, and the definition of done into `moc/backlog.md`
   ([`../patterns/backlog-notes.md`](../patterns/backlog-notes.md)).
10. **Run `prd.py check` then `prd.py moc`**, and do not report success until the check passes
    ([`run-the-checks.md`](run-the-checks.md)).

**Done when** every requirement carries one of the five `coverage` values, the ids in each story's
*Source grounding* are exactly the ids its criteria cite, the PRD hub is unchanged, the generated
coverage table matches the notes, and the counts of Epics, Features, stories, covered, blocked and
skipped are reported.
