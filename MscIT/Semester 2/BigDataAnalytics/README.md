# Big Data Analytics

M. Sc (Information Technology)
PSIT2P1 Big Data Analytics



## Index

| Sr.No. | Name | README |
| --- | --- | --- |
| [Prac1](/MscIT/Semester%202/BigDataAnalytics/Practical%201/) | 1. K means clustering. [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%202/BigDataAnalytics/Practical%201/K_meansclustering.R) | [Prac1](#prac1) |
| [Prac2A](/MscIT/Semester%202/BigDataAnalytics/Practical%202/)  <br> [Prac2B](/MscIT/Semester%202/BigDataAnalytics/Practical%202/) <br> [Prac2C](/MscIT/Semester%202/BigDataAnalytics/Practical%201/) | 2A.	Logistic Regression.  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%202/BigDataAnalytics/Practical%202/Prac_2A(Logistic%20Regression).R) <br> 2B. MULTIPLE REGRESSION [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%202/BigDataAnalytics/Practical%202/Prac_2B(Multiple%20Regression).R) <br> 2C. Simple Linear Regression(TakeHomeTask) [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%202/BigDataAnalytics/Practical%202/Prac_2C(TakeHomeTask).R)  | [Prac2A](#prac2A) <br> [Prac2B](#Prac2B) <br> [Prac2C](#prac2C) |




******************
---------------------

## Prac1

1. K means clustering .


<details>
<summary>CODE</summary>


```python
# install required packages
install.packages("plyr")
install.packages("ggplot2")
install.packages("cluster")
install.packages("lattice")
install.packages("grid")
install.packages("gridExtra")
# Load the package
library(plyr)
library(ggplot2)
library(cluster)
library(lattice)
library(grid)
library(gridExtra)
# A data frame is a two-dimensional array-like structure in which each column contains values of one variable and each row contains one set of values from each column.
grade_input=as.data.frame(read.csv("F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/BigDataAnalytics/Dataset/grades_km_input.csv"))
kmdata_orig=as.matrix(grade_input[, c ("Student","English","Math","Science")])
kmdata=kmdata_orig[,2:4]
kmdata[1:10,]
# the k-means algorithm is used to identify clusters for k = 1, 2, .. . , 15. For each value of k, the WSS is calculated.
wss=numeric(15)
# the option n start=25 specifies that the k-means algorithm will be repeated 25 times, each starting with k random initial centroids
for(k in 1:15)wss[k]=sum(kmeans(kmdata,centers=k,nstart=25)$withinss)
plot(1:15,wss,type="b",xlab="Number of Clusters",ylab="Within sum of square")
#As can be seen, the WSS is greatly reduced when k increases from one to two. Another substantial reduction in WSS occurs at k = 3. However, the improvement in WSS is fairly linear fork > 3.
km = kmeans(kmdata,3,nstart=25)
km
c( wss[3] , sum(km$withinss))
df=as.data.frame(kmdata_orig[,2:4])
df$cluster=factor(km$cluster)
centers=as.data.frame(km$centers)

g1=ggplot(data=df, aes(x=English, y=Math, color=cluster )) + geom_point() + theme(legend.position="right") + geom_point(data=centers,aes(x=English,y=Math, color=as.factor(c(1,2,3))),size=10, alpha=.3, show.legend =FALSE)

g2=ggplot(data=df, aes(x=English, y=Science, color=cluster )) + geom_point () +geom_point(data=centers,aes(x=English,y=Science, color=as.factor(c(1,2,3))),size=10, alpha=.3, show.legend=FALSE)

g3 = ggplot(data=df, aes(x=Math, y=Science, color=cluster )) + geom_point () + geom_point(data=centers,aes(x=Math,y=Science, color=as.factor(c(1,2,3))),size=10, alpha=.3, show.legend=FALSE)
tmp=ggplot_gtable(ggplot_build(g1))

grid.arrange(arrangeGrob(g1 + theme(legend.position="none"),g2 + theme(legend.position="none"),g3 + theme(legend.position="none"),top ="High School Student Cluster Analysis" ,ncol=1))
```

</details>



<details>
<summary>OUTPUT</summary>

<img src="https://user-images.githubusercontent.com/88243315/221430084-6842ec4f-3e93-423e-beaf-45010a8a8112.png" width="600px"  alt ="BDA_prac1_1">

<img src="https://user-images.githubusercontent.com/88243315/221430085-9a1d4975-1212-410e-8813-963041c0c887.png" width="600px"  alt ="BDA_prac1_2">



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





























<!-- 

## Index

| Sr.No. | Name | ReadME |
| --- | --- | --- |
| [Prac1A-i](/MscIT/Semester%202/BigDataAnalytics/) <br> [Prac1A-ii](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%201/)| 1A-i. Design a **simple linear neural network** model. <br> 1A-ii. Calculate the **output** of **neural net** for given data. | [Prac1A-i](#prac1a-i) <br>  [Prac1A-ii](#prac1a-ii) | 

*************************
***********************

<BR>

## Prac1A-i

- 1A-i. Heading .





```python

```

<details>
<summary>OUTPUT</summary>

![]()
![]()



</details>


[🔝](#index)

**************


**************

### [Go To Top](#soft-computing-techniques)
 -->
