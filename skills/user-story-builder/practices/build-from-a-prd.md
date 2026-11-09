# Build from a PRD

**When** the source is an approved PRD with requirement ids. It is a Mode A source and its `R-` and
`X-` ids are rule ids.

**Why.** A PRD has already done the sourcing and the gating, so the story work is placement rather
than interpretation — and the placement has to be exact, because the PRD's coverage table is what
proves nothing was dropped.

**Steps.**

1. **Check the status first.** Not `Accepted` → write `PREVIEW` in each story note's first lines and
   a `[!warning] PREVIEW` callout on the MOC, and **do not publish it**
   ([`../principles/drafting-and-publishing-are-separate.md`](../principles/drafting-and-publishing-are-separate.md)).
2. **Assign each in-scope `R-` requirement to exactly one story** in its own Feature.
3. **Slice by the buildable-output standard, not by the hour bands.** A PRD carries no hours
   ([`slice-a-feature-into-stories.md`](slice-a-feature-into-stories.md)).
4. **Place the `X-` requirements.** One naming a Feature goes into each story of that Feature whose
   behaviour it changes. One applying to `All` goes in the Definition of Done, once
   ([`../patterns/backlog-notes.md`](../patterns/backlog-notes.md)).
5. **Skip and report** anything an open question blocks, anything marked `PROPOSED`, and anything
   `P3`. Each skip is a reported result, not an omission.
6. **Tag each story with the highest priority of its requirements.** A story holding only `P2`
   requirements is tagged `Stretch`, and `P2` is never mixed with `P0` or `P1`.
7. **Use the PRD's feature flag names** from its rollout section. Do not invent one.
8. **Tag the criteria** `[R-001]` where one PRD is in play, `[PRD-001 R-001]` where several are
   ([`../patterns/source-tag.md`](../patterns/source-tag.md)).
9. **Copy the Epic and Feature ids and names** across unchanged.
10. **End with the coverage table** and the counts.

**Done when** every in-scope requirement sits in exactly one story or has a reported skip, the `X-`
requirements are placed or in the Definition of Done, the priorities tag correctly, and a non-Accepted
PRD produced a `PREVIEW` that was not published.

**Note.** When the whole backlog is being generated from a PRD in one pass, `agentic-prd` owns that
decomposition and its coverage proof. This practice is for writing stories from a PRD within this
skill's own run.
