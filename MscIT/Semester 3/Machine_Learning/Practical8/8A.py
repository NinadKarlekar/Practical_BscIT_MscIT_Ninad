## Aim: For a given set of training data examples stored in a .CSV file implement Least Square Regression algorithm. 

# Making imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (12.0, 9.0)

np.random.seed(42)
X = np.linspace(0, 10, 100)
Y = 2.5 * X + 1.5 + np.random.normal(0, 2, 100)
data = pd.DataFrame({"X": X, "Y": Y})
plt.scatter(X, Y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Synthetic Data for Least Square Regression")
plt.show()

import numpy as np

# Assuming X and Y are your data arrays
X_mean = np.mean(X)
Y_mean = np.mean(Y)

num = 0
den = 0

for i in range(len(X)):
    num += (X[i] - X_mean) * (Y[i] - Y_mean)
    den += (X[i] - X_mean) ** 2

m = num / den
c = Y_mean - m * X_mean

print(m, c)

# Making predictions

Y_pred = m * X + c
plt.scatter(X, Y)  # actual
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color="red")  # prediction
plt.show()