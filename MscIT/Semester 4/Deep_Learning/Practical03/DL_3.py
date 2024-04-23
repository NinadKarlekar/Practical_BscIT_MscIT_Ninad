# Aim: Implementing deep neural network for performing binary classification task.
# pip install keras
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd

names = [
    "No. of pregnancies",
    "Glucose level",
    "Blood Pressure",
    "skin thickness",
    "Insulin",
    "BMI",
    "Diabetes pedigree",
    "Age",
    "Class",
]

#csv file with no column names expected
df = pd.read_csv("/content/pima-indians-diabetes.data.csv", names=names) 
df.head(3)
binaryc = Sequential()

from tensorflow.tools.docs.doc_controls import doc_in_current_and_subclasses

binaryc.add(Dense(units=10, activation="relu", input_dim=8))
binaryc.add(Dense(units=8, activation="relu"))
binaryc.add(Dense(units=1, activation="sigmoid"))
binaryc.compile(loss="binary_crossentropy", optimizer="adam", metrics="accuracy")
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.25, random_state=1)
xtrain.shape
ytrain.shape
binaryc.fit(xtrain, ytrain, epochs=200, batch_size=20)
predictions = binaryc.predict(xtest)
predictions.shape
class_labels = []
for i in predictions:
    if i > 0.5:
        class_labels.append(1)
    else:
        class_labels.append(0)
class_labels
from sklearn.metrics import accuracy_score

print("Accuracy Score", accuracy_score(ytest, class_labels))
