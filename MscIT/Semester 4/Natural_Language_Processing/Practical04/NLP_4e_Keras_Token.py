#4e. Tokenization using Keras [COLAB]

import keras

from tensorflow.keras.preprocessing.text import text_to_word_sequence #works on colab

# Create a string input
str = "Hello ! My name is Ninad Karlekar I live in mumbai"

# tokenizing the text
tokens = text_to_word_sequence(str)
print("="*60)
print("4e. Tokenization using Keras")
print("-"*10)
print("Tokens:", tokens)
print("="*60)

####
# to run on local IDE(jupyter) use tenserflow version 2.13.0
# pip uninstall tensorflow     ## to uninstall latest version if installed
# pip install tensorflow==2.13.0
####

