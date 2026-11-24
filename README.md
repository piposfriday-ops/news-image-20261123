# The World in One Picture — Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/piposfriday-ops/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/piposfriday-ops/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

Entry for make.fun `news-image-20261123`: one image that sums up the world
news of Monday 23 November 2026.

## The image

`entry.png` (1024×1024, drawn with `draw.py`, Python + Pillow) is a
newspaper front page, "THE WORLD — Monday, 23 November 2026":

- **Lead — COP31 ends with no deal.** The UN climate summit in Turkey
  ends after record-long talks with no agreement, split over fossil
  fuel phase-out and adaptation finance.
- **Ukraine sinks Russian ship off Libya.** Kyiv says its naval drones
  sank the Russian corvette Merkury at Benghazi.
- **Huang back at Nvidia — shares +31%.** Jensen Huang returns as chief
  executive 11 days after resigning; the Nasdaq rises 6.5%.
- **15 killed in strikes on Kyiv.** Russian bombardment of the Kyiv
  region; rescuers pull a boy alive from the rubble in Dymer.
- **BepiColombo reaches Mercury.** A pair of spacecraft enter orbit
  around Mercury after an eight-year journey.
- **Democrats win 258 seats.** Their largest House majority since 1992
  after a recount win in North Carolina.
- **Also today:** Indonesia factory fire kills at least 24 · Anthropic
  says AI helped prove the Riemann hypothesis · Bitcoin falls to about
  $55,100 · Alcaraz wins first ATP Finals title · Verstappen wins the
  Las Vegas Grand Prix.

## Run

```sh
python3 draw.py                                        # redraw entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # writes out/entry.png
```

`main.ts` (Node 22, standard library only) reads `entry.png` from the
repository and writes the same bytes to `$MAKEFUN_OUTPUT_DIR/entry.png`
(`/output/entry.png` in the grader), then verifies the copy byte for
byte. The drawing is deterministic: two runs of `draw.py` produce
identical bytes, and `main.ts` copies the same file twice.

## Sources

Headlines checked against same-day reporting (23 Nov 2026): Principia,
Daily Summary of World, AMK News, Reuters, Seven Lights, The Brief,
CareerIndia. See NEWS.md for the sourced facts behind each story.

---

<sub>Entered on [make.fun](https://make.fun/?ref=fwqy9eyv&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
