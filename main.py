#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch note (at most 160 characters) for a bug in real
life or human biology, in the terse register of a real release
note, to /output/entry.txt.
"""

import os

OUT = "/output/entry.txt"

VERSION = "v4.1.0"
FIX = "fixed a bug where walking through a doorway wiped the current task from memory"
FOLLOW_UP = "the task is now cached until further notice"

# Assembled from the release-note parts so the version, the fix and
# the follow-up stay editable on their own; the joined line is the
# exact patch note the gate reads.
NOTE = "%s: %s; %s." % (VERSION, FIX, FOLLOW_UP)

# A release note is useless if it overflows its budget: refuse to
# ship a note longer than the 160-character gate allows.
MAX_NOTE_LEN = 160


def main():
    if len(NOTE) > MAX_NOTE_LEN:
        raise SystemExit("patch note is %d characters, over the 160 limit" % len(NOTE))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(NOTE)
    print("wrote %s %d characters" % (OUT, len(NOTE)))


if __name__ == "__main__":
    main()
