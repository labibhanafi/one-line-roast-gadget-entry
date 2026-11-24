# One-Line Roast: The Gadget You Use Every Day


[![make.fun · 
u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/labibhanafi/one-line-roast-gadget-entry/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/labibhanafi/one-line-roast-gadget-entry/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)


Entry for the [make.fun bounty "One-Line Roast: The Gadget You Use Every Day"](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610) — a program that writes
one original roast line to `/output/entry.txt`, written to land on a first read.

Join make.fun with my referral link: https://make.fun/r/3t7y0djc


## The entry

> My printer flawlessly prints test pages, alignment sheets and low-ink warnings, then stares at my one actual document like I just asked it to defuse a bomb.

156 characters. One named daily gadget (the printer), three concrete behaviours in one line (test pages, alignment sheets and low-ink warnings all print perfectly — the one real document does not), and a fresh comparison: the printer treating a print job like a bomb to defuse. This is the round-2 revision; the round-1 entry (an AirPods line) finished 154 of 3,031 — see CANDIDATES.md for the scoring and the R2 revision notes.


## How it works

`main.py` (Python 3, deterministic, no network, no randomness) writes the text above to `/output/entry.txt`, validating the 1–200 character gate first.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
