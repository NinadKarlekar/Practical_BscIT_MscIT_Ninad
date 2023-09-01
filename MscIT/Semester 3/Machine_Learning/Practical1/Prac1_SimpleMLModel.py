import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Set a random seed for reproducibility
np.random.seed(2)

# Generate random data
x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x

# Visualize the data
plt.figure(figsize=(8, 6))
plt.scatter(x, y)
plt.title("Scatter Plot of Data")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Split the data into training and testing sets
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.3)


plt.scatter(train_x,train_y)
plt.show()

plt.scatter(test_x,test_y)
plt.show()


# Create and visualize a polynomial regression model for training data
degree = 4  # Adjust the polynomial degree as needed
train_model = np.poly1d(np.polyfit(train_x, train_y, degree))
myline = np.linspace(0, 6, 200)

plt.figure(figsize=(8, 6))
plt.scatter(train_x, train_y)
plt.plot(myline, train_model(myline))
plt.title("Polynomial Regression Model (Training Data)")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Calculate and print the R-squared score for the training data
r2_train = r2_score(train_y, train_model(train_x))
print("R-squared score for training data:", r2_train)

# Create and visualize a polynomial regression model for testing data
test_model = np.poly1d(np.polyfit(test_x, test_y, degree))

plt.figure(figsize=(8, 6))
plt.scatter(test_x, test_y)
plt.plot(myline, test_model(myline))
plt.title("Polynomial Regression Model (Testing Data)")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Calculate and print the R-squared score for the testing data
r2_test = r2_score(test_y, test_model(test_x))
print("R-squared score for testing data:", r2_test)

# Make predictions using the model
prediction = test_model(5)
print("Prediction for x = 5:", prediction)
