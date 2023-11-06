## AAI_prac8A_clustering
### AIM: Write an application to implement clustering algorithm.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering

# Read the customer data from a CSV file
customer_data = pd.read_csv("Mall_Customers.csv")

# Display the shape and the first few rows of the data
print(customer_data.shape)
customer_data.head()

# Extract the relevant columns from the data
data = customer_data.iloc[:, 3:5].values

# Create a dendrogram plot
plt.figure(figsize=(10, 7))
plt.title("Customer Dendrograms")
dend = shc.dendrogram(shc.linkage(data, method="ward"))

# Perform hierarchical clustering
cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
cluster_labels = cluster.fit_predict(data)

# Create a scatter plot to visualize the clusters
plt.figure(figsize=(10, 7))
plt.scatter(data[:, 0], data[:, 1], c=cluster_labels, cmap='rainbow')
plt.show()