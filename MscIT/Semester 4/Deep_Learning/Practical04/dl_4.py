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

