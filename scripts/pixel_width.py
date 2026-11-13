#!/usr/bin/env python3
"""pixel_width.py — measure title and meta description values in pixels.

Part of the title-meta-gap-fill skill (Eoghan Henn and contributors,
CC BY 4.0). A character count is not a width: an "i" and a "W" count the
same and render three times apart, so a limit expressed in characters
passes values the result page truncates. This script renders each value
with a TrueType font at the size the limit assumes and reports its width
against the limit.

Usage
-----
  python3 pixel_width.py --limit 580 --size 20 [--font FILE] [--column title] FILE.csv
  python3 pixel_width.py --limit 580 --size 20 --text "One value to measure"
  python3 pixel_width.py --selftest

  FILE.csv      a CSV with a header row; the measured column is named
                with --column (default: the first column). Use "-" to read
                values one per line from stdin.
  --limit N     the width limit in pixels — an intake parameter, never a
                default of this script, because it depends on the result
                page, the device and the field.
  --size N      the font size in pixels the limit assumes (the same
                intake parameter; a title limit and a description limit
                usually assume different sizes).
  --font FILE   a TrueType font file. Without it the script looks for
                Arial, then Liberation Sans (metric-compatible with Arial),
                then DejaVu Sans, and names the one it used: widths from
                different fonts are not comparable, so the font is part of
                every report.
  --bold        render bold (some result pages render the title bold).
  --format      table (default) or csv. The csv form echoes the input
                columns and appends width_px, limit_px, over_px and
                verdict, so it can be joined back by the stable key.

Exit status: 0 when every value fits, 1 when any is over the limit,
2 on a usage error or a missing dependency. A value over the limit is a
finding, not a crash, so the report is complete either way.

Requires Pillow (`pip install Pillow`). Without it the script stops with
that message rather than estimating: an estimate presented as a width is
the error this script exists to remove.
"""
import argparse
import csv
import glob
import os
import sys

FONT_CANDIDATES = {
    "regular": [
        "Arial.ttf", "arial.ttf",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ],
    "bold": [
        "Arial Bold.ttf", "arialbd.ttf",
        "/Library/Fonts/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
        "/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ],
}


def load_pillow():
    try:
        from PIL import ImageFont  # noqa: F401
    except ImportError:
        sys.stderr.write("pixel_width.py: Pillow is not installed — "
                         "`pip install Pillow`; no width is estimated without it.\n")
        sys.exit(2)
    from PIL import ImageFont
    return ImageFont


def find_font(explicit, bold):
    if explicit:
        if not os.path.isfile(explicit):
            sys.stderr.write(f"pixel_width.py: font file not found: {explicit}\n")
            sys.exit(2)
        return explicit
    for cand in FONT_CANDIDATES["bold" if bold else "regular"]:
        if os.path.isfile(cand):
            return cand
        for hit in glob.glob(os.path.join("/usr/share/fonts", "**", os.path.basename(cand)),
                             recursive=True):
            return hit
    sys.stderr.write("pixel_width.py: no Arial, Liberation Sans or DejaVu Sans found — "
                     "pass --font FILE.\n")
    sys.exit(2)


def measure(values, font_path, size):
    ImageFont = load_pillow()
    font = ImageFont.truetype(font_path, size)
    out = []
    for v in values:
        v = "" if v is None else str(v)
        if not v:
            out.append(0)
            continue
        # getlength() is the advance width, which is what a result page
        # lays the text out by; a bounding box would drop trailing space
        # and side bearings and under-report.
        out.append(int(round(font.getlength(v))))
    return out


def read_values(path, column):
    if path == "-":
        rows = [{"value": line.rstrip("\n")} for line in sys.stdin]
        return rows, "value"
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        if not reader.fieldnames:
            sys.stderr.write("pixel_width.py: the CSV has no header row.\n")
            sys.exit(2)
        col = column or reader.fieldnames[0]
        if col not in reader.fieldnames:
            sys.stderr.write(f"pixel_width.py: column {col!r} not in {reader.fieldnames}\n")
            sys.exit(2)
        return rows, col


def selftest():
    """Assert the properties a width check must have, against the font found."""
    font_path = find_font(None, False)
    narrow, wide = measure(["iiiiiiiiii", "WWWWWWWWWW"], font_path, 20)
    longer = measure(["Garden hose", "Garden hose reel with wall bracket"], font_path, 20)
    empty = measure([""], font_path, 20)
    sizes = measure(["Garden hose reel with wall bracket"], font_path, 14) + \
        measure(["Garden hose reel with wall bracket"], font_path, 20)
    checks = [
        ("empty value measures 0", empty[0] == 0),
        ("ten W wider than ten i (a width is not a count)", wide > narrow * 2),
        ("a longer string is wider", longer[1] > longer[0]),
        ("the same string is narrower at a smaller size", sizes[0] < sizes[1]),
        ("a plausible band for a 34-character title at 20 px", 250 < sizes[1] < 450),
    ]
    ok = True
    for name, passed in checks:
        print(f"{'ok  ' if passed else 'FAIL'} {name}")
        ok = ok and passed
    print(f"font: {font_path}")
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("file", nargs="?")
    ap.add_argument("--text")
    ap.add_argument("--column")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--size", type=int)
    ap.add_argument("--font")
    ap.add_argument("--bold", action="store_true")
    ap.add_argument("--format", choices=["table", "csv"], default="table")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("-h", "--help", action="store_true")
    args = ap.parse_args(argv)
    if args.help:
        print(__doc__)
        return 0
    if args.selftest:
        return selftest()
    if args.limit is None or args.size is None:
        sys.stderr.write("pixel_width.py: --limit and --size are required (intake "
                         "parameters; this script has no defaults for them).\n")
        return 2
    if not args.text and not args.file:
        sys.stderr.write("pixel_width.py: give a FILE.csv, '-' for stdin, or --text.\n")
        return 2
    font_path = find_font(args.font, args.bold)
    if args.text:
        rows, col = [{"value": args.text}], "value"
    else:
        rows, col = read_values(args.file, args.column)
    widths = measure([r.get(col) for r in rows], font_path, args.size)
    over_any = False
    if args.format == "csv":
        fields = list(rows[0].keys()) if rows else [col]
        w = csv.DictWriter(sys.stdout, fieldnames=fields + ["width_px", "limit_px", "over_px", "verdict"])
        w.writeheader()
    print_rows = []
    for r, width in zip(rows, widths):
        over = max(0, width - args.limit)
        over_any = over_any or over > 0
        verdict = "over" if over else "fits"
        if args.format == "csv":
            r2 = dict(r)
            r2.update(width_px=width, limit_px=args.limit, over_px=over, verdict=verdict)
            w.writerow(r2)
        else:
            print_rows.append((width, over, verdict, r.get(col) or ""))
    if args.format == "table":
        print(f"font {font_path} at {args.size} px, limit {args.limit} px")
        print("width_px over_px verdict value")
        for width, over, verdict, v in print_rows:
            print(f"{width:8d} {over:7d} {verdict:7s} {v}")
        n_over = sum(1 for _, o, _, _ in print_rows if o)
        print(f"{len(print_rows)} values, {n_over} over the limit")
    return 1 if over_any else 0


if __name__ == "__main__":
    sys.exit(main())
