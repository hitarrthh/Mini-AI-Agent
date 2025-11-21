#Task-3
import re
import json

with open(r"C:\Users\Admin\Desktop\Work\Task\Wesourseu\utils\outputs\extracted_text.json", "r", encoding="utf-8") as f:
    text = f.read()

data = {
    "definitions": [],
    "obligations": [],
    "responsibilities": [],
    "eligibility": [],
    "payments": [],
    "penalties": [],
    "record_keeping": []
}

definitions = re.findall(r'“([^”]+)” has the meaning in regulation [\dA-Z]+\(\d+\)', text)
for d in definitions:
    data["definitions"].append({"term": d, "meaning": "see corresponding regulation"})

eligibility_patterns = [
    r'pre-2026 claimant',
    r'severe conditions criteria claimant',
    r'terminally ill'
]
for e in eligibility_patterns:
    if e in text:
        data["eligibility"].append(e)

obligation_sentences = re.findall(r'([^.]*?\bmust\b[^.]*\.)', text)
data["obligations"].extend(obligation_sentences)

payment_sentences = re.findall(r'amounts? of [^.;\n]+', text)
data["payments"].extend(payment_sentences)

record_sentences = re.findall(r'(information requirement[^.;\n]*|reporting[^.;\n]*)', text, re.IGNORECASE)
data["record_keeping"].extend(record_sentences)

penalty_sentences = re.findall(r'(penalt(?:y|ies)|enforcement)[^.;\n]*', text, re.IGNORECASE)
data["penalties"].extend(penalty_sentences)

responsibility_sentences = re.findall(r'([^.]*\bresponsibilit(?:y|ies)\b[^.]*\.)', text)
data["responsibilities"].extend(responsibility_sentences)

with open(r"C:\Users\Admin\Desktop\Work\Task\Wesourseu\utils\outputs\legislation_extracted.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("Extraction completed. JSON saved as 'legislation_extracted.json'")
