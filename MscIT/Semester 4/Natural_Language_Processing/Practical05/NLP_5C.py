## 5C. Identify the Indian language from the given text.

#pip install langid

import nltk
import langid
 
# Download necessary NLTK data
nltk.download('punkt')
 
def identify_language(text):
    lang, _ = langid.classify(text)
    return lang
 
# Identify the Indian Language from the given text
language = identify_language("नमस्ते, आप कैसे हैं?")
print("Identified language:", language)
