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
