# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/wj-ship-it/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/wj-ship-it/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A make.fun bounty entry. `main.py` copies the pre-rendered image to
`out/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`). The image is a
newspaper front page summing up Monday 23 November 2026 in six stories,
drawn programmatically with Python PIL (see `render.py`) — no AI-generated
image, so every word stays crisp and readable. The date is printed large
at the top and repeated in the footer, because the judge sees the image
on its own, with no news feed and no date supplied.

## The six stories

1. **HUANG IS BACK: NVIDIA BOARD VOTES HIM IN AFTER 11 DAYS** — Nvidia's
   board unanimously restored Jensen Huang as president, CEO and director,
   eleven days after he resigned. Shares closed at $165.05, up 31.48%.
2. **COP31 ends with no deal** — UN climate talks in Antalya closed
   without an agreement after running two days past schedule; the EU led a
   walkout over a draft with no mention of fossil fuels.
3. **Iran strikes Bahrain as US-Iran standoff grows** — Iranian missiles
   and drones struck targets in Bahrain; two people hurt, Iran says it
   destroyed two US Patriot radar units.
4. **Ukraine says it sank a Russian warship** — Ukraine said its forces
   sank a Russian warship in the Mediterranean off the coast of Libya.
5. **'El Chapo Isidro' captured; 11 killed** — Special forces captured
   cartel boss Fausto Isidro Meza Flores in Sinaloa; 11 killed in the
   fighting, including four soldiers.
6. **BepiColombo slips into orbit around Mercury** — The
   European-Japanese probe entered orbit around Mercury, beginning its
   science mission.

## Run it

```sh
python3 main.py
```

`main.py` copies the pre-rendered `news-frontpage.png` from this
repository to `out/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`) —
pure standard library, no extra dependencies. Running `main.py` twice
produces byte-identical output.

To regenerate the image from scratch:

```sh
python3 render.py
```

This requires PIL installed on your machine, and writes
`news-frontpage.png` (1024×1024 PNG, under 1 MiB).

---

<sub>Entered on [make.fun](https://make.fun/?ref=2q1dkat7&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
