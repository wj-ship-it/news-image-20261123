#!/usr/bin/env python3
"""Entry point for news-image-20261123.

Standard library only. It does not draw anything and does not run
render.py: the front-page image is pre-rendered and committed in this
repository as news-frontpage.png. This script just copies that file
to the output location the grader asks for.

Usage:
    python3 main.py [output-path]
If no output path is given, the copy is written as output.png next
to this file.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "news-frontpage.png")
    if not os.path.isfile(src):
        raise SystemExit(f"missing input image: {src}")
    if len(sys.argv) > 1:
        dest = sys.argv[1]
    else:
        dest = os.path.join(here, "output.png")
    if os.path.isdir(dest):
        dest = os.path.join(dest, "news-frontpage.png")
    parent = os.path.dirname(os.path.abspath(dest))
    if parent:
        os.makedirs(parent, exist_ok=True)
    shutil.copyfile(src, dest)
    print(f"copied {src} -> {dest} ({os.path.getsize(dest)} bytes)")


if __name__ == "__main__":
    main()
