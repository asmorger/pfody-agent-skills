"""Check the layout contract the skills are written to: front matter is well formed, relative links
resolve, link labels match their targets, and no router or folder file has outgrown its size limit.

    python3 scripts/check-skill-layout.py              # every skill
    python3 scripts/check-skill-layout.py agentic-prd  # one of them

Templates, worked examples and prompts are exempt from the size limit — they are artifacts a project
copies, not files a model reads to learn a rule. Exit code 1 on any finding.

The front matter checks exist because nothing read it before. `user-story-builder`'s description was
1027 characters against a 1024 cap, and `transcript-knowledge-base`'s non-negotiables ran
1 2 3 4 5 7 8 9 10 — two defects in files that four other checkers walked over every run, because
every one of them started after the closing `---`.
"""
import os, re, sys, pathlib

REPO = pathlib.Path(__file__).resolve().parents[1]
FOLDERS = ("principles", "patterns", "practices", "anti-patterns")
EXEMPT = ("assets/", "references/", "reference/", "prompts/", "sample_data/", "examples/")
# The budget is on the body. Front matter is metadata the harness reads, not prose a model reads to
# learn a rule, so `allowed-tools` and `metadata` do not spend the router's line budget.
LIMITS = {"SKILL.md": 100, "folder": 60}
DESCRIPTION_LIMIT = 1024
# A sibling skill is named by its folder; anything else a skill delegates to has to be listed here,
# so `metadata.requires` cannot quietly name something that does not exist.
EXTERNAL_SKILLS = {"git-guide"}

LINK = re.compile(r"\[`([^`]+)`\]\(([^)]+)\)")
BARE = re.compile(r"`((?:" + "|".join(FOLDERS) + r"|references|reference|assets|scripts|evals|prompts)/[A-Za-z0-9._/-]+)`")


def folded(block, key):
    """A YAML folded scalar (`key: >`) as the harness will see it: newlines become spaces.

    Written by hand rather than with PyYAML so the checks run on a bare interpreter, which is what
    every other script in this repo assumes.
    """
    lines = block.split("\n")
    try:
        start = lines.index(f"{key}: >")
    except ValueError:
        return None
    out = []
    for line in lines[start + 1:]:
        if re.match(r"^[a-z][a-z-]*:", line):
            break
        out.append(line.strip())
    return " ".join(x for x in out if x) + "\n"


def check_frontmatter(skill_dir, skill):
    """The part of SKILL.md no checker used to read."""
    findings = []
    text = skill.read_text()
    if not text.startswith("---\n"):
        return ["SKILL.md: no front matter"]
    end = text.find("\n---", 4)
    if end == -1:
        return ["SKILL.md: front matter is not closed"]
    block, body = text[4:end], text[end + 4:]

    name = re.search(r"^name: *(\S+)", block, re.M)
    if not name:
        findings.append("SKILL.md: no name")
    elif name.group(1) != skill_dir.name:
        findings.append(f"SKILL.md: name '{name.group(1)}' is not the folder name "
                        f"'{skill_dir.name}' — the folder is what a project installs")

    description = folded(block, "description")
    if description is None:
        findings.append("SKILL.md: no description, or it is not a `description: >` block")
    elif len(description) > DESCRIPTION_LIMIT:
        findings.append(f"SKILL.md: description is {len(description)} characters, limit "
                        f"{DESCRIPTION_LIMIT} — it is what the model matches a task against, and an "
                        f"over-long one may be rejected or truncated")

    if not re.search(r"^allowed-tools:", block, re.M):
        findings.append("SKILL.md: no allowed-tools — the skill's tool needs are documented in "
                        "prose but nothing declares them")

    # `metadata.requires` replaces the "Related skills" prose as the record of what a skill
    # delegates to. Prose cannot be checked; a list can.
    if not re.search(r"^metadata:", block, re.M):
        findings.append("SKILL.md: no metadata block")
    siblings = {p.name for p in (REPO / "skills").iterdir() if (p / "SKILL.md").exists()}
    for key in ("requires", "related"):
        found = re.search(rf"^[ \t]+{key}: *\[([^\]]*)\]", block, re.M)
        if not found:
            findings.append(f"SKILL.md: no metadata.{key} — use `{key}: []` where there is none")
            continue
        for dep in [d.strip() for d in found.group(1).split(",") if d.strip()]:
            if dep not in siblings | EXTERNAL_SKILLS:
                findings.append(f"SKILL.md: metadata.{key} names '{dep}', which is neither a "
                                f"skill in this repo nor a declared external")
            if dep == skill_dir.name:
                findings.append(f"SKILL.md: metadata.{key} names itself")

    # The non-negotiables are a numbered list a reader counts on. `transcript-knowledge-base` ran
    # 1 2 3 4 5 7 8 9 10 for as long as nothing counted them.
    section = re.search(r"## Non-negotiables\n(.*?)(?=\n## |\Z)", body, re.S)
    if section:
        nums = [int(n) for n in re.findall(r"^(\d+)\. ", section.group(1), re.M)]
        if nums != list(range(1, len(nums) + 1)):
            findings.append(f"SKILL.md: the non-negotiables are numbered {nums}, not 1..n")
    return findings


def check(skill_dir):
    findings = []
    for dirpath, dirnames, filenames in os.walk(skill_dir):
        dirnames[:] = [d for d in dirnames if d not in ("__pycache__", ".knowledge-index.work")]
        for name in sorted(filenames):
            if not name.endswith(".md"):
                continue
            path = pathlib.Path(dirpath) / name
            rel = path.relative_to(skill_dir)
            text = path.read_text()
            limit = LIMITS["SKILL.md"] if rel.name == "SKILL.md" else LIMITS["folder"]
            body = text
            if rel.name == "SKILL.md" and text.startswith("---\n"):
                end = text.find("\n---", 4)
                body = text[end + 4:] if end != -1 else text
            if not str(rel).startswith(EXEMPT) and body.count("\n") > limit:
                findings.append(f"{rel}: {body.count(chr(10))} body lines, limit {limit}")
            fenced = False
            for n, line in enumerate(text.splitlines(), 1):
                if line.startswith("```"):
                    fenced = not fenced
                if fenced:
                    continue
                for label, target in LINK.findall(line):
                    t = target.split("#")[0]
                    if t.startswith("http") or not t:
                        continue
                    if not (pathlib.Path(dirpath) / t).exists():
                        findings.append(f"{rel}:{n}: broken link {t}")
                    elif label != t:
                        findings.append(f"{rel}:{n}: label `{label}` does not match target {t}")
                for bare in BARE.findall(line):
                    if not ((skill_dir / bare).exists() or (pathlib.Path(dirpath) / bare).exists()):
                        findings.append(f"{rel}:{n}: names a file that does not exist: {bare}")
    skill = skill_dir / "SKILL.md"
    if not skill.exists():
        findings.append("no SKILL.md")
    else:
        findings += check_frontmatter(skill_dir, skill)
    if not (skill_dir / "evals/trigger-queries.json").exists():
        findings.append("no evals/trigger-queries.json")
    for folder in FOLDERS:
        if not (skill_dir / folder).is_dir():
            findings.append(f"no {folder}/")
    return findings


if __name__ == "__main__":
    wanted = sys.argv[1:] or sorted(p.name for p in (REPO / "skills").iterdir() if (p / "SKILL.md").exists())
    failed = False
    for name in wanted:
        findings = check(REPO / "skills" / name)
        print(f"{name}: {'ok' if not findings else str(len(findings)) + ' findings'}")
        for f in findings:
            print(f"  {f}")
        failed = failed or bool(findings)
    sys.exit(1 if failed else 0)
