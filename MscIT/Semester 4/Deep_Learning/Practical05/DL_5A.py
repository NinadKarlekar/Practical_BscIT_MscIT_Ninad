
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