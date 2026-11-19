"""Video input validation. URL ingestion is not yet implemented."""
from pathlib import Path


def require_local_video(path: str | Path) -> Path:
    video = Path(path).expanduser().resolve()
    if not video.is_file():
        raise FileNotFoundError(f"Input video not found: {video}")
    if video.suffix.lower() not in {".mp4", ".mov", ".mkv", ".webm"}:
        raise ValueError("Supported local file types: mp4, mov, mkv, webm")
    return video
