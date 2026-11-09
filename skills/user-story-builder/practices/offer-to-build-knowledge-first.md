# Offer to build knowledge first

**When** discovery turns up no usable knowledge corpus — no `Knowledge/` or `Docs/`, no SOW, no
requirements documents, only raw notes or the user's request. Step 0b-2.

**Why.** Dropping silently to the lowest mode produces a narrow story and a missed opportunity: the
project needed a corpus anyway, and building one first turns every later story from Mode C into Mode
A. But forcing it is worse — sometimes the user wants one story from one conversation, and that is a
legitimate ask.

**Steps.**

1. **Confirm the corpus is genuinely absent.** Thin is not absent. A SOW alone is Mode B, and this
   fork does not apply ([`determine-the-source-mode.md`](determine-the-source-mode.md)).
2. **Present both options**, plainly, as a fork rather than a recommendation:
   - **Build sourced knowledge first → Mode A.** Delegate to `anchored-knowledge`, or an equivalent
     knowledge builder, to stand up a source register, anchored entries, ids and open questions.
   - **Proceed now → Mode B or C.** Write from what exists.
3. **Never build without a yes.** Standing up a knowledge system is a substantial, visible change to
   someone's project ([`../principles/delegation-not-inclusion.md`](../principles/delegation-not-inclusion.md)).
4. **On yes, delegate and then re-enter intake from discovery.** The scan now finds the corpus and
   drafts a Mode A config whose `authoritative_sources`, `rule_id_scheme` and `supplemental_sources`
   map onto what the builder produced
   ([`../patterns/knowledge-config.md`](../patterns/knowledge-config.md)).
5. **No builder available?** Offer instead to scaffold a minimal source file, and proceed in the lower
   mode. Say which you did.
6. **One-way handoff.** This skill invokes the builder; it never contains it, and the builder does not
   call back.

**Done when** the user chose, nothing was built without their yes, and either a Mode A config now
exists over a real corpus or the run is proceeding in a named lower mode with its gaps visible.
