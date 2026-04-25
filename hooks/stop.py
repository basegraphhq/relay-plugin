#!/usr/bin/env python3
"""Relay Stop hook.

Copies the Claude Code session transcript into the latest Relay session
directory (`<cwd>/.relay/sessions/session-*/transcript.jsonl`) so the
conversation is preserved alongside its decisions and summary in the repo.

Silent on failure — never blocks the Stop event.
"""

import json
import os
import shutil
import sys
from pathlib import Path


def find_latest_session_dir(cwd: str) -> Path | None:
    sessions = Path(cwd) / ".relay" / "sessions"
    if not sessions.is_dir():
        return None

    candidates = []
    for entry in sessions.iterdir():
        if not entry.is_dir() or not entry.name.startswith("session-"):
            continue
        if not (entry / "session.json").is_file():
            continue
        candidates.append((entry.stat().st_mtime, entry))

    if not candidates:
        return None
    candidates.sort(reverse=True)
    return candidates[0][1]


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)

    if data.get("stop_hook_active"):
        sys.exit(0)

    cwd = data.get("cwd") or os.getcwd()
    session_dir = find_latest_session_dir(cwd)
    if session_dir is None:
        sys.exit(0)

    transcript_path = os.path.expanduser(data.get("transcript_path", ""))
    if not transcript_path or not os.path.isfile(transcript_path):
        sys.exit(0)

    try:
        shutil.copyfile(transcript_path, session_dir / "transcript.jsonl")
    except OSError:
        pass


if __name__ == "__main__":
    main()
