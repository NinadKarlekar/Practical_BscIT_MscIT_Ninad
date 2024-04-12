#python -m spacy download en_core_web_sm

import spacy
import nltk
from nltk.tokenize import word_tokenize
print("NLP 3E 3 Using Spacy Adding and Removing Stop Words in Default Spacy Stop Words List")
# Load spaCy model (assuming en_core_web_sm is already downloaded)
sp = spacy.load("en_core_web_sm")

# Get default stop words from spaCy
all_stopwords = sp.Defaults.stop_words

# Adding Stop Words

text = "Ninad likes to play Chess, however he is not too good with the football."
text_tokens = word_tokenize(text)

# Add "play" to stop words
all_stopwords.add("play")
tokens_without_sw = [word for word in text_tokens if word not in all_stopwords]
print("Original sentence (tokens):", text_tokens)
print("Stop word 'play' added:", tokens_without_sw)

# Removing Specific Stop Word

# Remove "not" from stop words (modify with caution)
all_stopwords.remove("not")
tokens_without_sw = [word for word in text_tokens if word not in all_stopwords]
print("Original sentence (tokens):", text_tokens)
print("Stop word 'not' removed:", tokens_without_sw)
