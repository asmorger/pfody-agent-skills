# Re-running intake every time

**Smell.** The user asks for a story and gets a round of configuration questions — again — on a
project that was configured last week. Or a config written to a path the detection order does not
check, so every run rediscovers nothing.

**Why it is wrong.** It is the failure that gets a skill abandoned. The second round of questions
reads as not having been listened to, and the usual response is to stop invoking the skill and write
the story by hand. There is a correctness cost too: answers given twice diverge, so the project ends
up with two different ideas of which sources are authoritative, and the stories drift with them.

**Instead.** Detect, confirm, save — **once**. Write the config to a detected path with its
`config_version` stamp, and on a later run validate it and proceed. Re-run intake only on an explicit
"reconfigure" or a version older than the template's. Where validation finds a moved path, fix that
one field rather than restarting the interview, and remember that intake is a means — save it, show
the path, and answer the original request in the same turn
([`../principles/detect-confirm-save.md`](../principles/detect-confirm-save.md),
[`../practices/load-or-provision-the-config.md`](../practices/load-or-provision-the-config.md)).
