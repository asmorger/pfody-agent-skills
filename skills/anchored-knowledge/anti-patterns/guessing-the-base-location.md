# Guessing the base location

**Smell.** A run that opens by creating `Knowledge/` because no config was found, in a repository that
already keeps its knowledge in `docs/`. Or a `business-rules.md` written beside an existing
`business_rules.md`. Or a confident "I'll put this in `docs/knowledge/`" with nothing asked.

**Why it is wrong.** The failure is specific and expensive: a second knowledge base beside the real
one. Two rule files, two id schemes, two source registers, and no source of record — which is the
exact thing the base exists to provide. It is also hard to unwind, because by the time anyone notices,
both halves have real content and real citations. A project that had scattered knowledge now has
scattered knowledge with structure.

**Instead.** Discover first — scan for the folder that holds `business-rules.md`, `glossary.md` and
`adr/` together, and for files named like the governance set. Then **propose both locations and let
the user confirm**. Where discovery cannot settle something — the base, the scope baseline, the id
scheme, the transcripts folder — ask, and write the answer into the config so the next run does not
ask again ([`../principles/config-before-anything.md`](../principles/config-before-anything.md),
[`../practices/locate-the-base.md`](../practices/locate-the-base.md)).
