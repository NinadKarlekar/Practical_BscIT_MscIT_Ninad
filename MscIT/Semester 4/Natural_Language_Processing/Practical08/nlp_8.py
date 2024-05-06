# -*- coding: utf-8 -*-
#NLP_8

# PorterStemmer
import nltk
from nltk.stem import PorterStemmer
word_stemmer = PorterStemmer()
print("Output of PorterStemmer:-")
print(word_stemmer.stem('Ninad is running'))
print("*"*50)

# LancasterStemmer
import nltk
from nltk.stem import LancasterStemmer
Lanc_stemmer = LancasterStemmer()
print("Output of LancasterStemmer:-")
print(Lanc_stemmer.stem('jumping'))
print("*"*50)

#RegexpStemmer
import nltk
from nltk.stem import RegexpStemmer
Reg_stemmer = RegexpStemmer('ing$|s$|e$|able$', min=4)
print("Output of RegexpStemmer:-")
print(Reg_stemmer.stem('writing'))
print("*"*50)

# SnowballStemmer
import nltk
from nltk.stem import SnowballStemmer
english_stemmer = SnowballStemmer('english')
print("Output of SnowballStemmer:-")
print(english_stemmer.stem ('writing'))
print("*"*50)

# WordNetLemmatizer
print("Output of WordNetLemmatizer:-")
import nltk
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
print("word :\tlemma")
print("rocks :", lemmatizer.lemmatize("books"))
print("corpora :", lemmatizer.lemmatize("corpora"))

# a denotes adjective in "pos"
print("worse :", lemmatizer.lemmatize("worse", pos ="a"))
print("*"*50)

