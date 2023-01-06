# Google colab
#8.Write a program for computing different correlation
#C.	No/Weak Correlation:
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
x = np.random.randint(0, 50, 1000)
y = np.random.randint(0, 50, 1000)
np.corrcoef(x, y)
plt.scatter(x, y)
plt.show()

print("Practical 8-C")