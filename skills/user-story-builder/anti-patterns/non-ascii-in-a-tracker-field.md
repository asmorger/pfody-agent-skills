# Non-ASCII in a tracker field

**Smell.** A published acceptance criterion reading `Given a clerkâ€™s printed label, when â€¦`. Curly
quotes, em dashes, `§`, arrows and ellipses sent straight from the markdown into the tracker. The
publish reported success.

**Why it is wrong.** On Windows the encoding hops between the CLI, the shell and the tracker's API
corrupt non-ASCII characters silently — nothing errors, and the damage is only visible in the tracker
afterwards, inside a field a developer is about to work from. A mangled criterion is worse than a
missing one, because it still reads as instructions. The failure is also platform-dependent, so it
passes on the author's machine and appears on a colleague's.

**Instead.** Normalise every rich-text field to pure ASCII before sending: straight quotes, `-` for
dashes, `->` for arrows, `"Section"` for `§`, `...` for an ellipsis. Do it after the markdown is final
and before the conversion to the tracker's markup, so nothing reintroduces a character afterwards, and
apply it to every field — criteria, notes, assumptions, the demo scenario — not only the description.
Then verify by reading the created item back
([`../principles/tracker-text-is-ascii.md`](../principles/tracker-text-is-ascii.md),
[`../references/adapters/azure-devops.md`](../references/adapters/azure-devops.md)).
