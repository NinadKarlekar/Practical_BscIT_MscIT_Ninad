# 11 a. Multiword Expressions in NLP

# Multiword Expressions in NLP
from nltk.tokenize import MWETokenizer
from nltk import sent_tokenize, word_tokenize

s = '''Good cake cost Rs.1500\kg in Mumbai. Please buy me one of them.\n\nThanks.'''
mwe = MWETokenizer([('New', 'York'), ('Hong', 'Kong')], separator='_')

for sent in sent_tokenize(s):
    print(mwe.tokenize(word_tokenize(sent)))
