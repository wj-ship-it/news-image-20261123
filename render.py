#!/usr/bin/env python3
"""Render a one-page newspaper front page (1024x1024 PNG).

Written from scratch for news-image-20261123: six stories from
23 November 2026, black-and-white newspaper style. Only PIL is used.
Run:  python3 render.py   (writes news-frontpage.png next to this file)
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 42
TEXT_W = W - 2 * MARGIN

FONT_DIRS = [
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts/truetype/liberation",
]


def find_font(names):
    for d in FONT_DIRS:
        for name in names:
            p = os.path.join(d, name)
            if os.path.isfile(p):
                return p
    return None


def load(size, bold=False, italic=False):
    if italic:
        names = ["DejaVuSans-Oblique.ttf", "LiberationSans-Italic.ttf",
                 "DejaVuSans.ttf", "LiberationSans-Regular.ttf"]
    elif bold:
        names = ["DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf",
                 "DejaVuSans.ttf", "LiberationSans-Regular.ttf"]
    else:
        names = ["DejaVuSans.ttf", "LiberationSans-Regular.ttf"]
    path = find_font(names)
    if path:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            pass
    return ImageFont.load_default(size=size if hasattr(ImageFont, "load_default") else None) \
        if False else ImageFont.load_default()


def wrap(draw, text, font, max_width):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


STORIES = [
    ("Huang Returns: Nvidia Board Votes Him Back",
     "Eleven days after resigning, Jensen Huang was unanimously "
     "reinstated as president, CEO and director. Nvidia shares "
     "closed at $165.05, up 31.48%.",
     "Source: Nvidia investor announcement"),
    ("COP31 Ends Without a Deal",
     "The COP31 climate summit closed without an agreement, after "
     "negotiators failed to bridge their differences in the final "
     "round of talks.",
     "Source: COP31 closing reports"),
    ("Iran Strikes Bahrain as US-Iran Standoff Escalates",
     "Iran attacked Bahrain, sharply escalating the standoff with "
     "the United States and raising fears of a wider regional conflict.",
     "Source: Wire reports"),
    ("Ukraine Says It Sank a Russian Warship off Libya",
     "Ukraine said its forces sank a Russian warship in the "
     "Mediterranean off Libya, in a strike far from the Black Sea "
     "front line.",
     "Source: Ukrainian officials"),
    ("'El Chapo Isidro' Captured; 11 Killed",
     "Mexican forces captured the drug lord known as 'El Chapo "
     "Isidro' in an operation that left 11 people dead, officials said.",
     "Source: Mexican authorities"),
    ("BepiColombo Enters Orbit Around Mercury",
     "The European-Japanese BepiColombo probe entered orbit around "
     "Mercury, beginning its long-planned study of the solar "
     "system's smallest planet.",
     "Source: ESA / JAXA"),
]


def main():
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    black = (0, 0, 0)
    grey = (90, 90, 90)

    # Outer frame.
    draw.rectangle([14, 14, W - 15, H - 15], outline=black, width=3)
    draw.rectangle([22, 22, W - 23, H - 23], outline=black, width=1)

    title_font = load(56, bold=True)
    sub_font = load(21)
    num_font = load(26, bold=True)
    head_font = load(25, bold=True)
    body_font = load(19)
    src_font = load(15, italic=True)
    foot_font = load(14, italic=True)

    # Masthead.
    title = "THE WORLD IN ONE PAGE"
    tw = draw.textlength(title, font=title_font)
    draw.text(((W - tw) / 2, 44), title, font=title_font, fill=black)
    sub = "23 November 2026 — Six stories that moved the world"
    sw = draw.textlength(sub, font=sub_font)
    draw.text(((W - sw) / 2, 122), sub, font=sub_font, fill=black)
    draw.line([(MARGIN, 164), (W - MARGIN, 164)], fill=black, width=3)
    draw.line([(MARGIN, 171), (W - MARGIN, 171)], fill=black, width=1)

    # Six stories, one column.
    y = 192
    for i, (head, body, src) in enumerate(STORIES, start=1):
        num = f"{i}."
        nw = draw.textlength(num, font=num_font)
        draw.text((MARGIN, y), num, font=num_font, fill=black)
        draw.text((MARGIN + nw + 10, y + 1), head, font=head_font, fill=black)
        y += 36
        for line in wrap(draw, body, body_font, TEXT_W):
            draw.text((MARGIN, y), line, font=body_font, fill=black)
            y += 27
        draw.text((MARGIN, y + 2), src, font=src_font, fill=grey)
        y += 26
        if i < len(STORIES):
            draw.line([(MARGIN, y + 4), (W - MARGIN, y + 4)],
                      fill=(180, 180, 180), width=1)
            y += 16

    # Footer.
    foot = ("Sources: Nvidia, COP31, wire reports, Ukrainian officials, "
            "Mexican authorities, ESA/JAXA.")
    fw = draw.textlength(foot, font=foot_font)
    draw.text(((W - fw) / 2, H - 50), foot, font=foot_font, fill=grey)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "news-frontpage.png")
    img.save(out, "PNG")
    print(f"wrote {out} {os.path.getsize(out)} bytes")


if __name__ == "__main__":
    main()
