#pip install scipy==1.12

import gensim
from gensim.parsing.preprocessing import remove_stopwords, STOPWORDS

text = "Ninad likes to play Chess, however he is not too good with the football."

# Removing Stop Words
filtered_sentence = remove_stopwords(text)
print("-"*30)
print("Original sentence:", text)
print("-"*30)
print("Stop words removed:", filtered_sentence)
print("-"*30)

# Adding Stop Words
all_stopwords = STOPWORDS.union(set(['likes', 'play']))
text_tokens = text.split()
tokens_without_sw = [word for word in text_tokens if word not in all_stopwords]
print("Original sentence (tokens):", text_tokens)
print("-"*30)
print("Stop words 'likes' and 'play' added:", tokens_without_sw)
print("-"*30)

# Removing Specific Stop Word
all_stopwords = STOPWORDS.difference({"not"})
tokens_without_sw = [word for word in text.split() if word not in all_stopwords]
print("Original sentence (tokens):", text.split())
print("-"*30)
print("Stop word 'not' removed:", tokens_without_sw)
print("-"*30)
