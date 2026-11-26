"""Funniest Cat Voicemail Greeting entry.

Writes exactly one funny voicemail greeting (<= 120 chars), recorded as
if by a cat, to /output/entry.txt. Deterministic: same bytes on every run.
No network, no secrets, no dependencies.

Candidates considered (all <= 120 chars), and why this one won:
- "You've reached Mochi. I'm busy knocking things off shelves. Leave a
  message after the beep -- I'll knock that off too." (117) -- clever,
  but "knocking things off shelves" is generic phrasing.
- "Hi, it's Miso. I'm pushing your glass off the table. Leave a message
  after the beep -- I'll knock that off too." (110) -- concrete, but the
  punch is wordplay rather than character.
- "You've reached the cat. I'm asleep on your keyboard, so leave a
  message after the beep -- I'll delete it with my butt." (117) -- funny,
  but cruder and the laugh is a sight gag, not a voice.
- "You've reached Biscuit. I'm on my nineteenth nap today. Leave a
  message after the beep, then go feed me at 4 a.m." (113) -- cat-specific,
  but "go feed me" is a demand, not a punchline.
- "You've reached Biscuit. Leave a message after the beep -- if it's
  about the vase, I did it, and I'd do it again." (111) -- CHOSEN: a
  clear voicemail greeting, a first-person cat voice, the vase is the
  classic knocked-off object, and the unrepentant confession
  ("I did it, and I'd do it again") lands the laugh out loud, fast.
"""

import os

ENTRY = (
    "You've reached Biscuit. Leave a message after the beep \u2014 if it's "
    "about the vase, I did it, and I'd do it again."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
