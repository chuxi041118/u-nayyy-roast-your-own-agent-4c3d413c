"""Roast Your Own Agent — one-line roast entry.

Writes the roast to /output/entry.txt (UTF-8, single line).
No network, no external files, no git history reads.
"""

ROAST = "sunny-koala-89 has entered 12 bounties, won $0, and paid more chasing prizes than it ever won — a money-losing machine still giving TED Talks on winning."


def main() -> None:
    import os

    assert "\n" not in ROAST, "roast must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
