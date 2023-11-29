# 9A. Build an artificial Neural Network by implementing the Backpropagation algorithm and test the same using appropriate data sets.

import numpy as np

X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
Y = np.array(([92], [86], [89]), dtype=float)

# Normalize input data
X = X / np.amax(X, axis=0)
Y = Y / 100

class NeuralNetwork(object):
    def __init__(self):
        self.input_size = 2
        self.output_size = 1
        self.hidden_size = 3
        self.W1 = np.random.randn(self.input_size, self.hidden_size)
        self.W2 = np.random.randn(self.hidden_size, self.output_size)

    def forward(self, X):
        self.z = np.dot(X, self.W1)
        self.z2 = self.sigmoidal(self.z)
        self.z3 = np.dot(self.z2, self.W2)
        op = self.sigmoidal(self.z3)
        return op

    def sigmoidal(self, s):
        return 1 / (1 + np.exp(-s))

    def sigmoidalprime(self, s):
        return s * (1 - s)

    def backward(self, X, Y, o):
        self.o_error = Y - o
        self.o_delta = self.o_error * self.sigmoidalprime(o)
        self.z2_error = self.o_delta.dot(self.W2.T)
        self.z2_delta = self.z2_error * self.sigmoidalprime(self.z2)
        self.W1 = self.W1 + X.T.dot(self.z2_delta)
        self.W2 = self.W2 + self.z2.T.dot(self.o_delta)

    def train(self, X, Y):
        o = self.forward(X)
        self.backward(X, Y, o)

# Create an instance of the NeuralNetwork class
nn = NeuralNetwork()

# Training loop
for i in range(2000):
    print("Input: " + str(X))
    print("Actual Output: " + str(Y))
    print("Predicted Output: " + str(nn.forward(X)))
    print("Loss: " + str(np.mean(np.square(Y - nn.forward(X)))))
    nn.train(X, Y)