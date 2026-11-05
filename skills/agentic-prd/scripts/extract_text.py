#!/usr/bin/env python3
"""Extract plain text from a source file so that an agent can read and cite it.

Supports .docx, .txt, .md, .vtt, .srt with the standard library.
Supports .pdf when pypdf or pymupdf is installed. PDF pages get a [page n] marker.

Usage: python extract_text.py <file> [<file> ...] --out <directory>
"""
import argparse
import html
import importlib
import pathlib
import re
import sys
import zipfile


def from_docx(path):
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf8")
    lines = []
    for para in re.findall(r"<w:p[ >].*?</w:p>", xml, flags=re.S):
        text = "".join(re.findall(r"<w:t(?: [^>]*)?>([^<]*)</w:t>", para))
        if text.strip():
            lines.append(html.unescape(text))
    return "\n".join(lines)


def from_pdf(path):
    for name in ("pypdf", "pymupdf", "fitz"):
        try:
            lib = importlib.import_module(name)
        except ImportError:
            continue
        if name == "pypdf":
            pages = [p.extract_text() or "" for p in lib.PdfReader(str(path)).pages]
        else:
            pages = [p.get_text() for p in lib.open(str(path))]
        return "\n\n".join(f"[page {i + 1}]\n{t}" for i, t in enumerate(pages))
    raise RuntimeError("PDF needs pypdf or pymupdf. Install one, or give the person a text copy.")


def extract(path):
    suffix = path.suffix.lower()
    if suffix == ".docx":
        return from_docx(path)
    if suffix == ".pdf":
        return from_pdf(path)
    if suffix in (".txt", ".md", ".vtt", ".srt"):
        return path.read_text(encoding="utf8", errors="replace")
    raise RuntimeError(f"Unsupported file type: {suffix}")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("files", nargs="+", type=pathlib.Path)
    parser.add_argument("--out", required=True, type=pathlib.Path)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    status = 0
    for path in args.files:
        try:
            text = extract(path)
        except (OSError, RuntimeError, KeyError, zipfile.BadZipFile) as exc:
            print(f"FAILED {path.name}: {exc}", file=sys.stderr)
            status = 1
            continue
        target = args.out / (path.stem + ".txt")
        target.write_text(text, encoding="utf8")
        print(f"{path.name}: {len(text.split())} words -> {target}")
    return status


if __name__ == "__main__":
    sys.exit(main())
