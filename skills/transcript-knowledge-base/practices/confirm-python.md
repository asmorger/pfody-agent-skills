# Confirm Python

**When** once, before the first `tkb.cli` call of a session. Step 0.

**Why.** Everything this skill guarantees comes from the tool. Discovering halfway through that it
cannot run is the moment where hand-writing the index becomes tempting, and a hand-written index is
indistinguishable from a real one.

**Steps.**

1. **Check the version:**

       python --version        # need 3.10+; also try python3 or py -3

2. **3.10 or newer** → go to [`prepare-the-briefs.md`](prepare-the-briefs.md). Use whichever command
   worked — `python`, `python3`, `py -3` — for every command in this skill.
3. **Older** → look for a newer one that is already installed: `python3.11`, `python3.12`, `py -3.11`.
4. **None found** → **stop and tell the user.** Offer the install paths and wait, then re-run this
   preflight:
   - Windows: `winget install Python.Python.3.12`, or python.org with "Add python.exe to PATH"
     ticked. Open a new terminal afterwards.
   - macOS: `brew install python@3.12`, or python.org.
   - Linux: `sudo apt install python3`, `sudo dnf install python3`, or the distribution's own.
5. **Do not install anything with pip.** The tool is standard library only; `requirements.txt` lists
   optional extras, and PDF or YAML support is not needed for a normal run.
6. **Never fake the output** while waiting
   ([`../principles/never-fake-the-output.md`](../principles/never-fake-the-output.md)).

**Done when** a 3.10+ interpreter is confirmed and you know which command invokes it, or the user has
been told plainly that the run cannot proceed and what to install.
