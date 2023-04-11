# Naive Bayes

# Importing the dataset
dataset <- read.csv("F:\\GitHub\\Practical_BscIT_MscIT_Ninad\\MscIT\\Semester 2\\BigDataAnalytics\\Dataset\\Social_Network_Ads.csv")
dataset <- dataset[3:5]
head(dataset)

# Encoding the target feature as factor
dataset$Purchased <- factor(dataset$Purchased, levels = c(0, 1))

# Splitting the dataset into the Training set and Test set
library(caTools)
set.seed(123)
split <- sample.split(dataset$Purchased, SplitRatio = 0.75)
training_set <- subset(dataset, split == TRUE)
test_set <- subset(dataset, split == FALSE)

# Feature Scaling
training_set[-3] <- scale(training_set[-3])
test_set[-3] <- scale(test_set[-3])

# Fitting Naive Bayes to the Training set 
library(e1071)
classifier <- naiveBayes(x = training_set[-3], y = training_set$Purchased)

# Predicting the Test set results 
y_pred <- predict(classifier, newdata = test_set[-3])

# Making the Confusion Matrix
cm <- table(test_set[, 3], y_pred)
print(cm)
