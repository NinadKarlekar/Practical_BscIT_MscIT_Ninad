#4d. Tokenization using the spaCy library

import spacy

# Load the English language model
nlp = spacy.blank("en")

# Text to be tokenized
text = "Hello ! My name is Ninad Karlekar I live in mumbai"

# Process the text with SpaCy
doc = nlp(text)

# Extract tokens
tokens = [token.text for token in doc]

# Print tokens
print("="*60)
print("4d. Tokenization using the spaCy library")
print("-"*10)
print("Tokens:", tokens)
print("="*60)
