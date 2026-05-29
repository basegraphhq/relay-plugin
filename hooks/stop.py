#!/usr/bin/env python3
"""Relay Stop hook.

No-op kept for compatibility with older plugin installs.
Relay no longer writes transcripts or session state by default.
"""

import sys


def main() -> None:
    sys.exit(0)


if __name__ == "__main__":
    main()
