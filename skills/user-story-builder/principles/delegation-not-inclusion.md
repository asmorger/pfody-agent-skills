# Delegation, not inclusion

**Rule.** This skill consumes a knowledge corpus; it does not build one. When a project has none,
offer to delegate to `anchored-knowledge` — or an equivalent knowledge builder — and re-enter intake
once it finishes. Never embed the builder's work here, and never build a knowledge system without the
user's yes.

**Why.** Producer and consumer have genuinely different jobs, and a skill that does both does neither
well: building a corpus means reconciliation, authority ladders and change control, which have nothing
to do with story craft. Keeping them separate also means the corpus is built once and serves
everything — stories, PRDs, specs, tests — rather than being rebuilt inside each consumer. The handoff
is one-way by design: this skill invokes the builder, and the builder never calls back.

**In the story.**
- The offer appears **only** when the corpus is genuinely absent — no `Knowledge/` or `Docs/`, no SOW,
  no requirements docs, only raw notes or the request itself
  ([`../practices/offer-to-build-knowledge-first.md`](../practices/offer-to-build-knowledge-first.md)).
- It is a fork, not a prerequisite: build first and reach Mode A, or proceed now in Mode B or C.
- No builder available → offer to scaffold a minimal source file and proceed in the lower mode.
- The config is the contract between them. The builder's authority levels 1–3 become
  `authoritative_sources`, 4–6 become `supplemental_sources`, its stable ids become the `rule_id_scheme`,
  and only `Confirmed` content is Mode A eligible
  ([`../patterns/knowledge-config.md`](../patterns/knowledge-config.md)).
- Any skill producing a sourced, id-bearing corpus can stand in. The handoff is written generically.

**Breaks when.** Knowledge is built here, or built without being asked →
[`../anti-patterns/building-knowledge-unasked.md`](../anti-patterns/building-knowledge-unasked.md).
