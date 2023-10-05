# Prac 5: Naive Bayes and Gaussian Classification
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.metrics import confusion_matrix

wine = datasets.load_wine()
print("Features: ", wine.feature_names)
print("Labels: ", wine.target_names)

X = pd.DataFrame(wine['data'])
print(X.head())
print(wine.data.shape)

y = wine.target  # Remove print()

X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.30, random_state=10)

gnb = GaussianNB()
gnb.fit(X_train, y_train)

y_pred = gnb.predict(X_test)
print(y_pred)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)  # No need for np.array()
cm
