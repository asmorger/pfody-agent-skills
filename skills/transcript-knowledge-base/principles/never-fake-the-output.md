# Never fake the output

**Rule.** Confirm Python 3.10+ before the first `tkb.cli` call. If no suitable interpreter exists,
stop, say so, and offer the install paths. Never produce the index, the briefs or the state file by
hand, and never report a run that did not happen.

**Why.** Every guarantee this skill makes comes from the tool: provenance enforcement, change
detection, dedup, markdown escaping. A hand-made file has none of them and is indistinguishable from
a real one, so a faked index poisons the thing a sourced index exists to provide — the ability to
trust it without checking. Stopping is also cheap and recoverable: the user installs Python and the
run proceeds. A fabricated index is discovered weeks later, by which point stories cite it.

**In the index.**
- Check once, first: `python --version`, falling back to `python3` or `py -3`. Use whichever command
  worked for every later call ([`../practices/confirm-python.md`](../practices/confirm-python.md)).
- An older interpreter: look for `python3.11`, `py -3.11` and so on before concluding there is none.
- No interpreter: offer `winget install Python.Python.3.12`, `brew install python@3.12`, or the
  distribution's package manager, then wait and re-run the preflight.
- No `pip install` is needed. The tool is standard library only, which removes the usual reason to
  work around a missing dependency.
- The same honesty applies to a partial run: report which files errored in the manifest rather than
  filling their items in ([`../practices/diagnose-a-failed-run.md`](../practices/diagnose-a-failed-run.md)).

**Breaks when.** The index is written by hand because the tool would not run →
[`../anti-patterns/faking-the-output-when-python-is-missing.md`](../anti-patterns/faking-the-output-when-python-is-missing.md).
