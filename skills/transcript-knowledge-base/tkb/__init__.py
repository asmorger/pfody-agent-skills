"""transcript-knowledge-base (tkb)

Build a curated, categorized **knowledge index** from a folder of conversation
transcripts. Each item is a clean, canonical statement (a rule / decision /
requirement / fact) with stable id and provenance back to the meeting, speaker,
timestamp, and quote it came from. Output is an Obsidian vault of small linked
notes — one per statement, one per meeting, one MOC — plus a small JSON state
cache for incremental re-runs. No database.

Layers:
    parsers/  ->  prepare (scan, change-detect, citation-tag)
    -> [agent extracts]  ->  index (merge/dedup) -> markdown deliverable

See SKILL.md for the agent workflow and README.md for the architecture.
"""

from .index import KnowledgeIndex, KnowledgeItem, Source

__all__ = ["KnowledgeIndex", "KnowledgeItem", "Source"]
__version__ = "2.0.0"
