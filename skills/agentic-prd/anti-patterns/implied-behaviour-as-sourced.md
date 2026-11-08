# Implied behaviour as sourced

**Smell.** A requirement with a clean `SRC-07 @14:02` whose source, at 14:02, does not say it. The
source mentions a void button; the requirement specifies who may void. The source names a report; the
requirement specifies its columns. Every step is reasonable and the citation is real — it just does
not cover the sentence it is attached to.

**Why it is wrong.** This is the one defect no reviewer catches and no script can catch. The citation
makes the requirement look checked, so nobody opens the source; the script confirms the locator
exists, which is all it can confirm. The requirement is then built, tested and accepted, and the
first person to notice is the stakeholder who never agreed to it. It is also how an inference becomes
precedent: the next requirement cites this one's neighbourhood, and the drift compounds.

**Instead.** Quote the sentence to yourself before writing the citation. If you cannot, the source
does not state it: mark the requirement `PROPOSED`, or raise an open question and let a person
promote it. An honest `PROPOSED` is often approved in one message — it is the dressing-up that costs
a release
([`../principles/implied-is-not-stated.md`](../principles/implied-is-not-stated.md),
[`../practices/cite-a-source.md`](../practices/cite-a-source.md)).
