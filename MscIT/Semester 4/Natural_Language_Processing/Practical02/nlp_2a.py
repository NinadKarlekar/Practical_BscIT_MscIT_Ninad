"""## 2A. Study of various corpus – Brown, Inaugural, Reuters, udhr with various methods like fields, raw, words, sents, categories."""

import nltk
from nltk.corpus import brown

nltk.download('brown')

# Display file ids of brown corpus
print('File ids of brown corpus\n', brown.fileids())

# Pick out the first of these texts — Emma by Jane Austen — and give it a short name, ca01
ca01 = brown.words('ca01')
# Display first few words
print('\nca01 has the following words:\n', ca01[:20])
# Total number of words in ca01
print('\nca01 has', len(ca01), 'words')

# Categories or files in brown corpus
print('\n\nCategories or files in brown corpus:\n')
print(brown.categories())

# Display other information about each text by looping over all the values of fileid
# and then computing statistics for each text.
print('\n\nStatistics for each text:\n')
print('AvgWordLen\tAvgSentenceLen\tNo. of Times Each Word Appears On Avg\tFileName')

for fileid in brown.fileids():
    num_chars = len(brown.raw(fileid))
    num_words = len(brown.words(fileid))
    num_sents = len(brown.sents(fileid))
    num_vocab = len(set(w.lower() for w in brown.words(fileid)))

    print(f"{int(num_chars / num_words)}\t\t\t"
          f"{int(num_words / num_sents)}\t\t\t"
          f"{int(num_words / num_vocab)}\t\t\t"
          f"{fileid}")