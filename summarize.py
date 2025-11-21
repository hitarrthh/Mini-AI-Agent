#Task-2
import json
import re

with open(r"C:\Users\Admin\Desktop\Work\Task\Wesourseu\utils\outputs\extracted_text.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    act_text = data.get("extracted_text", "")

paragraphs = [p.strip() for p in act_text.split("\n\n") if p.strip()]

summary_bullets = []

for para in paragraphs:
    if len(para) < 30:
        continue
    sentences = re.split(r'(?<=[.!?])\s+', para)
    bullet = ' '.join(sentences[:2])
    summary_bullets.append(bullet)
    if len(summary_bullets) >= 10:
        break

with open(r"C:\Users\Admin\Desktop\Work\Task\Wesourseu\utils\outputs\summarize.json", "w", encoding="utf-8") as f:
    json.dump({"summary": summary_bullets}, f, indent=4)

print("Summary saved to 'C:\\Users\\Admin\\Desktop\\Work\\Task\\Wesourseu\\utils\\outputs\\summarize.json'")
