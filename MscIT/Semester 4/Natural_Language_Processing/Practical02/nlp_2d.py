## 2d. Study of tagged corpora with methods like tagged_sents, tagged_words.
import nltk
from nltk import tokenize

nltk.download('punkt')
nltk.download('words')

para = "Hello! My name is Ninad Karlekar. Today you'll be learning NLTK."
sents = tokenize.sent_tokenize(para)

print("\nSentence tokenization\n===================\n", sents)

# Word tokenization
print("\nWord tokenization\n===================\n")
for index in range(len(sents)):
    words = tokenize.word_tokenize(sents[index])
    print(words)