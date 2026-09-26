import re


def extract_patient_info(text):

    patient = {
        "name": None,
        "age": None,
        "gender": None,
        "patient_id": None,
        "visit_type": None,
        "referring_doctor": None
    }

    # Patient name
    match = re.search(r"Patient Name:\s*(.+)", text)

    if match:
        patient["name"] = match.group(1).strip()

    # Age and gender
    match = re.search(
        r"Age / Gender:\s*(\d+)\s*Years\s*/\s*(Male|Female|Other)",
        text,
        re.IGNORECASE
    )

    if match:
        patient["age"] = int(match.group(1))
        patient["gender"] = match.group(2).capitalize()

    # Patient ID
    match = re.search(r"Patient ID:\s*(.+)", text)

    if match:
        patient["patient_id"] = match.group(1).strip()

    # Visit type
    match = re.search(r"Visit Type:\s*(.+)", text)

    if match:
        patient["visit_type"] = match.group(1).strip()

    # Referring doctor
    match = re.search(r"Ref\. By:\s*(.+)", text)

    if match:
        patient["referring_doctor"] = match.group(1).strip()

    return patient


def extract_lab_results(text):

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    results = []

    # Known laboratory test names from the OCR report
    test_names = [
        "Fasting Blood Sugar (FBS)",
        "Post Prandial Blood Sugar (PPBS)",
        "HbA1c",
        "Total Cholesterol",
        "Triglycerides",
        "HDL Cholesterol",
        "LDL Cholesterol",
        "Serum Creatinine",
        "Urea",
        "Hemoglobin"
    ]

    for i, line in enumerate(lines):

        if line not in test_names:
            continue

        # Expected structure:
        # Test name
        # value
        # unit
        # reference range

        if i + 3 >= len(lines):
            continue

        value = lines[i + 1]
        unit = lines[i + 2]
        reference_range = lines[i + 3]

        results.append({
            "test": line,
            "value": value,
            "unit": unit,
            "reference_range": reference_range
        })

    return results


def extract_impression(text):

    if "IMPRESSION" not in text:
        return []

    impression_text = text.split("IMPRESSION", 1)[1]

    # Stop before unrelated footer information
    if "Scan for" in impression_text:
        impression_text = impression_text.split("Scan for", 1)[0]

    lines = [
        line.strip()
        for line in impression_text.splitlines()
        if line.strip()
    ]

    return lines


def parse_medical_report(text):

    patient = extract_patient_info(text)
    lab_results = extract_lab_results(text)
    impression = extract_impression(text)

    return {
        "patient": patient,
        "medical_history": {
            "lab_results": lab_results,
            "impression": impression
        }
    }