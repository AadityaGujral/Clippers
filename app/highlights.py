"""A simple deterministic selector for testing; NOT AI highlights."""


def fixed_segments(duration: float, clip_length: float = 30.0, maximum: int = 4):
    if duration <= 0 or clip_length <= 0 or maximum <= 0:
        raise ValueError("duration, clip_length and maximum must be positive")
    return [(start, min(start + clip_length, duration)) for start in
            (i * clip_length for i in range(maximum)) if start < duration]
