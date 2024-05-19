# 7D. Implementation of Deductive Chart Parsing using context free grammar and a given sentence.

import nltk
from nltk import tokenize

# Define the context-free grammar (CFG)
grammar1 = nltk.CFG.fromstring("""
    S -> NP VP
    PP -> P NP
    NP -> Det N | Det N PP | 'I'
    VP -> V NP | VP PP
    Det -> 'a' | 'my'
    N -> 'bird' | 'balcony'
    V -> 'saw'
    P -> 'in'
""")

# Sentence to be tokenized and parsed
sentence = "I saw a bird in my balcony"
all_tokens = tokenize.word_tokenize(sentence)
print(all_tokens)
# all_tokens = ['I', 'saw', 'a', 'bird', 'in', 'my', 'balcony']

# Create a parser using the defined grammar
parser = nltk.ChartParser(grammar1)

# Parse the tokenized sentence and print the parse trees
for tree in parser.parse(all_tokens):
    print(tree)
    tree.draw()
