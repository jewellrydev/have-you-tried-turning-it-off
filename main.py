"""Have You Tried Turning It Off? — a make.fun entry.

Prints exactly one line: what a hopeless tech support agent says to a
desperate customer, under 200 characters.
"""

LINE = (
    "Have you tried turning it off and on again? Sir, the smoke means it "
    "already turned itself off for good, but I admire your optimism."
)


def build_line() -> str:
    line = LINE
    assert len(line) < 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
