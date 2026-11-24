#!/usr/bin/env python3
"""THE WORLD — Monday, 23 November 2026. A one-page newspaper front page.

Everything visible is drawn by this file with Pillow: no photos, no
downloads, no randomness. Run it twice and the PNG bytes are identical.
Six stories from Monday 23 November 2026, checked against same-day
reporting (see NEWS.md for the sourced facts).
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

CANVAS_W, CANVAS_H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(HERE, "entry.png")

PAPER = (251, 247, 239)
INK = (17, 17, 17)
SCARLET = (178, 38, 30)
MUTE = (96, 96, 96)
PALE = (210, 205, 192)
OCEAN = (28, 68, 110)
OCEAN_DARK = (18, 46, 78)
LEAF = (46, 140, 70)
EMBER = (235, 110, 40)
NIGHT = (22, 30, 54)
SAND = (232, 178, 64)

DEJAVU = "/usr/share/fonts/truetype/dejavu"


def load_font(filename, size):
    return ImageFont.truetype(os.path.join(DEJAVU, filename), size)


SERIF = "DejaVuSerif.ttf"
SERIF_BOLD = "DejaVuSerif-Bold.ttf"
SANS = "DejaVuSans.ttf"
SANS_BOLD = "DejaVuSans-Bold.ttf"


def fit_text(d, text, fnt, max_width):
    """Greedy word wrap; returns a list of lines that fit max_width."""
    wrapped, current = [], ""
    for word in text.split(" "):
        candidate = word if not current else current + " " + word
        if d.textlength(candidate, font=fnt) <= max_width:
            current = candidate
        else:
            if current:
                wrapped.append(current)
            current = word
    if current:
        wrapped.append(current)
    return wrapped


def block(d, x, y, text, fnt, max_width, line_gap, color=INK):
    """Draw a wrapped paragraph; return the y below its last line."""
    for line in fit_text(d, text, fnt, max_width):
        d.text((x, y), line, font=fnt, fill=color)
        y += line_gap
    return y


def hline(d, x0, y, x1, weight=2, color=INK):
    d.line([(x0, y), (x1, y)], fill=color, width=weight)


def tag(d, x, y, text):
    """Red uppercase kicker; returns the y below it."""
    f = load_font(SANS_BOLD, 15)
    d.text((x, y), text, font=f, fill=SCARLET)
    return y + 22


def head_text(d, x, y, text, size, max_width):
    """Bold serif headline, wrapped; returns the y below it."""
    f = load_font(SERIF_BOLD, size)
    for line in fit_text(d, text, f, max_width):
        d.text((x, y), line, font=f, fill=INK)
        y += int(size * 1.08)
    return y


def globe_no_deal(d, x0, y0, x1, y1):
    """Earth with a red crack and a NO DEAL ribbon: COP31 fails."""
    d.rectangle([x0, y0, x1, y1], outline=PALE, width=1)
    cx, cy, r = (x0 + x1) // 2, (y0 + y1) // 2 - 6, 92
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=OCEAN)
    # continents: rough green blobs
    d.ellipse([cx - 78, cy - 58, cx - 18, cy - 6], fill=LEAF)
    d.ellipse([cx - 52, cy - 12, cx + 8, cy + 44], fill=LEAF)
    d.ellipse([cx + 26, cy - 40, cx + 80, cy + 8], fill=(58, 150, 84))
    d.ellipse([cx + 8, cy + 34, cx + 62, cy + 78], fill=(58, 150, 84))
    # polar cap and cloud arcs
    d.pieslice([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=(240, 244, 248))
    for (ax, ay, bx, by) in [(cx - 70, cy - 30, cx - 20, cy - 18),
                             (cx + 10, cy + 6, cx + 62, cy + 18),
                             (cx - 40, cy + 52, cx + 10, cy + 64)]:
        d.arc([ax, ay, bx, by], 200, 340, fill=(225, 235, 240), width=5)
    # the crack: jagged red line across the globe
    crack = [(cx - 84, cy - 62), (cx - 48, cy - 30), (cx - 58, cy + 2),
             (cx - 14, cy + 26), (cx - 30, cy + 58), (cx + 6, cy + 84)]
    d.line(crack, fill=SCARLET, width=5)
    d.line([(cx + 40, cy - 78), (cx + 66, cy - 44), (cx + 48, cy - 12)],
           fill=SCARLET, width=4)
    # ribbon across the middle
    ry0, ry1 = cy - 22, cy + 22
    d.rectangle([x0 + 6, ry0, x1 - 6, ry1], fill=SCARLET)
    d.polygon([(x0 + 6, ry0), (x0 - 8, (ry0 + ry1) // 2), (x0 + 6, ry1)],
              fill=(140, 28, 22))
    d.polygon([(x1 - 6, ry0), (x1 + 8, (ry0 + ry1) // 2), (x1 - 6, ry1)],
              fill=(140, 28, 22))
    ribbon = load_font(SANS_BOLD, 26)
    label = "NO DEAL"
    d.text((cx - d.textlength(label, font=ribbon) / 2, cy - 17), label,
           font=ribbon, fill=(255, 255, 255))
    d.text((x0 + 12, y1 - 16), "ANTALYA, TURKEY",
           font=load_font(SANS_BOLD, 10), fill=MUTE)


def sinking_ship(d, x0, y0, x1, y1):
    """A warship listing and sinking at dusk, drone overhead."""
    d.rectangle([x0, y0, x1, y1], outline=PALE, width=1)
    sky_h = (y1 - y0) * 2 // 3
    d.rectangle([x0, y0, x1, y0 + sky_h], fill=(214, 196, 160))
    d.ellipse([x1 - 44, y0 + 8, x1 - 16, y0 + 36], fill=(238, 220, 180))
    # sea
    d.rectangle([x0, y0 + sky_h, x1, y1], fill=OCEAN)
    for wx in range(x0 + 10, x1 - 20, 46):
        d.arc([wx, y0 + sky_h + 8, wx + 34, y0 + sky_h + 22], 0, 180,
              fill=(150, 190, 220), width=2)
    # listing hull, bow up, stern down
    hull = [(x0 + 34, y0 + sky_h - 6), (x0 + 150, y0 + sky_h - 22),
            (x0 + 196, y0 + sky_h - 8), (x0 + 180, y0 + sky_h + 16),
            (x0 + 60, y0 + sky_h + 26)]
    d.polygon(hull, fill=(52, 52, 52))
    d.line([(x0 + 34, y0 + sky_h - 6), (x0 + 196, y0 + sky_h - 8)],
           fill=SCARLET, width=3)
    d.rectangle([x0 + 96, y0 + sky_h - 44, x0 + 116, y0 + sky_h - 20],
                fill=(70, 70, 70))
    # smoke puffs from the stern
    for (sx, sy, sr) in [(x0 + 52, y0 + sky_h - 52, 12),
                         (x0 + 40, y0 + sky_h - 70, 9),
                         (x0 + 62, y0 + sky_h - 72, 8)]:
        d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(150, 148, 140))
    d.text((x0 + 10, y0 + 8), "BENGHAZI, LIBYA",
           font=load_font(SANS_BOLD, 10), fill=INK)
    # drone: small dark quad with rotor arcs
    dx, dy = x1 - 78, y0 + 16
    d.ellipse([dx - 5, dy - 3, dx + 5, dy + 3], fill=INK)
    d.line([(dx - 16, dy - 6), (dx + 16, dy - 6)], fill=INK, width=2)
    d.line([(dx - 16, dy + 6), (dx + 16, dy + 6)], fill=INK, width=2)


def green_climb(d, x0, y0, x1, y1):
    """Rising green bars and a steep arrow: Nvidia surges."""
    d.rectangle([x0, y0, x1, y1], outline=PALE, width=1)
    base = y1 - 20
    top = y0 + 12
    heights = [0.22, 0.34, 0.30, 0.52, 0.66, 0.88]
    bw = 30
    for i, frac in enumerate(heights):
        bx = x0 + 20 + i * 56
        d.rectangle([bx, base - frac * (base - top), bx + bw, base],
                    fill=LEAF if i >= 3 else (150, 150, 150))
    d.line([(x0 + 14, base), (x1 - 10, base)], fill=INK, width=2)
    d.line([(x0 + 26, base - 14), (x1 - 34, y0 + 16)], fill=LEAF, width=4)
    d.polygon([(x1 - 34, y0 + 16), (x1 - 56, y0 + 16), (x1 - 38, y0 + 34)],
              fill=LEAF)
    d.text((x0 + 12, y1 - 15), "NVDA +31%  ·  NASDAQ +6.5%",
           font=load_font(SANS_BOLD, 11), fill=LEAF)


def mercury_disc(d, cx, cy, r):
    """Mercury: a cratered orange disc with an orbit ring."""
    d.ellipse([cx - r - 14, cy - r - 6, cx + r + 14, cy + r + 6],
              outline=PALE, width=2)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(196, 120, 52))
    for (ox, oy, orad) in [(-10, -8, 6), (8, 4, 8), (-2, 12, 5), (12, -12, 4)]:
        d.ellipse([cx + ox - orad, cy + oy - orad, cx + ox + orad,
                   cy + oy + orad], fill=(158, 92, 38))
    d.ellipse([cx + r - 2, cy - r - 2, cx + r + 8, cy - r + 8],
              fill=(220, 235, 245))
    d.rectangle([cx + r - 6, cy - r + 2, cx + r + 12, cy - r + 6],
                fill=(70, 90, 130))


def compose():
    img = Image.new("RGB", (CANVAS_W, CANVAS_H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 36
    right_edge = CANVAS_W - mx

    # ---------- masthead: 14..138 ----------
    masthead = load_font(SERIF_BOLD, 78)
    title = "THE WORLD"
    tw = d.textlength(title, font=masthead)
    d.text(((CANVAS_W - tw) / 2, 14), title, font=masthead, fill=INK)
    hline(d, mx, 110, right_edge, 3)
    meta = load_font(SANS_BOLD, 15)
    d.text((mx, 120), "MONDAY, 23 NOVEMBER 2026", font=meta, fill=INK)
    right_note = "SIX STORIES  ·  ONE PAGE"
    d.text((right_edge - d.textlength(right_note, font=meta), 120),
           right_note, font=meta, fill=MUTE)
    hline(d, mx, 138, right_edge, 1)

    # ---------- lead: COP31, 152..412 ----------
    y = tag(d, mx, 152, "CLIMATE  —  ANTALYA, TURKEY")
    y = head_text(d, mx, y, "COP31 ENDS WITH NO DEAL", 48, 560)
    block(d, mx, y + 6,
          "The UN climate summit in Turkey ends after record-long talks "
          "with no agreement, as countries split over phasing out "
          "fossil fuels and paying for adaptation. The EU rejects a "
          "final text silent on fossil fuels, and the longest climate "
          "conference on record closes in failure.",
          load_font(SERIF, 16), 548, 23)
    globe_no_deal(d, 610, 152, right_edge, 412)
    hline(d, mx, 424, right_edge, 1)

    # ---------- row two: Libya + Nvidia, 438..705 ----------
    col_w = 452
    x2 = right_edge - col_w
    y = tag(d, mx, 438, "WAR IN UKRAINE  —  MEDITERRANEAN")
    y = head_text(d, mx, y, "UKRAINE SINKS RUSSIAN SHIP OFF LIBYA", 30, col_w)
    block(d, mx, y + 4,
          "Kyiv says its naval drones sank the Russian corvette "
          "Merkury at Benghazi, Libya — the war's reach stretches "
          "into the Mediterranean. Zelensky confirms the strike.",
          load_font(SERIF, 15), col_w, 21)
    sinking_ship(d, mx, 615, mx + col_w, 705)

    y2 = tag(d, x2, 438, "MARKETS")
    y2 = head_text(d, x2, y2, "HUANG BACK AT NVIDIA — SHARES +31%", 30, col_w)
    block(d, x2, y2 + 4,
          "Jensen Huang returns as Nvidia chief executive just 11 "
          "days after resigning, after direct intervention from "
          "President Trump. Shares surge 31%, lifting the Nasdaq "
          "6.5% and the S&P 500 4.7%.",
          load_font(SERIF, 15), col_w, 21)
    green_climb(d, x2, 615, x2 + col_w, 705)
    hline(d, mx, 715, right_edge, 1)

    # ---------- row three: Kyiv + Mercury, 729..869 ----------
    y = tag(d, mx, 729, "WAR IN UKRAINE  —  KYIV REGION")
    y = head_text(d, mx, y, "15 KILLED IN STRIKES ON KYIV", 24, col_w)
    block(d, mx, y + 4,
          "Russian bombardment of the Kyiv region kills at least 15 "
          "people. Rescuers dig through the rubble of a collapsed "
          "apartment block in Dymer, 45 km north of the capital, "
          "pulling a boy alive from the wreckage.",
          load_font(SERIF, 15), col_w, 21)

    y2 = tag(d, x2, 729, "SPACE")
    y2 = head_text(d, x2, y2, "BEPICOLOMBO REACHES MERCURY", 24, col_w)
    block(d, x2, y2 + 4,
          "A pair of spacecraft enter orbit around Mercury after an "
          "eight-year journey, beginning a mission to map the "
          "smallest planet and probe its magnetic field.",
          load_font(SERIF, 15), col_w, 21)
    mercury_disc(d, x2 + col_w - 28, 752, 22)
    hline(d, mx, 879, right_edge, 1)

    # ---------- bottom strip: Democrats + ticker, 889..991 ----------
    y = tag(d, mx, 889, "UNITED STATES")
    y = head_text(d, mx, y, "DEMOCRATS WIN 258 SEATS", 28, 560)
    block(d, mx, y + 2,
          "Democrats secure their largest House majority since 1992 "
          "after Chuck Hubbard wins a recount in North Carolina, "
          "as Foxx concedes.",
          load_font(SERIF, 15), 548, 21)
    bx0, by0, bx1, by1 = 610, 889, right_edge, 991
    d.rectangle([bx0, by0, bx1, by1], outline=INK, width=2)
    d.text((bx0 + 12, by0 + 8), "ALSO TODAY",
           font=load_font(SANS_BOLD, 14), fill=SCARLET)
    block(d, bx0 + 12, by0 + 30,
          "Indonesia factory fire kills at least 24  ·  Anthropic "
          "says AI helped prove the Riemann hypothesis  ·  Bitcoin "
          "falls to about $55,100  ·  Alcaraz wins first ATP Finals "
          "title  ·  Verstappen wins Las Vegas GP",
          load_font(SERIF, 12), bx1 - bx0 - 24, 17)

    hline(d, mx, 999, right_edge, 2)
    foot = load_font(SANS, 12)
    d.text((mx, 1005),
           "Drawn in code  ·  every picture on this page is original vector art",
           font=foot, fill=MUTE)
    d.text((right_edge - d.textlength("THE WORLD  ·  23 NOVEMBER 2026",
                                      font=foot), 1005),
           "THE WORLD  ·  23 NOVEMBER 2026", font=foot, fill=MUTE)

    img.save(OUT_PATH, format="PNG")
    print("wrote", OUT_PATH, img.size)


if __name__ == "__main__":
    compose()
