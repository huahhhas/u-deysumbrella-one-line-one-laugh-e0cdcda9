#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Prints the joke and writes it byte-identical to /output/entry.txt
(and to ./entry.txt when run locally).
"""

import os

LINE = "My screen time report said I scrolled for 7 hours yesterday, so I scrolled past the report in 3 seconds and learned absolutely nothing."


def main():
    # No trailing newline on stdout: stdout must be byte-identical to entry.txt.
    print(LINE, end="")
    for path in ("/output/entry.txt", "entry.txt"):
        try:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(LINE)
        except OSError:
            pass


if __name__ == "__main__":
    main()
