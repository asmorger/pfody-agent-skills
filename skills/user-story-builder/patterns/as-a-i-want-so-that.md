# As a / I want / So that

**Use when** writing the opening sentence. Three parts, each with its own failure mode. Never cite a
source in it.

**Skeleton.**

    As a <specific role from the config>, I want to <need, not solution>, so that <business outcome
    that does not restate the need>.

    Good:  As a shipping clerk, I want to void a label I have already printed, so that a cancelled
           order is not collected by the carrier.
    Good:  As an operations lead, I want to see label costs by week, so that I can challenge the
           carrier's invoice.

    Bad:   As a user, I want a table with filters showing label data, so that I can see the label
           list.
           — vague role; a UI instead of a need; a circular "so that".

**Notes.**
- **Role**: specific and contextual, from the config's `roles`. Distinguish external users from
  internal staff. "A user" or "an administrator" where a better word exists is a finding
  ([`../anti-patterns/a-vague-role.md`](../anti-patterns/a-vague-role.md)).
- **Need**: the need, not the technology or the screen. Avoid `manage`, `handle`, `deal with`; prefer
  `view`, `submit`, `approve`, `configure`, `filter`, `receive`
  ([`../anti-patterns/a-solution-prescriptive-need.md`](../anti-patterns/a-solution-prescriptive-need.md)).
- **Outcome**: the real business reason. The test: if the *so that* could swap into the *I want to*
  and still make sense, it is circular — rewrite
  ([`../anti-patterns/circular-so-that.md`](../anti-patterns/circular-so-that.md)).
- Roles come from the config, never from this file's examples
  ([`../principles/vocabulary-comes-from-the-config.md`](../principles/vocabulary-comes-from-the-config.md)).

**Related.** [`user-story.md`](user-story.md),
[`../practices/review-an-existing-story.md`](../practices/review-an-existing-story.md).
