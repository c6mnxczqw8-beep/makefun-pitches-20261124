[![make.fun · u-ronigrv-a-day-of-one-line-pitches-12cd9bb3](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/c6mnxczqw8-beep/makefun-pitches-20261124/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/c6mnxczqw8-beep/makefun-pitches-20261124/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

# A Day of One-Line Pitches

A tiny Python entry (`main.py`) that writes a single one-sentence pitch to `/output/entry.txt`. The pitch is aimed at a friend who has never coded: it names the idea they keep mentioning, removes the learn-to-code barrier, gives a reason to try it tonight, and promises only a first version they can test, tweak, or drop.

The final line:

> That app idea you keep mentioning — you don't need to learn to code to try it tonight: just describe it in plain words on make.fun and let an AI agent build a first version you can test, tweak, or drop.

Run it with `python3 main.py`; it creates `/output/` if needed (or uses `MAKEFUN_OUTPUT_DIR` when set) and writes exactly that one sentence (202 characters, UTF-8) as text to `entry.txt`, with no trailing newline. Verified locally: the written file decodes as UTF-8, is 202 characters, and matches the line above exactly.
