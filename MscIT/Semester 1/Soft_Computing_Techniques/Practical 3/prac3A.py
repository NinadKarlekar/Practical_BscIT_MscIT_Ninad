# 3A. Write a program to implement Hebb’s rule.

import numpy as np

x1 = np.array([1, -1, -1, 1, -1, -1, 1, 1, 1])
x2 = np.array([1, -1, 1, 1, -1, 1, 1, 1, 1])
b = 0

y = np.array([1, -1])
wtold = np.zeros((9,))
wtnew = np.zeros((9,))

wtnew = wtnew.astype(int)
wtold = wtold.astype(int)

bais = 0
print("First input with target = 1")
for i in range(0, 9):
    wtnew[i] = wtold[i] + x1[i] * y[0]
wtold = wtnew
b = b + y[0]
print("New wt=", wtnew)
print("Bias value ", b)

print("**********************************")

print("second input with target = 1")
for i in range(0, 9):
    wtnew[i] = wtold[i] + x2[i] * y[1]
wtold = wtnew
b = b + y[1]
print("New wt=", wtnew)
print("Bias value= ", b)