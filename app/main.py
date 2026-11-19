"""Command-line entry point for a manually selected vertical clip."""
import argparse
from pathlib import Path
from .render import render_vertical_clip


def main():
    parser = argparse.ArgumentParser(description="Render a 9:16 vertical MP4 from a local video")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--start", required=True, type=float, help="Start time in seconds")
    parser.add_argument("--end", required=True, type=float, help="End time in seconds")
    parser.add_argument("--output", type=Path, default=Path("output/short.mp4"))
    parser.add_argument("--srt", type=Path, default=None, help="Optional subtitle file")
    args = parser.parse_args()
    render_vertical_clip(args.input, args.start, args.end, args.output, args.srt)
    print(f"Created {args.output}")


if __name__ == "__main__":
    main()
