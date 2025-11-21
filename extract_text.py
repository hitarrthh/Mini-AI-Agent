#Task-1
import re
import json
import os
import pdfplumber

def clean_text(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"\n{2,}", "\n", text)
    text = re.sub(r" {2,}", " ", text)
    text = re.sub(r"\bPage \d+\b", "", text)
    text = re.sub(r"\n?\s*\d+\s*\n", "\n", text)
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def extract_text_from_pdf(pdf_path: str, output_json_path: str):
    folder = os.path.dirname(output_json_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"{pdf_path} not found")

    full_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            raw = page.extract_text() or ""
            full_text += raw + "\n"

    cleaned = clean_text(full_text)

    output = {
        "document_name": "Universal Credit Act 2025",
        "extracted_text": cleaned,
        "length_characters": len(cleaned),
        "length_words": len(cleaned.split())
    }

    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)

    return output


if __name__ == "__main__":
    extract_text_from_pdf(
        r"C:\Users\Admin\Desktop\Work\Task\Wesourseu\data\ukpga_20250022_en.pdf",
        "outputs/extracted_text.json"
    )
