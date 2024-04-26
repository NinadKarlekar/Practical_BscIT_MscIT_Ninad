#4c. Tokenization using NLTK

import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

# Sample text to tokenize
text = "Hello ! My name is Ninad Karlekar I live in mumbai"

# Tokenizing the text using NLTK's word_tokenize()
tokens = word_tokenize(text)

# Printing the tokens
print("-"*30)
print("4c. Tokenization using NLTK")
print("-"*10)
print("Tokens:", tokens)
print("-"*30)