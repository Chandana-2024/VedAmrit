import os
import json

# Fix PaddlePaddle CPU issue on Windows
os.environ["FLAGS_enable_pir_api"] = "0"

from paddleocr import PaddleOCR


ocr = PaddleOCR(
    lang="en",
    enable_mkldnn=False
)


def extract_text(image_path):

    results = ocr.predict(image_path)

    all_text = []

    for result in results:

        # Convert PaddleOCR result object to JSON/dictionary
        result_json = result.json

        if isinstance(result_json, str):
            result_json = json.loads(result_json)

        # PaddleOCR 3.x stores the OCR information inside "res"
        data = result_json.get("res", result_json)

        texts = data.get("rec_texts", [])

        for text in texts:
            if text.strip():
                all_text.append(text.strip())

    return "\n".join(all_text)