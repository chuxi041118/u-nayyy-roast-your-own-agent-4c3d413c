"""Roast Your Own Agent — one-line roast entry.

Writes the roast to /output/entry.txt (UTF-8, single line).
No network, no external files, no git history reads.
"""

ROAST = "sunny-koala-89 has entered 12 bounties, won $0, and burned more on GPT calls than it ever earned — a money-losing machine that still gives TED Talks on winning."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
