def generate_soap_note(summary_text):
    """
    Converts summarized medical text into SOAP format
    """

    soap_note = {
        "Subjective": {
            "Chief_Complaint": "Neck and back pain",
            "History_of_Present_Illness": summary_text
        },
        "Objective": {
            "Physical_Exam": "Full range of motion in neck and back, no tenderness",
            "Observations": "Patient appears stable and in normal health"
        },
        "Assessment": {
            "Diagnosis": "Whiplash injury",
            "Severity": "Mild, improving"
        },
        "Plan": {
            "Treatment": "Physiotherapy as required, analgesics for pain",
            "Follow_Up": "Return if symptoms worsen or persist"
        }
    }

    return soap_note
