"""Lint an anchored-knowledge Obsidian vault, and regenerate the MOC snapshots in it.

    python3 scripts/vault.py lint      <vault> [--baseline FILE] [--git]   # exit 1 on a finding
    python3 scripts/vault.py moc       <vault> [--check]          # rewrite the generated blocks
    python3 scripts/vault.py narrative <vault> [--check]          # stamp the derived narratives

`lint` reports what the convention promises and prose cannot enforce: dangling wikilinks, orphans,
values outside the closed vocabularies, a confirmed note with no source, a note over its size
budget, and duplicate ids.

**Links resolve the way Obsidian resolves them.** A wikilink reaches a note by its file name or its
path, never through its `aliases` — so `[[ORDER-1]]` is a dangling link that opens a new empty note,
and the citable form is `[[order-address-frozen-on-confirmation|ORDER-1]]`. A linter that accepts
the alias cannot tell the two apart, which is the one failure that silently empties a citation
layer. `lint` also checks the part after `#` against the target's real headings and `^block-ids`,
and checks that display text shaped like an id *is* the target's id.

`--baseline FILE` reports only findings absent from FILE (the output of an earlier run), so a change
is judged by what it broke rather than by what was already broken. That is what makes the linter
usable on a vault you have just adopted instead of something people learn to ignore.

`moc` reads each MOC's `snapshot` frontmatter and rewrites only the block between the markers, then
stamps the note's provenance. `--check` writes nothing and fails if regeneration would change
anything, so a stale index is caught in review instead of being silently repaired by the next run.

`--git` adds the one check only version control can make: a note whose `updated` predates the last
commit that touched it. `updated` is a claim about the file rather than a fact about the world, and
nobody remembers to bump it — so the MOC tables and Bases views that sort on it sort on fiction.
It is opt-in because a vault's dates may legitimately be fictional, as this skill's own worked
example's are. Standard library only, Python 3.10+.
"""
import hashlib, os, re, subprocess, sys, pathlib, collections

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
    "narrative": {"draft", "current", "stale"},
}
AUTHORITY = {"1-contractual", "2-approved-requirements", "3-client-clarification",
             "4-source-artifact", "5-internal-interpretation", "6-unreviewed-intake"}
BODY_LIMIT = {"decision": 120, "reference": 10**6, "moc": 10**6, "narrative": 10**6}
GAPS_HEADING = "gaps found while deriving"
# A date written into a narrative's prose. `covers-through` is the only date it may carry: a
# hand-written one is a claim about freshness that nothing checks and nobody updates.
PROSE_DATE = re.compile(r"(?:last updated|as of|updated)\s*:?\s*\d{4}-\d\d-\d\d", re.I)
DEFAULT_BODY_LIMIT = 25
CITABLE = {"business-rule", "fact", "scope-boundary", "glossary-term", "decision", "reference"}
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
        self.refs = _refs(text)
        self.links = {r["target"] for r in self.refs}
        # Links inside a generated block are derived, so they do not rescue an orphan. A dangling
        # one there still counts: it means the generator emitted a reference to nothing.
        self.authored_links = {r["target"] for r in _refs(GEN_BLOCK.sub("", text))}
        # Anchor targets, for the links that point into this note.
        prose = FENCED.sub("", self.body)
        self.headings = {_norm(h) for h in HEADING.findall(prose)}
        self.blocks = {b.lower() for b in BLOCK_ID.findall(prose)}
        self.title = _title(self.body, self.id, self.stem)


def _refs(text):
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


def _norm(text):
    """Compare a heading the way Obsidian's anchors do: punctuation out, case and spacing flat."""
    return re.sub(r"\s+", " ", re.sub(r"[#|^:\[\]]|%%", " ", text)).strip().lower()


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
    """Every name that a wikilink may legitimately use to reach this note.

    The file name and the path to it — and nothing else. **Not `aliases`, and not `id`.** Obsidian
    resolves a wikilink against file names and paths only; an alias feeds autocomplete and search.
    A linter that accepted either would pass `[[ORDER-1]]`, which opens a new empty note, and the
    citation layer would be hollow with every check green.
    """
    rel = str(note.rel).replace(os.sep, "/")
    return {note.stem, rel, rel[:-3] if rel.endswith(".md") else rel}


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


def lint(vault, baseline=None, use_git=False):
    notes, others = load(vault)
    commits = _git_dates(vault) if use_git else None
    findings, by_target, ids = [], collections.defaultdict(list), collections.defaultdict(list)
    by_stem = collections.defaultdict(list)
    for n in notes:
        for t in _link_targets(n):
            by_target[t].append(n)
        by_stem[n.stem].append(n.rel)
        if n.id:
            ids[n.id].append(n.rel)
    inbound = collections.Counter()

    # A file name is the link target, so two notes cannot share one. Obsidian picks between them by
    # proximity, which means the same link text resolves differently depending on where it is
    # written — and under the stem-link convention one of the two becomes uncitable outright.
    for stem, where in sorted(by_stem.items()):
        if len(where) > 1:
            findings.append(f"duplicate file name {stem}.md: {', '.join(str(w) for w in where)}")

    for n in notes:
        for ref in n.refs:
            target = ref["target"]
            hits = by_target.get(target) or by_target.get(target.rsplit("/", 1)[-1])
            if not hits and target not in others and target.rsplit("/", 1)[-1] not in others:
                if target in ids:
                    stem = pathlib.Path(str(ids[target][0])).stem
                    findings.append(f"{n.rel}: [[{target}]] is a bare id, which Obsidian does not "
                                    f"resolve — write [[{stem}|{target}]]")
                else:
                    findings.append(f"{n.rel}: dangling wikilink [[{target}]]")
                continue
            if not hits:
                continue
            dest = hits[0]
            # An anchor the target does not have scrolls nowhere, and nothing else reports it.
            if ref["anchor"]:
                anchor = ref["anchor"]
                if anchor.startswith("^"):
                    if anchor[1:].lower() not in dest.blocks:
                        findings.append(f"{n.rel}: [[{target}#{anchor}]] — no such block in "
                                        f"{dest.rel}")
                elif _norm(anchor) not in dest.headings:
                    findings.append(f"{n.rel}: [[{target}#{anchor}]] — no such heading in "
                                    f"{dest.rel}")
            # Display text shaped like an id must be the id of the note the link opens. The link
            # works, so the reader has no way to see that the citation names something else.
            shown = ref["display"]
            if shown and IDLIKE.match(shown) and dest.id and shown != dest.id:
                findings.append(f"{n.rel}: [[{target}|{shown}]] opens {dest.rel}, whose id is "
                                f"{dest.id}")
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
        if n.meta.get("snapshot"):
            missing = [k for k in PROV if not str(n.meta.get(k, ""))]
            if missing:
                findings.append(f"{n.rel}: generated note is missing {', '.join(missing)}")
        if n.type == "narrative":
            findings += _narrative(n, notes)
        if commits:
            rel = str(n.rel).replace(os.sep, "/")
            last = commits.get(rel, "")
            updated = str(n.meta.get("updated", ""))
            if last and updated and updated < last:
                findings.append(f"{n.rel}: updated says {updated} but the note last changed "
                                f"{last} — a freshness date nobody bumps is read as current")
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
        # A hand edit between the markers is a change the next `moc` run would throw away. Catch it
        # while the edit still exists, rather than letting the generator quietly win.
        declared = str(n.meta.get("managed-block-sha256", ""))
        if declared:
            actual = _block_hash(n.path.read_text(encoding="utf-8"))
            if actual and actual != declared:
                findings.append(f"{n.rel}: the generated block was edited by hand — "
                                f"managed-block-sha256 says {declared[:12]}, the block hashes "
                                f"{actual[:12]}")
    return _new_only(sorted(findings), baseline)


def _narrative(note, notes):
    """Hold a derived narrative to the one thing that makes it safe: it owns nothing.

    A readable story over the notes is the surface people actually read, which is exactly why a
    hand-written one rots — the note gets the correction and the prose keeps the old number, and the
    prose is what the reader believes. Prose cannot be generated, so the model writes it and this
    checks the mechanical part of the promise: every section cites, every claim links, the only date
    is `covers-through`, gaps are listed rather than filled, and the note says which version of the
    notes it was derived from so a stale narrative is provable rather than a matter of opinion.
    """
    findings = []
    for key in ("covers-through", "derived-from", "input-manifest-sha256"):
        if not str(note.meta.get(key, "")):
            findings.append(f"{note.rel}: a narrative must carry {key}")
    folders = [str(f).strip("/") for f in _as_list(note.meta.get("derived-from"))]
    if folders:
        inputs = [n for n in notes
                  if str(pathlib.PurePosixPath(str(n.rel)).parent).strip("/") in folders]
        declared = str(note.meta.get("input-manifest-sha256", ""))
        if declared and inputs and declared != _manifest(inputs):
            findings.append(f"{note.rel}: derived from notes that have changed since — "
                            f"regenerate it, or its story is about an older vault")
    # Sections, and what each one owes.
    sections, current = {}, None
    for line in note.body.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections[current] = []
        elif current is not None:
            sections[current].append(line)
    if not any(_norm(s) == GAPS_HEADING for s in sections):
        findings.append(f"{note.rel}: no '## Gaps found while deriving' section — a narrative "
                        f"reports what no note holds instead of writing it")
    for name, lines in sections.items():
        text = "\n".join(lines)
        if _norm(name) == GAPS_HEADING:
            continue
        if text.strip() and not WIKILINK.search(text):
            findings.append(f"{note.rel}: section '{name}' cites nothing, so its claims have no "
                            f"start note")
        # Per claim, not per line: a bullet's link often wraps onto the next line, and a narrative
        # judged line by line would be unwritable at a sane column width.
        for claim in _claims(lines):
            body = claim.strip().lstrip("-*0123456789. ").strip()
            if len(body.split()) >= 8 and not WIKILINK.search(claim):
                findings.append(f"{note.rel}: '{body[:48]}…' makes a claim with no link to the "
                                f"note that holds it")
    if PROSE_DATE.search(note.body):
        findings.append(f"{note.rel}: a hand-written date in the prose — `covers-through` is the "
                        f"only date a narrative carries")
    return findings


def _git_dates(vault):
    """Vault-relative path -> the date of the last commit that touched it.

    One `git log` pass, because a call per note is slow enough on a real vault that people stop
    running the check. Returns None when there is no git here, or git is not installed: the check
    then reports nothing rather than guessing, since a wrong staleness claim is the thing it exists
    to prevent.
    """
    def git(*args):
        try:
            out = subprocess.run(["git", "-C", str(vault), *args],
                                 capture_output=True, text=True, timeout=60)
        except (OSError, subprocess.SubprocessError):
            return None
        return out.stdout if out.returncode == 0 else None

    prefix = git("rev-parse", "--show-prefix")
    # Author date, not committer date: a rebase or an amend resets the committer date and would
    # mark the whole vault stale at once, which is how a check earns its way onto the ignore list.
    log = git("log", "--format=%as", "--name-only")
    if prefix is None or log is None:
        return None
    prefix = prefix.strip()
    dates, date = {}, ""
    for line in log.splitlines():
        line = line.strip()
        if re.fullmatch(r"\d{4}-\d\d-\d\d", line):
            date = line
        elif line:
            # Paths come out relative to the repo root; the first time a path appears is its
            # newest commit, because `git log` walks history backwards.
            if not prefix or line.startswith(prefix):
                dates.setdefault(line[len(prefix):], date)
    return dates


def _claims(lines):
    """Prose grouped into claims: a bullet or a paragraph, with its wrapped continuation lines.

    Callouts are skipped. A `> [!warning]` block is framing for the reader, not a claim about the
    domain, and demanding a citation inside one only teaches people to bury the warning.
    """
    out, current = [], []
    for line in lines:
        stripped = line.strip()
        starts = stripped.startswith(("-", "*")) or re.match(r"^\d+\.\s", stripped)
        if not stripped or starts or stripped.startswith(("#", ">", "|", "```")):
            if current:
                out.append(" ".join(current))
                current = []
            if starts:
                current = [stripped]
            continue
        current.append(stripped)
    if current:
        out.append(" ".join(current))
    return out


def _block_hash(text):
    m = GEN.search(text)
    return hashlib.sha256(m.group(2).encode("utf-8")).hexdigest() if m else ""


def _manifest(notes):
    """A hash over every input note's id and content: the generated view's reproducibility claim."""
    h = hashlib.sha256()
    for n in sorted(notes, key=lambda x: str(x.rel)):
        h.update(str(n.rel).encode("utf-8"))
        h.update(n.path.read_bytes())
    return h.hexdigest()


def _new_only(findings, baseline):
    """Findings absent from an earlier run's output, so a change is judged by what it broke.

    Without this, the first run on an adopted vault reports everything at once, and the honest
    response — reading several hundred findings — is the one nobody has time for. So the linter
    gets ignored, which is worse than not having it.
    """
    if not baseline:
        return findings
    known = {line.strip().lstrip("- ").strip()
             for line in pathlib.Path(baseline).read_text(encoding="utf-8").splitlines()
             if line.strip()}
    return [f for f in findings if f not in known]


def moc(vault, check=False):
    """Rewrite every generated block, or (check) report the ones that would change.

    Returns (findings, written). A stale block is a finding, not something to repair in silence:
    silently repairing it means a committed index that disagrees with the notes is invisible in
    review, and a hand edit between the markers disappears without anyone being told.
    """
    notes, _ = load(vault)
    findings = []
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
            findings.append(f"{n.rel}: snapshot spec but no <!-- generated --> markers")
            continue
        manifest = _manifest(rows)
        fresh = (m.group(2) == body
                 and str(n.meta.get("input-manifest-sha256", "")) == manifest)
        if fresh:
            continue          # unchanged: leave the file and its date stamp alone
        if check:
            why = "rows have changed" if m.group(2) != body else "inputs have changed"
            findings.append(f"{n.rel}: the generated block is stale — {why}")
            continue
        stamp = spec.get("as-of") or _today()
        new = GEN.sub(lambda mm: f"<!-- generated: do not edit · {stamp} -->\n{body}{mm.group(3)}",
                      text, count=1)
        new = _stamp(new, {
            "generator": "vault.py moc",
            "generated": stamp,
            "input-paths": sorted({str(pathlib.PurePosixPath(r.rel).parent) + "/" for r in rows}),
            "input-manifest-sha256": manifest,
            "managed-block-sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
        })
        n.path.write_text(new, encoding="utf-8")
        written.append(f"{n.rel}: {len(rows)} rows")
    return findings, written


def narrative(vault, check=False):
    """Stamp each narrative note with the version of the notes it was derived from.

    The prose is written by hand (or by a model); only this is mechanical. Separating the two is the
    point: a narrative can be as readable as anybody likes, and still never be the place a fact
    lives, because the stamp makes "derived from a vault that has since moved on" a finding.
    """
    notes, _ = load(vault)
    findings, written = [], []
    for n in notes:
        if n.type != "narrative":
            continue
        folders = [str(f).strip("/") for f in _as_list(n.meta.get("derived-from"))]
        if not folders:
            findings.append(f"{n.rel}: no derived-from, so there is nothing to stamp it against")
            continue
        inputs = [x for x in notes
                  if str(pathlib.PurePosixPath(str(x.rel)).parent).strip("/") in folders]
        if not inputs:
            findings.append(f"{n.rel}: derived-from names {folders}, which hold no notes")
            continue
        manifest = _manifest(inputs)
        if str(n.meta.get("input-manifest-sha256", "")) == manifest:
            continue
        if check:
            findings.append(f"{n.rel}: stale — the notes it derives from have changed")
            continue
        newest = max((str(x.meta.get("updated", "")) or str(x.meta.get("created", ""))
                      for x in inputs), default=_today())
        text = _stamp(n.path.read_text(encoding="utf-8"), {
            "covers-through": newest or _today(),
            "input-manifest-sha256": manifest,
        })
        n.path.write_text(text, encoding="utf-8")
        written.append(f"{n.rel}: derived from {len(inputs)} notes, covers through {newest}")
    return findings, written


def _stamp(text, fields):
    """Set each field in the note's front matter, in order, inserting what is not there yet.

    A generated note has to say what produced it, from what, and at which version of the inputs.
    Without that, "is this index current?" is answered by reading the notes it indexes — which is
    the work the index existed to save.
    """
    end = text.find("\n---", 4)
    if not text.startswith("---\n") or end == -1:
        return text
    head, tail = text[4:end], text[end:]
    lines = head.splitlines()
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


def _header(column):
    return "ID" if column == "id" else column.replace("-", " ").capitalize()


def _cell(note, column):
    if column == "title":
        return note.title
    if column == "id":
        # The stem is the link target and the id is the display text, with the pipe escaped because
        # this lands in a table cell. A generator that emitted [[ID]] would write the one link form
        # Obsidian cannot resolve, several hundred times, and call it an index.
        return f"[[{note.stem}\\|{note.id}]]" if note.id else f"[[{note.stem}]]"
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
    argv = sys.argv[1:]
    check = "--check" in argv
    baseline = None
    if "--baseline" in argv:
        i = argv.index("--baseline")
        if i + 1 >= len(argv):
            print(__doc__)
            sys.exit(2)
        baseline = argv[i + 1]
        del argv[i:i + 2]
    use_git = "--git" in argv
    argv = [a for a in argv if a not in ("--check", "--git")]
    if len(argv) != 2 or argv[0] not in ("lint", "moc", "narrative"):
        print(__doc__)
        sys.exit(2)
    cmd, vault = argv[0], pathlib.Path(argv[1]).resolve()
    if not vault.is_dir():
        print(f"not a directory: {vault}")
        sys.exit(2)
    if cmd == "lint":
        out = lint(vault, baseline, use_git)
        print(f"{len(out)} findings" if out else "ok")
        for line in out:
            print(f"  {line}")
        sys.exit(1 if out else 0)
    problems, written = narrative(vault, check) if cmd == "narrative" else moc(vault, check)
    for line in written:
        print(line)
    for line in problems:
        print(f"  {line}")
    if problems:
        print(f"{len(problems)} findings")
    elif check:
        print("ok — every narrative is current" if cmd == "narrative"
              else "ok — every generated block is current")
    sys.exit(1 if problems else 0)
