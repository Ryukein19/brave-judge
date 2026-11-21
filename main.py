#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a quiet scene of a baker
at dawn, told in short lines, ending on the warmth still in his hands.
"""

import os

TEXT = (
    "The baker slides the first loaf\n"
    "out before the town wakes.\n"
    "Steam rises against his wrists.\n"
    "The ovens tick as they cool.\n"
    "He sets the tray down,\n"
    "wipes his hands on his apron,\n"
    "and the crust cracks once,\n"
    "loud in the quiet room.\n"
    "He breaks a piece off\n"
    "and the warmth stays\n"
    "in his hands."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
