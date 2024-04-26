#pip install gensim
from gensim.utils import tokenize
# Create a string input
str = "Hello ! My name is Ninad Karlekar I live in mumbai"
# tokenizing the text
# Tokenizing the text
tokenized_words = list(tokenize(str))

# Printing each tokenized word separately
print(tokenized_words)