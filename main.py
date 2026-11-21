#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: an old woman waters dry
earth every morning, nothing shows, she waters it anyway — and one
morning a green shoot stands where there was only dust. Quiet patience:
a small act, repeated, and something grows on its own, ending on the
warmth of the earth under her palm.
"""

import os

TEXT = (
    "The old woman waters the dry earth\n"
    "every morning, the same small can.\n"
    "Nothing shows.\n"
    "The earth takes it.\n"
    "She waters it anyway.\n"
    "One morning the soil is dark\n"
    "and a green shoot stands\n"
    "where there was only dust.\n"
    "She puts her hand down\n"
    "and the earth is warm\n"
    "under her palm."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
