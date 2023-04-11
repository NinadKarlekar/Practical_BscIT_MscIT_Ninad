# K-Means Clustering

# Importing the dataset
dataset <- read.csv('F:\\GitHub\\Practical_BscIT_MscIT_Ninad\\MscIT\\Semester 2\\BigDataAnalytics\\Dataset\\Mall_Customers.csv')
head(dataset)
dataset <- dataset[4:5]
head(dataset)

# Compute the Within Cluster Sum of Squares (WCSS) for different number of clusters
wcss <- vector()
for (i in 1:10) {
  wcss[i] <- sum(kmeans(dataset, i)$withinss)
}

# Plot the WCSS values
plot(1:10, wcss, type = 'b', main = paste('The Elbow Method'),
    xlab = 'Number of clusters', ylab = 'WSS')

# Fit K-Means to the dataset with 5 clusters
kmeans_model <- kmeans(x = dataset, centers = 5)
y_kmeans <- kmeans_model$cluster

# Visualize the clusters
library("cluster")
clusplot(dataset, y_kmeans, lines = 0, shade = TRUE, color = TRUE, labels = 2,
         main = paste('Clusters of customers'),
         xlab = "Annual Income",
         ylab = "Spending Score")
