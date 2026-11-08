# Config before anything

**Rule.** Every run starts by locating the base and loading its config. Nothing is read, drafted or
written first. If no config exists, provision one with the user — discover, propose, confirm, save —
and only then continue with what they actually asked for.

**Why.** Every path, filename, id prefix and authority ladder in this skill differs per project, and
a wrong guess is expensive in a specific way: it writes a second knowledge base beside the real one.
The project then has two `business-rules.md` files, two id schemes and no source of record, which is
the exact failure the base exists to prevent. The config is also what makes the skill consistent
across runs — a second session reads the same file and reaches the same folders instead of
rediscovering them differently.

**In the base.**
- Look for the config in `docs/`, then `Knowledge/`, then `.claude/`, in that order; first found wins
  ([`../practices/locate-the-base.md`](../practices/locate-the-base.md)).
- Found: validate that the paths it names still exist, then proceed. A missing folder is flagged to
  the user, not silently cited as nothing.
- Not found: run intake once. Re-run it only on an explicit "reconfigure", or when `config_version`
  is older than the template's.
- Ask about what discovery cannot settle: the base location, the SOW's name and location, the id
  scheme, the transcripts folder.
- Intake is a means, not the deliverable. Save the config, show the path, then answer the original
  request in the same turn.

**Breaks when.** A default is assumed rather than confirmed →
[`../anti-patterns/guessing-the-base-location.md`](../anti-patterns/guessing-the-base-location.md).
