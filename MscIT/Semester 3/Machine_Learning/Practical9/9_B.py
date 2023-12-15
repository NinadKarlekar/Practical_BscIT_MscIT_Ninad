# 9B. Perform Text pre-processing, Text clustering, classification with Prediction, Test Score and Confusion Matrix

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset

# csv_file = 'Restaurant_Reviews.tsv'
csv_file = 'https://raw.githubusercontent.com/SarthakRana/Restaurant-Reviews-using-NLP-/master/Restaurant_Reviews.tsv'

dataset = pd.read_csv(csv_file, delimiter='\t', quoting=3)

# Text preprocessing using Natural Language Toolkit (nltk)
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = []
for i in range(0, 1000):    
    review = re.sub('[^a-zA-Z]', '', dataset['Review'][i]) # Remove non-alphabetic characters
    review = review.lower()  # Convert to lowercase
    review = review.split() # Tokenize the words
    ps = PorterStemmer() # Stemming and removing stopwords
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    # Join the words to form the processed review
    review = ' '.join(review)
    corpus.append(review)

# Creating the bag of words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
Y = dataset.iloc[:, 1].values

# Splitting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=100)

# Fitting Naive Bayes to the training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, Y_train)

# Predicting the test set results
Y_pred = classifier.predict(X_test)

# Model Accuracy
from sklearn import metrics
from sklearn.metrics import confusion_matrix
print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))

# Making the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)
print(cm)