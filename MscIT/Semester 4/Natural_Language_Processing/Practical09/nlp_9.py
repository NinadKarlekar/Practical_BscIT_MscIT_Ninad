# 9. Implement Naive Bayes classifier

# pip install pandas
# pip install sklearn
import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Download NLTK stopwords
nltk.download('stopwords')

# Read the SMS data
sms_data = pd.read_csv("MscIT\\Semester 4\\Natural_Language_Processing\\Practical09\\spam.csv", encoding='latin-1')

# Initialize the Porter Stemmer
stemming = PorterStemmer()
corpus = []

# Create the corpus with stemmed words
for i in range(len(sms_data)):
    s1 = re.sub('[^a-zA-Z]', ' ', sms_data['v2'][i])
    s1 = s1.lower()
    s1 = s1.split()
    s1 = [stemming.stem(word) for word in s1 if word not in set(stopwords.words('english'))]
    s1 = ' '.join(s1)
    corpus.append(s1)

# Convert the corpus into a matrix of token counts
countvectorizer = CountVectorizer()
x = countvectorizer.fit_transform(corpus).toarray()
print(x)

# Extract the target variable
y = sms_data['v1'].values
print(y)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, stratify=y, random_state=2)

# Initialize the Multinomial Naïve Bayes model
multinomialnb = MultinomialNB()
multinomialnb.fit(x_train, y_train)

# Predicting on test data
y_pred = multinomialnb.predict(x_test)
print(y_pred)

# Results of our models
print(classification_report(y_test, y_pred))
print("accuracy_score: ", accuracy_score(y_test, y_pred))