# 5B. Generate similar sentences from a given Hindi text input

# Install required packages
# !pip install torch==1.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
# !pip install inltk
# !pip install tornado==4.5.3

# Setup for Hindi language
from inltk.inltk import setup
setup('hi')

# Import get_similar_sentences from inltk
from inltk.inltk import get_similar_sentences

# Get similar sentences to the one given in Hindi
output = get_similar_sentences('मैं आज बहुत खुश हूं', 5, 'hi')

# Print the similar sentences
print(output)
