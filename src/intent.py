def detect_intent(text):
    text_lower = text.lower()

    if any(word in text_lower for word in ["worried", "concerned", "afraid", "hope"]):
        return "Seeking reassurance"
    elif any(word in text_lower for word in ["pain", "hurt", "ache", "symptom"]):
        return "Reporting symptoms"
    else:
        return "Expressing concern"
