"""Check the layout contract the skills are written to: relative links resolve, link labels match
their targets, and no router or folder file has outgrown its size limit.

    python3 scripts/check-skill-layout.py              # every skill
    python3 scripts/check-skill-layout.py agentic-prd  # one of them

Templates, worked examples and prompts are exempt from the size limit — they are artifacts a project
copies, not files a model reads to learn a rule. Exit code 1 on any finding.
"""
import os, re, sys, pathlib

REPO = pathlib.Path(__file__).resolve().parents[1]
FOLDERS = ("principles", "patterns", "practices", "anti-patterns")
EXEMPT = ("assets/", "references/", "reference/", "prompts/", "sample_data/", "examples/")
LIMITS = {"SKILL.md": 100, "folder": 60}

LINK = re.compile(r"\[`([^`]+)`\]\(([^)]+)\)")
BARE = re.compile(r"`((?:" + "|".join(FOLDERS) + r"|references|reference|assets|scripts|evals|prompts)/[A-Za-z0-9._/-]+)`")


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
            if not str(rel).startswith(EXEMPT) and text.count("\n") > limit:
                findings.append(f"{rel}: {text.count(chr(10))} lines, limit {limit}")
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
