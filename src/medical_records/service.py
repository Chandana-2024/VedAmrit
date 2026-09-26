from src.medical_ocr.medical_history_service import process_medical_document
from src.medical_records.record import MedicalRecord
from src.medical_records.storage import save_record


def add_medical_document(
    patient_id: str,
    file_path: str,
    document_type: str,
):
    result = process_medical_document(file_path)

    medical_record = MedicalRecord(
        patient_id=patient_id,
        document_name=result["document_name"],
        document_type=document_type,
        original_file_path=file_path,
        ocr_text=result["raw_ocr_text"],
        structured_data=result["structured_data"],
    )

    save_record(medical_record)

    return medical_record