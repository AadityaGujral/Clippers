"""Caption helpers: SRT pass-through only in the initial release."""
from pathlib import Path


def validate_srt(path: str | Path) -> Path:
    file = Path(path)
    if file.suffix.lower() != ".srt" or not file.is_file():
        raise ValueError("A readable .srt subtitle file is required")
    return file
