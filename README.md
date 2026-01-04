# Physician Notetaker

## Overview

This project implements an **AI-powered Physician Notetaker system** that automates medical documentation from doctor–patient conversations. The system extracts key clinical information, analyzes patient sentiment and intent, and generates structured medical notes to assist healthcare professionals.

---

## System Components

### 1. Medical NLP Summarization

- Extracts **Symptoms, Diagnosis, Treatment, and Prognosis** from transcripts
- Uses **SciSpacy** for medical Named Entity Recognition (NER)
- Uses **Transformer-based summarization (BART)** to generate concise clinical summaries

### 2. Sentiment & Intent Analysis

- Classifies patient sentiment as **Anxious, Neutral, or Reassured**
- Detects patient intent such as **Seeking reassurance** or **Reporting symptoms**
- Uses **DistilBERT** along with rule-assisted logic for interpretability

### 3. SOAP Note Generation

- Converts transcripts into standard **SOAP (Subjective, Objective, Assessment, Plan)** format
- Uses a hybrid approach combining NLP summarization and rule-based structuring
- Ensures clinical readability and safety

---

## Tech Stack

- Python 3.9+
- spaCy & SciSpacy
- HuggingFace Transformers
- KeyBERT
- PyTorch

---

## Project Structure

```
Physician-Notetaker/
│
├── data/
│   ├── sample_transcript.txt
│   └── patient_utterances.txt
│
├── src/
│   ├── preprocess.py
│   ├── ner_extraction.py
│   ├── keyword_extraction.py
│   ├── summarization.py
│   ├── sentiment.py
│   ├── intent.py
│   ├── soap_mapper.py
│   ├── pipeline.py
│   ├── pipeline_2.py
│   └── pipeline_3.py
│
├── output/
│   ├── structured_summary.json
│   ├── sentiment_intent.json
│   └── soap_note.json
│
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### Clone the Repository

```bash
git clone <repository-link>
cd Physician-Notetaker
```

### Install Dependencies

```bash
pip install -r requirements.txt
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_md-0.5.4.tar.gz
```

⚠️ **Note:** On the first run, large transformer models (BERT, BART) will be downloaded automatically. This may take a few minutes depending on internet speed.

---

## How to Run the Project

### Medical NLP Summarization

```bash
cd src
python pipeline.py
```

### Sentiment & Intent Analysis

```bash
python pipeline_ps2.py
```

### SOAP Note Generation

```bash
python pipeline_ps3.py
```

All outputs will be saved in the `output/` directory.

---

## Output Files

- **`structured_summary.json`** → Extracted medical details and summarized clinical note
- **`sentiment_intent.json`** → Patient sentiment and intent classification
- **`soap_note.json`** → Structured SOAP note in clinical format

---

## Demo

An interactive demo of the system has been deployed using Streamlit to showcase real-time processing of medical transcripts.

🔗 **Demo Link:** (add Streamlit app URL here)

The Streamlit deployment is provided as an optional enhancement beyond the required submission.

---

## Contributors

- Harshit Jain

---

## Acknowledgments

- SciSpacy for medical NLP capabilities
- HuggingFace for pre-trained transformer models
- The open-source community for supporting healthcare AI innovation
