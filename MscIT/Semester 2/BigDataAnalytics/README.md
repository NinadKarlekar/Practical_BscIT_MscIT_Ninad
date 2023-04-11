# Big Data Analytics

M. Sc (Information Technology)
PSIT2P1 Big Data Analytics



## Index

| Sr.No. | Name | README | DOWNLOAD |
| --- | --- | --- | --- |
| [Prac1](/MscIT/Semester%202/BigDataAnalytics/Practical%201/) | 1. K means clustering. | [Prac1](#prac1) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%202/BigDataAnalytics/Practical%201/K_meansclustering.R) |
| [Prac2A](/MscIT/Semester%202/BigDataAnalytics/Practical%202/)  <br> [Prac2B](/MscIT/Semester%202/BigDataAnalytics/Practical%202/) <br> [Prac2C](/MscIT/Semester%202/BigDataAnalytics/Practical%201/) | 2A.	Logistic Regression.   <br> 2B. MULTIPLE REGRESSION  <br> 2C. Simple Linear Regression(TakeHomeTask)   | [Prac2A](#prac2A) <br> [Prac2B](#Prac2B) <br> [Prac2C](#prac2C) | [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%202/BigDataAnalytics/Practical%202/Prac_2A(Logistic%20Regression).R) <br> [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%202/BigDataAnalytics/Practical%202/Prac_2B(Multiple%20Regression).R) <br> [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%202/BigDataAnalytics/Practical%202/Prac_2C(TakeHomeTask).R)  |




******************
---------------------

## Prac1A

1. K means clustering .


<details>
<summary>CODE</summary>


```python
# K-Means Clustering

# Importing the dataset
dataset <- read.csv('D:\\nk\\Mall_Customers.csv')
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

```

</details>



<details>
<summary>OUTPUT</summary>

<img src="https://user-images.githubusercontent.com/88243315/231265010-57e36a7d-cc69-476c-9781-5bccd8dffb50.png" width="600px"  alt ="BDA_prac1A-1">

<img src="https://user-images.githubusercontent.com/88243315/231265015-5454c092-3f2a-4dec-93c2-0fac7202a80b.png" width="600px"  alt ="BDA_prac1A-2">

<img src="https://user-images.githubusercontent.com/88243315/231265016-d81dcf2e-8649-4595-8fa4-1a9404fe8a4b.png" width="600px"  alt ="BDA_prac1A-3">

<img src="https://user-images.githubusercontent.com/88243315/231265019-b537fa3b-7b8e-4c49-b545-992205fee88c.png" width="600px"  alt ="BDA_prac1A-4">



</details>


[🔝](#index)

**************

## Prac1B

1. AprioriAlgorithm .


<details>
<summary>CODE</summary>


```python
install.packages("arules")
install.packages("arulesViz")
install.packages("RColorBrewer")
# Loading Libraries
library(arules)
library(arulesViz)
library(RColorBrewer)
# import dataset
data(Groceries)
Groceries
summary(Groceries)
class(Groceries)
# using apriori() function
rules = apriori(Groceries, parameter = list(supp = 0.02, conf = 0.2))
summary (rules)
# using inspect() function
inspect(rules[1:10])
# using itemFrequencyPlot() function
arules::itemFrequencyPlot(Groceries, topN = 20,
                          col = brewer.pal(8, 'Pastel2'),
                          main = 'Relative Item Frequency Plot',
                          type = "relative",
                          ylab = "Item Frequency (Relative)")
itemsets = apriori(Groceries, parameter = list(minlen=2, maxlen=2,support=0.02, target="frequent itemsets"))
summary(itemsets)
# using inspect() function
inspect(itemsets[1:10])
itemsets_3 = apriori(Groceries, parameter = list(minlen=3, maxlen=3,support=0.02, target="frequent itemsets"))
summary(itemsets_3)
# using inspect() function
inspect(itemsets_3)

```

</details>



<details>
<summary>OUTPUT</summary>

<img src="https://user-images.githubusercontent.com/88243315/231265025-82f41051-4b45-4a08-b6bd-4ae7924b02d3.png" width="600px"  alt ="BDA_prac1B-1">

<img src="https://user-images.githubusercontent.com/88243315/231265027-fe068c4b-5735-4916-a374-3b72add55432.png" width="600px"  alt ="BDA_prac1B-2">

<img src="https://user-images.githubusercontent.com/88243315/231265029-a472afd7-d35e-4bbd-a998-0a363fa8199f.png" width="600px"  alt ="BDA_prac1B-3">

<img src="https://user-images.githubusercontent.com/88243315/231265034-723b6011-591c-442d-b835-c8429908588e.png" width="600px"  alt ="BDA_prac1B-4">

<img src="https://user-images.githubusercontent.com/88243315/231265037-4dd731f5-d6f3-4361-922d-48d8fbf939cd.png" width="600px"  alt ="BDA_prac1B-5">



</details>


[🔝](#index)

**************


## Prac2A

1. Logistic Regression. 


<details>
<summary>CODE</summary>


```python
college <- read.csv("https://raw.githubusercontent.com/ropensci/datapack/main/inst/extdata/pkg-example/binary.csv") 
head(college) 
nrow(college) 

install.packages("caTools") 
library(caTools) 
split <- sample.split(college, SplitRatio = 0.75) 
split 

training_reg <- subset(college, split == "TRUE") 
test_reg <- subset(college, split == "FALSE") 
fit_logistic_model <- glm(admit ~ .,data = training_reg,family = "binomial") 

coef(fit_logistic_model)["gre"] 
coef(fit_logistic_model)["gpa"] 
coef(fit_logistic_model)["rank"]  
predict_reg <- predict(fit_logistic_model,test_reg, type = "response")
predict_reg 

cdplot(as.factor(admit)~ gpa, data=college) 
cdplot(as.factor(admit)~ gre, data=college) 
cdplot(as.factor(admit)~ rank, data=college) 
predict_reg <- ifelse(predict_reg >0.5,1,0) 
predict_reg 
table(test_reg$admit, predict_reg)

```

</details>

<details>
<summary>OUTPUT</summary>

<img src="https://user-images.githubusercontent.com/88243315/225115544-0029ab08-c562-41f4-83e7-ae0d4fef2cb2.png" width="600px"  alt ="BDA_prac2A_1">

<img src="https://user-images.githubusercontent.com/88243315/225115555-4436bd5d-43ab-4ac7-90c6-035fd327eb6a.png" width="420px"  alt ="BDA_prac2A_2">

<img src="https://user-images.githubusercontent.com/88243315/225115557-869f0651-536f-42f6-961a-93ea918978dd.png" width="420px"  alt ="BDA_prac2A_3">

<img src="https://user-images.githubusercontent.com/88243315/225115560-0aa345a5-7d87-4de6-8d61-aaf5a2806691.png" width="420px"  alt ="BDA_prac2A_4">



</details>


[🔝](#index)

**************

## Prac2B

2. MULTIPLE REGRESSION. 


<details>
<summary>CODE</summary>


```python
college <- read.csv("https://raw.githubusercontent.com/csquared/udacity-dlnd/master/nn/binary.csv") 

head(college)
nrow(college)

install.packages("caTools")
library(caTools)
split <- sample.split(college, SplitRatio = 0.75)
split 

training_reg <- subset(college, split == "TRUE")
test_reg <- subset(college, split == "FALSE")

fit_MRegressor_model <- lm(formula = admit ~ gre+gpa+rank, data = training_reg)

predict_reg <- predict(fit_MRegressor_model,newdata = test_reg)
predict_reg 

cdplot(as.factor(admit)~ gpa, data=college)
cdplot(as.factor(admit)~ gre, data=college)
cdplot(as.factor(admit)~ rank, data=college) 

predict_reg <- ifelse(predict_reg >0.5,1,0)
predict_reg
table(test_reg$admit, predict_reg)

```

</details>

<details>
<summary>OUTPUT</summary>

<img src="https://user-images.githubusercontent.com/88243315/225115562-3e4011d5-2b88-47bb-b5c4-2a5a312f2404.png" width="600px"  alt ="BDA_prac2B_1">

<img src="https://user-images.githubusercontent.com/88243315/225115563-3b6b3369-c434-4c71-81bd-32348cf886f8.png" width="420px"  alt ="BDA_prac2B_2">

<img src="https://user-images.githubusercontent.com/88243315/225115567-d66c20f3-5973-4d2a-97b2-7ede8c098d13.png" width="420px"  alt ="BDA_prac2B_3">

<img src="https://user-images.githubusercontent.com/88243315/225115569-2a57a16a-cb49-4eee-a8f2-4dc811506b44.png" width="420px"  alt ="BDA_prac2B_4">



</details>


[🔝](#index)

---------------------------

## Prac2C

3. Simple Linear Regression(TakeHomeTask). 


<details>
<summary>CODE</summary>


```python
# Load the dataset
data <- read.csv("https://raw.githubusercontent.com/csquared/udacity-dlnd/master/nn/binary.csv")

# Plot the relationship between gre and chance of admission
plot(data$gre, data$admit, xlab = "gre Score", ylab = "Chance of Admission", main = "Take Home Task prac 2" )


# Fit a simple linear regression model
model <- lm(admit ~ gre, data = data)

# Print the summary of the model
summary(model)

# Plot the regression line
abline(model, col = "red")

# Make a prediction using the model
new_data <- data.frame(gre = 3.5)
prediction <- predict(model, newdata = new_data)
prediction

```

</details>

<details>
<summary>OUTPUT</summary>

<img src="https://user-images.githubusercontent.com/88243315/225115574-5ded86c6-17cc-41a5-85d8-4bd1682c9b99.png" width="400px"  alt ="BDA_prac2C_1">

<img src="https://user-images.githubusercontent.com/88243315/225115577-6f557fa3-2d8c-473a-870f-a64f0ddfd5f2.png" width="200px"  alt ="BDA_prac2C_2">

<img src="https://user-images.githubusercontent.com/88243315/225115581-b92e135d-c1f4-483d-b1a0-e59b61c6ec60.png" width="600px"  alt ="BDA_prac2C_3">



</details>


[🔝](#index)


*******************************

## Prac3A

1. Decision Tree Classification. 


<details>
<summary>CODE</summary>


```python
# Decision Tree Classification
# Importing the dataset
dataset = read.csv('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/BigDataAnalytics/Dataset/Social_Network_Ads.csv')
dataset = dataset[3:5]
print(dataset)
# Encoding the target feature as factor
dataset$Purchased = factor(dataset$Purchased, levels = c(0, 1))
# Splitting the dataset into the Training set and Test set
install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.75)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)# Feature Scaling
training_set[-3] = scale(training_set[-3])
test_set[-3] = scale(test_set[-3])
# Fitting Decision Tree Classification to the Training set
install.packages('rpart')
library(rpart)
classifier = rpart(formula = Purchased ~ .,data = training_set)
# Predicting the Test set results
y_pred = predict(classifier, newdata = test_set[-3], type = 'class')
# Making the Confusion Matrix
cm = table(test_set[, 3], y_pred)
# Visualising the Training set results
#install.packages("ElemStatLearn")
library(ElemStatLearn)
set = training_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('Age', 'EstimatedSalary')
y_grid = predict(classifier, newdata = grid_set, type = 'class')
plot(set[, -3],
     main = 'Decision Tree Classification (Training set)',
     xlab = 'Age', ylab = 'Estimated Salary',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))
# Visualising the Test set results
library(ElemStatLearn)
set = test_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('Age', 'EstimatedSalary')
y_grid = predict(classifier, newdata = grid_set, type = 'class')
plot(set[, -3], main = 'Decision Tree Classification (Test set)',
     xlab = 'Age', ylab = 'Estimated Salary',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))
# Plotting the tree
plot(classifier)
text(classifier)

```

</details>

<details>
<summary>OUTPUT</summary>

<img src="https://user-images.githubusercontent.com/88243315/231261698-45c2b0cd-581c-4d89-ac08-1dfbee2e71c6.png" width="600px"  alt ="BDA_prac3_1">

</details>


[🔝](#index)

**************

## Prac3B

2. Support vector machine. 


<details>
<summary>CODE</summary>


```python
# Support vector machine
# Importing the dataset
dataset = read.csv('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/BigDataAnalytics/Dataset/Social_Network_Ads.csv')
dataset = dataset[3:5]
print(dataset)
# Encoding the target feature as factor
dataset$Purchased = factor(dataset$Purchased, levels = c(0, 1))
# Splitting the dataset into the Training set and Test set
install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.75)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)# Feature Scaling
training_set[-3] = scale(training_set[-3])
test_set[-3] = scale(test_set[-3])
# Fitting SVM
install.packages('e1071')
library(e1071)
classifier = svm(formula = Purchased ~ .,data = training_set,type = 'C-classification',kernel = 'linear')

print(classifier)


# Predicting the Test set results
y_pred = predict(classifier, newdata = test_set[-3])
# Making the Confusion Matrix
cm = table(test_set[, 3], y_pred)
# Visualising the Training set results
#install.packages("ElemStatLearn")
library(ElemStatLearn)
set = training_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('Age', 'EstimatedSalary')
y_grid = predict(classifier, newdata = grid_set, type = 'class')
plot(set[, -3],
     main = 'SVM (Training set)',
     xlab = 'Age', ylab = 'Estimated Salary',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))
# Visualising the Test set results
library(ElemStatLearn)
set = test_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('Age', 'EstimatedSalary')
y_grid = predict(classifier, newdata = grid_set, type = 'class')
plot(set[, -3], main = 'Decision Tree Classification (Test set)',
     xlab = 'Age', ylab = 'Estimated Salary',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))
# Plotting the tree
#plot(classifier)
#text(classifier)
```

</details>

<details>
<summary>OUTPUT</summary>

<img src="https://user-images.githubusercontent.com/88243315/231261690-d4a46d60-47ba-43c3-93b1-52ca701dffde.png" width="600px"  alt ="BDA_prac3_2">

</details>


[🔝](#index)

**************


## Prac4A

4. 1. Naive Bayes. 


<details>
<summary>CODE</summary>


```python
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


```

</details>

<details>
<summary>OUTPUT</summary>

<img src="https://user-images.githubusercontent.com/88243315/231260888-5f8caeba-6f14-4e9f-91b1-0de4b13dd6a0.png" width="250px"  alt ="BDA_prac4_1-1">
<img src="https://user-images.githubusercontent.com/88243315/231260892-1eb45f54-eab9-471d-94ea-55cb7836842b.png" width="250px"  alt ="BDA_prac4_1-2">

</details>


[🔝](#index)

**************


## Prac4B

2. TextAnalysis. 


<details>
<summary>CODE</summary>


```python
# Read in the data
dataset_original <- read.delim("F:\\GitHub\\Practical_BscIT_MscIT_Ninad\\MscIT\\Semester 2\\BigDataAnalytics\\Dataset\\Restaurant_Reviews.tsv", quote = "", stringsAsFactors = FALSE)
head(dataset_original)
# Install and load required packages
install.packages('tm')
install.packages('SnowballC')
install.packages('randomForest')
library(tm)
library(SnowballC)
library(caTools)
library(randomForest)

# Create a corpus
corpus <- VCorpus(VectorSource(dataset_original$Review))
corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeWords, stopwords())
corpus <- tm_map(corpus, stemDocument)
corpus <- tm_map(corpus, stripWhitespace)

# Create a document term matrix
dtm <- DocumentTermMatrix(corpus)
dtm <- removeSparseTerms(dtm, 0.999)

# Convert the dtm to a data frame
dataset <- as.data.frame(as.matrix(dtm))
dataset$Liked <- dataset_original$Liked
dataset$Liked <- factor(dataset$Liked, levels = c(0,1))

# Split the data into training and test sets
set.seed(123)
split <- sample.split(dataset$Liked, SplitRatio = 0.8)
training_set <- subset(dataset, split == TRUE)
test_set <- subset(dataset, split == FALSE)

# Train a random forest classifier
classifier <- randomForest(x = training_set[-692], y = training_set$Liked, ntree = 10)

# Make predictions on the test set and create a confusion matrix
y_pred <- predict(classifier, newdata = test_set[-692])
cm <- table(test_set[,692], y_pred)
print(cm)
```

</details>

<details>
<summary>OUTPUT</summary>

<img src="https://user-images.githubusercontent.com/88243315/231260894-552fcdd2-9c6e-4125-8d02-48431d0f15ba.png" width="300px"  alt ="BDA_prac4_2">

</details>


[🔝](#index)

**************




















<!-- 

## Index

| Sr.No. | Name | ReadME |
| --- | --- | --- |
| [Prac1A-i](/MscIT/Semester%202/BigDataAnalytics/) <br> [Prac1A-ii](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%201/)| 1A-i. Design a **simple linear neural network** model. <br> 1A-ii. Calculate the **output** of **neural net** for given data. | [Prac1A-i](#prac1a-i) <br>  [Prac1A-ii](#prac1a-ii) | 

*************************
***********************

<BR>

---------------------------

## Prac2C

3. Simple Linear Regression(TakeHomeTask). 


<details>
<summary>CODE</summary>


```python


```

</details>

<details>
<summary>OUTPUT</summary>

<img src="" width="600px"  alt ="">

</details>


[🔝](#index)

**************


**************

### [Go To Top](#soft-computing-techniques)
 -->
