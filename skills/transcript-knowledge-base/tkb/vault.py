"""Render the knowledge index as an Obsidian vault of small, linked notes.

One note per knowledge item, one note per meeting, one MOC with a Bases embed and a generated
table. Everything here is generated, so a re-run overwrites it — which is the opposite of the
record vault that `anchored-knowledge` keeps, where notes are hand-written and promoted.

Two things make a re-run safe. A note's ``created`` date is read back from the existing file and
preserved, so only ``updated`` moves. And the files this renderer wrote are recorded in
``.tkb-manifest.json``; on the next run, any of them that is no longer generated is deleted, while a
file the manifest does not name is never touched — so a note somebody dropped into the folder
survives.

The state file keeps the quotes and timestamps too. That is not a second home for them: it is the
merge cache that makes an incremental run possible, and it is regenerable from nothing but the
notes it wrote.
"""

from __future__ import annotations

import json
import os
import re
from typing import Iterable, Optional

from .index import KnowledgeIndex, KnowledgeItem, Source, slugify
from .utils import now_iso

MANIFEST = ".tkb-manifest.json"
GEN_OPEN = "<!-- generated: do not edit"
GEN_CLOSE = "<!-- /generated -->"
NAME_MAX = 72


def render_vault(idx: KnowledgeIndex, out_dir: str) -> dict:
    """Write the whole vault. Returns a summary dict for the CLI to print."""
    idx.generated_at = now_iso()
    today = idx.generated_at[:10]
    previous = _read_manifest(out_dir)

    meetings = _meeting_notes(idx)
    # Filenames first, because a citation's target is a filename: an item cannot be linked until
    # the note that holds it has a name. Both the item notes and the MOC cite from this one map.
    stems = _item_stems(idx)
    items = _item_notes(idx, meetings, stems)
    written: list[str] = []

    for rel, body in sorted(meetings_payload(idx, meetings, today).items()):
        written.append(_write(out_dir, rel, body))
    for rel, body in sorted(items.items()):
        written.append(_write(out_dir, rel, body))

    moc_rel = "moc/" + _slug(idx.title or "transcript knowledge") + ".md"
    base_rel = "bases/" + _slug(idx.title or "transcript knowledge") + ".base"
    written.append(_write(out_dir, base_rel, _base_definition()))
    written.append(_write(out_dir, moc_rel, _moc_note(idx, today, base_rel, stems)))

    removed = _prune(out_dir, previous, written)
    _write_manifest(out_dir, written)
    return {
        "vault": out_dir,
        "moc": moc_rel,
        "items": len(items),
        "meetings": len(meetings),
        "files_written": len(written),
        "files_removed": removed,
        "categories": len([c for c in idx.category_order
                           if any(i.category == c for i in idx.items.values())]),
    }


# ---------------------------------------------------------------------------- #
# Meetings
# ---------------------------------------------------------------------------- #
def _meeting_notes(idx: KnowledgeIndex) -> dict[tuple, str]:
    """Map (meeting name, date) -> note stem, for every meeting any item cites.

    Built from the items rather than from ``ingested_files``, because what earns a meeting a note
    is having produced a statement. A transcript that yielded nothing is recorded in the state and
    needs no note.
    """
    stems: dict[tuple, str] = {}
    used: set[str] = set()
    for key in sorted(_cited_meetings(idx)):
        name, date = key
        stem = f"{date}-{_slug(name)}" if date else _slug(name)
        stems[key] = _unique(stem or "meeting", used)
    return stems


def _cited_meetings(idx: KnowledgeIndex) -> set[tuple]:
    out = set()
    for item in idx.items.values():
        for s in item.sources:
            if s.meeting:
                out.add((s.meeting, s.date))
    return out


def meetings_payload(idx: KnowledgeIndex, stems: dict[tuple, str], today: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for (name, date), stem in stems.items():
        speakers, files, hashes = set(), set(), set()
        for item in idx.items.values():
            for s in item.sources:
                if (s.meeting, s.date) == (name, date):
                    if s.speaker:
                        speakers.add(s.speaker)
                    if s.file:
                        files.add(s.file)
        for path, rec in idx.ingested_files.items():
            if rec.get("name") == name:
                files.add(path)
                if rec.get("hash"):
                    hashes.add(rec["hash"])
        meta = {
            "type": "meeting",
            "status": "ingested",
            "meeting-date": date or "",
            "participants": sorted(speakers),
            "transcript": sorted(files)[0] if files else "",
            "content-hash": sorted(hashes)[0][:16] if hashes else "",
            "citable": "false",
            "created": today,
            "updated": today,
            }
        body = [
            f"# {name}" + (f" — {date}" if date else ""),
            "",
            "Indexed by `transcript-knowledge-base`. **What this meeting produced is its "
            "backlinks** — every statement that cites it links here, so no list on this side needs "
            "maintaining.",
            "",
            "> [!warning] Evidence, not record",
            "> A statement that exists only here cannot be cited by a story, a spec or a test. It is "
            "> promoted into the project's record first.",
        ]
        out[f"meetings/{stem}.md"] = _note(meta, body)
    return out


# ---------------------------------------------------------------------------- #
# Items
# ---------------------------------------------------------------------------- #
def _item_stems(idx: KnowledgeIndex) -> dict[str, str]:
    """id -> note filename, assigned once so every citation of an item agrees on its target."""
    used: set[str] = set()
    stems: dict[str, str] = {}
    for item in sorted(idx.items.values(), key=lambda i: _sort_key(i.id)):
        stems[item.id] = _unique(_slug(item.statement) or item.id.lower(), used)
    return stems


def _cite(ident: str, stems: dict[str, str], table: bool = False) -> str:
    """An id as a link Obsidian resolves: filename as target, id as display text.

    Obsidian matches a wikilink against filenames and paths, never against `aliases`, so a bare
    `[[AUTH-1]]` opens a new empty note however faithfully the alias is written. In a table cell
    the pipe has to be escaped or it ends the column.
    """
    stem = stems.get(ident)
    if not stem:
        return ident
    return f"[[{stem}\\|{ident}]]" if table else f"[[{stem}|{ident}]]"


def _item_notes(idx: KnowledgeIndex, meetings: dict[tuple, str],
                stems: dict[str, str]) -> dict[str, str]:
    out: dict[str, str] = {}
    by_id = {it.id: it for it in idx.items.values()}
    for item in sorted(idx.items.values(), key=lambda i: _sort_key(i.id)):
        stem = stems[item.id]
        out[f"items/{stem}.md"] = _item_note(item, meetings, by_id, used_stem=stem, stems=stems)
    return out


def _item_note(item: KnowledgeItem, meetings: dict[tuple, str],
               by_id: dict[str, KnowledgeItem], used_stem: str,
               stems: dict[str, str]) -> str:
    sources = sorted({meetings[(s.meeting, s.date)]
                      for s in item.sources if s.meeting and (s.meeting, s.date) in meetings})
    meta = {
        "id": item.id,
        "aliases": [item.id],
        "type": "transcript-item",
        "status": item.status,
        "category": item.category,
        "sources": [f"[[{s}]]" for s in sources],
        "supersedes": [_cite(s, stems) for s in item.supersedes],
        "related": [_cite(r, stems) for r in item.related],
        "citable": "false",
        "created": "",          # filled by _write from the existing file, or today
        "updated": "",
    }
    body = [f"# {item.id} — {item.statement}", ""]
    if item.status != "confirmed" or item.note:
        label = item.status.capitalize() if item.status != "confirmed" else "Note"
        callout = {"superseded": "abstract", "deferred": "failure"}.get(item.status, "warning")
        if item.status == "confirmed":
            callout = "info"
        body += [f"> [!{callout}] {label}"]
        if item.note:
            body += [f"> {item.note}"]
        if item.supersedes:
            body += ["> Supersedes " + ", ".join(_cite(s, stems) for s in item.supersedes) + "."]
        body += [""]
    for s in item.sources:
        if not s.quote:
            continue
        who = s.speaker or "unattributed"
        where = meetings.get((s.meeting, s.date))
        cite = f"[[{where}]]" if where else (s.meeting or "unknown meeting")
        stamp = f" {s.timestamp}" if s.timestamp else ""
        body += ["> [!quote] Evidence", f'> "{s.quote.strip()}"', f"> — {who}, {cite}{stamp}", ""]
    if item.related:
        body += ["**Also** " + " · ".join(_cite(r, stems) for r in item.related)]
    return _note(meta, body)


# ---------------------------------------------------------------------------- #
# MOC and Bases
# ---------------------------------------------------------------------------- #
def _moc_note(idx: KnowledgeIndex, today: str, base_rel: str, stems: dict[str, str]) -> str:
    meta = {
        "type": "moc",
        "updated": today,
        "transcripts": len(idx.ingested_files),
    }
    body = [f"# {idx.title}", ""]
    if idx.intro:
        body += [idx.intro, ""]
    body += [
        f"{len(idx.items)} statements from {len(idx.ingested_files)} transcript(s), each a note in "
        "`items/` citing the meeting it came from. Generated by `transcript-knowledge-base` — "
        "**every note in this folder is overwritten on the next run**, so curate by re-extracting, "
        "not by editing.",
        "",
        "> [!warning] Evidence, not record",
        "> This index is a **supplemental source**. A statement here is what somebody said in a "
        "> meeting, not what the project has agreed; the meeting two weeks later may have reversed "
        "> it. Reconcile it into the project's record before anything cites it.",
        "",
        f"![[{os.path.basename(base_rel)}]]",
        "",
        f"{GEN_OPEN} · {today} -->",
    ]
    for category in idx.category_order:
        rows = [it for it in idx.items.values() if it.category == category]
        if not rows:
            continue
        rows.sort(key=lambda i: _sort_key(i.id))
        body += [f"### {category}", "", "| ID | Statement | Status | Sources |", "|---|---|---|---|"]
        for it in rows:
            srcs = sorted({f"[[{m}]]" for m in _item_meeting_stems(it, idx)})
            body.append(f"| {_cite(it.id, stems, table=True)} | {_cell(it.statement)} | "
                        f"{it.status} | {' · '.join(srcs) or '—'} |")
        body.append("")
    body.append(GEN_CLOSE)
    return _note(meta, body)


def _item_meeting_stems(item: KnowledgeItem, idx: KnowledgeIndex) -> set[str]:
    stems = _meeting_notes(idx)
    return {stems[(s.meeting, s.date)] for s in item.sources
            if s.meeting and (s.meeting, s.date) in stems}


def _base_definition() -> str:
    return """filters:
  and:
    - file.hasTag("transcript-item")
properties:
  note.id:
    displayName: ID
  note.status:
    displayName: Status
  note.sources:
    displayName: Meetings
views:
  - type: table
    name: All statements
    order:
      - note.id
      - file.name
      - note.status
      - note.sources
    groupBy:
      property: note.category
      direction: ASC
  - type: table
    name: Needs a decision
    filters:
      or:
        - 'note.status == "tentative"'
        - 'note.status == "draft"'
        - 'note.status == "pending"'
    order:
      - note.id
      - file.name
      - note.status
  - type: table
    name: Superseded and deferred
    filters:
      or:
        - 'note.status == "superseded"'
        - 'note.status == "deferred"'
    order:
      - note.id
      - file.name
      - note.status
      - note.supersedes
"""


# ---------------------------------------------------------------------------- #
# Writing
# ---------------------------------------------------------------------------- #
def _note(meta: dict, body: Iterable[str]) -> str:
    lines = ["---"]
    for key, value in meta.items():
        lines.append(f"{key}: {_yaml(value)}")
    lines += ["---", ""]
    return "\n".join(lines + list(body)).rstrip() + "\n"


def _yaml(value) -> str:
    if isinstance(value, list):
        if not value:
            return "[]"
        return "[" + ", ".join(_yaml_scalar(v) for v in value) + "]"
    return _yaml_scalar(value)


def _yaml_scalar(value) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    text = str(value)
    if text == "":
        return ""
    # Wikilinks and anything with YAML-significant punctuation must be quoted.
    if text.startswith("[[") or re.search(r'[:#,\[\]{}&*!|>\'"%@`]', text) or text != text.strip():
        return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return text


def _write(out_dir: str, rel: str, body: str) -> str:
    path = os.path.join(out_dir, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    body = _preserve_created(path, body)
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            if fh.read() == body:
                return rel
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)
    return rel


def _preserve_created(path: str, body: str) -> str:
    """Keep the note's original ``created`` date, and fill a blank one with today."""
    today = now_iso()[:10]
    existing = ""
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            head = fh.read(2048)
        m = re.search(r"^created:\s*(\S+)\s*$", head, re.M)
        if m:
            existing = m.group(1)
    if "\ncreated: \n" in body or body.startswith("created: \n"):
        body = body.replace("\ncreated: \n", f"\ncreated: {existing or today}\n", 1)
    if "\nupdated: \n" in body:
        body = body.replace("\nupdated: \n", f"\nupdated: {today}\n", 1)
    return body


def _read_manifest(out_dir: str) -> list[str]:
    path = os.path.join(out_dir, MANIFEST)
    if not os.path.exists(path):
        return []
    try:
        with open(path, encoding="utf-8") as fh:
            return list(json.load(fh).get("files", []))
    except (json.JSONDecodeError, OSError):
        return []


def _write_manifest(out_dir: str, written: list[str]) -> None:
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, MANIFEST), "w", encoding="utf-8") as fh:
        json.dump({"generated": now_iso(), "files": sorted(set(written))}, fh, indent=2)
        fh.write("\n")


def _prune(out_dir: str, previous: list[str], written: list[str]) -> int:
    """Delete only files this renderer wrote before and no longer writes."""
    gone = set(previous) - set(written)
    removed = 0
    for rel in sorted(gone):
        path = os.path.join(out_dir, rel)
        if os.path.exists(path):
            os.remove(path)
            removed += 1
    for sub in ("items", "meetings", "moc", "bases"):
        d = os.path.join(out_dir, sub)
        if os.path.isdir(d) and not os.listdir(d):
            os.rmdir(d)
    return removed


# ---------------------------------------------------------------------------- #
# Small helpers
# ---------------------------------------------------------------------------- #
def _slug(text: str) -> str:
    s = slugify(text or "")
    if len(s) <= NAME_MAX:
        return s
    cut = s[:NAME_MAX]
    return cut.rsplit("-", 1)[0] if "-" in cut else cut


def _unique(stem: str, used: set[str]) -> str:
    candidate, n = stem, 2
    while candidate in used:
        candidate, n = f"{stem}-{n}", n + 1
    used.add(candidate)
    return candidate


def _cell(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").replace("|", "\\|")).strip()


def _sort_key(ident: str) -> tuple:
    m = re.match(r"([A-Za-z-]*)(\d*)", ident or "")
    return (m.group(1), int(m.group(2) or 0))
