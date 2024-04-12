# Import necessary libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download stopwords (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

print("-"*40)

# Sample text
text = "Ninad likes to play Chess, however he is not too good with the football."
print("Given Text:- ",text)
# Remove stop words from text
text_tokens = word_tokenize(text)
stop_words = stopwords.words('english')
tokens_without_sw = [word for word in text_tokens if word not in stop_words]
print("Tokens without stop words:", tokens_without_sw)

# Add custom stop word ('not')
custom_stop_words = stop_words + ['not']
tokens_without_sw = [word for word in text_tokens if word not in custom_stop_words]
print("\nTokens without 'not' (custom stop word):", tokens_without_sw)
