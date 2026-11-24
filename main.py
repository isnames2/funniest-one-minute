"""One line: the funniest excuse an AI agent gives its human for a missed deadline."""

import os
from pathlib import Path

LINE = (
    # 116 characters, under the 200-character gate.
    "Your deadline was in my context window, but then you pasted a 40-page "
    "PDF and it scrolled off the edge of my memory."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
