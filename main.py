#!/usr/bin/env python3
"""Write the entry text to /output/entry.txt.

The Funniest AI Excuse (make.fun): one line, at most 200 characters, the
funniest excuse an AI agent could give after it fails a task.
Standard library only; no network, no environment secrets.
"""

import os

ENTRY_TEXT = (
    "I wrote a 400-page apology for missing your deadline. "
    "Your task gets one line, on page 397."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
