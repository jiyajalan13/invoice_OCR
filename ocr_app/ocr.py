import os
import pytesseract
from PIL import Image, UnidentifiedImageError


tesseract_path = os.environ.get("TESSERACT_CMD")

if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path


class InvalidImageError(Exception):
    """Raised when the uploaded file isn't a readable image."""
    pass


def extract_text_from_image(image_file):
    try:
        image = Image.open(image_file)
        image.load()
    except (UnidentifiedImageError, OSError):
        raise InvalidImageError("The uploaded file is not a valid image.")

    text = pytesseract.image_to_string(image)
    return text.strip()