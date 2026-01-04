import json
import os

from sentiment import classify_sentiment
from intent import detect_intent

# Ensure output folder exists
os.makedirs("../output", exist_ok=True)

# Load patient utterance
with open("../data/patient_utterances.txt", "r") as f:
    text = f.read().strip()

# Run models
sentiment = classify_sentiment(text)
intent = detect_intent(text)

# Final output
result = {
    "Text": text,
    "Sentiment": sentiment,
    "Intent": intent
}

# Save output
with open("../output/sentiment_intent.json", "w") as f:
    json.dump(result, f, indent=4)

print("Sentiment & Intent analysis completed.")
