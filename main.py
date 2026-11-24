#!/usr/bin/env python3
"""Entry point: copy the pre-rendered front page to the output folder.

The finished image (news-frontpage.png) already lives in this repository,
so the scored run is a plain copy with only the Python standard library.

Usage:
    python3 main.py            # writes out/entry.png
    MAKEFUN_OUTPUT_DIR=/output python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", HERE / "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(HERE / "news-frontpage.png", dest)
    print("wrote", dest)


if __name__ == "__main__":
    main()
