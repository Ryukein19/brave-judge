#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a quiet scene of an old dog
laying its head in a child's lap, told in short lines, ending on the
weight of him being the whole evening.
"""

import os

TEXT = (
    "The old dog crosses the room\n"
    "one slow step at a time\n"
    "and lays his head\n"
    "in your lap.\n"
    "His muzzle is grey now,\n"
    "his ears are soft as cloth.\n"
    "His breathing slows.\n"
    "Your hand stays where it is,\n"
    "resting on the warm spot\n"
    "between his ears,\n"
    "and the weight of him\n"
    "is the whole evening."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
