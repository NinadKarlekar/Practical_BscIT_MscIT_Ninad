# 5A. Word tokenization in Hindi

# Install required packages
# !pip install torch==1.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
# !pip install inltk
# !pip install tornado==4.5.3

# Setup for Hindi language
from inltk.inltk import setup
setup('hi')

# Import tokenize from inltk
from inltk.inltk import tokenize

# Hindi text to be tokenized
hindi_text = """प्राकृतिक भाषा सीखना बहुत दिलचस्प है।"""

# Tokenize the input text in Hindi
tokens = tokenize(hindi_text, "hi")

# Print the tokens
print(tokens)
