from pathlib import Path

from src.medical_ocr.ocr_engine import extract_text
from src.medical_ocr.text_cleaner import clean_text
from src.medical_ocr.medical_parser import parse_medical_report


def process_medical_document(file_path):
    """
    Process one medical document and return structured medical history.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Medical document not found: {file_path}"
        )

    raw_text = extract_text(str(path))

    if not raw_text.strip():
        raise ValueError(
            "OCR did not extract any text from the medical document."
        )

    cleaned_text = clean_text(raw_text)

    structured_data = parse_medical_report(cleaned_text)

    return {
        "document_name": path.name,
        "raw_ocr_text": raw_text,
        "cleaned_text": cleaned_text,
        "structured_data": structured_data,
    }