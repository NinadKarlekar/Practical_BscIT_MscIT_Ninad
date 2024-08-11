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


# !pip install keras (2.15.0)
# !pip install scikit_learn
# !pip install scikeras

import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
# from keras.wrappers.scikit_learn import KerasRegressor
from scikeras.wrappers import KerasRegressor
from sklearn.model_selection import cross_val_score, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPRegressor


dataframe = pd.read_csv("MscIT\Semester 4\Deep_Learning\Practical05\housing.csv")
# dataframe = pd.read_csv("/content/housing.csv")
dataset = dataframe.values

# Print the shape of dataset to verify the number of features and samples
print("Shape of dataset:", dataset.shape)

# Ensure correct slicing for features and target variable
X = dataset[:, :-1]  # Select all columns except the last one as features
Y = dataset[:, -1]   # Select the last column as target variable

def wider_model():
    model = Sequential()
    model.add(Dense(15, input_dim=13, kernel_initializer='normal', activation='relu'))
    # model.add(Dense(20, input_dim=13, kernel_initializer='normal', activation='relu'))
    model.add(Dense(13, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasRegressor(build_fn=wider_model, epochs=10, batch_size=5)))
pipeline = Pipeline(estimators)
kfold = KFold(n_splits=10)

results = cross_val_score(pipeline, X, Y, cv=kfold)
print("Wider: %.2f (%.2f) MSE" % (results.mean(), results.std()))

```

</details>

<br>

5b. Evaluating feed forward deep network for multiclass Classification using KFold cross-validation.

<details>
<summary>CODE</summary>

```python

# 5B. Evaluating feed forward deep network for multiclass Classification using KFold cross-validation.


# !pip install scikeras
# !pip install np_utils

# loading libraries
import pandas
from keras.models import Sequential
from keras.layers import Dense
from scikeras.wrappers import KerasClassifier
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder

# loading dataset
df = pandas.read_csv('/content/flowers.csv', header=None) #remove , header=None if dataset contains column name
print(df)

# splitting dataset into input and output variables
X = df.iloc[:, 0:4].astype(float)
y = df.iloc[:, 4]
# print(X)
# print(y)

# encoding string output into numeric output
encoder = LabelEncoder()
encoder.fit(y)
encoded_y = encoder.transform(y)
print(encoded_y)
dummy_Y = to_categorical(encoded_y)
print(dummy_Y)

def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(8, input_dim=4, activation='relu'))
    model.add(Dense(3, activation='softmax'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

estimator = baseline_model()
estimator.fit(X, dummy_Y, epochs=100, shuffle=True)
action = estimator.predict(X)
for i in range(25):
    print(dummy_Y[i])
    print('^^^^^^^^^^^^^^^^^^^^^^')
for i in range(25):
    print(action[i])



```

</details>

<br>

******************************************************

## Prac6

6a. Implementing regularization to avoid overfitting in binary classification.

<details>
<summary>CODE</summary>

```python

from matplotlib import pyplot
from sklearn.datasets import make_moons
from keras.models import Sequential
from keras.layers import Dense
X,Y=make_moons(n_samples=100,noise=0.2,random_state=1)
n_train=30
trainX,testX=X[:n_train,:],X[n_train:]
trainY,testY=Y[:n_train],Y[n_train:]
#print(trainX)
#print(trainY)
#print(testX)
#print(testY)
model=Sequential()
model.add(Dense(500,input_dim=2,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
history=model.fit(trainX,trainY,validation_data=(testX,testY),epochs=1000)
pyplot.plot(history.history['accuracy'],label='train')
pyplot.plot(history.history['val_accuracy'],label='test')
pyplot.legend()
pyplot.show()

pyplot.plot(history.history['accuracy'],label='train')
pyplot.plot(history.history['val_accuracy'],label='test')
pyplot.legend()
pyplot.show()

```

</details>

<br>

6b. Implement 12 regularization with alpha=0.001.

<details>
<summary>CODE</summary>

```python

from matplotlib import pyplot
from sklearn.datasets import make_moons
from keras.models import Sequential
from keras.layers import Dense
from keras.regularizers import l2

X,Y=make_moons(n_samples=100,noise=0.2,random_state=1)
n_train=30
trainX,testX=X[:n_train,:],X[n_train:]
trainY,testY=Y[:n_train],Y[n_train:]
#print(trainX)
#print(trainY)
#print(testX)
#print(testY)
model=Sequential()
model.add(Dense(500,input_dim=2,activation='relu',kernel_regularizer=l2(0.001)))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
history=model.fit(trainX,trainY,validation_data=(testX,testY),epochs=1000)

pyplot.plot(history.history['accuracy'],label='train')
pyplot.plot(history.history['val_accuracy'],label='test')
pyplot.legend()
pyplot.show()

```

</details>

<br>

6c. Replace 12 regularization with l2 regularization.

<details>
<summary>CODE</summary>

```python

# !pip install pandas
# !pip install matplotlib
# !pip install keras
# !pip install tensorflow

from matplotlib import pyplot
from sklearn.datasets import make_moons
from keras.models import Sequential
from keras.layers import Dense
from keras.regularizers import l1_l2
X,Y=make_moons(n_samples=100,noise=0.2,random_state=1)
n_train=30
trainX,testX=X[:n_train,:],X[n_train:]
trainY,testY=Y[:n_train],Y[n_train:]
#print(trainX)
#print(trainY)
#print(testX)
#print(testY)

model=Sequential()
model.add(Dense(500,input_dim=2,activation='relu',kernel_regularizer=l1_l2(l1=0.001,l2=0.001)))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
history=model.fit(trainX,trainY,validation_data=(testX,testY),epochs=400)
pyplot.plot(history.history['accuracy'],label='train')
pyplot.plot(history.history['val_accuracy'],label='test')
pyplot.legend()
pyplot.show()

```

</details>

<br>

******************************************************

## Prac7

7. Demonstrate recurrent neural network that learns to perform sequence analysis for stock price.

<details>
<summary>CODE</summary>

```python

# -*- coding: utf-8 -*-
"""DL_7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1M8AweS1adIDt5F_5xLoA5-Iw94gY5nkM

# 7. Demonstrate recurrent neural network that learns to perform sequence analysis for stock price.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from sklearn.preprocessing import MinMaxScaler

# Read training dataset
dataset_train = pd.read_csv('/content/Google_Stock_Price_Train.csv')
training_set = dataset_train.iloc[:, 1:2].values

# Scale the training set
sc = MinMaxScaler(feature_range=(0,1))
training_set_scaled = sc.fit_transform(training_set)

# Create X_train and Y_train
X_train = []
Y_train = []
for i in range(60, 1258):
    X_train.append(training_set_scaled[i-60:i, 0])
    Y_train.append(training_set_scaled[i, 0])
X_train, Y_train = np.array(X_train), np.array(Y_train)

# Reshape X_train for LSTM
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# Build the LSTM model
regressor = Sequential()
regressor.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units=50, return_sequences=True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units=50, return_sequences=True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units=50))
regressor.add(Dropout(0.2))
regressor.add(Dense(units=1))
regressor.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
regressor.fit(X_train, Y_train, epochs=100, batch_size=32)

# Read test dataset
dataset_test = pd.read_csv('/content/Google_Stock_Price_Test.csv')
real_stock_price = dataset_test.iloc[:, 1:2].values

# Concatenate total dataset
dataset_total = pd.concat((dataset_train['Open'], dataset_test['Open']), axis=0)
inputs = dataset_total[len(dataset_total)-len(dataset_test)-60:].values
inputs = inputs.reshape(-1, 1)
inputs = sc.transform(inputs)

# Create X_test
X_test = []
for i in range(60, 80):
    X_test.append(inputs[i-60:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# Predict stock prices
predicted_stock_price = regressor.predict(X_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

# Visualize results
plt.plot(real_stock_price, color='red', label='Real Google Stock Price')
plt.plot(predicted_stock_price, color='blue', label='Predicted Stock Price')
plt.xlabel('Time')
plt.ylabel('Google Stock Price')
plt.legend()
plt.show()

```

</details>

<br>

******************************************************

## Prac8

8. Performing encoding and decoding of images using deep autoencoder.

<details>
<summary>CODE</summary>

```python

# 8. Performing encoding and decoding of images using deep autoencoder.

import keras
from keras import layers
from keras.datasets import mnist
import numpy as np

encoding_dim = 32

# this is our input image
input_img = keras.Input(shape=(784,))

# "encoded" is the encoded representation of the input
encoded = layers.Dense(encoding_dim, activation='relu')(input_img)

# "decoded" is the lossy reconstruction of the input
decoded = layers.Dense(784, activation='sigmoid')(encoded)

# creating autoencoder model
autoencoder = keras.Model(input_img, decoded)

# create the encoder model
encoder = keras.Model(input_img, encoded)

encoded_input = keras.Input(shape=(encoding_dim,))

# Retrieve the last layer of the autoencoder model
decoder_layer = autoencoder.layers[-1]

# create the decoder model
decoder = keras.Model(encoded_input, decoder_layer(encoded_input))

autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

# scale and make train and test dataset
(X_train, _), (X_test, _) = mnist.load_data()
X_train = X_train.astype('float32') / 255.
X_test = X_test.astype('float32') / 255.
X_train = X_train.reshape((len(X_train), np.prod(X_train.shape[1:])))
X_test = X_test.reshape((len(X_test), np.prod(X_test.shape[1:])))

print(X_train.shape)
print(X_test.shape)

# train autoencoder with training dataset
autoencoder.fit(X_train, X_train,
                epochs=50,
                batch_size=256,
                shuffle=True,
                validation_data=(X_test, X_test))

encoded_imgs = encoder.predict(X_test)
decoded_imgs = decoder.predict(encoded_imgs)

import matplotlib.pyplot as plt

n = 10  # How many digits we will display
plt.figure(figsize=(40, 4))
for i in range(10):
    # display original
    ax = plt.subplot(3, 20, i + 1)
    plt.imshow(X_test[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # display encoded image
    ax = plt.subplot(3, 20, i + 1 + 20)
    plt.imshow(encoded_imgs[i].reshape(8, 4))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # display reconstruction
    ax = plt.subplot(3, 20, 2 * 20 + i + 1)
    plt.imshow(decoded_imgs[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

plt.show()

```

</details>

<br>

******************************************************

## Prac9

9. Implementation of convolutional neural network to predict numbers from number images.

<details>
<summary>CODE</summary>

```python

# 9. Aim: Implementation of convolutional neural network to predict number from number images

from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
import matplotlib.pyplot as plt

# Download MNIST data and split into train and test sets
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# Plot the first image in the dataset
plt.imshow(X_train[0])
plt.show()
print(X_train[0].shape)

# Reshape data for CNN (add channel dimension)
X_train = X_train.reshape(60000, 28, 28, 1)
X_test = X_test.reshape(10000, 28, 28, 1)

# One-hot encode labels
Y_train = to_categorical(Y_train)
Y_test = to_categorical(Y_test)

# Print an example of one-hot encoded label
print(Y_train[0])

# Define the model architecture
model = Sequential()

# Learn image features with convolutional layers
model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(28, 28, 1)))
model.add(Conv2D(32, kernel_size=3, activation='relu'))
model.add(Flatten())

# Add a dense layer with softmax activation for 10-class classification
model.add(Dense(10, activation='softmax'))

# Compile the model for training
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model with validation data
model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=3)

# Make predictions on the first 4 test images
predictions = model.predict(X_test[:4])
print(predictions)  # Predicted probabilities for each class

# Print the actual labels for the first 4 test images
print(Y_test[:4])  # One-hot encoded labels

```

</details>

<br>

******************************************************

## Prac10

10. Denoising of images using autoencoder.

<details>
<summary>CODE</summary>

```python

# 10. Denoising of images using autoencoder.

import keras
from keras.datasets import mnist
from keras import layers
import numpy as np
from keras.callbacks import TensorBoard
import matplotlib.pyplot as plt

(X_train,_),(X_test,_)=mnist.load_data()
X_train=X_train.astype('float32')/255.
X_test=X_test.astype('float32')/255.
X_train=np.reshape(X_train,(len(X_train),28,28,1))
X_test=np.reshape(X_test,(len(X_test),28,28,1))
noise_factor=0.5
X_train_noisy=X_train+noise_factor*np.random.normal(loc=0.0,scale=1.0,size=X_train.shape)
X_test_noisy=X_test+noise_factor*np.random.normal(loc=0.0,scale=1.0,size=X_test.shape)
X_train_noisy=np.clip(X_train_noisy,0.,1.)
X_test_noisy=np.clip(X_test_noisy,0.,1.)

n=10
plt.figure(figsize=(20,2))
for i in range(1,n+1):
    ax=plt.subplot(1,n,i)
    plt.imshow(X_test_noisy[i].reshape(28,28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()

input_img=keras.Input(shape=(28,28,1))
x=layers.Conv2D(32,(3,3),activation='relu',padding='same')(input_img)
x=layers.MaxPooling2D((2,2),padding='same')(x)
x=layers.Conv2D(32,(3,3),activation='relu',padding='same')(x)
encoded=layers.MaxPooling2D((2,2),padding='same')(x)
x=layers.Conv2D(32,(3,3),activation='relu',padding='same')(encoded)
x=layers.UpSampling2D((2,2))(x)
x=layers.Conv2D(32,(3,3),activation='relu',padding='same')(x)
x=layers.UpSampling2D((2,2))(x)
decoded=layers.Conv2D(1,(3,3),activation='sigmoid',padding='same')(x)

autoencoder=keras.Model(input_img,decoded)
autoencoder.compile(optimizer='adam',loss='binary_crossentropy')
autoencoder.fit(X_train_noisy,X_train, epochs=3, batch_size=128, shuffle=True, validation_data=(X_test_noisy,X_test), callbacks=[TensorBoard(log_dir='/tmo/tb',histogram_freq=0,write_graph=False)])

predictions=autoencoder.predict(X_test_noisy)

m=10
plt.figure(figsize=(20,2))
for i in range(1,m+1):
    ax=plt.subplot(1,m,i)
    plt.imshow(predictions[i].reshape(28,28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()

```

</details>

<br>

******************************************************




<!-- | Sr.No. | Name | README | DOWNLOAD |
| --- | --- | --- | --- |
| [Prac1](/MscIT/Semester%204/Deep_Learning/Practical01/) | 1. Performing matrix multiplication and finding eigen vectors and eigen values using TensorFlow.. | [Prac1](#prac1) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%204/Deep_Learning/Practical01/DL_1.py) | -->