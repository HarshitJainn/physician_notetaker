from transformers import pipeline

sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def classify_sentiment(text):
    if not text.strip():
        return "Neutral"

    result = sentiment_model(
        text,
        truncation=True,
        max_length=512
    )[0]

    if result["label"] == "NEGATIVE":
        return "Anxious"
    elif result["label"] == "POSITIVE":
        return "Reassured"
    else:
        return "Neutral"
