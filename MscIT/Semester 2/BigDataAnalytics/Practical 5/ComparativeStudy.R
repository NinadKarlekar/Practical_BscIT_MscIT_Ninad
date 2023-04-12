# Install required packages
install.packages('rpart')
install.packages('rpart.plot')
install.packages('gmodels')
install.packages('e1071')

# Load required libraries
library(rpart)
library(rpart.plot)
library(gmodels)
library(e1071)

# Load iris dataset
data(iris)
summary(iris)

# Normalize the continuous variables before performing any analysis on the dataset
temp <- as.data.frame(scale(iris[, 1:4]))
temp$Species <- iris$Species  # levels: setosa versicolor virginica
summary(temp)

# Split the dataset into the Training set and Test set
install.packages('caTools')
library(caTools)
set.seed(123)
split <- sample.split(temp$Species, SplitRatio = 0.75)
train <- subset(temp, split == TRUE)
test <- subset(temp, split == FALSE)
nrow(train)
nrow(test)

# 1. Decision Trees
dt_classifier <- rpart(formula = Species ~ ., data = train)

# Predict the Test set results for Decision Trees
dt_y_pred <- predict(dt_classifier, newdata = test, type = 'class')
print(dt_y_pred)

# Make the Confusion Matrix for Decision Tree
cm <- table(test$Species, dt_y_pred)
print(cm)

# Calculate the accuracy of DT model
DTaccu <- ((12+9+11)/nrow(test))*100  # true positive numbers of 3*3 confusion matrix
DTaccu

# 2. k-Nearest Neighbours
install.packages('class')
library(class)

cl <- train$Species
set.seed(1234)
knn_y_pred <- knn(train[, 1:4], test[, 1:4], cl, k = 5)

# Make the Confusion Matrix for k-Nearest Neighbours
cm <- table(test$Species, knn_y_pred)
print(cm)

# Calculate the accuracy of KNN model
KNNaccu <- ((12+11+11)/nrow(test))*100  # true positive numbers of 3*3 confusion matrix
KNNaccu

# 3. Support Vector Machine(SVM)
svmclassifier <- svm(Species ~ ., data = train)
svm_y_pred <- predict(svmclassifier, newdata = test) 

cm <- table(test$Species, svm_y_pred) 
print(cm) 

# Calculate the accuracy of SVM model 
SVMaccu <- ((12+11+11)/nrow(test))*100 
SVMaccu

# Comparison of the accuracy of different models on testing dataset
which(dt_y_pred != knn_y_pred) 
which(dt_y_pred != svm_y_pred) 

# Compare SVM vs kNN
which(svm_y_pred != knn_y_pred) # both are equal 

# Create a dataframe of accuracy percentages for each model
models <- data.frame(Technique = c("Decision Tree", "KNN", "SVM"), 
                     Accuracy_Percentage = c(DTaccu, KNNaccu, SVMaccu))
models 
    
print("Hence KNN and SVM are better than decision tree")