# Transcript brief

**Use when** reading what `prepare` produced. One brief per new or changed transcript, in the work
directory, every line a turn tagged with the three things a citation needs.

**Skeleton.**

    # Brief: Order Fulfilment Scope Call
    # Date: 2026-01-21
    # File: /transcripts/2026-01-21-scope-call.docx

    [t0078 @ 0:16:40 | Sam Ortiz] so when the clerk hits save, that's a draft right
    [t0079 @ 0:16:48 | Dana Lee] yes. saving a draft, not submitting
    [t0080 @ 0:17:03 | Sam Ortiz] and submitting is the thing that locks the address
    [t0081 @ 0:17:11 | Dana Lee] correct. after submit the address is frozen
    [t0082 @ 0:17:20 | Sam Ortiz] I'll check with ops about split orders, don't quote me

A line's three fields are the `turn_id`, the timestamp and the speaker. The manifest beside the briefs
lists each file with its `hash`, name, meeting and date.

**Notes.**
- The brief is the only legal source of a citation. Copy the `turn_id` and the quote from it; never
  retype either from memory
  ([`../principles/every-item-carries-a-source.md`](../principles/every-item-carries-a-source.md)).
- Some exports carry no speaker labels — newer Copilot `-en-US` files among them. The field is then
  empty and the citation is meeting plus date. Do not infer who spoke.
- `t0082` above is the shape of a non-item: a speaker explicitly declining to commit. Skip it
  ([`../principles/precision-over-volume.md`](../principles/precision-over-volume.md)).
- The rule often spans turns — `t0079` and `t0081` together say that submit freezes the address. Cite
  the turn whose words support the statement, and cite both when both do.
- Briefs are regenerated every run and are not a deliverable. Nothing should cite the work directory.

**Related.** [`knowledge-item.md`](knowledge-item.md), [`items-json.md`](items-json.md),
[`../practices/prepare-the-briefs.md`](../practices/prepare-the-briefs.md).
