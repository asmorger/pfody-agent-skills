# A vague role

**Smell.** "As a user…" "As a system administrator…" "As a stakeholder…" — in a project whose config
lists shipping clerks, support agents and operations leads.

**Why it is wrong.** The role is what carries the context: what the person can see, what they are
trying to achieve, what permissions apply, what the demo looks like. "A user" implies none of it, so
the developer supplies the missing context themselves — usually by imagining the most capable user,
which is how a clerk's screen acquires an operations lead's controls. It also makes the permission
bullet unanswerable, and an unanswerable permission bullet gets inferred.

**Instead.** Take the role from the config's persona vocabulary, and distinguish external end users
from internal staff — they almost never want the same thing. Where the source genuinely does not say
which role, that is an Open Question, because the answer changes the permission behaviour. "A user" is
acceptable only when the config says the system has exactly one kind
([`../patterns/as-a-i-want-so-that.md`](../patterns/as-a-i-want-so-that.md),
[`../principles/vocabulary-comes-from-the-config.md`](../principles/vocabulary-comes-from-the-config.md)).
