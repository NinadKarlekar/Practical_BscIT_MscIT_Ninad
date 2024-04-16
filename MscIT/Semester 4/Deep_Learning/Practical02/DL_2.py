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
