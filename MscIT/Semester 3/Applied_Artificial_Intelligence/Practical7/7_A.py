### 7a)	AIM: Implement joint probability using Python.
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set()

# Read the dataset
data = pd.read_csv("student-mat.csv")

# Create a joint plot
sns.jointplot(data=data, x="G3", y="absences", kind="kde")

# Display the plot
plt.show()