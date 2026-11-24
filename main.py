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
    if not 1 <= len(PITCH) <= 220:
        raise ValueError("pitch must be 1-220 characters, got %d" % len(PITCH))
    if PITCH.count(".") != 1 or not PITCH.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
