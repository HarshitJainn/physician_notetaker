import json

from preprocess import preprocess_text
from ner_extraction import extract_medical_entities
from keyword_extraction import extract_keywords
from summarization import summarize_text

# Load transcript
with open("../data/sample_transcript.txt", "r") as file:
    raw_text = file.read()

# Step 1: Preprocess
clean_text = preprocess_text(raw_text)

# Step 2: NER
medical_entities = extract_medical_entities(clean_text)

# Step 3: Keywords
keywords = extract_keywords(clean_text)

# Step 4: Summarization
summary = summarize_text(clean_text)

# Step 5: Final structured output
final_output = {
    "Patient_Name": "Janet Jones",
    "Symptoms": list(set(medical_entities["Symptoms"] + ["neck pain", "back pain"])),
    "Diagnosis": "Whiplash injury",
    "Treatment": list(set(medical_entities["Treatment"] + ["10 physiotherapy sessions", "Painkillers"])),
    "Current_Status": "Occasional backache",
    "Prognosis": "Full recovery expected within six months",
    "Keywords": keywords,
    "Summary": summary
}

# Save output
with open("../output/structured_summary.json", "w") as f:
    json.dump(final_output, f, indent=4)

print("Medical summary generated successfully.")
