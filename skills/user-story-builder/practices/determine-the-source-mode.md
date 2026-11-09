# Determine the source mode

**When** the config is loaded. Step 1. The config declares a mode; otherwise infer it from what is
actually available.

**Why.** The mode sets the citation rules and how much the story can claim. Getting it wrong in the
generous direction produces invented ids; getting it wrong in the cautious direction wastes a corpus
somebody built.

**Steps.**

1. **Mode A — curated corpus.** A defined set of authoritative, id-bearing sources exists: a docs
   folder with rule ids and ADRs, or an accepted PRD with requirement ids. Enforce strict citation —
   every cited id must resolve to a real file — and apply the config's two-tier discrepancy protocol
   where it is enabled ([`gather-and-rank-sources.md`](gather-and-rank-sources.md)).
2. **Mode B — sparse source.** A SOW, a ticket, a requirements document or notes exist, with no
   curated id scheme. Same anti-inference discipline; cite by source name and section; **never invent
   an id**; lean harder on Assumptions and Open Questions
   ([`../patterns/source-tag.md`](../patterns/source-tag.md)).
3. **Mode C — conversational.** The only source is the user's request. Transcribe exactly what they
   said. Everything beyond it is an Assumption or an Open Question, and the story stays deliberately
   narrow.
4. **Prefer the config's declaration** over your inference. Where they disagree because the sources
   moved, that is a validation finding
   ([`load-or-provision-the-config.md`](load-or-provision-the-config.md)).
5. **Say which mode you are in**, and say it when the mode is lower than the config expected
   ([`../principles/mode-honesty.md`](../principles/mode-honesty.md)).
6. **Omit the coverage table** in B and C — there are no requirement ids to trace
   ([`../patterns/backlog-file.md`](../patterns/backlog-file.md)).

**Done when** the mode is named, the citation form that goes with it is clear, and a downgrade from
the config's expectation has been reported rather than absorbed.
