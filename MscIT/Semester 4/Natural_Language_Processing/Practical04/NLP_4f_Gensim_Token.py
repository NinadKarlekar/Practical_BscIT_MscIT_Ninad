# 4f. Tokenization using Gensim
#pip install gensim
from gensim.utils import tokenize
# Create a string input
str = "Hello ! My name is Ninad Karlekar I live in mumbai"
# tokenizing the text
# Tokenizing the text
tokenized_words = list(tokenize(str))

# Printing each tokenized word separately
print("="*60)
print("4f. Tokenization using Gensim")
print("-"*10)
print("Tokens:", tokenized_words)
print("="*60)