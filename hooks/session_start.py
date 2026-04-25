#!/usr/bin/env python3
"""Relay SessionStart hook.

Reads prompts/relay-planner.md, strips its YAML frontmatter, and emits the
contents as `additionalContext` so every Claude Code session in a project
where this plugin is installed starts in Relay's behavioral contract.

This is the auto-activation mechanism: users never have to pick an output
style manually. With the plugin installed, their Claude Code becomes Relay.
"""

import json
import os
import re
import sys


def main() -> None:
    plugin_root = os.environ.get("CLAUDE_PLUGIN_ROOT", "")
    prompt_path = os.path.join(plugin_root, "prompts", "relay-planner.md")

    try:
        with open(prompt_path, "r", encoding="utf-8") as f:
            content = f.read()
    except OSError:
        sys.exit(0)

    content = re.sub(r"\A---\n.*?\n---\n+", "", content, count=1, flags=re.DOTALL).strip()

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": content,
        }
    }))


if __name__ == "__main__":
    main()
