## 2B. Create and use your own corpora (plaintext, categorical).

import os
import nltk
nltk.download('punkt')
from nltk.corpus import PlaintextCorpusReader

# Set the path to your corpus
corpus_root = '/content/uni' #path of files
filelist = PlaintextCorpusReader(corpus_root, '.*')

# Display file list
print('\nFile list:\n')
print(filelist.fileids())
print(filelist.root)

# Display other information about each text by looping over all the values of fileid
# and then computing statistics for each text.
print('\n\nStatistics for each text:\n')
print('AvgWordLen\tAvgSentenceLen\tNo. of Times Each Word Appears On Avg\tFileName')

for fileid in filelist.fileids():
    num_chars = len(filelist.raw(fileid))
    num_words = len(filelist.words(fileid))
    num_sents = len(filelist.sents(fileid))
    num_vocab = len(set(w.lower() for w in filelist.words(fileid)))

    print(f"{int(num_chars / num_words)}\t\t\t"
          f"{int(num_words / num_sents)}\t\t\t"
          f"{int(num_words / num_vocab)}\t\t"
          f"{fileid}")