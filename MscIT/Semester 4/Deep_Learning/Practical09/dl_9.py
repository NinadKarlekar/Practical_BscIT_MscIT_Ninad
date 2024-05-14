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