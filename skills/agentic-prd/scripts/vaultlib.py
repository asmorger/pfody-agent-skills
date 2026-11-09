"""The vault primitives every skill's checker needs: notes, links, front matter, generated blocks.

`anchored-knowledge`'s `vault.py`, `agentic-prd`'s `prd.py` and `user-story-builder`'s `story.py`
each held their own copy of this — three front matter parsers, three wikilink readers, three
provenance stampers, three implementations of the one taxonomy check. They had already drifted:
two spellings of the same finding, two sort keys, and a `title` cell that collapsed whitespace in
one script and not in another, which would have ended a table row early the day a heading wrapped.

Each skill carries a byte-identical copy at `scripts/vaultlib.py`, because a skill has to work when
it is the only one installed, and the repo's `check-taxonomy.py` fails when a copy drifts. Same
discipline as `vault-taxonomy.json`: one source, copies checked.

**What is not here.** Each `moc` generator stays in its own script. They differ on purpose — one
stamps the marker with a date and reads `as-of`, one leaves the marker alone; one builds a coverage
table from requirement notes, one refuses to touch a snapshot it does not own. Those are decisions
about a particular vault, not primitives. What is shared is everything underneath them, including
the row and cell rendering, so that two generators writing one index cannot disagree about it.

Standard library only, Python 3.10+.
"""
from __future__ import annotations

import collections
import datetime
import hashlib
import json
import os
import pathlib
import re
import sys

UNLIMITED = 10 ** 6
DEFAULT_BODY_LIMIT = 25

WIKILINK = re.compile(r"(!?)\[\[([^\]|#]+)(#[^\]|]*)?(?:\|([^\]]*))?\]\]")
GEN = re.compile(r"(<!-- generated:[^\n]*-->\n)(.*?)(<!-- /generated -->)", re.S)
GEN_BLOCK = re.compile(r"<!-- generated:.*?<!-- /generated -->", re.S)
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.M)
BLOCK_ID = re.compile(r"(?:^|\s)\^([A-Za-z0-9-]+)\s*$", re.M)
FENCED = re.compile(r"```.*?```", re.S)
# Display text shaped like an id: a prefix, a dash, digits. `[[one-label-per-order|LABEL-9]]` is a
# lie the reader cannot see, because the link still opens the right note.
IDLIKE = re.compile(r"^[A-Z][A-Za-z]*-\d+$")
# Provenance on a generated note, so a stale block is provable rather than a judgement call.
PROV = ("generator", "generated", "input-paths", "input-manifest-sha256", "managed-block-sha256")


# ---------------------------------------------------------------------------- #
# The taxonomy
# ---------------------------------------------------------------------------- #
def taxonomy(script_file: str) -> dict:
    """The shared note taxonomy, read from the calling skill's copy of the registry.

    `script_file` is the caller's `__file__`. The skill-local copy is tried first, so a skill
    installed on its own still works; the repo's canonical file is the fallback for a checkout.
    """
    here = pathlib.Path(script_file).resolve()
    for path in (here.parent.parent / "references" / "vault-taxonomy.json",
                 here.parents[3] / "shared" / "vault-taxonomy.json"):
        if path.is_file():
            return json.loads(path.read_text(encoding="utf-8"))
    sys.exit(f"{here.name}: references/vault-taxonomy.json is missing — copy it from the skill "
             f"folder")


class Taxonomy:
    """The registry, in the shapes a checker actually indexes by."""

    def __init__(self, script_file: str):
        self.raw = taxonomy(script_file)
        self.types = self.raw["types"]
        self.status = {name: set(spec["status"]) for name, spec in self.types.items()}
        self.status_order = {name: tuple(spec["status"]) for name, spec in self.types.items()}
        self.id_pattern = {name: spec["id"] for name, spec in self.types.items()}
        self.group_by = {name: spec["group-by"] for name, spec in self.types.items()}
        self.authority = set(self.raw["authority"])
        self.citable = {name for name, spec in self.types.items() if spec["citable"]}
        self.body_limit = {name: (UNLIMITED if spec["body-budget"] is None else spec["body-budget"])
                           for name, spec in self.types.items()}
        self.citable_id = tuple(spec["id"] for spec in self.types.values()
                                if spec["citable"] and spec["id"])


# ---------------------------------------------------------------------------- #
# Front matter and links
# ---------------------------------------------------------------------------- #
def refs(text: str) -> list[dict]:
    """Every wikilink, with its anchor and display text, outside fenced code."""
    out = []
    # A link inside a table cell escapes its pipe as `\|`. Unescape first, or the target captures
    # the backslash and every generated index reads as a vault full of dangling links.
    for m in WIKILINK.finditer(FENCED.sub("", text).replace("\\|", "|")):
        embed, target, anchor, display = m.groups()
        out.append({"embed": bool(embed), "target": target.strip(),
                    "anchor": (anchor or "")[1:].strip(),
                    "display": (display or "").replace("\\|", "|").strip(),
                    "raw": m.group(0)})
    return out


def norm_anchor(text: str) -> str:
    """Compare a heading the way Obsidian's anchors do: punctuation out, case and spacing flat."""
    return re.sub(r"\s+", " ", re.sub(r"[#|^:\[\]]|%%", " ", text)).strip().lower()


def split_front_matter(text: str):
    """Front matter as a flat dict. Scalars, inline lists and one level of nesting; no YAML dep."""
    meta, body = {}, text
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            raw, body = text[4:end], text[end + 4:].lstrip("\n")
            parent = None
            for line in raw.splitlines():
                if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
                    continue
                indented = line[0] in " \t"
                key, _, val = line.strip().partition(":")
                key, val = key.strip(), val.strip()
                if indented and parent is not None and isinstance(meta.get(parent), dict):
                    meta[parent][key] = scalar(val)
                    continue
                if val == "":
                    parent, meta[key] = key, {}
                else:
                    parent, meta[key] = None, scalar(val)
            # `key:` with nothing under it is an empty value, not an empty mapping. Left as {} it
            # reads as truthy, and every "is this field filled in?" check silently passes. That is
            # the bug `check-vault-tools.py` was written for, and its guard asserts this survives.
            for key, value in list(meta.items()):
                if value == {}:
                    meta[key] = ""
    return meta, body


def scalar(val: str):
    val = val.strip()
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1].strip()
        return [p.strip().strip("\"'") for p in inner.split(",") if p.strip()] if inner else []
    return val.strip("\"'")


def as_list(val):
    if val is None or val == "":
        return []
    return val if isinstance(val, list) else [val]


def ids_in(val) -> list[str]:
    """Every id named in a property, whether written as a wikilink or bare.

    Under the `[[stem|ID]]` convention the id is the link's *display* text, not its target, so read
    the display first and fall back to the target for a link that carries no id.
    """
    out = []
    for item in as_list(val):
        text = str(item)
        found = [(r["display"] if IDLIKE.match(r["display"]) else r["target"]) for r in refs(text)]
        out += found or [t for t in re.findall(r"[A-Z][A-Za-z]*-\d+", text)]
    return out


def title_of(body: str, ident: str, stem: str) -> str:
    """The H1, with any leading id and dash stripped. Falls back to the filename."""
    for line in body.splitlines():
        if line.startswith("# "):
            head = line[2:].strip()
            if ident and head.startswith(ident):
                head = head[len(ident):].lstrip(" -—–:")
            return head or stem.replace("-", " ")
    return stem.replace("-", " ")


def article(word: str) -> str:
    """`a` or `an`, so a finding about `an open-question` reads like English.

    `u` counts as a consonant here because the one type that starts with one — `user-story` — is
    read aloud as "a user story".
    """
    return ("an " if word[:1] in "aeio" else "a ") + word


class Note:
    def __init__(self, path: pathlib.Path, root: pathlib.Path):
        self.path, self.rel = path, path.relative_to(root)
        text = path.read_text(encoding="utf-8")
        self.text = text
        self.has_frontmatter = self.has_fm = text.startswith("---\n")
        self.meta, self.body = split_front_matter(text)
        self.id = str(self.meta.get("id", "") or "")
        self.type = str(self.meta.get("type", "") or "")
        self.status = str(self.meta.get("status", "") or "")
        self.stem = path.stem
        self.aliases = as_list(self.meta.get("aliases"))
        self.refs = refs(text)
        self.links = {r["target"] for r in self.refs}
        # Links inside a generated block are derived, so they do not rescue an orphan. A dangling
        # one there still counts: it means the generator emitted a reference to nothing.
        self.authored_links = {r["target"] for r in refs(GEN_BLOCK.sub("", text))}
        prose = FENCED.sub("", self.body)
        self.headings = {norm_anchor(h) for h in HEADING.findall(prose)}
        self.blocks = {b.lower() for b in BLOCK_ID.findall(prose)}
        self.title = title_of(self.body, self.id, self.stem)

    def prop(self, key, default=""):
        return self.meta.get(key, default)

    @property
    def body_lines(self) -> int:
        return len([l for l in self.body.splitlines() if l.strip()])


def link_targets(note: Note) -> set[str]:
    """Every name a wikilink may legitimately use to reach this note.

    The file name and the path to it — and nothing else. **Not `aliases`, and not `id`.** Obsidian
    resolves a wikilink against file names and paths only; an alias feeds autocomplete and search.
    A linter that accepted either would pass `[[ORDER-1]]`, which opens a new empty note, and the
    citation layer would be hollow with every check green.
    """
    rel = str(note.rel).replace(os.sep, "/")
    return {note.stem, rel, rel[:-3] if rel.endswith(".md") else rel}


def load(root: pathlib.Path):
    """Notes, plus the names of every other file a wikilink may legitimately target.

    A markdown file with no front matter is not a note and not a checker's business: the vault may
    share its folder with a repo's other docs. Front matter with no `type` IS a malformed note, and
    is reported by whoever called this.
    """
    notes, others = [], set()
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for name in sorted(filenames):
            path = pathlib.Path(dirpath) / name
            if name.endswith(".md"):
                note = Note(path, root)
                if note.has_frontmatter:
                    notes.append(note)
                else:
                    others.update({name, path.stem})
            elif not name.startswith("."):
                others.update({name, path.stem})     # e.g. business-rules.base, as [[x.base]]
    return notes, others


# ---------------------------------------------------------------------------- #
# Reporting
# ---------------------------------------------------------------------------- #
class Report:
    def __init__(self):
        self.errors, self.warnings, self.checks = [], [], 0

    def require(self, ok, message) -> bool:
        self.checks += 1
        if not ok:
            self.errors.append(message)
        return bool(ok)

    def warn(self, message):
        self.warnings.append(message)


def new_only(findings: list[str], baseline) -> list[str]:
    """Findings absent from an earlier run's output, so a change is judged by what it broke.

    Without this, the first run on an adopted vault reports everything at once, and the honest
    response — reading several hundred findings — is the one nobody has time for. So the linter
    gets ignored, which is worse than not having it.
    """
    if not baseline:
        return findings
    path = pathlib.Path(baseline)
    if not path.exists():
        return findings
    known = {line.strip().lstrip("- ").strip()
             for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}
    return [f for f in findings if f.strip() not in known]


# ---------------------------------------------------------------------------- #
# The one taxonomy check
# ---------------------------------------------------------------------------- #
def check_shape(note: Note, tax: Taxonomy, require) -> None:
    """What the registry promises about any note, whichever skill wrote it.

    A vault holds a PRD's notes beside the knowledge base's and a backlog's, so each checker meets
    types it does not own. One implementation means a note is held to one contract rather than to
    whichever script happened to walk over it — and means one wording for the finding, which the
    three scripts had already lost.

    `require(ok, message)` is the caller's: a `Report.require`, or a closure appending to a list.
    """
    if not note.type:
        require(False, f"{note.rel}: no type")
        return
    if note.type not in tax.types:
        require(False, f"{note.rel}: unknown type '{note.type}'")
        return

    if note.status:
        allowed = tax.status_order[note.type]
        require(note.status in tax.status[note.type],
                f"{note.rel}: status '{note.status}' is not valid for type '{note.type}' "
                f"({' | '.join(allowed) or 'this type has no status'})")

    pattern = tax.id_pattern[note.type]
    if pattern and note.id:
        # An id scheme nothing checks is an id scheme that drifts. `SRC-01` and `SRC-0001` were the
        # same type in two skills for as long as the width lived only in prose.
        require(bool(re.fullmatch(pattern, note.id)),
                f"{note.rel}: id '{note.id}' does not match the {note.type} pattern {pattern}")
    elif pattern:
        require(False, f"{note.rel}: {article(note.type)} carries an id matching {pattern}")
    if not pattern and note.id:
        require(False, f"{note.rel}: {article(note.type)} is cited by file name and carries no id, "
                       f"but this one has id '{note.id}'")
    # The id belongs in `aliases` too, for search and autocomplete. Nothing resolves through it, so
    # its absence is invisible until someone types the id and finds nothing.
    if note.id:
        require(note.id in note.aliases, f"{note.rel}: id '{note.id}' is not in aliases")

    # The grouping key. There is no `tags` property — `type` and this are what a Bases view and a
    # MOC group by, so a type without one has no retrieval dimension at all.
    key = tax.group_by[note.type]
    if key:
        require(bool(str(note.prop(key, "")).strip()),
                f"{note.rel}: no '{key}' — {article(note.type)} is grouped by it")

    limit = tax.body_limit.get(note.type, DEFAULT_BODY_LIMIT)
    require(note.body_lines <= limit,
            f"{note.rel}: body is {note.body_lines} lines, budget {limit}")


# ---------------------------------------------------------------------------- #
# Generated blocks
# ---------------------------------------------------------------------------- #
def manifest(notes) -> str:
    """A hash over the input notes: the generated view's claim to be reproducible from them."""
    h = hashlib.sha256()
    for n in sorted(notes, key=lambda x: str(x.rel)):
        h.update(str(n.rel).encode("utf-8"))
        h.update(n.path.read_bytes())
    return h.hexdigest()


def block_hash(text: str) -> str:
    """The hash of the generated block in this note's text, for detecting a hand edit."""
    m = GEN.search(text)
    return hashlib.sha256(m.group(2).encode("utf-8")).hexdigest() if m else ""


def today() -> str:
    return datetime.date.today().isoformat()


def stamp(text: str, fields: dict) -> str:
    """Set each field in the note's front matter, in order, inserting what is not there yet.

    A generated note has to say what produced it, from what, and at which version of the inputs.
    Without that, "is this index current?" is answered by reading the notes it indexes — which is
    the work the index existed to save.
    """
    end = text.find("\n---", 4)
    if not text.startswith("---\n") or end == -1:
        return text
    lines, tail = text[4:end].splitlines(), text[end:]
    for key, value in fields.items():
        rendered = ("[" + ", ".join(str(v) for v in value) + "]"
                    if isinstance(value, list) else str(value))
        line = f"{key}: {rendered}"
        for i, existing in enumerate(lines):
            if existing.split(":", 1)[0].strip() == key and not existing[:1].isspace():
                lines[i] = line
                break
        else:
            lines.append(line)
    return "---\n" + "\n".join(lines) + tail


def input_paths(rows) -> list[str]:
    return sorted({str(pathlib.PurePosixPath(r.rel).parent) + "/" for r in rows})


def provenance(generator: str, rows, body: str, when: str | None = None) -> dict:
    """The five fields a generated note carries, ready for `stamp`."""
    return {"generator": generator,
            "generated": when or today(),
            "input-paths": input_paths(rows),
            "input-manifest-sha256": manifest(rows),
            "managed-block-sha256": hashlib.sha256(body.encode("utf-8")).hexdigest()}


def idkey(ident: str, tiebreak: str = ""):
    """Sort an id by prefix then numerically, so `LABEL-2` comes before `LABEL-10`.

    `tiebreak` orders notes that carry no id — a glossary term, a scope boundary — by title.
    """
    m = re.match(r"([A-Za-z]+)-0*(\d+)", ident or "")
    return (m.group(1), int(m.group(2)), tiebreak) if m else (ident or "", 0, tiebreak)


def header(column: str) -> str:
    return "ID" if column == "id" else column.replace("-", " ").capitalize()


def cell(note: Note, column: str) -> str:
    """One table cell. Shared so two generators writing one index cannot disagree about it."""
    if column == "title":
        # Collapsed, because an H1 that wrapped across two lines would otherwise end the row early
        # and silently drop every column after it.
        return re.sub(r"\s+", " ", note.title.replace("|", "\\|")).strip()
    if column == "id":
        # The stem is the link target and the id is the display text, with the pipe escaped because
        # this lands in a table cell. A generator that emitted `[[ID]]` would write the one link
        # form Obsidian cannot resolve, once per row, and call it an index.
        return f"[[{note.stem}\\|{note.id}]]" if note.id else f"[[{note.stem}]]"
    value = note.prop(column, "")
    if isinstance(value, list):
        return " · ".join(str(v) for v in value) or "—"
    return str(value).replace("|", "\\|") or "—"


def table(rows, spec: dict, group_fallback: str = "ungrouped") -> str:
    """The generated block's body: one row per note, grouped when the snapshot says to.

    The caller keeps its own marker handling and its own choice of which snapshots it owns; this is
    only the table. `group-fallback` in the spec wins over the argument, which is the default a
    particular skill prefers.
    """
    columns = as_list(spec.get("columns")) or ["id", "title", "status"]
    group = spec.get("group-by")
    fallback = str(spec.get("group-fallback") or group_fallback)
    groups = collections.defaultdict(list)
    for r in rows:
        groups[str(r.prop(group, "")) if group else ""].append(r)
    out = []
    # An empty group goes last: it is the leftover bucket, not the first thing to read.
    for key in sorted(groups, key=lambda k: (k == "", k)):
        if group:
            out.append(f"### {key or fallback}\n")
        out.append("| " + " | ".join(header(c) for c in columns) + " |")
        out.append("|" + "---|" * len(columns))
        for r in sorted(groups[key], key=lambda x: idkey(x.id, x.title)):
            out.append("| " + " | ".join(cell(r, c) for c in columns) + " |")
        out.append("")
    return "\n".join(out).rstrip() + "\n"
