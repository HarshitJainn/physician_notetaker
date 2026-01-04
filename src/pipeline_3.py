import json
import os

from preprocess import preprocess_text
from summarization import summarize_text
from soap_mapper import generate_soap_note

# Ensure output directory exists
os.makedirs("../output", exist_ok=True)

# Load transcript
with open("../data/sample_transcript.txt", "r") as f:
    raw_text = f.read()

# Preprocess
clean_text = preprocess_text(raw_text)

# Summarize
summary = summarize_text(clean_text)

# Generate SOAP note
soap_note = generate_soap_note(summary)

# Save output
with open("../output/soap_note.json", "w") as f:
    json.dump(soap_note, f, indent=4)

print("✅ SOAP note generated successfully.")
