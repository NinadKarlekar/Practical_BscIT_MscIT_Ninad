#g. Study i) DefaultTagger, ii) Regular expression tagger, iii) UnigramTagger

from nltk.tag import UnigramTagger
from nltk.corpus import treebank
train_sents = treebank.tagged_sents()[:10]
tagger = UnigramTagger(train_sents) # Initializing 
print(treebank.sents()[0])
print('\n',tagger.tag(treebank.sents()[0]))
tagger.tag(treebank.sents()[0])
tagger = UnigramTagger(model ={'Pierre': 'NN'}) #Overriding the context model print('\n',tagger.tag(treebank.sents()[0]))
