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