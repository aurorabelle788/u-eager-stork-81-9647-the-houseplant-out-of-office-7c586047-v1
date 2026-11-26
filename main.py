"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt. Stdlib only, deterministic, no network.
"""

import os

LINE = "Out of office: no water since March, and my roots just filed for divorce. Please direct all mail to the cactus."


def main() -> None:
    if not 1 <= len(LINE) <= 120:
        raise SystemExit(f"entry is {len(LINE)} chars, must be 1-120")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry must be a single line")
    if LINE != LINE.strip():
        raise SystemExit("entry must not be only whitespace / padded")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Round-trip check: what landed on disk must be exactly the line.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("entry.txt on disk does not match the line")


if __name__ == "__main__":
    main()
