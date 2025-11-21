# 📄 Universal Credit Act 2025 — PDF Processing & Analysis Pipeline

This repository contains a modular Python pipeline for extracting, cleaning, summarizing, classifying, and rule-checking legal documents — demonstrated using the Universal Credit Act 2025.

The project includes four main modules:

1. Text Extraction (`extract_text.py`)
2. Summarization (`summarize.py`)
3. Key Section Extraction (`key_section.py`)
4. Rule Compliance Checking (`rule_check.py`)

Each module is standalone but works together as a full analysis workflow.

---

## 🔧 Requirements

Install dependencies:

pip install pdfplumber PyMuPDF

---
Project Structure
.
├── extract_text.py
├── summarize.py
├── key_section.py
├── rule_check.py
└── outputs/
    ├── extracted_text.json
    ├── summarize.json
    ├── legislation_extracted.json
    └── rule_check_task4.json
---

# 🚀 1. Text Extraction (`extract_text.py`)

Purpose:
- Extract text from the PDF  
- Clean whitespace, remove page numbers  
- Export structured JSON with metadata

Output: outputs/extracted_text.json  

Run:

python extract_text.py

---

# 📝 2. Automatic Summarization (`summarize.py`)

Purpose:
- Split Act text into paragraphs  
- Take first 1–2 sentences of the first 10 meaningful paragraphs  
- Export 10-bullet summary  

Output: outputs/summarize.json  

Run:

python summarize.py

---

# 🔍 3. Key Section Extraction (`key_section.py`)

Purpose:
Extract via regex:
- Definitions  
- Eligibility criteria  
- Obligations (contains “must”)  
- Responsibilities  
- Payment/allowance references  
- Penalties/enforcement  
- Reporting / record-keeping lines  

Output: outputs/legislation_extracted.json  

Run:

python key_section.py

---

# ✅ 4. Rule-based Compliance Checker (`rule_check.py`)

Purpose:
Checks if the Act contains:
- Definitions  
- Eligibility criteria  
- Responsibilities  
- Penalties  
- Payment structures  
- Record-keeping requirements  

Each rule provides:
- pass/fail  
- Evidence snippet  
- Confidence score  

Output: outputs/rule_check_task4.json  

Run:

python rule_check.py

---

# 🧠 Workflow Summary

| Step | Script | Description |
|------|---------|-------------|
| 1 | extract_text.py | Extract + clean PDF text |
| 2 | summarize.py | Create 10-bullet summary |
| 3 | key_section.py | Extract important clauses |
| 4 | rule_check.py | Check compliance rules |

---

# 📌 Notes

- Scripts use absolute paths — modify for your environment.  
- Regex patterns are optimized for legal/legislative documents.  
- All processed outputs are saved in the outputs/ folder automatically.

