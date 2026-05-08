import argparse
from PIL import Image
from PIL.ExifTags import TAGS
import os
import sys
from utils import Style

# ---------- Metadata Extraction ----------
def extract_metadata(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()

        if not exif_data:
            return {}

        metadata = {}
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            metadata[tag] = value

        return metadata

    except Exception as e:
        print(f"{Style.RED}[ERROR]{Style.END} Failed to process image: {e}")
        sys.exit(1)


# ---------- GPS Extraction ----------
def get_gps_info(exif_data):
    if "GPSInfo" not in exif_data:
        return None

    gps_info = exif_data["GPSInfo"]

    def convert_to_degrees(value):
        d, m, s = value
        return float(d) + float(m)/60 + float(s)/3600

    try:
        lat = convert_to_degrees(gps_info[2])
        if gps_info[1] != 'N':
            lat = -lat

        lon = convert_to_degrees(gps_info[4])
        if gps_info[3] != 'E':
            lon = -lon

        return lat, lon
    except Exception:
        return None
