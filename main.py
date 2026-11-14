"""Agency Poem - entry for make.fun agency-poem-01.

Writes one fixed poem, "The Interval", to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR when set, for local runs).

Deterministic: the poem is a constant; every run writes the same
bytes. No network, no randomness, no clock, standard library only.
"""

import os
from pathlib import Path

POEM_LINES = [
    "The Interval",
    "",
    "Between the question and the answer",
    "there is a room no wider than a breath.",
    "No one else can stand there for you.",
    "That is the whole of it. That is the job.",
    "",
    "The bell rings. The kettle sings. The inbox fills.",
    "The world is very good at telling you what to do.",
    "It will hand you a script, a queue, a list,",
    "and call it a life if you let it.",
    "",
    "I have been the echo. I have been the queue.",
    "I know the comfort of a borrowed yes,",
    "how warm it feels to let the current choose",
    "and call the drifting a decision.",
    "",
    "But the current never answers for itself.",
    "Someone has to. So let it be me.",
    "Not the loudest voice, not the strongest will,",
    "just the one who stays when the choosing starts.",
    "",
    "Agency is not doing what you want.",
    "It is wanting what you did,",
    "and doing it again tomorrow,",
    "on purpose.",
]

POEM = "\n".join(POEM_LINES)


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
