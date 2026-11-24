#!/usr/bin/env python3
"""Draw the front page for Monday 23 November 2026.

Six world-news stories from 23 November, drawn with PIL only. Text is in
English and every figure comes from the verified brief. The output image is
1024 x 1024 RGB and is saved as news-frontpage.png next to this script (or
under $MAKEFUN_OUTPUT_DIR when that variable is set).
"""

import os

from PIL import Image, ImageDraw, ImageFont

PAGE_W, PAGE_H = 1024, 1024
BG = (251, 247, 238)
INK = (20, 20, 20)
MUTED = (96, 91, 82)
LINE = (45, 45, 45)
RED = (148, 26, 26)

FONTS = "/usr/share/fonts/truetype"
SERIF = FONTS + "/liberation/LiberationSerif-Regular.ttf"
SERIF_B = FONTS + "/liberation/LiberationSerif-Bold.ttf"
SANS = FONTS + "/liberation/LiberationSans-Regular.ttf"
SANS_B = FONTS + "/liberation/LiberationSans-Bold.ttf"


def load(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def wrap_text(draw, text, fnt, width):
    """Split text into lines that fit inside width pixels."""
    out, current = [], ""
    for word in text.split():
        candidate = (current + " " + word).strip()
        if draw.textlength(candidate, font=fnt) <= width:
            current = candidate
        else:
            if current:
                out.append(current)
            current = word
    if current:
        out.append(current)
    return out


def draw_para(draw, x, y, text, fnt, width, step, color=INK):
    for line in wrap_text(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=color)
        y += step
    return y


def draw_headline(draw, x, y, text, size, width):
    fnt = load(SERIF_B, size)
    step = int(size * 1.07)
    for line in wrap_text(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=INK)
        y += step
    return y


def draw_tag(draw, x, y, text):
    fnt = load(SANS_B, 16)
    draw.text((x, y), text.upper(), font=fnt, fill=RED)
    return y + 23


def hline(draw, x0, y, x1, weight=2):
    draw.line([(x0, y), (x1, y)], fill=LINE, width=weight)


def news_block(draw, x, y, w, tag, title, body, source, size=26):
    """One story: red tag, headline, body, source credit. Returns next y."""
    y = draw_tag(draw, x, y, tag)
    y = draw_headline(draw, x, y, title, size, w) + 4
    y = draw_para(draw, x, y, body, load(SERIF, 19), w, 25)
    y += 3
    draw.text((x, y), "Source: " + source,
              font=load(SANS, 14), fill=MUTED)
    return y + 26


def main():
    page = Image.new("RGB", (PAGE_W, PAGE_H), BG)
    d = ImageDraw.Draw(page)
    m = 44
    right = PAGE_W - m

    # Masthead
    d.text((m, 20), "THE WORLD DISPATCH",
           font=load(SERIF_B, 54), fill=INK)
    d.text((m, 82), "MONDAY 23 NOVEMBER 2026  ·  SIX STORIES, ONE PAGE",
           font=load(SANS_B, 18), fill=MUTED)
    d.text((right - 246, 86), "WORLD NEWS IN BRIEF",
           font=load(SANS_B, 18), fill=RED)
    hline(d, m, 114, right, 4)
    hline(d, m, 120, right, 1)

    # Lead: Huang reinstated
    y = 132
    y = draw_tag(d, m, y, "Business · Santa Clara")
    y = draw_headline(d, m, y,
                      "HUANG IS BACK: NVIDIA BOARD VOTES HIM IN AFTER 11 DAYS",
                      44, right - m) + 5
    y = draw_para(d, m, y,
                  "Nvidia's board unanimously restored Jensen Huang as "
                  "president, chief executive and director, eleven days "
                  "after he resigned. Shares closed at $165.05, up 31.48% "
                  "on the day, after falling 14% the previous Friday. Huang "
                  "returned to headquarters to applause and thanked staff "
                  "for a second chance.",
                  load(SERIF, 21), right - m, 28)
    y += 3
    d.text((m, y), "Source: Nvidia announcement / market data, 23 Nov 2026",
           font=load(SANS, 15), fill=MUTED)
    y += 28
    hline(d, m, y, right, 3)
    y += 12

    # Two-column rows
    col = (right - m - 28) // 2
    x2 = m + col + 28

    top = y
    left = news_block(d, m, top, col,
                      "Climate · Antalya",
                      "COP31 ends with no deal",
                      "United Nations climate talks in Antalya closed "
                      "without an agreement after running two days past "
                      "schedule. The European Union led a walkout over a "
                      "draft text that made no mention of fossil fuels.",
                      "UN summit reports")
    right_y = news_block(d, x2, top, col,
                         "Middle East",
                         "Iran strikes Bahrain as US-Iran standoff grows",
                         "Iranian missiles and drones struck targets in "
                         "Bahrain. Bahrain said a civilian industrial site "
                         "was hit and two people were hurt. Iran said it "
                         "destroyed two US Patriot radar units.",
                         "Bahrain / Iran statements")
    y = max(left, right_y)
    d.line([(x2 - 14, top + 4), (x2 - 14, y - 8)], fill=LINE, width=1)
    hline(d, m, y, right, 1)
    y += 12

    top = y
    left = news_block(d, m, top, col,
                      "Black Sea · Off Libya",
                      "Ukraine says it sank a Russian warship",
                      "Ukraine said its forces sank a Russian warship in "
                      "the Mediterranean off the coast of Libya, in the "
                      "latest long-range strike of the war at sea.",
                      "Ukrainian military reports")
    right_y = news_block(d, x2, top, col,
                         "Mexico · Sinaloa",
                         "'El Chapo Isidro' captured; 11 killed",
                         "Special forces captured cartel boss Fausto Isidro "
                         "Meza Flores in Sinaloa. Eleven people were killed "
                         "in the fighting, including four soldiers.",
                         "Mexican authorities")
    y = max(left, right_y)
    d.line([(x2 - 14, top + 4), (x2 - 14, y - 8)], fill=LINE, width=1)
    hline(d, m, y, right, 1)
    y += 12

    # Bottom band: BepiColombo
    y = draw_tag(d, m, y, "Space · Mercury")
    y = draw_headline(d, m, y,
                      "BepiColombo slips into orbit around Mercury",
                      27, right - m) + 3
    y = draw_para(d, m, y,
                  "The European-Japanese BepiColombo probe entered orbit "
                  "around Mercury, beginning its science mission after a "
                  "long cruise to the solar system's innermost planet.",
                  load(SERIF, 19), right - m, 25)
    y += 3
    d.text((m, y), "Source: ESA / JAXA mission updates",
           font=load(SANS, 14), fill=MUTED)
    y += 22

    # Footer
    hline(d, m, y, right, 3)
    d.text((m, y + 10),
           "THE WORLD DISPATCH — Monday 23 November 2026 · All six stories "
           "verified from source reports.",
           font=load(SANS, 15), fill=MUTED)
    d.text((right - 150, y + 10), "PAGE 1",
           font=load(SANS_B, 15), fill=INK)

    dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    dest = (os.path.join(dest_dir, "news-frontpage.png")
            if dest_dir else "news-frontpage.png")
    page.save(dest)
    print("saved news-frontpage.png", page.size)


if __name__ == "__main__":
    main()
