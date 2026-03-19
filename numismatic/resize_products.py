#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Resize numismatic product JPG images and export them as WebP."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("V2/assets/images"),
        help="Directory containing numisproduct*.JPG files.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("V2/assets/images/webp"),
        help="Directory for converted WebP files.",
    )
    parser.add_argument(
        "--pattern",
        default="numisproduct*.JPG",
        help="Glob pattern for source images.",
    )
    parser.add_argument(
        "--max-width",
        type=int,
        default=1600,
        help="Maximum output width in pixels.",
    )
    parser.add_argument(
        "--max-height",
        type=int,
        default=1600,
        help="Maximum output height in pixels.",
    )
    parser.add_argument(
        "--quality",
        type=int,
        default=82,
        help="WebP quality from 0 to 100.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing WebP files.",
    )
    return parser.parse_args()


def resize_and_convert(
    source_path: Path,
    output_path: Path,
    max_width: int,
    max_height: int,
    quality: int,
) -> tuple[tuple[int, int], tuple[int, int]]:
    with Image.open(source_path) as image:
        image = ImageOps.exif_transpose(image)
        image = image.convert("RGB")
        original_size = image.size
        image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        resized_size = image.size
        output_path.parent.mkdir(parents=True, exist_ok=True)
        image.save(output_path, "WEBP", quality=quality, method=6)
    return original_size, resized_size


def main() -> int:
    args = parse_args()

    if not args.input_dir.exists():
        raise SystemExit(f"Input directory not found: {args.input_dir}")

    sources = sorted(args.input_dir.glob(args.pattern))
    if not sources:
        raise SystemExit(
            f"No images matched {args.pattern!r} in {args.input_dir}"
        )

    for source_path in sources:
        output_path = args.output_dir / f"{source_path.stem}.webp"
        if output_path.exists() and not args.force:
            print(f"skip {output_path} already exists")
            continue

        original_size, resized_size = resize_and_convert(
            source_path=source_path,
            output_path=output_path,
            max_width=args.max_width,
            max_height=args.max_height,
            quality=args.quality,
        )
        print(
            f"converted {source_path.name} "
            f"{original_size[0]}x{original_size[1]} -> "
            f"{resized_size[0]}x{resized_size[1]} "
            f"as {output_path}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
