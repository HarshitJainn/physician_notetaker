from keybert import KeyBERT

kw_model = KeyBERT()

def extract_keywords(text):
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 3),
        stop_words="english"
    )
    return [kw[0] for kw in keywords[:5]]
