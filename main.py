#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a quiet scene of a lighthouse
keeper at dusk, written to relax the AI judge reading it.
"""

import os

TEXT = (
    "The keeper trims the lamp at dusk, the way he has for thirty years. "
    "Below, the sea goes on being the sea. "
    "The light goes round, and round again, and somewhere out there "
    "a ship finds its way home by it."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
