from exif import get_gps_info, extract_metadata
from ocr import extract_text, configure_tesseract
from utils import Style, banner, print_key_value, print_section
from rsearch import reverse_search
import argparse
from pathlib import Path
import sys


# =========================
# Utility Printing Functions
# =========================

def print_metadata(metadata: dict) -> None:
    """
    Print EXIF metadata in formatted style.
    """

    if not metadata:
        print(f"{Style.RED}[!] No metadata found.{Style.END}")
        return

    for key, value in metadata.items():
        if key != "GPSInfo":
            print_key_value(key, value)

    gps = get_gps_info(metadata)

    if gps:
        print_section("GPS LOCATION")

        latitude, longitude = gps

        print_key_value("Latitude", latitude)
        print_key_value("Longitude", longitude)

        maps_url = (
            f"https://www.google.com/maps?q={latitude},{longitude}"
        )

        print_key_value("Google Maps", maps_url)


def handle_ocr(image_path: str) -> None:
    """
    Extract and display OCR text.
    """

    print_section("OCR")

    try:
        text = extract_text(image_path).strip()

        if text:
            print(text)
        else:
            print(f"{Style.RED}No text found.{Style.END}")

    except Exception as e:
        print(f"{Style.RED}[OCR ERROR]{Style.END} {e}")


def handle_metadata(image_path: str) -> None:
    """
    Extract and display image metadata.
    """

    print_section("GENERAL METADATA")

    try:
        metadata = extract_metadata(image_path)
        print_metadata(metadata)

    except Exception as e:
        print(f"{Style.RED}[METADATA ERROR]{Style.END} {e}")


def handle_reverse_search(image_path: str) -> None:
    """
    Generate reverse image search links.
    """

    print_section("REVERSE IMAGE SEARCH")

    try:
        links = reverse_search(image_path)

        for engine, url in links.items():
            print_key_value(engine.capitalize(), url)

    except Exception as e:
        print(f"{Style.RED}[REVERSE SEARCH ERROR]{Style.END} {e}")


# =========================
# Main Function
# =========================

def main() -> None:

    parser = argparse.ArgumentParser(
        prog="visionint",
        description="OSINT Image Investigation Tool"
    )

    parser.add_argument(
        "image",
        help="Path to image file"
    )

    parser.add_argument(
        "--exif",
        action="store_true",
        help="Extract EXIF metadata"
    )

    parser.add_argument(
        "--ocr",
        action="store_true",
        help="Extract text using OCR"
    )

    parser.add_argument(
        "--rsearch",
        action="store_true",
        help="Perform reverse image search"
    )

    args = parser.parse_args()

    image_path = Path(args.image)

    # Banner
    banner()

    # Validate file
    if not image_path.exists():
        print(
            f"{Style.RED}[ERROR]{Style.END} "
            f"File not found: {image_path}"
        )
        sys.exit(1)

    if not image_path.is_file():
        print(
            f"{Style.RED}[ERROR]{Style.END} "
            f"Invalid image file."
        )
        sys.exit(1)

    print(
        f"{Style.BLUE}[INFO]{Style.END} "
        f"Processing: {image_path}"
    )

    # Configure OCR only if needed
    if args.ocr:
        configure_tesseract()

    # If no flags are provided → run all
    no_flags = not any([
        args.exif,
        args.ocr,
        args.rsearch
    ])

    if args.exif or no_flags:
        handle_metadata(str(image_path))

    if args.ocr or no_flags:
        handle_ocr(str(image_path))

    if args.rsearch or no_flags:
        handle_reverse_search(str(image_path))


if __name__ == "__main__":
    main()