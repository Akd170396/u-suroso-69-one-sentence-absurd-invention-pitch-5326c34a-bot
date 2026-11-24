"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance: burnt toast. The toaster ejects the toast on a
tiny parachute the instant it starts to burn, so breakfast lands safely
instead of smoking on the counter.
"""

import os

PITCH = (
    "A toaster that launches your toast out on a tiny parachute the instant "
    "it starts to burn, so breakfast lands safely instead of smoking on "
    "the counter."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")
    if not 1 <= len(PITCH) <= 220:
        raise ValueError(
            "pitch must be 1-220 characters (max 220), got %d; "
            "output file %s not written" % (len(PITCH), out_path)
        )
    if PITCH.count(".") != 1 or not PITCH.endswith("."):
        raise ValueError(
            "pitch must be exactly one sentence ending with a single "
            "period; output file %s not written" % out_path
        )
    if PITCH != PITCH.strip() or "\n" in PITCH or "  " in PITCH:
        raise ValueError(
            "pitch must be a single clean line (no leading/trailing "
            "whitespace, no newlines, no double spaces); output file "
            "%s not written" % out_path
        )
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
