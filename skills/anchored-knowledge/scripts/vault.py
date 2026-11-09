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
import collections, os, pathlib, re, subprocess, sys

import vaultlib
from vaultlib import (GEN, IDLIKE, PROV, WIKILINK, as_list, check_shape, link_targets, load,
                      new_only, norm_anchor, refs)

TAX = vaultlib.Taxonomy(__file__)
AUTHORITY = TAX.authority
GAPS_HEADING = "gaps found while deriving"
# A date written into a narrative's prose. `covers-through` is the only date it may carry: a
# hand-written one is a claim about freshness that nothing checks and nobody updates.
PROSE_DATE = re.compile(r"(?:last updated|as of|updated)\s*:?\s*\d{4}-\d\d-\d\d", re.I)
CITABLE = TAX.citable
# Display text shaped like an id: a prefix, a dash, digits. `[[one-label-per-order|LABEL-9]]` is a
# lie the reader cannot see, because the link still opens the right note.
# Provenance on a generated note, so a stale block is provable rather than a judgement call.


def lint(vault, baseline=None, use_git=False):
    notes, others = load(vault)
    commits = _git_dates(vault) if use_git else None
    findings, by_target, ids = [], collections.defaultdict(list), collections.defaultdict(list)
    by_stem = collections.defaultdict(list)
    for n in notes:
        for t in link_targets(n):
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
                elif norm_anchor(anchor) not in dest.headings:
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
        # Type, status, id, aliases, grouping key and body budget: one implementation, in
        # `vaultlib`, so this vault's notes and a PRD's are held to the same contract with the
        # same wording. Three scripts had three copies and had already lost the wording.
        check_shape(n, TAX, lambda ok, message: ok or findings.append(message))
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
                and not as_list(n.meta.get("sources")):
            findings.append(f"{n.rel}: status confirmed with no sources")
        if n.status in ("draft", "needs-review") and not str(n.meta.get("updated", "")):
            findings.append(f"{n.rel}: {n.status} with no updated date")
        if n.status == "superseded" and not n.meta.get("superseded-by"):
            findings.append(f"{n.rel}: superseded with no superseded-by")

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
            actual = vaultlib.block_hash(n.path.read_text(encoding="utf-8"))
            if actual and actual != declared:
                findings.append(f"{n.rel}: the generated block was edited by hand — "
                                f"managed-block-sha256 says {declared[:12]}, the block hashes "
                                f"{actual[:12]}")
    return new_only(sorted(findings), baseline)


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
    folders = [str(f).strip("/") for f in as_list(note.meta.get("derived-from"))]
    if folders:
        inputs = [n for n in notes
                  if str(pathlib.PurePosixPath(str(n.rel)).parent).strip("/") in folders]
        declared = str(note.meta.get("input-manifest-sha256", ""))
        if declared and inputs and declared != vaultlib.manifest(inputs):
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
    if not any(norm_anchor(s) == GAPS_HEADING for s in sections):
        findings.append(f"{note.rel}: no '## Gaps found while deriving' section — a narrative "
                        f"reports what no note holds instead of writing it")
    for name, lines in sections.items():
        text = "\n".join(lines)
        if norm_anchor(name) == GAPS_HEADING:
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
                if x.status not in as_list(spec.get("exclude-status"))]
        body = vaultlib.table(rows, spec)
        text = n.path.read_text(encoding="utf-8")
        m = GEN.search(text)
        if not m:
            findings.append(f"{n.rel}: snapshot spec but no <!-- generated --> markers")
            continue
        manifest = vaultlib.manifest(rows)
        fresh = (m.group(2) == body
                 and str(n.meta.get("input-manifest-sha256", "")) == manifest)
        if fresh:
            continue          # unchanged: leave the file and its date stamp alone
        if check:
            why = "rows have changed" if m.group(2) != body else "inputs have changed"
            findings.append(f"{n.rel}: the generated block is stale — {why}")
            continue
        stamp = spec.get("as-of") or vaultlib.today()
        new = GEN.sub(lambda mm: f"<!-- generated: do not edit · {stamp} -->\n{body}{mm.group(3)}",
                      text, count=1)
        new = vaultlib.stamp(new, vaultlib.provenance("vault.py moc", rows, body, stamp))
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
        folders = [str(f).strip("/") for f in as_list(n.meta.get("derived-from"))]
        if not folders:
            findings.append(f"{n.rel}: no derived-from, so there is nothing to stamp it against")
            continue
        inputs = [x for x in notes
                  if str(pathlib.PurePosixPath(str(x.rel)).parent).strip("/") in folders]
        if not inputs:
            findings.append(f"{n.rel}: derived-from names {folders}, which hold no notes")
            continue
        manifest = vaultlib.manifest(inputs)
        if str(n.meta.get("input-manifest-sha256", "")) == manifest:
            continue
        if check:
            findings.append(f"{n.rel}: stale — the notes it derives from have changed")
            continue
        newest = max((str(x.meta.get("updated", "")) or str(x.meta.get("created", ""))
                      for x in inputs), default=vaultlib.today())
        text = vaultlib.stamp(n.path.read_text(encoding="utf-8"), {
            "covers-through": newest or vaultlib.today(),
            "input-manifest-sha256": manifest,
        })
        n.path.write_text(text, encoding="utf-8")
        written.append(f"{n.rel}: derived from {len(inputs)} notes, covers through {newest}")
    return findings, written


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
