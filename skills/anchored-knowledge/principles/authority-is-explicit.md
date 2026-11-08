# Authority is explicit

**Rule.** Every source gets an authority level when it is registered, from the project's ladder. The
level is recorded on the Source Register row, not inferred at the moment it matters.

**Why.** A conflict is settled by authority, and authority is a fact about where a statement came
from — a contract clause, an approved requirement, a named stakeholder's answer, an export, somebody's
interpretation, an unreviewed note. Recorded up front, the comparison is mechanical. Judged later, it
becomes an argument about how much to trust a document, conducted by whoever happens to be reading,
and the answer drifts. Writing the level down also exposes the base's weak foundations honestly: a
rule set resting on level 5 and 6 sources is a rule set nobody has confirmed, and that is worth
seeing.

**In the base.**
- The default ladder, strongest first: contractual baseline (SOW or signed change request) · approved
  requirements · client clarification · source artifact · internal interpretation · unreviewed intake
  ([`../patterns/authority-ladder.md`](../patterns/authority-ladder.md)).
- The ladder is overridable per project in the config. An internal project with no SOW names what
  serves as its scope baseline instead.
- Find the scope baseline during bootstrap. If you cannot, ask what it is and where it lives, and
  record the answer ([`../practices/bootstrap-a-base.md`](../practices/bootstrap-a-base.md)).
- Seed the Source Register highest authority first, so the base is built from its baseline outward.

**Breaks when.** Two sources are weighed without their levels →
[`../anti-patterns/resolving-a-conflict-silently.md`](../anti-patterns/resolving-a-conflict-silently.md).
