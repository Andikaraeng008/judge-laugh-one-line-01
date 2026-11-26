"""Make the Judge Laugh in One Line — entry program.

Writes one funny line (1-200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt).
"""

import os

LINE = "My smart fridge texted me at 3 a.m. to say it was leaving me \u2014 apparently I kept opening it just to stare, and it felt used."


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line length {len(LINE)} out of range"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR is a directory; fall back to /output/entry.txt.
    # The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
    out_path = out_dir if out_dir.endswith(".txt") else os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
