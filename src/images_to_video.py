#!/usr/bin/env python3
"""Convert an image sequence into an MP4 video with user-defined duration.

Usage (Linux/Mac):
    python src/images_to_video.py \
        --input-dir path/to/images \
        --output path/to/video.mp4 \
        --duration 12

Usage (Windows):
    python src\\images_to_video.py --input-dir img\\map_data\\images --output video\\panorama_of_hall.mp4 --duration 12
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


SUPPORTED_EXTS = {".png", ".jpg", ".jpeg", ".bmp", ".webp"}


def natural_key(path: Path) -> list[object]:
    parts = re.split(r"(\d+)", path.name)
    key: list[object] = []
    for part in parts:
        if part.isdigit():
            key.append(int(part))
        else:
            key.append(part.lower())
    return key


def resolve_input_dir(raw_dir: str) -> Path:
    candidate = Path(raw_dir)
    if candidate.exists():
        return candidate

    # Helpful fallback for this workspace layout.
    fallback = Path("img") / raw_dir
    if fallback.exists():
        return fallback

    return candidate


def collect_images(input_dir: Path) -> list[Path]:
    files = [p for p in input_dir.iterdir() if p.is_file() and p.suffix.lower() in SUPPORTED_EXTS]
    return sorted(files, key=natural_key)


def build_video(images: list[Path], output_path: Path, duration: float) -> None:
    if duration <= 0:
        raise ValueError("duration must be > 0")

    if shutil.which("ffmpeg") is None:
        raise RuntimeError("ffmpeg was not found in PATH. Please install ffmpeg first.")

    fps = len(images) / duration

    output_path.parent.mkdir(parents=True, exist_ok=True)

    per_frame = duration / len(images)
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as fp:
        list_path = Path(fp.name)
        for image_path in images:
            quoted = image_path.resolve().as_posix().replace("'", "'\\''")
            fp.write(f"file '{quoted}'\n")
            fp.write(f"duration {per_frame:.10f}\n")
        quoted_last = images[-1].resolve().as_posix().replace("'", "'\\''")
        fp.write(f"file '{quoted_last}'\n")

    cmd = [
        "ffmpeg",
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(list_path),
        "-vf",
        "format=yuv420p",
        "-movflags",
        "+faststart",
        "-r",
        f"{fps:.8f}",
        str(output_path),
    ]

    try:
        subprocess.run(cmd, check=True)
    finally:
        if list_path.exists():
            list_path.unlink()

    print(f"Done: {len(images)} frames -> {output_path}")
    print(f"Duration: {duration:.2f}s, FPS: {fps:.3f}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Merge images into MP4 and control final duration from command line."
    )
    parser.add_argument(
        "--input-dir",
        default="map_data/images",
        help="Image folder. Default: map_data/images (also tries img/map_data/images)",
    )
    parser.add_argument(
        "--output",
        default="video/map_data.mp4",
        help="Output MP4 path. Default: video/map_data.mp4",
    )
    parser.add_argument(
        "--duration",
        type=float,
        required=True,
        help="Target video duration in seconds, e.g. --duration 8",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    input_dir = resolve_input_dir(args.input_dir)
    if not input_dir.exists() or not input_dir.is_dir():
        raise FileNotFoundError(f"Input directory not found: {input_dir}")

    images = collect_images(input_dir)
    if not images:
        raise FileNotFoundError(f"No images found in: {input_dir}")

    build_video(images=images, output_path=Path(args.output), duration=args.duration)


if __name__ == "__main__":
    main()
