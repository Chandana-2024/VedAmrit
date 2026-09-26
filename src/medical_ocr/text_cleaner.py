import re


def clean_text(text):

    lines = text.splitlines()

    cleaned_lines = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Remove unnecessary website/contact information
        if line.startswith("www."):
            continue

        if "info@" in line:
            continue

        # Remove decorative hospital slogan
        if line == "Better Health · Brighter Future":
            continue

        cleaned_lines.append(line)

    text = "\n".join(cleaned_lines)

    # Fix common OCR formatting
    text = re.sub(r"Patient Name\s*:\s*", "Patient Name: ", text)
    text = re.sub(r"Patient ID\s*\n\s*:\s*", "Patient ID: ", text)
    text = re.sub(r"Visit Type\s*\n\s*:\s*", "Visit Type: ", text)
    text = re.sub(r"Ref\. By\s*\n\s*:\s*", "Ref. By: ", text)

    # Age / Gender appears on two lines
    text = re.sub(
        r"Age / Gender\s*\n\s*:\s*",
        "Age / Gender: ",
        text
    )

    return text