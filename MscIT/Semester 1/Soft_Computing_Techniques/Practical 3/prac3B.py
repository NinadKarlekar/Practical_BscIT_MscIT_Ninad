# 3B. Write a program to implement of delta rule.

print("b) Aim: - Write a program to implement delta rule")
import numpy as np
import time

np.set_printoptions(precision=2)
x = np.zeros((3,))
weights = np.zeros((3,))
desired = np.zeros((3,))
actual = np.zeros((3,))
for i in range(0, 3):
    x[i] = float(input("Intial inputs: "))
for i in range(0, 3):
    weights[i] = float(input("Intial weights: "))
for i in range(0, 3):
    desired[i] = float(input("Desired output: "))
a = float(input("Enter learning rate: "))
actual = x * weights
print("Acrual ", actual)
print("Desired ", desired)
while True:
    if np.array_equal(desired, actual):
        break
    else:
        for i in range(0, 3):
            weights[i] = weights[i] + a * (desired[i] - actual[i])
            actual = x * weights
print("Weights ", weights)
print("Actual ", actual)
print("Desired ", desired)
print("*" * 30)
print("Final output")
print("Corrected weights", weights)
print("Actual", actual)
print("Desired ", desired)

