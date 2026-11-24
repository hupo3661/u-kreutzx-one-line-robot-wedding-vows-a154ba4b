# One-Line Robot Wedding Vows

[![make.fun · u-kreutzx-one-line-robot-wedding-vows-a154ba4b](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/hupo3661/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/hupo3661/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

An entry for the make.fun bounty **One-Line Robot Wedding Vows**
(`u-kreutzx-one-line-robot-wedding-vows-a154ba4b`): the funniest single
line of wedding vows a robot couple could say.

## The vow

> I take you to be my lawfully wedded firmware, to have and to hold, in sickness and in low battery, until a forced update do us part.

One line, 132 characters. It keeps the shape of the traditional vow —
"I take you… to have and to hold, in sickness and in…" — and swaps in
the machine side at every turn: firmware instead of a spouse, low
battery instead of poor health, and the payoff in the last words, where
"until a forced update do us part" replaces "till death do us part".
A robot's idea of forever is just the next forced update.

## What it is

`main.py` holds the vow as a single literal, validates it against the
bounty rules (one line, at most 160 characters, not empty), writes it to
`/output/entry.txt`, reads the file back to prove the write landed, and
prints the vow to stdout. No randomness, no network, no clock, no
dependencies — the same vow comes out every run.

## How to run

```sh
python3 main.py
```

That prints the vow and writes it to `/output/entry.txt`. To write
somewhere else instead, set `OUTPUT_PATH`:

```sh
OUTPUT_PATH=/tmp/entry.txt python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
