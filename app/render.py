"""FFmpeg-backed vertical clip rendering with optional user-provided SRT."""
from pathlib import Path
import shutil
import subprocess
from .ingest import require_local_video


def render_vertical_clip(source: Path, start: float, end: float, output: Path, srt: Path | None = None) -> Path:
    source = require_local_video(source)
    if not 0 <= start < end:
        raise ValueError("Times must satisfy 0 <= start < end")
    if shutil.which("ffmpeg") is None:
        raise RuntimeError("FFmpeg is required and must be on PATH")
    output = Path(output).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    # Scale to fill, then center-crop. Explicit subtitle paths require FFmpeg filter escaping.
    vf = "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1"
    if srt is not None:
        subtitle = Path(srt).expanduser().resolve()
        if not subtitle.is_file():
            raise FileNotFoundError(f"Subtitle file not found: {subtitle}")
        escaped = subtitle.as_posix().replace(":", r"\:").replace("[", r"\[").replace("]", r"\]")
        vf += f",subtitles=filename='{escaped}'"
    command = ["ffmpeg", "-hide_banner", "-y", "-ss", str(start), "-i", str(source),
               "-t", str(end - start), "-vf", vf, "-c:v", "libx264", "-preset", "fast",
               "-crf", "23", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", str(output)]
    subprocess.run(command, check=True)
    return output
