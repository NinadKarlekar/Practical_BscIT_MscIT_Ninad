# 4b. Tokenization using Regular Expressions (RegEx)

import re

# Sample text to tokenize
text = "Hello ! My name is Ninad Karlekar I live in mumbai"

# Define the regex pattern for tokenization (splitting by whitespace)
pattern = r'\s+'

# Tokenizing the text using re.split()
tokens = re.split(pattern, text)

# Printing the tokens
print("="*60)
print("4b. Tokenization using Regular Expressions (RegEx)")
print("-"*10)
print("Tokens:", tokens)
print("="*60)