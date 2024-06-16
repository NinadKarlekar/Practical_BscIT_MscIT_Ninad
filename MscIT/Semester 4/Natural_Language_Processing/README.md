# Natural Language Processing

M. Sc (Information Technology)
Natural Language Processing



## Index

| Sr.No. | Name | README | DOWNLOAD |
| --- | --- | --- | --- |
| [Prac1A](/MscIT/Semester%204/Natural_Language_Processing/Practical01/) <br> [Prac1B](/MscIT/Semester%204/Natural_Language_Processing/Practical01/) | 1A. Convert file Text to Speech. <br> 1B. Convert file Speech to Text. | [Prac1A](#prac1) <br> [Prac1B](#prac1) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%204/Natural_Language_Processing/Practical01/NLP_1A_TTS.py) <br> [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%204/Natural_Language_Processing/Practical01/NLP_1B_STT.py) |


******************
---------------------

## Prac1

1A. Convert file Text to Speech.


<details>
<summary>CODE</summary>

```python
# Import the required module for text to speech conversion

#!pip install gtts
from gtts import gTTS

# This module is imported so that we can play the converted audio
import os

# The text that you want to convert to audio
mytext = "Hello Everyone!My name is Ninad"

# Language in which you want to convert
language = "en"

# Passing the text and language to the engine, here we have marked slow=False. Which tells the module that the converted audio should have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named welcome
myobj.save("welcome1.mp3")

# Playing the converted file
#os.system("mpg321 welcome.mp3")

```

</details>

<br>


1B. Convert file Speech to Text.


<details>
<summary>CODE</summary>


```python
#Aim: Convert audio file Speech to Text.
#Note: required to store the input file "NLP_test.wav" in the current folder before running the program.

#!pip install SpeechRecognition pydub
import speech_recognition as sr
filename = "MscIT\\Semester 4\\Natural_Language_Processing\\Practical01\\NLP_test.wav"

# initialize the recognizer
r = sr.Recognizer()
# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)

```

</details>

******************************************************

## Prac2

2a. Study of various corpus – Brown, Inaugural, Reuters, udhr with various methods like fields, raw, words, sents, categories.

<details>
<summary>CODE</summary>

```python
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

```

</details>

<br>

2b. Create and use your own corpora (plaintext, categorical).

<details>
<summary>CODE</summary>

```python
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
```

</details>

<br>

2c. Study conditional frequency distribution.

<details>
<summary>CODE</summary>

```python
## 2c. Study Conditional frequency distributions

# Process a sequence of pairs
text = ['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
pairs = [('news', 'The'), ('news', 'Fulton'), ('news', 'County'), ...]

import nltk
from nltk.corpus import brown
nltk.download('inaugural')
nltk.download('udhr')

fd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)
)

genre_word = [
    (genre, word)
    for genre in ['news', 'romance']
    for word in brown.words(categories=genre)
]

print(len(genre_word))
print(genre_word[:4])
print(genre_word[-4:])

cfd = nltk.ConditionalFreqDist(genre_word)

print(cfd)
print(cfd.conditions())
print(cfd['news'])
print(cfd['romance'])
print(list(cfd['romance']))

from nltk.corpus import inaugural

cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target)
)

from nltk.corpus import udhr

languages = [
    'Chickasaw', 'English', 'German_Deutsch',
    'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik'
]

cfd = nltk.ConditionalFreqDist(
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latin1')
)

cfd.tabulate(conditions=['English', 'German_Deutsch'], samples=range(10), cumulative=True)
```

</details>

<br>

2d. Study of tagged corpora with methods like tagged_sents, tagged_words.

<details>
<summary>CODE</summary>

```python
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
```

</details>

<br>

2e. Write a program to find the most frequent noun tags.

<details>
<summary>CODE</summary>

```python
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
```

</details>

<br>

2f. Map words to the properties using Python Dictionaries.

<details>
<summary>CODE</summary>

```python
## 2f. Map Words to Properties Using Python Dictionaries

# Creating and printing a dictionary by mapping word with its properties
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))
```

</details>

<br>

2g. Study i) DefaultTagger, ii) Regular expression tagger, iii) UnigramTagger

<details>
<summary>CODE</summary>

```python
# i) DefaultTagger
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


####

# ii) Regular expression tagger, 

from nltk.corpus import brown 
from nltk.tag import RegexpTagger 
test_sent = brown.sents(categories='news')[0] 
regexp_tagger = RegexpTagger( 
[(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),   # cardinal numbers 
(r'(The|the|A|a|An|an)$', 'AT'),   # articles 
(r'.*able$', 'JJ'),                # adjectives 
(r'.*ness$', 'NN'),   # nouns formed from adjectives      
(r'.*ly$', 'RB'),     # adverbs        
(r'.*s$', 'NNS'),         # plural nouns   
(r'.*ing$', 'VBG'),   # gerunds              
(r'.*ed$', 'VBD'),  # past tense verbs 
(r'.*', 'NN')    # nouns (default)                    
]) 
print(regexp_tagger) 
print(regexp_tagger.tag(test_sent))

####

# iii) UnigramTagger

from nltk.tag import UnigramTagger
from nltk.corpus import treebank
train_sents = treebank.tagged_sents()[:10]
tagger = UnigramTagger(train_sents) # Initializing 
print(treebank.sents()[0])
print('\n',tagger.tag(treebank.sents()[0]))
tagger.tag(treebank.sents()[0])
tagger = UnigramTagger(model ={'Pierre': 'NN'}) #Overriding the context model print('\n',tagger.tag(treebank.sents()[0]))

```

</details>

<br>

2h. Find different words from a given plaintext without any spaces by comparing this text with a given corpus of words. Also find the score of words.

<details>
<summary>CODE</summary>

```python
## 2h. Find different words from a given plain text without any space by comparing this text with a given corpus of words. Also find the score of words.

from __future__ import with_statement  # with statement for reading file
import re  # Regular expression

words = []  # corpus file words
testword = []  # test words
ans = []  # words matches with corpus

print("MENU")
print("-----------")
print(" 1. Hash tag segmentation")
print(" 2. URL segmentation")
print("Enter the input choice for performing word segmentation:")
choice = int(input())

if choice == 1:
    text = "#whatismyname"  # hash tag test data to segment
    print("Input with HashTag:", text)
    pattern = re.compile("[^\w']")
    a = pattern.sub('', text)
elif choice == 2:
    text = "www.whatismyname.com"  # URL test data to segment
    print("Input with URL:", text)
    a = re.split('\s|(?<!\d)[,.](?!\d)', text)
    splitwords = ["www", "com", "in"]  # remove the words which is containing in the list
    a = "".join([each for each in a if each not in splitwords])
else:
    print("Wrong choice...try again")
    exit()

print(a)

for each in a:
    testword.append(each)  # test word
test_lenth = len(testword)  # length of the test data

# Reading the corpus
with open('words.txt', 'r') as f:
    lines = f.readlines()
    words = [e.strip() for e in lines]

def Seg(a, lenth):
    ans = []
    for k in range(0, lenth + 1):  # this loop checks char by char in the corpus
        if a[0:k] in words:
            print(a[0:k], "- appears in the corpus")
            ans.append(a[0:k])
            break
    if ans != []:
        g = max(ans, key=len)
        return g
    return ""

test_tot_itr = 0  # each iteration value
answer = []  # Store each word that contains the corpus
Score = 0  # initial value for score
N = 37  # total number of corpus
M = 0
C = 0

while test_tot_itr < test_lenth:
    ans_words = Seg(a, test_lenth)
    if ans_words != "":
        test_itr = len(ans_words)
        answer.append(ans_words)
        a = a[test_itr:test_lenth]
        test_tot_itr += test_itr

Aft_Seg = " ".join([each for each in answer])
# print segmented words in the list
print("Output")
print("---------")
print(Aft_Seg)  # print after segmentation the input

# Calculating Score
C = len(answer)
score = C * N / N  # Calculate the score
print("Score", score)
```

</details>

<br>




******************************************************

## Prac3

3a. Study of Wordnet Dictionary with methods as synsets, definitions, examples, antonyms.

<details>
<summary>CODE</summary>

```python
# NLP 3A. Study of Wordnet Dictionary with methods as synsets, definitions, examples, antonyms
# Import necessary libraries
import nltk
from nltk.corpus import wordnet

# Download WordNet (if not already downloaded)
nltk.download('wordnet')

# Get synsets (collection of synonyms) for "phone"
synsets = wordnet.synsets("phone")

# Print information about "phone"
print("**Word:** phone")
print("  * Synsets:")

# Loop through each synset and print its definition and examples
for synset in synsets:
    # Get the first word from the synset (considered the most representative)
    word = synset.lemmas()[0].name()
    print(f"      - Word: {word}")
    print(f"        - Definition: {synset.definition()}")
    print(f"          - Examples: {synset.examples()}")


print("-"*40)
# Get antonyms for "buy" (verb)
antonyms = wordnet.lemma('buy.v.01.buy').antonyms()

# Print antonyms for "buy"
print("\n**Antonyms for 'buy':")
for antonym in antonyms:
    print(f"  - {antonym.name()}")
```

</details>

<br>

3b. Study lemmas, hyponyms, hypernyms, entailments.

<details>
<summary>CODE</summary>

```python
# NLP 3B Study lemmas, hyponyms, hypernyms.

# Import necessary libraries
import nltk
from nltk.corpus import wordnet

# Download WordNet (if not already downloaded)
nltk.download('wordnet')

# Exploring Lemmas
print("\n**Lemmas**")
synsets = wordnet.synsets("computer")
print("  * Synsets and Lemmas:")
for synset in synsets:
    lemma_names = [lemma.name() for lemma in synset.lemmas()]
    print(f"      - Synset: {synset} --> Lemmas: {lemma_names}")

# Exploring Hyponyms
print("\n**Hyponyms**")
computer_synset = wordnet.synset("computer.n.01")
hyponyms = computer_synset.hyponyms()
print("  * Hyponyms of 'computer.n.01':")
for synset in hyponyms:
    lemma_names = [lemma.name() for lemma in synset.lemmas()]
    print(f"      - Synset: {synset} --> Lemmas: {lemma_names}")

# Exploring Hypernyms
print("\n**Hypernyms**")
vehicle_synset = wordnet.synset("vehicle.n.01")
car_synset = wordnet.synset("car.n.01")
lowest_common_hypernym = car_synset.lowest_common_hypernyms(vehicle_synset)
print(f"  * Lowest common hypernym of 'vehicle' and 'car': {lowest_common_hypernym[0]}")
```

</details>

<br>

3c. Write a program using python to find synonym and antonym of word "active" using Wordnet.

<details>
<summary>CODE</summary>

```python
# NLP 3C. Write a program using python to find synonym and antonym of word "active" using Wordnet.

import nltk
from nltk.corpus import wordnet
nltk.download('omw-1.4')

def get_synonyms_antonyms(word):
    synonyms = []
    antonyms = []

    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())

    return set(synonyms), set(antonyms)

def main():
    word = input("Enter the word:-")
    synonyms, antonyms = get_synonyms_antonyms(word)
    
    print("Synonyms of", word + ":", synonyms)
    print("Antonyms of", word + ":", antonyms)

if __name__ == "__main__":
    nltk.download('wordnet')
    main()
```

</details>

<br>

3d. Compare two nouns.

<details>
<summary>CODE</summary>

```python
# Code for comparing two nouns
# Insert your code here
```

</details>

<br>

3e. Handling stopword

3e_i. Using nltk, add or remove stop words in NLTK's Default stop word list

<details>
<summary>CODE</summary>

```python
# Code for handling stopwords using NLTK
# Insert your code here
```

</details>

<br>

3e_ii. Using Gensim, add or remove stop words in Default Gensim stop words List.

<details>
<summary>CODE</summary>

```python
# Code for handling stopwords using Gensim
# Insert your code here
```

</details>

<br>

3e_iii. Using SpaCy, add or remove Stop Words in Default SpaCy stop words List.

<details>
<summary>CODE</summary>

```python
# Code for handling stopwords using SpaCy
# Insert your code here
```

</details>

<br>

******************************************************

## Prac4

4A. Convert file Text to Speech.


<details>
<summary>CODE</summary>

```python


```

</details>

<br>

******************************************************

## Prac5

5A. Convert file Text to Speech.


<details>
<summary>CODE</summary>

```python


```

</details>

<br>

******************************************************

## Prac6

6A. Convert file Text to Speech.


<details>
<summary>CODE</summary>

```python


```

</details>

<br>

******************************************************

## Prac7

7A. Convert file Text to Speech.


<details>
<summary>CODE</summary>

```python


```

</details>

<br>

******************************************************

## Prac8

8A. Convert file Text to Speech.


<details>
<summary>CODE</summary>

```python


```

</details>

<br>

******************************************************

## Prac9

9A. Convert file Text to Speech.


<details>
<summary>CODE</summary>

```python


```

</details>

<br>

******************************************************

## Prac10

10A. Convert file Text to Speech.


<details>
<summary>CODE</summary>

```python


```

</details>

<br>

******************************************************

## Prac11

11A. Convert file Text to Speech.


<details>
<summary>CODE</summary>

```python


```

</details>

<br>

******************************************************





