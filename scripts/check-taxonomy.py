"""Check the shared note taxonomy: one registry, four identical copies, and nothing contradicting it.

    python3 scripts/check-taxonomy.py              # exit 1 on any finding
    python3 scripts/check-taxonomy.py --fix        # push the canonical file to the skill copies

`shared/vault-taxonomy.json` declares, per note type, the owning skill, the folder, the id pattern,
the status vocabulary, the grouping key, whether the type is citable and its body budget. Each skill
carries a byte-identical copy at `references/vault-taxonomy.json`, because a skill has to work when
it is the only one installed; this script is what stops those copies becoming four registries.

It exists because they already had. The same three shared types carried two id widths (`SRC-01` and
`SRC-0001`), two prefixes for one decision (`DEC-02` and `ADR-0004`), two status casings, and the
knowledge base's linter called six of the PRD's types `unknown type` although both skills write into
one `docs/` tree. Every one of those was documented in prose, in two places, and no check could
compare two prose files.

What it checks:

1. **The copies.** Byte-identical to the canonical file. `--fix` rewrites them.
2. **Every front matter block in every skill**, the worked examples and the skeletons inside fenced
   blocks alike: the type exists, the status is in its vocabulary, the id matches its pattern, a
   type with no id pattern carries no id, and the grouping key is present. A skeleton is what a
   model copies, so a skeleton that contradicts the registry is the defect that ships.
3. **The inline vocabulary comments.** `status: accepted  # draft | accepted | retired` is a second
   copy of the status set, written where a reader believes it. It must equal the registry's.
4. **The folders**, in the worked example vaults: a note of a type lives in that type's folder. This
   is what catches one decision filed as a source in one vault and as a decision in another.
"""
import argparse
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[1]
CANON = REPO / "shared" / "vault-taxonomy.json"
# Every file a skill carries a byte-identical copy of, so that it installs on its own without the
# shared contract becoming four contracts. `vaultlib.py` joined the registry when three scripts'
# duplicated parsers, link readers and provenance stampers were extracted into it.
SHARED = ("vault-taxonomy.json", "vaultlib.py")
# Where each one is copied to inside a skill.
COPY_DIR = {"vault-taxonomy.json": "references", "vaultlib.py": "scripts"}
# A frontmatter block, at the top of a note or inside a fenced skeleton.
BLOCK = re.compile(r"(?:\A|\n)---\n(.*?)\n---(?:\n|\Z)", re.S)
# `status: accepted          # draft | accepted | retired`
VOCAB_COMMENT = re.compile(r"^status: *\S+ *# *([a-z|\- ]+)$", re.M)
# A value a skeleton leaves for the author to fill: `<owner>`, `SRC-NNNN`, `ADR-xxxx`, `TBD`, blank.
PLACEHOLDER = re.compile(r"^(|<.*>|\.\.\.|TBD|tbd|[A-Z][A-Z0-9]*-[NnXx]+)$")


def field(block, key):
    m = re.search(rf"^{key}: *([^\n#]*?) *(?:#.*)?$", block, re.M)
    return m.group(1).strip().strip("\"'") if m else None


def check_copies(fix):
    """Each skill's copy of every shared file is byte-identical to the canonical one.

    `vaultlib.py` is only copied into a skill whose scripts import it; a skill with no scripts of
    its own is not expected to carry one.
    """
    findings = []
    for name in SHARED:
        canonical = (REPO / "shared" / name).read_text(encoding="utf-8")
        where = COPY_DIR[name]
        for skill in sorted((REPO / "skills").iterdir()):
            if not (skill / "SKILL.md").exists():
                continue
            copy = skill / where / name
            if not copy.exists():
                if name == "vaultlib.py" and not list(skill.glob("scripts/*.py")):
                    continue        # no scripts, so nothing to import it
                if fix:
                    copy.parent.mkdir(parents=True, exist_ok=True)
                    copy.write_text(canonical, encoding="utf-8")
                else:
                    findings.append(f"{skill.name}: {where}/{name} is missing — the skill cannot "
                                    f"be installed on its own without it")
                continue
            if copy.read_text(encoding="utf-8") != canonical:
                if fix:
                    copy.write_text(canonical, encoding="utf-8")
                else:
                    findings.append(f"{skill.name}: {where}/{name} has drifted from shared/{name} "
                                    f"— run --fix, or move the edit into the canonical file")
    return findings


def check_block(rel, block, types, in_example_vault, path):
    """One front matter block against the registry. Returns findings."""
    findings = []
    name = field(block, "type")
    if name is None:
        return findings
    if name not in types:
        return [f"{rel}: unknown type '{name}' — add it to shared/vault-taxonomy.json or fix the "
                f"note"]
    spec = types[name]

    status = field(block, "status")
    if status and "|" in status:
        # A template whose value *is* the vocabulary. Still a second copy, so still compared.
        listed = [p.strip() for p in status.split("|") if p.strip()]
        if listed != list(spec["status"]):
            findings.append(f"{rel}: the status vocabulary written here disagrees with the "
                            f"registry for '{name}' ({' | '.join(spec['status'])})")
    elif status and not PLACEHOLDER.match(status):
        if status not in spec["status"]:
            allowed = " | ".join(spec["status"]) or "(none — this type has no status)"
            findings.append(f"{rel}: status '{status}' is not valid for '{name}' ({allowed})")
    # The inline comment is a second copy of the vocabulary, written where a reader believes it.
    for shown in VOCAB_COMMENT.findall(block):
        listed = [p.strip() for p in shown.split("|") if p.strip()]
        if listed and listed != list(spec["status"]):
            findings.append(f"{rel}: the `# {shown.strip()}` comment disagrees with the registry "
                            f"for '{name}' ({' | '.join(spec['status'])})")

    ident = field(block, "id")
    pattern = spec["id"]
    if ident and not PLACEHOLDER.match(ident):
        if pattern and not re.fullmatch(pattern, ident):
            findings.append(f"{rel}: id '{ident}' does not match the {name} pattern {pattern}")
        if not pattern:
            findings.append(f"{rel}: '{name}' is cited by file name and carries no id, but this "
                            f"one has id '{ident}'")
        aliases = field(block, "aliases") or ""
        if ident not in aliases:
            findings.append(f"{rel}: id '{ident}' is not in aliases")
    elif pattern and in_example_vault:
        findings.append(f"{rel}: a '{name}' carries an id matching {pattern}")

    key = spec["group-by"]
    if key:
        # The key must appear wherever the shape is written down, so an author copying a skeleton
        # cannot omit it without noticing. A template may leave the value as `<topic>`; a note in a
        # worked example may not, because a worked example is a vault.
        value = field(block, key)
        if value is None:
            findings.append(f"{rel}: no '{key}' — '{name}' is grouped by it, and there is no "
                            f"`tags` property to fall back on")
        elif PLACEHOLDER.match(value) and in_example_vault:
            findings.append(f"{rel}: '{key}' is still a placeholder")

    if in_example_vault and spec["folder"] not in (".", None):
        folder = path.parent.name
        if folder != spec["folder"]:
            findings.append(f"{rel}: a '{name}' belongs in {spec['folder']}/, not in {folder}/ — "
                            f"one folder per type, or two skills grow two registers for it")
    return findings


def check_shared_notes(types):
    """A note two skills both write is one note, so their worked examples must agree about it.

    The repo says it in prose — "where two skills write the same kind of note they write the same
    note, in the same folder, with the same type" — and its own examples used to contradict it:
    `questions/who-may-void-a-printed-label.md` existed in two vaults as `Q-0003` and `Q-03`, with
    different owners and a different heading, and one decision was written down twice as `ADR-0004`
    and `DEC-02`.

    A shared note cannot be byte-identical across two standalone examples, because each vault only
    holds the links its own layer has. What must agree is everything the registry governs: the
    type, the status, the id and the grouping key. That is the part a combined vault merges on.
    """
    findings = []
    by_rel = {}
    for skill in sorted((REPO / "skills").iterdir()):
        vault = skill / "examples" / "vault"
        if not vault.is_dir():
            continue
        for path in sorted(vault.rglob("*.md")):
            blocks = BLOCK.findall(path.read_text(encoding="utf-8"))
            if not blocks:
                continue
            name = field(blocks[0], "type")
            if name not in types:
                continue
            governed = (name, field(blocks[0], "status"), field(blocks[0], "id"),
                        field(blocks[0], types[name]["group-by"] or "type"))
            key = str(path.relative_to(vault))
            if key in by_rel:
                other_skill, other = by_rel[key]
                if other != governed:
                    findings.append(
                        f"{key}: {skill.name} and {other_skill} disagree about a note they both "
                        f"write — (type, status, id, grouping key) is {governed} here and {other} "
                        f"there. One note, or two registers for one fact.")
            else:
                by_rel[key] = (skill.name, governed)
    return findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true",
                    help="rewrite each skill's copy from the canonical file")
    args = ap.parse_args()

    tax_text = CANON.read_text(encoding="utf-8")
    types = json.loads(tax_text)["types"]
    findings = check_copies(args.fix)

    for path in sorted((REPO / "skills").rglob("*.md")):
        rel = path.relative_to(REPO)
        parts = set(rel.parts)
        # A worked example is a real vault and is held to everything. A skeleton in `patterns/` is
        # what a model copies, so it is held to the vocabularies but not to the folder map.
        in_example_vault = "examples" in parts and "vault" in parts
        for block in BLOCK.findall(path.read_text(encoding="utf-8")):
            findings += check_block(rel, block, types, in_example_vault, path)

    findings += check_shared_notes(types)

    for f in sorted(set(findings)):
        print(f"  {f}")
    copies = sum(len(list((REPO / "skills").glob(f"*/{COPY_DIR[n]}/{n}"))) for n in SHARED)
    print(f"{len(set(findings))} findings." if findings else
          f"ok — {len(types)} types, {len(SHARED)} shared files, {copies} identical copies.")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
