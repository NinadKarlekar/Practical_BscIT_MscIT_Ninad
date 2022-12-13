# Google colab
#8.Write a program for computing different correlation
#B.	Negative Correlation: 
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
# 1000 random integers between 0 and 50
x = np.random.randint(0, 50, 1000)
# Negative Correlation with some noise
y = 100 - x + np.random.normal(0, 5, 1000)
np.corrcoef(x, y)
plt.scatter(x, y)
plt.show()
print("\nNinad Karlekar 22306A1012")
print("Practical 8-B")

