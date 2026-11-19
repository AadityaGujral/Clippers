# Local Shorts Studio

**Status: initial independent scaffold, not yet a NeonClipping fork or an AI auto-clipper.**

A local Python starter for extracting vertical video clips from source recordings. The first milestone uses **your local MP4 files** and chosen start/end times; link ingestion, transcription, AI highlight ranking, karaoke captions and a browser interface are roadmap items, **not working features**.

## Credit and upstream inspiration

Architecture and workflow inspired by **[NeonClipping](https://github.com/iamajmeena/neonclipping)** by **Ajay K Meena** and NeonClipping contributors. Original project is MIT-licensed; the copyright and MIT permission notice supplied in its `LICENSE` file are retained here. This is a fresh scaffold and **does not contain copied NeonClipping implementation files**. If upstream source files are subsequently included, preserve their copyright notices and record their provenance.

## Requirements
- Windows, macOS or Linux; Python 3.10+; FFmpeg on PATH
- Optional future integrations: yt-dlp, faster-whisper, Ollama

## Install and run
```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m app.main --input path/to/video.mp4 --start 10 --end 40 --output output/short.mp4
```

The initial renderer center-crops to 9:16 and encodes an MP4. It does **not** identify facecam automatically, provide clips automatically or add subtitles unless an SRT is explicitly provided with `--srt path/to/captions.srt`.

## Test
```bash
python -m unittest discover -s tests -v
```

## Roadmap
1. yt-dlp URL ingestion with permission checks and clear errors
2. transcript extraction via captions and local Whisper
3. mode-specific highlight scoring (gaming versus narration)
4. subtitle timing and review/editing
5. clip previews and selectable layouts in a local web UI
6. Windows installer and regression suite

## Limitations and rights
- FFmpeg must be installed separately.
- Processing speed depends on computer and source video.
- Use only material you own or are authorized to reuse. Streaming-site technical accessibility is not a content license.
- Never commit personal recordings, downloaded media, API credentials or session cookies.

## License
MIT; see [LICENSE](LICENSE). The retained upstream notice is included for attribution. See the upstream project for its implementation and terms.
