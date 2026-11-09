"""Check each skill's `allowed-tools` against the commands its own instructions tell a model to run.

    python3 scripts/check-allowed-tools.py              # every skill
    python3 scripts/check-allowed-tools.py agentic-prd  # one of them

`allowed-tools` narrows what a skill may do while it is active, which makes it the one piece of
front matter that **fails closed**: declare too little and step 1 of a run is denied, with nothing
in the skill's own files to explain why. Declaring it by reading the prose and typing a plausible
list is how that happens, so this reads the prose mechanically instead.

It extracts every command the skill instructs — fenced `bash` blocks anywhere in the skill, and
inline backticked commands in `SKILL.md` and `practices/`, which is where a procedure's steps live —
then asks whether some `Bash(...)` entry covers each one, and whether any entry covers nothing.

**`anti-patterns/` and `principles/` are deliberately not scanned for inline commands.** A command
named there is usually the one the skill is telling you *not* to run: `anchored-knowledge` says
"Never run raw git against a knowledge base" and shows `git add docs/` as the smell, and
`transcript-knowledge-base` says "No `pip install` is needed". Scanning them would demand a
permission for the forbidden thing — the exact inversion this check exists to prevent.

Over-grants are reported too, as warnings rather than errors. An entry nothing instructs is either
dead or a sign the instructions are missing a step; both are worth knowing, neither is a failure.

Exit code 1 on any gap.
"""
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[1]
# Fences whose contents are commands. An unlabelled fence in these skills is almost always a note
# skeleton, so it is not scanned.
SHELL_FENCE = re.compile(r"```(?:bash|sh|shell|console|zsh)\n(.*?)```", re.S)
# These skills write commands as indented blocks as often as fenced ones — every router's `Folders`
# and `Checks` section does. A folder map is indented the same way, but its lines start with a path
# rather than a command head, so HEADS filters them out.
INDENTED = re.compile(r"^(?: {4,}|\t)(\S.*)$", re.M)
INLINE = re.compile(r"`([^`]{1,200})`", re.S)
# Where an inline backtick is a step rather than a mention. `references/` is included because the
# tracker adapters keep their real `az` invocations there.
INLINE_SOURCES = ("SKILL.md", "practices", "references")
# Command heads worth governing. Anything else in a fence — a path, a brace, an assignment — is not
# a command this check knows how to reason about, and guessing would produce noise.
HEADS = {"python", "python3", "pip", "pip3", "uv", "uvx", "az", "gh", "git", "pandoc", "jq",
         "curl", "node", "npm", "make", "pytest", "sha256sum", "shasum", "docker"}
# A skill that hands work to another skill needs the tool that does the handing.
DELEGATION_TOOL = "Skill"


def declared(skill):
    """The `allowed-tools` list, as written. `Bash(a *|b *)` is one entry holding two patterns."""
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    end = text.find("\n---", 4)
    block = text[4:end] if text.startswith("---\n") and end != -1 else ""
    line = re.search(r"^allowed-tools: *(.+)$", block, re.M)
    if not line:
        return None, block
    entries = [e.strip() for e in re.split(r",(?![^(]*\))", line.group(1)) if e.strip()]
    return entries, block


def bash_patterns(entries):
    """Every pattern inside a `Bash(...)` entry, paired with the entry it came from."""
    out = []
    for entry in entries:
        m = re.fullmatch(r"Bash\((.*)\)", entry)
        if m:
            for pattern in m.group(1).split("|"):
                out.append((pattern.strip(), entry))
    return out


def covers(pattern, command):
    """Does one `Bash(...)` pattern allow this command?

    `foo bar *` allows anything starting `foo bar `; `foo bar` allows exactly that. The leading
    tokens must match literally, which is what makes a narrow entry such as `git rev-parse *` mean
    something — it allows the detection the skill needs and denies the commits it forbids.
    """
    body = pattern.strip()
    if body.endswith("*"):
        prefix = body[:-1].rstrip()
        return command == prefix or command.startswith(prefix + " ")
    return command == body


def instructed(skill):
    """Every command the skill tells a model to run, as (command, where)."""
    found = {}
    for path in sorted(skill.rglob("*.md")):
        parts = set(path.relative_to(skill).parts)
        if parts & {"examples", "sample_data", "tests"}:
            continue
        rel = str(path.relative_to(skill))
        text = path.read_text(encoding="utf-8")

        lines = []
        for block in SHELL_FENCE.findall(text):
            lines += block.splitlines()
        lines += INDENTED.findall(re.sub(r"```.*?```", "", text, flags=re.S))
        if rel == "SKILL.md" or rel.split("/")[0] in INLINE_SOURCES:
            lines += [" ".join(m.split()) for m in INLINE.findall(text)]

        for raw in lines:
            command = raw.strip().lstrip("$").strip()
            # A pipeline or a `cd x && y` carries more than one command.
            for piece in re.split(r"&&|\|\||[|;]", command):
                piece = piece.strip()
                tokens = piece.split()
                if not tokens or tokens[0] not in HEADS:
                    continue
                found.setdefault(" ".join(tokens), rel)
    return found


def check(skill):
    findings, warnings = [], []
    entries, block = declared(skill)
    if entries is None:
        return ["SKILL.md: no allowed-tools"], []

    patterns = bash_patterns(entries)
    commands = instructed(skill)
    used = set()
    for command, where in sorted(commands.items()):
        hit = [entry for pattern, entry in patterns if covers(pattern, command)]
        if hit:
            used.update(hit)
        else:
            findings.append(f"{where} instructs `{command}`, which no allowed-tools entry covers — "
                            f"the run would be denied at that step")
    for _, entry in patterns:
        if entry not in used:
            warnings.append(f"{entry} covers nothing the skill instructs")

    # A skill that names a sibling in `metadata.requires` has to be able to invoke one.
    requires = re.search(r"^[ \t]+requires: *\[([^\]]*)\]", block, re.M)
    related = re.search(r"^[ \t]+related: *\[([^\]]*)\]", block, re.M)
    hard = bool(requires and requires.group(1).strip())
    any_sibling = hard or bool(related and related.group(1).strip())
    if hard and DELEGATION_TOOL not in entries:
        findings.append(f"metadata.requires names a skill it will not substitute for, but "
                        f"allowed-tools has no {DELEGATION_TOOL} — the delegation cannot happen")
    if DELEGATION_TOOL in entries and not any_sibling:
        warnings.append(f"{DELEGATION_TOOL} is allowed but no sibling is named in metadata")

    # A skill whose output is a vault reads, writes and locates files.
    if (skill / "references" / "vault-convention.md").exists():
        for tool in ("Read", "Write", "Edit", "Glob", "Grep"):
            if tool not in entries:
                findings.append(f"writes a vault but allowed-tools has no {tool}")
    return findings, warnings


if __name__ == "__main__":
    wanted = sys.argv[1:] or sorted(p.name for p in (REPO / "skills").iterdir()
                                    if (p / "SKILL.md").exists())
    failed = False
    for name in wanted:
        findings, warnings = check(REPO / "skills" / name)
        label = "ok" if not findings else f"{len(findings)} findings"
        print(f"{name}: {label}" + (f", {len(warnings)} warnings" if warnings else ""))
        for f in findings:
            print(f"  {f}")
        for w in warnings:
            print(f"  warning: {w}")
        failed = failed or bool(findings)
    sys.exit(1 if failed else 0)
