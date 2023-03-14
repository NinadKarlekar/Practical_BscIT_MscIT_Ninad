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
