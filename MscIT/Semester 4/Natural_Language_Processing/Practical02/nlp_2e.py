## 2e. Write a program to find the most frequent noun tags.
import nltk
from collections import defaultdict

nltk.download('averaged_perceptron_tagger')

text = nltk.word_tokenize("Ninad likes to play football. Ninad does not like to play cricket.")
tagged = nltk.pos_tag(text)
print(tagged)

# Checking if it is a noun or not
addNounWords = []
count = 0

for words in tagged:
    val = tagged[count][1]
    if val in ('NN', 'NNS', 'NNPS', 'NNP'):
        addNounWords.append(tagged[count][0])
    count += 1

print(addNounWords)

temp = defaultdict(int)

# Memoizing count
for sub in addNounWords:
    for wrd in sub.split():
        temp[wrd] += 1

# Getting max frequency
res = max(temp, key=temp.get)

# Printing result
print("Word with maximum frequency : " + str(res))
