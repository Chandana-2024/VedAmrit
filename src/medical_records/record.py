from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class MedicalRecord:
    patient_id: str
    document_name: str
    document_type: str
    original_file_path: str
    uploaded_at: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )
    ocr_text: str = ""
    structured_data: dict[str, Any] = field(default_factory=dict)