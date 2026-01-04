import streamlit as st
import sys
import os

# Allow imports from src/
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from preprocess import preprocess_text
from ner_extraction import extract_medical_entities
from keyword_extraction import extract_keywords
from summarization import summarize_text
from sentiment import classify_sentiment
from intent import detect_intent
from soap_mapper import generate_soap_note

# -------------------- UI --------------------

st.set_page_config(
    page_title="AI Physician Notetaker",
    layout="wide"
)

st.title("Physician Notetaker")
st.write(
    "Paste a doctor–patient conversation below to automatically generate "
    "medical summaries, sentiment analysis, and SOAP notes."
)

# Text input
transcript = st.text_area(
    "Doctor–Patient Transcript",
    height=250,
    placeholder="Paste the conversation here..."
)

# Run button
if st.button("Generate Notes"):

    if not transcript.strip():
        st.warning("Please enter a transcript.")
    else:
        with st.spinner("Processing medical transcript..."):
            # Preprocess
            clean_text = preprocess_text(transcript)

            # PS-1: Medical NLP
            entities = extract_medical_entities(clean_text)
            keywords = extract_keywords(clean_text)
            summary = summarize_text(clean_text)

            # PS-2: Sentiment & Intent
            sentiment = classify_sentiment(clean_text)
            intent = detect_intent(clean_text)

            # PS-3: SOAP Note
            soap_note = generate_soap_note(summary)

        st.success("Notes generated successfully!")

        # -------------------- OUTPUT --------------------

        st.subheader("Medical Summary")
        st.write(summary)

        st.subheader("Key Medical Phrases")
        st.write(keywords)

        st.subheader("Patient Sentiment & Intent")
        st.json({
            "Sentiment": sentiment,
            "Intent": intent
        })

        st.subheader("SOAP Note")
        st.json(soap_note)
