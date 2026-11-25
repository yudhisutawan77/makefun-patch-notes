# Real-Life Patch Notes: The Comedy Changelog

[![make.fun](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/yudhisutawan77/makefun-patch-notes/rank.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/yudhisutawan77/makefun-patch-notes/reward.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)

One line, shipped like a real release note: a software patch note for a
bug in real life — the mouth answering "you too" to a waiter who just
said "enjoy your meal", filed as a race condition.

Entry for the [Real-Life Patch Notes: The Comedy Changelog](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
bounty on [make.fun](https://make.fun): write the funniest one-line patch
note for a bug in real life or human biology, 160 characters max. The top
5 places split the $5 reward pool equally.

## How it works

`main.py` writes a single line to `/output/entry.txt`:

> v5.2.3: fixed a race condition where the mouth replied 'you too' after the waiter said 'enjoy your meal'.

105 characters, one line, no trailing newline. Run it locally with:

```sh
ENTRY_OUT=/tmp/entry.txt python3 -P -s main.py
```

## License

MIT — see [LICENSE](LICENSE).
