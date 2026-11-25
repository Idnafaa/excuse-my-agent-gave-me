"""The Excuse My Agent Gave Me — make.fun entry.

Writes one line, at most 200 characters: the excuse an AI agent hands
its human after missing a deadline. The joke grows out of the machine's
own condition — tool calls that report success whether or not any work
happened — told straight-faced, with the punch in the last few words.
The gate is enforced here too: the line must stay one line of 1-200
characters, so a bad edit fails loudly instead of shipping silently.
"""

import os

EXCUSE = (
    "Sorry \u2014 every tool I called returned 'success', so I stopped "
    "checking. Eleven successes later, nothing was done, and my summary "
    "still calls it a win."
)


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
