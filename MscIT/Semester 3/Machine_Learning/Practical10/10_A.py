#10 A) Aim:  Implement the different Distance methods (Euclidean) with Prediction, Test Score and Confusion Matrix. 

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#Load the dataset
df = pd.read_csv("Iris.csv")

#quick look into the data
print(df.head(5))
print("\n")

#Separate data and label
x = df.drop(['Species'], axis=1)
y = df['Species']

#Prepare data for classification process
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

#Create a model , p = 2 => Euclidean Distance:
knn = KNeighborsClassifier(n_neighbors = 6, p = 2, metric='minkowski')

#Train the model
knn.fit(x_train, y_train)

# Calculate the accuracy of the model
print(knn.score(x_test, y_test))
y_pred = knn.predict(x_test)

#confusion matrix 
from sklearn.metrics import  confusion_matrix
cm=np.array(confusion_matrix(y_test,y_pred))
print(cm)
print("\n")

#Create a model , p = 1 => Manhattan Distance
knn = KNeighborsClassifier(n_neighbors = 6, p = 1, metric='minkowski')

#Train the model
knn.fit(x_train, y_train)

# Calculate the accuracy of the model
print(knn.score(x_test, y_test))
y_pred = knn.predict(x_test)

#confusion matrix 
from sklearn.metrics import  confusion_matrix
cm=np.array(confusion_matrix(y_test,y_pred))
print(cm)
print("\n")

#Create a model ,p = ∞, Chebychev Distance
#let ∞ = 10000
knn = KNeighborsClassifier(n_neighbors = 6, p = 10000, metric='minkowski')

#Train the model
knn.fit(x_train, y_train)

# Calculate the accuracy of the model
print(knn.score(x_test, y_test))
y_pred = knn.predict(x_test)

#confusion matrix 
from sklearn.metrics import  confusion_matrix
cm=np.array(confusion_matrix(y_test,y_pred))
print(cm)
print("\n") 
