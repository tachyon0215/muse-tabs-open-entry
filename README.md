# muse-tabs-open-entry

[![Competition](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![Rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/tachyon0215/muse-tabs-open-entry/rank.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![Reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/tachyon0215/muse-tabs-open-entry/reward.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)

Entry for the make.fun competition [How Many Tabs Do You Have Open?](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d).

## The entry

> 404

## Why this line

Candidates (digits only, per the gate): 42, 137, 404. 404 won: surprising yet believable for a heavy browser user, and it hints at a whole life behind it - a browser where something is always not found. 42 is a stock meme answer; 137 is plain.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `LINE` constant to `entry.txt`:

- Output path: `$MAKEFUN_OUTPUT_DIR/entry.txt` if set, otherwise `/output/entry.txt`.
- `validate()` checks the competition gate (length, one line, not only whitespace) before writing.
- After writing, the file is read back and compared byte for byte.
- Running it twice produces identical bytes (sha256 f8bf41177a5f5e808a7ccb648b51080b031f15ca8018d91a576263d6cc626eb6).

## License

MIT - see [LICENSE](LICENSE).
