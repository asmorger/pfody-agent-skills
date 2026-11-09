# A dangling citation

**Smell.** `(see [[ORDER-9]])` rendering as unlinked text. `sources: ["[[sow-v3]]"]` where the note
is called `order-fulfilment-sow-v3`. A rule citing `[[ADR-0007]]` that was never written. In
Obsidian it looks almost right — slightly dimmer, and easy to read past.

**Why it is wrong.** This record is cited by builds. A story's source grounding, an acceptance
criterion and a test all resolve ids through it, so a dangling link is a claim of provenance with
nothing behind it — and it reads as checked. The usual cause makes it worse: the link was written
before the note, the note never arrived, and the rule now looks anchored to a source that does not
exist. In a zettelkasten a dangling link is a deliberate placeholder for a note you intend to write.
A record of what a client agreed to is not a zettelkasten in that respect.

**Instead.** Write the target note, or do not write the link. Where the target is a real intention
rather than a real note, say so in prose — "partial despatch is unaddressed; no question raised yet"
— so a reader sees an absence rather than a broken reference. Check links before promoting, and run
the vault lint at every audit; dangling links are the one finding that is fully mechanical to detect
([`../principles/links-are-the-structure.md`](../principles/links-are-the-structure.md),
[`../practices/audit-the-base.md`](../practices/audit-the-base.md)).
