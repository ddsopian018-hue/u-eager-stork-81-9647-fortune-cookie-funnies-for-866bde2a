"""Fortune Cookie Funnies for Engineers — one-line fortune (107 chars).

The line: a Friday deploy sails through every test, then the pager goes
off at 3:12 a.m. on Saturday — and the crash is on the one endpoint nobody
on the team owns. The joke lands on the gap between "all tests green" and
"the one unowned endpoint", with the very specific 3:12 a.m. page making
the scene concrete instead of generic. It reads as a fortune ("Your Friday
deploy will...") rather than a punchline about the reader, which is what
keeps it in the fortune-cookie register.
"""

import os

LINE = (
    "Your Friday deploy will pass every test, then page you at 3:12 a.m. "
    "Saturday from the endpoint nobody owns."
)


def main() -> None:
    assert 1 <= len(LINE) <= 120, f"fortune must be 1-120 chars, got {len(LINE)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
