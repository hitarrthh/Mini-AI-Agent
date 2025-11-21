import json
import fitz  # PyMuPDF

# --------------------------
# Step 1: Load PDF text
# --------------------------
pdf_path = r"C:\Users\Admin\Desktop\Work\Task\Wesourseu\data\ukpga_20250022_en.pdf"

doc = fitz.open(pdf_path)
full_text = ""
for page in doc:
    full_text += page.get_text()
doc.close()

# --------------------------
# Step 2: Define rules and keyword mapping
# --------------------------
rules = [
    {"rule": "Act must define key terms", "key": "definitions"},
    {"rule": "Act must specify eligibility criteria", "key": "eligibility"},
    {"rule": "Act must specify responsibilities of the administering authority", "key": "responsibilities"},
    {"rule": "Act must include enforcement or penalties", "key": "penalties"},
    {"rule": "Act must include payment calculation or entitlement structure", "key": "payments"},
    {"rule": "Act must include record-keeping or reporting requirements", "key": "record_keeping"}
]

keyword_map = {
    "definitions": "means",
    "eligibility": "entitled",
    "responsibilities": "must",
    "penalties": "penalty",
    "payments": "allowance",
    "record_keeping": "record"
}

# --------------------------
# Step 3: Rule evaluation functions
# --------------------------
def extract_section(text, keyword):
    text_lower = text.lower()
    if keyword in text_lower:
        start_idx = text_lower.find(keyword)
        end_idx = start_idx + 500  # 500 chars as evidence
        return text[start_idx:end_idx]
    return ""

def analyze_section(text):
    if not text:
        return "fail", "Not found", 20
    text_length = len(text.strip())
    if text_length < 20:
        return "fail", text.strip(), 40
    elif text_length < 100:
        return "pass", text.strip(), 70
    else:
        return "pass", text.strip()[:500], 90

# --------------------------
# Step 4: Apply rules
# --------------------------
rule_results = []
for r in rules:
    keyword = keyword_map[r["key"]]
    section_text = extract_section(full_text, keyword)
    status, evidence, confidence = analyze_section(section_text)
    rule_results.append({
        "rule": r["rule"],
        "status": status,
        "evidence": evidence,
        "confidence": confidence
    })

# --------------------------
# Step 5: Save results
# --------------------------
rule_check_path = r"C:\Users\Admin\Desktop\Work\Task\Wesourseu\utils\outputs\rule_check_task4.json"
with open(rule_check_path, "w", encoding="utf-8") as f:
    json.dump(rule_results, f, indent=4, ensure_ascii=False)

print(json.dumps(rule_results, indent=4, ensure_ascii=False))
