import os
import shutil
from PIL import Image
import pytesseract


def configure_tesseract(custom_path=None):
    """
    Configure Tesseract OCR executable.
    Compatible with local systems and Docker containers.
    """

    # User-provided custom path
    if custom_path:
        if os.path.exists(custom_path):
            pytesseract.pytesseract.tesseract_cmd = custom_path
            return
        else:
            raise FileNotFoundError(
                f"Tesseract not found at: {custom_path}"
            )

    # Auto-detect from PATH
    tesseract_path = shutil.which("tesseract")

    if tesseract_path:
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
        return

    raise EnvironmentError(
        "Tesseract OCR not found. Install it or add it to PATH."
    )


def extract_text(image_path, lang="eng"):

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    try:
        image = Image.open(image_path)

        raw_text = pytesseract.image_to_string(
            image,
            lang=lang
        )

        cleaned_text = " ".join(raw_text.split())

        return cleaned_text if cleaned_text else "[No readable text found]"

    except Exception as e:
        raise RuntimeError(
            f"OCR processing failed: {str(e)}"
        )