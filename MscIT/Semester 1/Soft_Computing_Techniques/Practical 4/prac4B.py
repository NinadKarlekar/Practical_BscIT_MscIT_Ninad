# 4B. Write a program for error Backpropagation algorithm.

import numpy as np

X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
Y = np.array(([92], [86], [89]), dtype=float)

X = X / np.amax(X, axis=0)
Y = Y / 100

class NN(object):
    def __init__(self):
        self.inputsize = 2
        self.outputsize = 1
        self.hiddensize = 3
        self.W1 = np.random.randn(self.inputsize, self.hiddensize)
        self.W2 = np.random.randn(self.hiddensize, self.outputsize)

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

obj = NN()
for i in range(2000):
    print("input\n" + str(X))
    print("Actual output\n" + str(Y))
    print("Predicted output\n" + str(obj.forward(X)))
    print("loss\n" + str(np.mean(np.square(Y - obj.forward(X)))))
    obj.train(X, Y)