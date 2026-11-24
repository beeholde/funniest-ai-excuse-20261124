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

# The gate refuses any text over 200 characters, so fail loudly here
# rather than silently shipping an entry the judge never sees.
MAX_CHARS = 200


def main() -> None:
    if len(ENTRY_TEXT) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(ENTRY_TEXT)} characters, over the {MAX_CHARS} limit"
        )
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
