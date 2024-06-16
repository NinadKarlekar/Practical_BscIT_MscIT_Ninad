# Deep Learning

M. Sc (Information Technology)
Deep Learning

## Index

| Sr.No. | Name | README |
| --- | --- | --- |
| [Prac1](/MscIT/Semester%204/Deep_Learning/Practical01/) | Performing matrix multiplication and finding eigen vectors and eigen values using TensorFlow. | [Prac1](#prac1) |
| [Prac2](/MscIT/Semester%204/Deep_Learning/Practical02/) | Solving XOR problem using deep feed forward network. | [Prac2](#prac2) |
| [Prac3](/MscIT/Semester%204/Deep_Learning/Practical03/) | Implementing deep neural network for performing binary classification task. | [Prac3](#prac3) |
| [Prac4A](/MscIT/Semester%204/Deep_Learning/Practical04/) <br> [Prac4B](/MscIT/Semester%204/Deep_Learning/Practical04/) <br> [Prac4C](/MscIT/Semester%204/Deep_Learning/Practical04/) | a) Using deep feed forward network with two hidden layers for performing multiclass classification and predicting the class. <br> b) Using a deep feed forward network with two hidden layers for performing classification and predicting the probability of class. <br> c) Using a deep feed forward network with two hidden layers for performing linear regression and predicting values. | [Prac4A](#prac4) <br> [Prac4B](#prac4) <br> [Prac4C](#prac4) |
| [Prac5A](/MscIT/Semester%204/Deep_Learning/Practical05/) <br> [Prac5B](/MscIT/Semester%204/Deep_Learning/Practical05/) | a) Evaluating feed forward deep network for regression using KFold cross validation. <br> b) Evaluating feed forward deep network for multiclass Classification using KFold cross-validation. | [Prac5A](#prac5) <br> [Prac5B](#prac5) |
| [Prac6A](/MscIT/Semester%204/Deep_Learning/Practical06/) <br> [Prac6B](/MscIT/Semester%204/Deep_Learning/Practical06/) <br> [Prac6C](/MscIT/Semester%204/Deep_Learning/Practical06/) | a) Implementing regularization to avoid overfitting in binary classification. <br> b) Implement l2 regularization with alpha=0.001 <br> c) Replace l2 regularization with l2 regularization. | [Prac6A](#prac6) <br> [Prac6B](#prac6) <br> [Prac6C](#prac6) |
| [Prac7](/MscIT/Semester%204/Deep_Learning/Practical07/) | Demonstrate recurrent neural network that learns to perform sequence analysis for stock price. | [Prac7](#prac7) |
| [Prac8](/MscIT/Semester%204/Deep_Learning/Practical08/) | Performing encoding and decoding of images using deep autoencoder. | [Prac8](#prac8) |
| [Prac9](/MscIT/Semester%204/Deep_Learning/Practical09/) | Implementation of convolutional neural network to predict numbers from number images. | [Prac9](#prac9) |
| [Prac10](/MscIT/Semester%204/Deep_Learning/Practical10/) | Denoising of images using autoencoder. | [Prac10](#prac10) |



******************
---------------------

## Prac1

1. Performing matrix multiplication and finding eigen vectors and eigen values using TensorFlow.



<details>
<summary>CODE</summary>

```python
# Aim: Performing matrix multiplication and finding eigen vectors and eigen values using TensorFlow.

import tensorflow as tf

print("Matrix Multiplication Demo")
x = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])
print(x)

y = tf.constant([7, 8, 9, 10, 11, 12], shape=[3, 2])
print(y)

z = tf.matmul(x, y)
print("Product:", z)

e_matrix_A = tf.random.uniform(
    [2, 2], minval=3, maxval=10, dtype=tf.float32, name="matrixA"
)
print("Matrix A:\n{}\n\n".format(e_matrix_A))
eigen_values_A, eigen_vectors_A = tf.linalg.eigh(e_matrix_A)
print(
    "Eigen Vectors:\n{}\n\nEigen Values:\n{}\n".format(eigen_vectors_A, eigen_values_A)
)


```

</details>


******************************************************

## Prac2

2. Solving XOR problem using deep feed forward network.

<details>
<summary>CODE</summary>

```python

import numpy as np
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(units=2, activation="relu", input_dim=2))
model.add(Dense(units=1, activation="sigmoid"))
model.compile(loss="binary_crossentropy", optimizer="adam", metrics="accuracy")

X = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
print("Input data:")
print(X)

y = np.array([0.0, 1.0, 1.0, 0.0])
print("\nTarget labels:")
print(y)

model.get_weights()
model.fit(X, y, epochs=500)
predictions = model.predict(X)
print("\nPredictions after training:")
print(predictions)

```

</details>

<br>


******************************************************

## Prac3

3. Implementing deep neural network for performing binary classification task.

<details>
<summary>CODE</summary>

```python

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

```

</details>

<br>

******************************************************

## Prac4

4a. Using deep feed forward network with two hidden layers for performing multiclass classification and predicting the class.

<details>
<summary>CODE</summary>

```python

# Aim: Using feed Forward Network with multiple hidden layers for performing multiclass classification and predicting the class. 

from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import numpy as np

df = pd.read_csv("/content/flower_1.csv")

#df = pd.read_csv("data/flower_1.csv")
# df = pd.read_csv("flower_1.csv")

df.head()

x=df.iloc[:,:-1].astype(float)
y=df.iloc[:,-1]

print(x.shape)
print(y.shape)

#labelencode y
from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()
y=lb.fit_transform(y)
y

import numpy as np
from tensorflow.keras.utils import to_categorical
#from keras.utils import np_utils
encoded_Y = to_categorical(y)
encoded_Y

#creating a model
model = Sequential()

model.add(Dense(units = 10, activation = 'relu', input_dim = 4))
model.add(Dense(units = 8, activation = 'relu'))
model.add(Dense(units = 3, activation = 'softmax'))

model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

model.fit(x,encoded_Y,epochs = 400,batch_size = 10)

predict = model.predict(x)
print(predict)

for i in range(35,150,3):
    print(predict[i],encoded_Y[i])

actual = []

for i in range(0,150):
    actual.append(np.argmax(predict[i]))

print(actual)

newdf = pd.DataFrame(list(zip(actual,y)),columns = ['Actual','Predicted'])
newdf


```

</details>

<br>

4b. Using a deep feed forward network with two hidden layers for performing classification and predicting the probability of class.

<details>
<summary>CODE</summary>

```python

# Paste your code here

```

</details>

<br>

4c. Using a deep feed forward network with two hidden layers for performing linear regression and predicting values.

<details>
<summary>CODE</summary>

```python

# Paste your code here

```

</details>

<br>

******************************************************

## Prac5

5a. Evaluating feed forward deep network for regression using KFold cross validation.

<details>
<summary>CODE</summary>

```python

# Paste your code here

```

</details>

<br>

5b. Evaluating feed forward deep network for multiclass Classification using KFold cross-validation.

<details>
<summary>CODE</summary>

```python

# Paste your code here

```

</details>

<br>

******************************************************

## Prac6

6a. Implementing regularization to avoid overfitting in binary classification.

<details>
<summary>CODE</summary>

```python

# Paste your code here

```

</details>

<br>

6b. Implement 12 regularization with alpha=0.001.

<details>
<summary>CODE</summary>

```python

# Paste your code here

```

</details>

<br>

6c. Replace 12 regularization with l2 regularization.

<details>
<summary>CODE</summary>

```python

# Paste your code here

```

</details>

<br>

******************************************************

## Prac7

7. Demonstrate recurrent neural network that learns to perform sequence analysis for stock price.

<details>
<summary>CODE</summary>

```python

# Paste your code here

```

</details>

<br>

******************************************************

## Prac8

8. Performing encoding and decoding of images using deep autoencoder.

<details>
<summary>CODE</summary>

```python

# Paste your code here

```

</details>

<br>

******************************************************

## Prac9

9. Implementation of convolutional neural network to predict numbers from number images.

<details>
<summary>CODE</summary>

```python

# Paste your code here

```

</details>

<br>

******************************************************

## Prac10

10. Denoising of images using autoencoder.

<details>
<summary>CODE</summary>

```python

# Paste your code here

```

</details>

<br>

******************************************************




<!-- | Sr.No. | Name | README | DOWNLOAD |
| --- | --- | --- | --- |
| [Prac1](/MscIT/Semester%204/Deep_Learning/Practical01/) | 1. Performing matrix multiplication and finding eigen vectors and eigen values using TensorFlow.. | [Prac1](#prac1) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%204/Deep_Learning/Practical01/DL_1.py) | -->