#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a person taking their first
step after an injury, told in short lines — fear (the floor is a long
way down), support (the nurse's hand on the elbow, then gone), and the
brave act (the first step), ending on the hallway shrinking from a mile
to only a hallway.
"""

import os

TEXT = (
    "The nurse took her hand off my elbow.\n"
    "One step, she said.\n"
    "The floor was a long way down.\n"
    "The rail was cold under my fingers.\n"
    "I put my foot out.\n"
    "The room went quiet.\n"
    "My leg held.\n"
    "I took another step,\n"
    "and the hallway,\n"
    "which had been a mile long,\n"
    "was only a hallway."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
