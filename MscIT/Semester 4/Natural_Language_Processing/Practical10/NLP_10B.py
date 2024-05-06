"""## b. speech tagging using nktl"""

import nltk
nltk.download('state_union')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

# Create our training and testing data:
train_text = state_union.raw("E:\\GitHub\\Practical_BscIT_MscIT_Ninad\\MscIT\\Semester 4\\Natural_Language_Processing\\Practical10\\2005-GWBush.txt")
sample_text = state_union.raw("E:\\GitHub\\Practical_BscIT_MscIT_Ninad\\MscIT\\Semester 4\\Natural_Language_Processing\\Practical10\\2006-GWBush.txt")

# Train the Punkt tokenizer:
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

# Tokenize:
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized[:2]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
    except Exception as e:
        print(str(e))

process_content()