"""Lint an anchored-knowledge Obsidian vault, and regenerate the MOC snapshots in it.

    python3 scripts/vault.py lint <vault>    # findings; exit 1 if any
    python3 scripts/vault.py moc  <vault>    # rewrite every <!-- generated --> block

`lint` reports what the convention promises and prose cannot enforce: dangling wikilinks, orphans,
values outside the closed vocabularies, a confirmed note with no source, a note over its size
budget, and duplicate ids. `moc` reads each MOC's `snapshot` frontmatter and rewrites only the block
between the markers. Standard library only, Python 3.10+.
"""
import os, re, sys, pathlib, collections

STATUS = {
    "business-rule": {"draft", "confirmed", "needs-review", "superseded", "out-of-scope", "rejected"},
    "fact": {"draft", "confirmed", "needs-review", "superseded", "out-of-scope", "rejected"},
    "scope-boundary": {"draft", "confirmed", "needs-review", "superseded", "out-of-scope", "rejected"},
    "glossary-term": {"draft", "confirmed", "needs-review", "superseded", "rejected"},
    "decision": {"proposed", "accepted", "superseded", "deprecated", "rejected"},
    "open-question": {"open", "partial", "answered", "blocked", "dropped"},
    "scope-watch": {"watch", "clarify", "in-scope", "deferred", "change-request", "closed"},
    "knowledge-change": {"proposed", "accepted", "needs-review", "closed"},
    "source": {"registered", "stale", "superseded"},
    "reference": {"draft", "confirmed", "needs-review", "superseded"},
    "moc": set(),
}
AUTHORITY = {"1-contractual", "2-approved-requirements", "3-client-clarification",
             "4-source-artifact", "5-internal-interpretation", "6-unreviewed-intake"}
BODY_LIMIT = {"decision": 120, "reference": 10**6, "moc": 10**6}
DEFAULT_BODY_LIMIT = 25
CITABLE = {"business-rule", "fact", "scope-boundary", "glossary-term", "decision", "reference"}
WIKILINK = re.compile(r"!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
GEN = re.compile(r"(<!-- generated:[^\n]*-->\n)(.*?)(<!-- /generated -->)", re.S)
GEN_BLOCK = re.compile(r"<!-- generated:.*?<!-- /generated -->", re.S)


class Note:
    def __init__(self, path, vault):
        self.path, self.rel = path, path.relative_to(vault)
        text = path.read_text(encoding="utf-8")
        self.has_frontmatter = text.startswith("---\n")
        self.meta, self.body = _split(text)
        self.id = str(self.meta.get("id", "") or "")
        self.type = str(self.meta.get("type", "") or "")
        self.status = str(self.meta.get("status", "") or "")
        self.stem = path.stem
        self.aliases = _as_list(self.meta.get("aliases"))
        self.links = {m.group(1).strip() for m in WIKILINK.finditer(text)}
        # Links inside a generated block are derived, so they do not rescue an orphan. A dangling
        # one there still counts: it means the generator emitted a reference to nothing.
        self.authored_links = {m.group(1).strip()
                               for m in WIKILINK.finditer(GEN_BLOCK.sub("", text))}
        self.title = _title(self.body, self.id, self.stem)


def _split(text):
    """Front matter as a flat dict. Scalars, inline lists and one level of nesting; no YAML dep."""
    meta, body = {}, text
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            raw, body = text[4:end], text[end + 4:].lstrip("\n")
            parent = None
            for line in raw.splitlines():
                if not line.strip() or line.lstrip().startswith("#"):
                    continue
                indented = line[0] in " \t"
                if ":" not in line:
                    continue
                key, _, val = line.strip().partition(":")
                key, val = key.strip(), val.strip()
                if indented and parent is not None:
                    meta.setdefault(parent, {})
                    if isinstance(meta[parent], dict):
                        meta[parent][key] = _scalar(val)
                    continue
                if val == "":
                    parent = key
                    meta[key] = {}
                else:
                    parent = None
                    meta[key] = _scalar(val)
            # `key:` with nothing under it is an empty value, not an empty mapping. Left as {} it
            # reads as truthy, and every "is this field filled in?" check silently passes.
            for key, value in list(meta.items()):
                if value == {}:
                    meta[key] = ""
    return meta, body


def _title(body, ident, stem):
    """The H1, with any leading id and dash stripped. Falls back to the filename."""
    for line in body.splitlines():
        if line.startswith("# "):
            head = line[2:].strip()
            if ident and head.startswith(ident):
                head = head[len(ident):].lstrip(" -\u2014\u2013:")
            return head or stem.replace("-", " ")
    return stem.replace("-", " ")


def _scalar(val):
    val = val.strip()
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1].strip()
        if not inner:
            return []
        return [p.strip().strip("\"'") for p in inner.split(",") if p.strip()]
    return val.strip("\"'")


def _as_list(val):
    if val is None or val == "":
        return []
    return val if isinstance(val, list) else [val]


def _link_targets(note):
    """Every name that a wikilink may legitimately use to reach this note."""
    return {note.stem, *note.aliases, *( [note.id] if note.id else [] )}


def load(vault):
    """Notes, plus the names of every other vault file a wikilink may legitimately target.

    A markdown file with no front matter is not a note and not this skill's business: the vault may
    share its folder with a repo's other docs. Front matter with no `type` IS a malformed note, and
    is reported.
    """
    notes, others = [], set()
    for dirpath, dirnames, filenames in os.walk(vault):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for name in sorted(filenames):
            path = pathlib.Path(dirpath) / name
            if name.endswith(".md"):
                note = Note(path, vault)
                if note.has_frontmatter:
                    notes.append(note)
                else:
                    others.add(name)
                    others.add(path.stem)
            elif not name.startswith("."):
                others.add(name)          # e.g. business-rules.base, embedded as [[x.base]]
                others.add(path.stem)
    return notes, others


def lint(vault):
    notes, others = load(vault)
    findings, by_target, ids = [], collections.defaultdict(list), collections.defaultdict(list)
    for n in notes:
        for t in _link_targets(n):
            by_target[t].append(n)
        if n.id:
            ids[n.id].append(n.rel)
    inbound = collections.Counter()

    for n in notes:
        for target in sorted(n.links):
            hits = by_target.get(target) or by_target.get(target.rsplit("/", 1)[-1])
            if not hits and target not in others and target.rsplit("/", 1)[-1] not in others:
                findings.append(f"{n.rel}: dangling wikilink [[{target}]]")
        for target in sorted(n.authored_links):
            for h in (by_target.get(target) or by_target.get(target.rsplit("/", 1)[-1]) or []):
                if h is not n:
                    inbound[h.rel] += 1
        if n.type and n.type not in STATUS:
            findings.append(f"{n.rel}: unknown type '{n.type}'")
        elif n.type and n.status and n.status not in STATUS[n.type]:
            findings.append(f"{n.rel}: status '{n.status}' is not valid for type '{n.type}'")
        if not n.type:
            findings.append(f"{n.rel}: no type")
        auth = n.meta.get("authority")
        if auth and str(auth) not in AUTHORITY:
            findings.append(f"{n.rel}: unknown authority '{auth}'")
        if n.id and n.id not in n.aliases:
            findings.append(f"{n.rel}: id {n.id} is not in aliases, so [[{n.id}]] will not resolve")
        if n.type in CITABLE and n.type != "reference" and n.status == "confirmed" \
                and not _as_list(n.meta.get("sources")):
            findings.append(f"{n.rel}: status confirmed with no sources")
        if n.status in ("draft", "needs-review") and not str(n.meta.get("updated", "")):
            findings.append(f"{n.rel}: {n.status} with no updated date")
        if n.status == "superseded" and not n.meta.get("superseded-by"):
            findings.append(f"{n.rel}: superseded with no superseded-by")
        limit = BODY_LIMIT.get(n.type, DEFAULT_BODY_LIMIT)
        lines = len([l for l in n.body.splitlines() if l.strip()])
        if lines > limit:
            findings.append(f"{n.rel}: body is {lines} lines, budget {limit}")

    for ident, where in sorted(ids.items()):
        if len(where) > 1:
            findings.append(f"duplicate id {ident}: {', '.join(str(w) for w in where)}")
    for n in notes:
        if n.type in CITABLE and not inbound[n.rel]:
            findings.append(f"{n.rel}: orphan — nothing links here")
    return sorted(findings)


def moc(vault):
    notes, _ = load(vault)
    by_type = collections.defaultdict(list)
    for n in notes:
        by_type[n.type].append(n)
    written = []
    for n in notes:
        spec = n.meta.get("snapshot")
        if not isinstance(spec, dict) or not spec.get("type"):
            continue
        rows = [x for x in by_type.get(spec["type"], [])
                if x.status not in _as_list(spec.get("exclude-status"))]
        columns = _as_list(spec.get("columns")) or ["id", "title", "status"]
        group = spec.get("group-by")
        out = []
        groups = collections.defaultdict(list)
        for r in rows:
            groups[str(r.meta.get(group, "")) if group else ""].append(r)
        for key in sorted(groups):
            if group:
                out.append(f"### {key or 'ungrouped'}\n")
            out.append("| " + " | ".join(_header(c) for c in columns) + " |")
            out.append("|" + "---|" * len(columns))
            for r in sorted(groups[key], key=lambda x: _idkey(x.id) if x.id else ("", 0, x.title)):
                out.append("| " + " | ".join(_cell(r, c) for c in columns) + " |")
            out.append("")
        body = "\n".join(out).rstrip() + "\n"
        text = n.path.read_text(encoding="utf-8")
        m = GEN.search(text)
        if not m:
            written.append(f"{n.rel}: snapshot spec but no <!-- generated --> markers")
            continue
        if m.group(2) == body:
            continue          # unchanged: leave the file and its date stamp alone
        stamp = spec.get("as-of") or _today()
        new = GEN.sub(lambda mm: f"<!-- generated: do not edit · {stamp} -->\n{body}{mm.group(3)}",
                      text, count=1)
        n.path.write_text(new, encoding="utf-8")
        written.append(f"{n.rel}: {len(rows)} rows")
    return written


def _header(column):
    return "ID" if column == "id" else column.replace("-", " ").capitalize()


def _cell(note, column):
    if column == "title":
        return note.title
    if column == "id":
        return f"[[{note.id}]]" if note.id else f"[[{note.stem}]]"
    val = note.meta.get(column, "")
    if isinstance(val, list):
        return " · ".join(str(v) for v in val) or "—"
    return str(val).replace("|", "\\|") or "—"


def _idkey(ident):
    m = re.match(r"([A-Za-z-]*)(\d*)", ident or "")
    return (m.group(1), int(m.group(2) or 0), "")


def _today():
    import datetime
    return datetime.date.today().isoformat()


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("lint", "moc"):
        print(__doc__)
        sys.exit(2)
    cmd, vault = sys.argv[1], pathlib.Path(sys.argv[2]).resolve()
    if not vault.is_dir():
        print(f"not a directory: {vault}")
        sys.exit(2)
    if cmd == "lint":
        out = lint(vault)
        print(f"{len(out)} findings" if out else "ok")
        for line in out:
            print(f"  {line}")
        sys.exit(1 if out else 0)
    for line in moc(vault):
        print(line)
