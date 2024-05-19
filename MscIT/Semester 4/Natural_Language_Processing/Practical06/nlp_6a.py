# 6. Illustrate part of speech tagging.
## a) sentence tokenization, word tokenization, Part of speech Tagging and chunking of user defined text.

import nltk
from nltk import tokenize
from nltk import tag
from nltk import chunk

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Paragraph to be tokenized
para = "Hello! My name is Ninad Karlekar. Today you'll be learning NLTK."

# Sentence tokenization
sents = tokenize.sent_tokenize(para)
print("\nsentence tokenization\n===================\n", sents)

# Word tokenization
print("\nword tokenization\n===================\n")
for index in range(len(sents)):
    words = tokenize.word_tokenize(sents[index])
    print(words)

# POS Tagging
tagged_words = []
for index in range(len(sents)):
    tagged_words.append(tag.pos_tag(words))
print("\nPOS Tagging\n===========\n", tagged_words)

# Chunking
tree = []
for index in range(len(sents)):
    tree.append(chunk.ne_chunk(tagged_words[index]))
print("\nchunking\n========\n", tree)