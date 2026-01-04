# Physician Notetaker

## Overview

Medical documentation takes up a significant portion of physicians' time. This project aims to reduce that burden by automatically processing doctor-patient conversations and generating structured clinical notes. The system listens to conversations, identifies important medical information, understands patient emotions, and creates properly formatted documentation that doctors can review and use.

## What Does It Do?

The system has three main capabilities:

**Medical Information Extraction**  
The system reads through conversation transcripts and pulls out important clinical details like symptoms the patient mentions, any diagnoses discussed, treatments prescribed, and what the expected outcomes are. It uses SciSpacy (a specialized medical language processing tool) to recognize medical terms accurately and BART transformers to create concise summaries.

**Understanding Patient Sentiment and Intent**  
Beyond just extracting facts, the system tries to understand how the patient is feeling - whether they're anxious about their condition, feeling neutral, or reassured after the consultation. It also identifies what the patient wants from the conversation, like seeking reassurance or reporting new symptoms. This uses DistilBERT combined with some rule-based logic to make interpretations.

**SOAP Note Generation**  
Doctors typically document visits using the SOAP format (Subjective, Objective, Assessment, Plan). The system automatically structures the conversation into this format, making it easier for healthcare providers to review and file the notes. This combines NLP techniques with structured formatting rules.

---

## Technology Used

- Python 3.9+
- spaCy and SciSpacy (for medical text processing)
- HuggingFace Transformers (BART and DistilBERT models)
- KeyBERT (for keyword extraction)
- PyTorch (deep learning framework)

---

## Project Structure

```
Physician-Notetaker/
│
├── data/                           # Sample input files
│   ├── sample_transcript.txt
│   └── patient_utterances.txt
│
├── src/                            # Source code modules
│   ├── preprocess.py              # Text cleaning and preprocessing
│   ├── ner_extraction.py          # Medical entity recognition
│   ├── keyword_extraction.py      # Important term extraction
│   ├── summarization.py           # Text summarization
│   ├── sentiment.py               # Sentiment classification
│   ├── intent.py                  # Intent detection
│   ├── soap_mapper.py             # SOAP note formatting
│   ├── pipeline.py                # Main NLP pipeline
│   ├── pipeline_2.py            # Sentiment analysis pipeline
│   └── pipeline_3.py            # SOAP generation pipeline
├── app.py                         # streamlit app
├── output/                         # Generated results
│   ├── structured_summary.json
│   ├── sentiment_intent.json
│   └── soap_note.json
│
├── requirements.txt                # Python dependencies
└── README.md
```

---

## Getting Started

### Installation

First, clone this repository and navigate to the project directory:

```bash
git clone https://github.com/HarshitJainn/physician_notetaker.git
cd Physician-Notetaker
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

You'll also need to install the SciSpacy medical model:

```bash
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_md-0.5.4.tar.gz
```

**Note:** The first time you run the system, it will download some large transformer models (BERT and BART). This is normal and might take a few minutes depending on your internet connection.

---

## Running the System

The system has three separate pipelines you can run:

### 1. Medical Information Extraction

```bash
cd src
python pipeline.py
```

This will process the transcript and extract medical entities, keywords, and generate a summary.

### 2. Sentiment and Intent Analysis

```bash
python pipeline_2.py
```

This analyzes the emotional tone and intent behind patient statements.

### 3. SOAP Note Generation

```bash
python pipeline_3.py
```

This creates a properly formatted SOAP note from the conversation.

All results are automatically saved to the `output/` directory as JSON files.

---

## Example Usage

If you want to try the system quickly, here's a sample transcript you can use:

```
Doctor: Good morning! How are you feeling today?
Patient: I'm a bit worried about my back pain, but it's better than before.
Doctor: That's good to hear there's some improvement. When did you first notice the pain?
Patient: It started about three weeks ago after I helped my friend move furniture.
Doctor: I see. Have you received any treatment for it so far?
Patient: Yes, I had physiotherapy sessions twice a week for the past two weeks.
Doctor: And how has the physiotherapy been working for you?
Patient: It's helping. The pain has reduced from about 8 out of 10 to maybe 4 out of 10 now.
Doctor: That's significant improvement. Let me examine your back to see how things are progressing.
Patient: Okay, thank you doctor.
Doctor: Based on the examination and your progress, I'd recommend continuing physiotherapy for another two weeks. Also, try to avoid heavy lifting.
Patient: Will do. Should I be worried about anything?
Doctor: No, you're responding well to treatment. This type of muscle strain typically resolves with continued therapy and rest.
Patient: That's reassuring. Thank you so much.
```

You can copy this transcript and paste it into the Streamlit app to see how the system processes real conversations and generates medical documentation.

### 4. Running the Streamlit Web Interface

If you want to use the interactive web interface locally:
```bash
streamlit run app.py
```

The app will open in your browser automatically at `http://localhost:8501`. You can paste any doctor-patient transcript and see the results in real-time.


## Output Files

The system generates three JSON files:

- **structured_summary.json** - Contains extracted symptoms, diagnoses, treatments, and a clinical summary
- **sentiment_intent.json** - Shows the patient's emotional state and what they were trying to communicate
- **soap_note.json** - A complete SOAP-formatted note ready for clinical use



## Challenges I Faced

During development, I encountered several interesting challenges:

- Getting the medical entity recognition to work accurately required fine-tuning with SciSpacy's specialized models
- Balancing between automation and medical accuracy was tricky - the system needed to be helpful but also safe
- The SOAP note formatting required careful mapping of conversational text to structured clinical categories
- Sentiment analysis in medical contexts is nuanced - a patient saying "I'm worried" might be normal concern or significant anxiety

## Technical Answers asked in Assignment - 

### How would you handle ambiguous or missing medical data in the transcript?
In healthcare, it’s important not to guess or hallucinate information. If certain details are missing in the transcript, the system explicitly marks them as “not mentioned” instead of making assumptions. For ambiguous information, uncertainty is preserved and flagged for clinician review to ensure safety and transparency.

---

### What pre-trained NLP models would you use for medical summarization?
Transformer-based models such as BART or T5 are well suited for summarization tasks. For medical contexts, domain-adapted variants like BioBERT or ClinicalBERT are preferred, as they better understand clinical terminology and documentation style.

---

### How would you fine-tune BERT for medical sentiment detection?
A domain-specific model like ClinicalBERT would be fine-tuned on labeled patient utterances with healthcare-relevant sentiment classes such as Anxious, Neutral, and Reassured. Training would focus only on patient-spoken text, followed by validation using clinician-reviewed samples.

---

### What datasets would you use for training a healthcare-specific sentiment model?
Public clinical datasets such as MIMIC-III or MIMIC-IV and i2b2 datasets would be used. These can be complemented with curated or synthetic doctor–patient conversations annotated for emotional context.

---

### How would you train an NLP model to map medical transcripts into SOAP format?
The model would be trained using paired datasets of transcripts and their corresponding SOAP notes. Sequence-to-sequence models like T5 or BART can be fine-tuned with section-aware prompts, and outputs should be reviewed by clinicians to ensure clinical correctness.

---

### What rule-based or deep-learning techniques would improve the accuracy of SOAP note generation?
A hybrid approach works best. Rule-based templates ensure correct SOAP structure, while deep-learning models handle language understanding and summarization. Medical entity extraction and confidence checks further improve reliability and safety.



## Future Improvements

There are several ways this could be enhanced:

- Add support for audio transcription so it works directly with recordings
- Implement multi-language support for non-English consultations  
- Create a feedback loop where doctors can correct the system and improve its accuracy over time
- Add integration with existing Electronic Health Record (EHR) systems
- Include more sophisticated clinical decision support features

## Acknowledgments

This project builds on some excellent open-source tools:

- The SciSpacy team for their medical NLP models
- HuggingFace for making state-of-the-art transformers accessible
- The broader healthcare AI research community for advancing this important field
