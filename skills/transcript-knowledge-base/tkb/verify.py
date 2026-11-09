"""Verify that every quote in the vault is really in the transcript it cites.

    python -m tkb.cli verify --vault ./transcript-knowledge --folder ./Transcripts

Everything else in this skill checks *shape*: that an item has a source, that an id is stable, that
a note is the right size. None of it can tell whether `"we never split an order"` was said by the
person the note names, at the timestamp the note gives, in those words. That gap is the whole reason
the output is called evidence, and a citation nobody can check is worth less than no citation —
it reads as proof and behaves as a rumour.

So this reads the transcripts again, through the same parsers that produced the briefs, and for
every `[!quote] Evidence` block checks:

- the cited cue exists in that transcript;
- the speaker at that cue is the speaker the note names;
- every quoted word appears in the turns at that cue, in order. Ellipsis (`...` or `…`) marks an
  elision and is allowed. Punctuation and capitalisation are ignored, because the transcription
  service supplied them and they are not what anybody said.
- `[bracketed text]` is an editorial correction, skipped when matching words but required to carry a
  row in the errata register — and a quote that contains a registered span without its annotation is
  a problem too, so a correction cannot be applied in one note and forgotten in another.

A quotation of three or more words on a line with no full citation is counted as **unchecked** and
reported separately. It is not a failure; it is the honest statement that nothing verified it.

Exit status 1 when any problem is found. Standard library plus this package's parsers.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field

from .parsers import base as parsers_base
from .parsers import caption_parser, csv_parser, docx_parser, json_parser, text_parser  # noqa: F401

QUOTE_BLOCK = re.compile(
    r"^> \[!quote\][^\n]*\n((?:^>.*\n?)*)", re.M)
QUOTED = re.compile(r'[“"]([^”"]+)[”"]')
# `— Speaker, [[meeting-stem]] 0:14:22` — the citation the renderer writes.
CITE = re.compile(
    r"—\s*(?P<who>[^,\[]+?)\s*,\s*\[\[(?P<stem>[^\]|#]+?)(?:[|#][^\]]*)?\]\]"
    r"(?:\s*(?P<cue>\d+:\d\d(?::\d\d)?))?")
CUE = re.compile(r"\d+:\d\d(?::\d\d)?")
ELIDE = re.compile(r"\s*(?:\.\.\.|…)\s*")
BRACKET = re.compile(r"\[([^\]]*)\]")
UNLABELLED = re.compile(r"^(?P<name>.+?)\s*\[unlabeled (?P<token>@\d+)\]$")
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)
# Errata register rows: | transcript | cue | speaker | transcript says | correction | state | … |
ROW = re.compile(r"^\|(?P<cells>.+)\|\s*$", re.M)


@dataclass
class Problem:
    note: str
    message: str

    def __str__(self) -> str:
        return f"{self.note}: {self.message}"


@dataclass
class Result:
    problems: list[Problem] = field(default_factory=list)
    checked: int = 0
    unchecked: list[Problem] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.problems


def words(text: str) -> list[str]:
    """The words somebody said, with everything the transcription service added stripped off."""
    return re.findall(r"[0-9a-z]+", text.lower())


def _norm_speaker(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (name or "").lower()).strip()


def _cue_seconds(cue: str) -> int:
    parts = [int(p) for p in cue.split(":")]
    while len(parts) < 3:
        parts.insert(0, 0)
    return parts[0] * 3600 + parts[1] * 60 + parts[2]


# ---------------------------------------------------------------------------- #
# Reading the vault
# ---------------------------------------------------------------------------- #
def _frontmatter(text: str) -> dict:
    m = FRONTMATTER.match(text)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line[:1].isspace():
            key, _, val = line.partition(":")
            out[key.strip()] = val.strip().strip("\"'")
    return out


def transcript_map(vault: str) -> dict[str, str]:
    """meeting note stem -> the transcript file it was indexed from."""
    out: dict[str, str] = {}
    folder = os.path.join(vault, "meetings")
    if not os.path.isdir(folder):
        return out
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".md"):
            continue
        meta = _frontmatter(open(os.path.join(folder, name), encoding="utf-8").read())
        if meta.get("transcript"):
            out[name[:-3]] = meta["transcript"]
    return out


def errata(vault: str) -> list[dict]:
    """Rows of `errata.md`: a mishearing, or an unlabeled speaker's identity.

    A register, not a transcript edit: the transcript and its original are never touched, so the
    source's own words stay findable and the correction stays visible as a correction.
    """
    path = os.path.join(vault, "errata.md")
    if not os.path.exists(path):
        return []
    rows = []
    for m in ROW.finditer(open(path, encoding="utf-8").read()):
        cells = [c.strip() for c in m.group("cells").split("|")]
        if len(cells) < 6 or set("".join(cells)) <= set("-: "):
            continue
        if cells[0].lower() in ("transcript", ""):
            continue
        rows.append({"transcript": cells[0], "cue": cells[1], "speaker": cells[2],
                     "says": cells[3], "correction": cells[4], "state": cells[5]})
    return rows


# ---------------------------------------------------------------------------- #
# Reading the transcripts
# ---------------------------------------------------------------------------- #
def turns_for(path: str, folder: str) -> list[parsers_base.RawTurn] | None:
    """Parse a transcript through the same parser that produced its brief."""
    for candidate in (path, os.path.join(folder, os.path.basename(path))):
        if os.path.exists(candidate):
            ext = os.path.splitext(candidate)[1].lower()
            parser = parsers_base.get_parser(ext)
            if parser is None:
                return None
            try:
                return parser(candidate, open(candidate, encoding="utf-8", errors="replace").read())
            except parsers_base.ParseError:
                return None
    return None


def _turns_at(turns: list[parsers_base.RawTurn], cue: str) -> list[parsers_base.RawTurn]:
    """The turn the cue names, plus the ones after it — a quote may run past a turn boundary."""
    want = _cue_seconds(cue)
    for i, turn in enumerate(turns):
        if turn.start_time and CUE.fullmatch(turn.start_time.strip()) \
                and _cue_seconds(turn.start_time.strip()) == want:
            return turns[i:i + 4]
    return []


def _contains(segments: list[list[str]], haystack: list[str]) -> bool:
    """Every segment's words, in order, with the gaps an ellipsis is allowed to hide."""
    at = 0
    for segment in segments:
        if not segment:
            continue
        for start in range(at, len(haystack) - len(segment) + 1):
            if haystack[start:start + len(segment)] == segment:
                at = start + len(segment)
                break
        else:
            return False
    return True


# ---------------------------------------------------------------------------- #
# The check
# ---------------------------------------------------------------------------- #
def verify(vault: str, folder: str) -> Result:
    result = Result()
    stems = transcript_map(vault)
    rows = errata(vault)
    cache: dict[str, list[parsers_base.RawTurn] | None] = {}

    for rel in sorted(_markdown(vault)):
        note = os.path.relpath(rel, vault)
        text = open(rel, encoding="utf-8").read()
        for block in QUOTE_BLOCK.findall(text):
            body = "\n".join(line.lstrip("> ").rstrip() for line in block.splitlines())
            cite = CITE.search(body)
            quotes = QUOTED.findall(body)
            if not cite or not cite.group("cue"):
                for q in quotes:
                    if len(words(q)) >= 3:
                        result.unchecked.append(Problem(note, f'no checkable citation: "{q[:60]}"'))
                continue
            _check_one(result, note, body, quotes, cite, stems, rows, cache, folder)
    return result


def _check_one(result, note, body, quotes, cite, stems, rows, cache, folder) -> None:
    stem, cue, who = cite.group("stem"), cite.group("cue"), cite.group("who").strip()
    if stem not in stems:
        result.problems.append(Problem(note, f"cites [[{stem}]], which is not an indexed meeting"))
        return
    path = stems[stem]
    if path not in cache:
        cache[path] = turns_for(path, folder)
    parsed = cache[path]
    if parsed is None:
        result.problems.append(Problem(note, f"cannot read the transcript for [[{stem}]] ({path})"))
        return
    turns = _turns_at(parsed.turns if hasattr(parsed, "turns") else parsed, cue)
    if not turns:
        result.problems.append(Problem(note, f"cue {cue} is not in [[{stem}]]"))
        return

    # Speaker. An `@N` the transcript never labelled is cited as `Name [unlabeled @N]`, and the
    # register is what licenses the name.
    said_by = turns[0].speaker or ""
    unlabelled = UNLABELLED.match(who)
    if unlabelled:
        token = unlabelled.group("token")
        if _norm_speaker(said_by) != _norm_speaker(token):
            result.problems.append(Problem(
                note, f"{cue} in [[{stem}]] is {said_by or 'unlabelled'}, not {token}"))
        elif not _row_for(rows, stem, token):
            result.problems.append(Problem(
                note, f"register: {unlabelled.group('name')} [unlabeled {token}] has no row in "
                      f"errata.md for [[{stem}]]"))
    elif _norm_speaker(who) != _norm_speaker(said_by):
        result.problems.append(Problem(
            note, f"{cue} in [[{stem}]] is {said_by or 'unattributed'}, but the note cites {who}"))

    spoken = words(" ".join(t.text for t in turns))
    for quote in quotes:
        result.checked += 1
        # A bracket is an editorial correction: skipped when matching, and it must be registered.
        for correction in BRACKET.findall(quote):
            if not _row_for(rows, stem, correction, cue=cue):
                result.problems.append(Problem(
                    note, f"register: [{correction}] in a quote of [[{stem}]] has no errata row"))
        bare = BRACKET.sub(" ", quote)
        segments = [words(s) for s in ELIDE.split(bare)]
        if not _contains(segments, spoken):
            result.problems.append(Problem(
                note, f'not in [[{stem}]] at {cue}: "{quote.strip()[:70]}"'))
        # The other direction: a correction recorded for this passage must travel with every quote
        # of it, or the register is true in one note and ignored in the next.
        for row in rows:
            if _slug_match(row["transcript"], stem) and row["says"] \
                    and _contains([words(row["says"])], words(bare)) \
                    and row["correction"] not in quote:
                result.problems.append(Problem(
                    note, f"register: this quote contains \"{row['says']}\", which errata.md "
                          f"corrects to \"{row['correction']}\" — the annotation is missing"))


def _row_for(rows, stem, needle, cue=None) -> dict | None:
    for row in rows:
        if not _slug_match(row["transcript"], stem):
            continue
        if needle in (row["correction"], row["speaker"], row["says"]):
            if cue is None or not row["cue"] or row["cue"] == cue:
                return row
    return None


def _slug_match(a: str, b: str) -> bool:
    norm = lambda s: re.sub(r"[^a-z0-9]+", "", s.lower().replace(".md", ""))  # noqa: E731
    return norm(a) in norm(b) or norm(b) in norm(a)


def _markdown(root: str):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for name in filenames:
            if name.endswith(".md"):
                yield os.path.join(dirpath, name)
