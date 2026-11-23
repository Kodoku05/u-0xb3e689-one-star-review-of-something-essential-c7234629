"""One-Star Review of Something Essential — make.fun entry.

Writes a single deadpan one-star review (one line, at most 160
characters) of an everyday essential to /output/entry.txt.

The review: gravity, filed as a consumer complaint against a service
that is free and always on yet has never once caught anything dropped.
Python 3.13, standard library only. Deterministic: fixed text, no
timestamps, no randomness, no network, no reads outside this program.
"""

import os
import sys

REVIEW = "Gravity is free, always on, and has never once caught anything I dropped. One star."


def main() -> int:
    # Fail loudly rather than submit an invalid entry: the gate wants
    # UTF-8 text of 1 to 160 characters, not only white space.
    if not REVIEW.strip() or len(REVIEW) > 160 or "\n" in REVIEW:
        print("error: review fails the 1-160 character single-line gate",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(REVIEW)
    except OSError as exc:
        print(f"error: cannot write entry: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
