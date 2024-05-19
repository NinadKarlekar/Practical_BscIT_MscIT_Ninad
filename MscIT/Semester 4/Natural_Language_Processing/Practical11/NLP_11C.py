# 11C. Word Sense Disambiguation
from nltk.corpus import wordnet as wn

def get_first_sense(word, pos=None):
    if pos:
        synsets = wn.synsets(word, pos)
    else:
        synsets = wn.synsets(word)
    return synsets[0]

best_synset = get_first_sense('bank')
print('%s: %s' % (best_synset.name(), best_synset.definition()))

best_synset = get_first_sense('set', 'n')
print('%s: %s' % (best_synset.name(), best_synset.definition()))

best_synset = get_first_sense('set', 'v')
print('%s: %s' % (best_synset.name(), best_synset.definition()))
