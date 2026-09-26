# VedAmrit 🌿

**VedAmrit** is an AI-powered Ayurvedic wellness platform that combines personalized Ayurvedic assessment, diet planning, lifestyle recommendations, doctor review, and patient medical-document management.

## 🌱 Overview

VedAmrit is designed around two independent modules:

```text
                         VEDAMRIT
                            │
             ┌──────────────┴──────────────┐
             │                             │
      MEDICAL RECORDS                AYURVEDIC CARE
             │                             │
       OCR + Storage                Dosha + Diet
             │                             │
   Patient Medical Documents       Doctor Review
```

### Medical Records

The Medical Records module allows patients to maintain their medical documents in a structured way.

Current workflow:

```text
Medical Document
       ↓
      OCR
       ↓
Text Cleaning
       ↓
Medical Information Extraction
       ↓
Structured Medical Record
       ↓
Local Storage
```

The current OCR pipeline can extract information such as:

* Patient name
* Age / gender
* Patient ID
* Visit type
* Referring doctor
* Laboratory results
* Medical impressions

### Ayurvedic Care

The Ayurvedic module provides an AI-assisted workflow for:

* Prakriti assessment
* Vikriti assessment
* Agni assessment
* Ayurvedic condition analysis
* Personalized diet planning
* Food retrieval and ranking
* Lifestyle recommendations
* Diet validation
* Doctor review
* Personalized wellness reports

The Ayurvedic workflow follows a doctor-in-the-loop approach, where generated recommendations can be reviewed before the final report is produced.

## 🧠 AI Architecture

The project uses modular agents and services for different parts of the Ayurvedic workflow.

Major components include:

* Intake processing
* Prakriti analysis
* Vikriti analysis
* Agni analysis
* Nutrition analysis
* Food retrieval
* Food filtering and ranking
* Personalized diet planning
* Lifestyle recommendations
* Safety and validation
* Doctor review
* Final report generation

## 📄 Medical OCR

The medical-document pipeline is implemented under:

```text
src/medical_ocr/
```

Main components:

```text
ocr_engine.py
medical_parser.py
text_cleaner.py
medical_history_service.py
```

The OCR engine currently uses **PaddleOCR**.

## 🗂️ Medical Records

The patient medical-record system is implemented under:

```text
src/medical_records/
```

Main components:

```text
record.py
storage.py
service.py
```

Current records contain:

* Patient ID
* Document name
* Document type
* Original file path
* Upload timestamp
* OCR text
* Structured medical data

Records are currently stored locally in:

```text
data/medical_records.json
```

## 📚 Ayurvedic RAG

VedAmrit includes a Retrieval-Augmented Generation (RAG) component using Ayurvedic reference materials.

Reference documents are maintained under:

```text
src/rag/books/
```

The project also contains vector-store components for retrieval.

## 🛠️ Technology Stack

* **Python**
* **LangGraph**
* **LangChain**
* **PaddleOCR**
* **ChromaDB**
* **Machine Learning**
* **RAG**
* **PDF report generation**
* **JSON / CSV**
* **Git & GitHub**

## 📁 Project Structure

```text
VedAmrit/
│
├── data/
│   ├── disease/
│   ├── demo_foods.csv
│   └── medical_records.json
│
├── models/
│
├── reports/
│
├── src/
│   ├── agents/
│   ├── medical_ocr/
│   ├── medical_records/
│   ├── ml/
│   ├── prompts/
│   ├── rag/
│   ├── services/
│   ├── graph.py
│   └── main.py
│
├── tests/
│
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/Chandana-2024/VedAmrit.git
cd VedAmrit
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Ayurvedic workflow:

```bash
python -m src.main
```

## 🔍 Current Medical OCR Example

A medical document can be processed through the medical-record service:

```python
from src.medical_records.service import add_medical_document

record = add_medical_document(
    patient_id="PATIENT_ID",
    file_path="path/to/medical_document.png",
    document_type="lab_report"
)

print(record)
```

## 🧪 Testing

The project contains automated tests covering different parts of the Ayurvedic workflow.

Run:

```bash
pytest
```

## 🔐 Security

Sensitive configuration such as API keys and environment variables should be stored in `.env`.

The `.env` file is excluded from Git using `.gitignore`.

Do not commit API keys, passwords, tokens, or other private credentials.

## 🔮 Future Development

Planned improvements include:

* Patient-facing medical-record interface
* Medical document categories
* Multiple-document management
* Duplicate-document protection
* Improved structured medical history
* Medical-record API
* Optional ABHA integration
* Improved OCR support for different document types
* Enhanced patient and doctor dashboards

## 👩‍💻 Project Status

VedAmrit is an actively developing project.

The current repository contains a working Ayurvedic AI workflow together with a functional medical-document OCR and medical-record storage pipeline.

---

**VedAmrit — AI-assisted Ayurvedic wellness and structured medical records.** 🌿
