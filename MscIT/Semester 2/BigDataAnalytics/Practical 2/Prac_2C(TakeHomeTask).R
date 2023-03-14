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
