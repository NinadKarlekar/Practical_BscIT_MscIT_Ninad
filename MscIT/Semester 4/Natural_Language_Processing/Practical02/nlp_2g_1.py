#g. Study i) DefaultTagger, ii) Regular expression tagger, iii) UnigramTagger

import nltk
from nltk.tag import DefaultTagger
from nltk.corpus import treebank

# Create a default tagger that tags everything as 'NN'
exptagger = DefaultTagger('NN')

# Get test sentences from the treebank corpus
testsentences = treebank.tagged_sents()[1000:]

# Evaluate the tagger on the test sentences
print(exptagger.evaluate(testsentences))

## Tagging a list of sentences
print(exptagger.tag_sents([['Hi', ','], ['How', 'are', 'you', '?']]))
