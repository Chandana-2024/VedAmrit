import json
from pathlib import Path

from src.medical_records.record import MedicalRecord


STORAGE_FILE = Path("data") / "medical_records.json"


def save_record(record: MedicalRecord):
    STORAGE_FILE.parent.mkdir(parents=True, exist_ok=True)

    records = []

    if STORAGE_FILE.exists():
        with open(STORAGE_FILE, "r", encoding="utf-8") as file:
            records = json.load(file)

    records.append({
        "patient_id": record.patient_id,
        "document_name": record.document_name,
        "document_type": record.document_type,
        "original_file_path": record.original_file_path,
        "uploaded_at": record.uploaded_at,
        "ocr_text": record.ocr_text,
        "structured_data": record.structured_data,
    })

    with open(STORAGE_FILE, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)


def get_patient_records(patient_id: str):
    if not STORAGE_FILE.exists():
        return []

    with open(STORAGE_FILE, "r", encoding="utf-8") as file:
        records = json.load(file)

    return [
        record
        for record in records
        if record["patient_id"] == patient_id
    ]