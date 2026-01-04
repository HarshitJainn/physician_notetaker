import spacy

nlp = spacy.load("en_core_sci_md")

def extract_medical_entities(text):
    doc = nlp(text)

    medical_data = {
        "Symptoms": [],
        "Treatment": [],
        "Diagnosis": [],
        "Prognosis": []
    }

    for ent in doc.ents:
        if ent.label_ in ["DISEASE", "SYMPTOM"]:
            medical_data["Symptoms"].append(ent.text)
        elif ent.label_ == "TREATMENT":
            medical_data["Treatment"].append(ent.text)

    return medical_data
