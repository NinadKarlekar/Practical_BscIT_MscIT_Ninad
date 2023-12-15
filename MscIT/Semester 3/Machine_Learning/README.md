# Machine Learning

M. Sc (Information Technology)
Machine Learning



## Index

| Sr.No. | Name | README | DOWNLOAD |
| --- | --- | --- | --- |
| [Prac1](/MscIT/Semester%203/Machine_Learning/Practical1/) | 1. Design a **simple machine learning model** to train the training instances and test the same. | [Prac1](#prac1) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%203/Machine_Learning/Practical1/1_A.py)  |
| [Prac2](/MscIT/Semester%203/Machine_Learning/Practical2/) | 2. Implement and demonstrate the **find-s algorithm** for finding the most specific. | [Prac2](#prac2) |  |
| [Prac3](/MscIT/Semester%203/Machine_Learning/Practical3/) | 3. **Support Vector Machine Algorithm** for Multiclass classification using Iris.CSV & wine dataset from sklearn | [Prac3](#prac3) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%203/Machine_Learning/Practical3/3A.py)  |
| [Prac4](/MscIT/Semester%203/Machine_Learning/Practical4/) | 4. For a given set of training data examples stored in a .csv file, implement and demonstrate the **candidate-elimination algorithm** to output a description of the set of all hypotheses consistent with the training examples. | [Prac4](#prac4) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%203/Machine_Learning/Practical4/4.py) |
| [Prac5](/MscIT/Semester%203/Machine_Learning/Practical5/) | 5. Write a program to implement the **Naïve Bayesian classifier** for a sample training data set stored as a .csv file. Compute the accuracy of the classifier, considering few test data sets. | [Prac5](#prac5) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%203/Machine_Learning/Practical5/5.py)  |
| [Prac6](/MscIT/Semester%203/Machine_Learning/Practical6/) | 6. Decision Tree classifier & Random Forest Classifier. | [Prac6](#prac6) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%203/Machine_Learning/Practical6/6.py)  |
| [Prac7](/MscIT/Semester%203/Machine_Learning/Practical7/) | 7. Data loading, feature scoring and ranking, **feature selection (principal component analysis)**. | [Prac7](#prac7) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%203/Machine_Learning/Practical7/7.py)  |
| [Prac8A](/MscIT/Semester%203/Machine_Learning/Practical8/) <br> [Prac8B](/MscIT/Semester%203/Machine_Learning/Practical8/) | 8A. For a given set of training data examples stored in a CSV. File implement **Least Square Regression Algorithm**. <br> 8B. For a given set of training data examples stored in a .CSV file implement **Logistic Regression algorithm** | [Prac8A](#prac8) <br> [Prac8B](#prac8) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%203/Machine_Learning/Practical8/8_A.py) <br> [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%203/Machine_Learning/Practical8/8_B.py) |
| [Prac9A](/MscIT/Semester%203/Machine_Learning/Practical9/) <br> [Prac9B](/MscIT/Semester%203/Machine_Learning/Practical9/) | 9A. Build an artificial Neural Network by implementing the **Backpropagation algorithm** and test the same using appropriate data sets. <br> 9B. Perform **Text pre-processing, Text clustering, classification with Prediction, Test Score and Confusion Matrix**. | [Prac9A](#prac9) <br> [Prac9B](#prac9) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%203/Machine_Learning/Practical9/9_A.py) <br> [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%203/Machine_Learning/Practical9/9_B.py) |
| [Prac10A](/MscIT/Semester%203/Machine_Learning/Practical10/) <br> [Prac10B](/MscIT/Semester%203/Machine_Learning/Practical10/) | 10A. Implement the different **Distance methods** (Euclidean) with Prediction, Test Score and Confusion Matrix. <br> 10B. Implement the classification model using **K means clustering** with Prediction, Test Score and Confusion Matrix. | [Prac10A](#prac10) <br> [Prac10B](#prac10) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%203/Machine_Learning/Practical10/10_A.py) <br> [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%203/Machine_Learning/Practical10/10_B.py) |

******************
---------------------

## Prac1

1. Design a **simple machine learning model** to train the training instances and test the same.


<details>
<summary>CODE</summary>


```python

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


```

</details>

******************************************************

## Prac2

2A. Implement and demonstrate the find-s algorithm for finding the most specific.


<details>
<summary>CODE</summary>


```python

import csv

num_attributes = 6
a = []

print("\n The Given Training Dataset \n")
with open("Book1.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    for row in reader:
        if count == 0:
            print(row)
            count += 1
        else:
            a.append(row)
            print(row)
            count += 1


# # URL of the CSV file
# csv_url = 'https://raw.githubusercontent.com/misbahulard/Machine-Learning/master/enjoysport.csv'

# # Read the CSV file into a pandas DataFrame
# df = pd.read_csv(csv_url)

# # Display the given training dataset
# print("\nThe Given Training Dataset \n")
# print(df)

print("\n The initial value of hypothesis: ")
hypothesis = ["0"] * num_attributes
print(hypothesis)

for j in range(0, num_attributes):
    hypothesis[j] = a[0][j]
    print(hypothesis)

print("\n find S:finding a Maximally specific Hypothesis\n")
for i in range(0, len(a)):
    if a[i][num_attributes] == "Yes":
        for j in range(0, num_attributes):
            if a[i][j] != hypothesis[j]:
                hypothesis[j] = "?"
            else:
                hypothesis[j] = a[i][j]
    print("for training example no :{0} the hypothesis is".format(i), hypothesis)

print(hypothesis)



```

</details>

<br>

2B. Implement and demonstrate the find-s algorithm for finding the most specific.


<details>
<summary>CODE</summary>


```python

import csv


a = []


with open("book2.csv", "r") as csvfile:
    next(csvfile)
    for row in csv.reader(csvfile):
        a.append(row)

for x in a:
    print(x)

print("\nThe total number of training instances are : ", len(a))

num_attribute = len(a[0]) - 1
print("\nThe initial hypothesis is : ")
hypothesis = ["0"] * num_attribute
print(hypothesis)

for i in range(0, len(a)):
    if a[i][num_attribute] == "yes":
        print("\nInstance ", i + 1, "is", a[i], " and is Positive Instance")

        for j in range(0, num_attribute):
            if hypothesis[j] == "0" or hypothesis[j] == a[i][j]:
                hypothesis[j] = a[i][j]

            else:
                hypothesis[j] = "?"

        print(
            "The hypothesis for the training instance", i + 1, " is: ", hypothesis, "\n"
        )

    if a[i][num_attribute] == "no":
        print(
            "\nInstance ", i + 1, "is", a[i], " and is Negative Instance Hence Ignored"
        )

        print(
            "The hypothesis for the training instance", i + 1, " is: ", hypothesis, "\n"
        )

print("\nThe Maximally specific hypothesis for the training instance is ", hypothesis)

```

</details>

******************************************************

## Prac3

3. Support Vector Machine Algorithm for Multiclass classification using Iris.CSV & wine dataset from sklearn.

    ### iris.csv

    <details>
    <summary>CODE</summary>


    ```python

    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    from sklearn import svm, datasets
    import sklearn.model_selection as model_selection
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import f1_score
    from sklearn.svm import SVC
    from sklearn.metrics import confusion_matrix

    iris = datasets.load_iris()
    #print(iris.data)
    x = iris.data[:, :2]
    y = iris.target
    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, train_size=0.80, test_size=0.20, random_state=101)

    x_train.shape, x_test.shape, y_train.shape, y_test.shape

    rbf = svm.SVC(kernel='rbf', gamma=0.5, C=0.1).fit(x_train, y_train)
    poly = svm.SVC(kernel='poly', degree=3, C=1).fit(x_train, y_train)
    poly_pred = poly.predict(x_test)
    rbf_pred = rbf.predict(x_test)

    poly_accuracy = accuracy_score(y_test, poly_pred)
    poly_f1 = f1_score(y_test, poly_pred, average='weighted')
    print('Accuracy (Polynomial Kernel): ', "%.2f" % (poly_accuracy*100))
    print('F1 (Polynomial Kernel): ', "%.2f" % (poly_f1*100))
    rbf_accuracy = accuracy_score(y_test, rbf_pred)
    rbf_f1 = f1_score(y_test, rbf_pred, average='weighted')
    print('Accuracy (RBF Kernel): ', "%.2f" % (rbf_accuracy*100))
    print('F1 (RBF Kernel): ', "%.2f" % (rbf_f1*100))

    # Calculate the confusion matrix
    cm = confusion_matrix(y_test, poly_pred)

    # Display the confusion matrix
    cm_df = pd.DataFrame(
        cm,
        index=["SETOSA", "VERSICOLR", "VIRGINICA"],
        columns=["SETOSA", "VERSICOLR", "VIRGINICA"],
    )

    plt.figure(figsize=(5, 4))
    sns.heatmap(cm_df, annot=True)
    plt.title("Confusion Matrix")
    plt.ylabel("Actual Values")
    plt.xlabel("Predicted Values")
    plt.show()


    ```

    </details>

    <br>

    ### wine.csv
    
    <details>
    <summary>CODE</summary>


    ```python

    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    from sklearn import svm, datasets
    import sklearn.model_selection as model_selection
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import f1_score
    from sklearn.svm import SVC
    from sklearn.metrics import confusion_matrix

    wine = datasets.load_wine()

    X = wine.data[:, :2]
    y = wine.target
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        X, y, train_size=0.80, test_size=0.20, random_state=101
    )

    X_train.shape, X_test.shape, y_train.shape, y_test.shape

    rbf = svm.SVC(kernel="rbf", gamma=0.5, C=0.1).fit(X_train, y_train)
    poly = svm.SVC(kernel="poly", degree=3, C=1).fit(X_train, y_train)
    poly_pred = poly.predict(X_test)
    rbf_pred = rbf.predict(X_test)

    poly_accuracy = accuracy_score(y_test, poly_pred)
    poly_f1 = f1_score(y_test, poly_pred, average="weighted")
    print("Accuracy (Polynomial Kernel): ", "%.2f" % (poly_accuracy * 100))
    print("F1 (Polynomial Kernel): ", "%.2f" % (poly_f1 * 100))

    rbf_accuracy = accuracy_score(y_test, rbf_pred)
    rbf_f1 = f1_score(y_test, rbf_pred, average="weighted")
    print("Accuracy (RBF Kernel): ", "%.2f" % (rbf_accuracy * 100))
    print("F1 (RBF Kernel): ", "%.2f" % (rbf_f1 * 100))

    cm = confusion_matrix(y_test, poly_pred)

    cm_df = pd.DataFrame(cm)

    plt.figure(figsize=(5, 4))
    # print(cm_df)
    sns.heatmap(cm_df, annot=True)
    plt.title("Confusion Matrix")
    plt.ylabel("Actual Values")
    plt.xlabel("Predicted Values")
    plt.show()


    ```

    </details>

<br>

******************************************************

## Prac4

4. For a given set of training data examples stored in a .csv file, implement and demonstrate the candidate-elimination algorithm to output a description of the set of all hypotheses consistent with the training examples.


<details>
<summary>CODE</summary>


```python

import numpy as np
import pandas as pd

#Loading data from a csv file.
data = pd.DataFrame(data=pd.read_csv('enjoysport.csv'))
print(data)

# # URL of the CSV file
# csv_url = 'https://raw.githubusercontent.com/misbahulard/Machine-Learning/master/enjoysport.csv'

# # Read the CSV file into a pandas DataFrame
# data = pd.read_csv(csv_url)

# # Display the given training dataset
# print("\nThe Given Training Dataset \n")
# print(df)

###########################################
#Separating concept features from Target

concepts = np.array(data.iloc[:,0:6])
print(concepts)

###########################################
#Isolating target into a separate DataFrame
#Copying last column to target  array
target = np.array(data.iloc[:,6])
print(target)
###########################################

def learn(concepts, target): 
#Initialise S0 with the first instance from concepts.
#.copy()makes sure a new list is created instead of just pointing to the same memory location.
    specific_h = concepts[0].copy()
    print("\nInitialization of specific_h and genearal_h")
    print("\nSpecific Boundary: ", specific_h)
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print("\nGeneric Boundary: ",general_h)  
# The learning iterations.
    for i, h in enumerate(concepts):
        print("\nInstance", i+1 , "is ", h)
# Checking if the hypothesis has a positive target.
        if target[i] == "yes":
            print("Instance is Positive ")
            for x in range(len(specific_h)): 
# Change values in S & G only if values change.
                if h[x]!= specific_h[x]:                    
                    specific_h[x] ='?'                     
                    general_h[x][x] ='?'
# Checking if the hypothesis has a positive target.                  
        if target[i] == "no":            
            print("Instance is Negative ")
            for x in range(len(specific_h)): 
# For negative hypothesis change values only in G.
                if h[x]!= specific_h[x]:                    
                    general_h[x][x] = specific_h[x]                
                else:                    
                    general_h[x][x] = '?'        
        
        print("Specific Bundary after ", i+1, "Instance is ", specific_h)         
        print("Generic Boundary after ", i+1, "Instance is ", general_h)
        print("\n")
# find indices where we have empty rows, meaning those that are unchanged.
    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]    
    for i in indices:   
# remove those rows from general_h
        general_h.remove(['?', '?', '?', '?', '?', '?']) 
# Return final values
    return specific_h, general_h 

s_final, g_final = learn(concepts, target)

print("Final Specific_h: ", s_final, sep="\n")
print("Final General_h: ", g_final, sep="\n")

```

</details>

******************************************************

## Prac5

5. Write a program to implement the Naïve Bayesian classifier for a sample training data set stored as a .csv file. Compute the accuracy of the classifier, considering few test data sets.


<details>
<summary>CODE</summary>


```python

# Prac 5: Naive Bayes and Gaussian Classification
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.metrics import confusion_matrix

wine = datasets.load_wine()
print("Features: ", wine.feature_names)
print("Labels: ", wine.target_names)

X = pd.DataFrame(wine['data'])
print(X.head())
print(wine.data.shape)

y = wine.target  # Remove print()

X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.30, random_state=10)

gnb = GaussianNB()
gnb.fit(X_train, y_train)

y_pred = gnb.predict(X_test)
print(y_pred)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)  # No need for np.array()
cm

```

</details>

******************************************************

## Prac6

6. Decision Tree classifier & Random Forest Classifier.


<details>
<summary>CODE</summary>


```python

# Decision Tree Classifier & Random Forest Classifier 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix 

###############################
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
df.head() 


# df = pd.read_csv('https://raw.githubusercontent.com/nelson-wu/employee-attrition-ml/master/WA_Fn-UseC_-HR-Employee-Attrition.csv')


###############################

# Exploratory Data Analysis

sns.countplot(x='Attrition', data=df)
from pandas.core.arrays import categorical
df.drop(['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours'], axis="columns", inplace=True)
categorical_col = []
for column in df.columns:
    if df[column].dtype == object:
        categorical_col.append(column) 

df['Attrition'] = df['Attrition'].astype("category").cat.codes 

for column in categorical_col:
    df[column] = LabelEncoder().fit_transform(df[column])

###############################
X = df.drop('Attrition', axis=1)
y = df['Attrition'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

###############################
def print_score(clf, X_train, y_train, X_test, y_test, train=True):

    if train:
        pred = clf.predict(X_train)
        clf_report = pd.DataFrame(classification_report(y_train, pred, output_dict=True))
        print("Train Result:\n=======================================")
        print(f"Accuracy Score: {accuracy_score(y_train, pred) * 100:.2f}%")
        print(" ")
        print(f"CLASSIFICATION REPORT:\n{clf_report}")
        print(" ")
        print(f"Confusion Matrix: \n{confusion_matrix(y_train, pred)}\n")
    elif not train:
        pred = clf.predict(X_test)
        clf_report = pd.DataFrame(classification_report(y_test, pred, output_dict=True))

        print("Test Result:\n=======================================")
        print(f"Accuracy Score: {accuracy_score(y_test, pred) * 100:.2f}%")
        print(" ")
        print(f"CLASSIFICATION REPORT:\n{clf_report}")
        print(" ")
        print(f"Confusion Matrix: \n{confusion_matrix(y_test, pred)}\n")

###############################
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from pickle import TRUE
from sklearn.tree import DecisionTreeClassifier
tree_clf = DecisionTreeClassifier(random_state=42)
tree_clf.fit(X_train, y_train)
print_score(tree_clf, X_train, y_train, X_test, y_test, train=True)
print_score(tree_clf, X_train, y_train, X_test, y_test, train=False)

###############################
from sklearn.ensemble import RandomForestClassifier
rf_clf = RandomForestClassifier(random_state=42)
rf_clf.fit(X_train, y_train)
print_score(rf_clf, X_train, y_train, X_test, y_test, train=True)
print_score(rf_clf, X_train, y_train, X_test, y_test, train=False)

```

</details>

******************************************************

## Prac7

7. Data loading, feature scoring and ranking, feature selection (principal component analysis).


<details>
<summary>CODE</summary>


```python

import pandas as pd

# Load the Iris dataset from a URL
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
dataset = pd.read_csv(url, names=names)
dataset.head()

# Store the feature sets into X variables and the series of corresponding variables in y
x = dataset.drop('Class', axis=1)
y = dataset['Class']
x.head()
y.head()

from sklearn.model_selection import train_test_split

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

from sklearn.preprocessing import StandardScaler

# Standardize the features
sc = StandardScaler()
x_train1 = sc.fit_transform(x_train)
x_test1 = sc.transform(x_test)
y_train1 = y_train
y_test1 = y_test

from sklearn.decomposition import PCA

# Apply Principal Component Analysis (PCA)
pca = PCA()
x_train1 = pca.fit_transform(x_train1)
x_test1 = pca.transform(x_test1)
explained_variance = pca.explained_variance_ratio_
print(explained_variance)

from sklearn.decomposition import PCA

# Apply PCA with a specific number of components
pca = PCA(n_components=1)
x_train1 = pca.fit_transform(x_train1)
x_test1 = pca.transform(x_test1)

from sklearn.ensemble import RandomForestClassifier

# Create and train a Random Forest classifier
classifier = RandomForestClassifier(max_depth=2, random_state=0)
classifier.fit(x_train1, y_train1)

# Make predictions on the test set
y_pred = classifier.predict(x_test1)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# Calculate and print the confusion matrix and accuracy
cm = confusion_matrix(y_test, y_pred)
print(cm)
print('Accuracy:', accuracy_score(y_test, y_pred))

```

</details>

******************************************************

## Prac8

8. For a given set of training data examples stored in a CSV. File implement-


    ###  8A. Least Square Regression Algorithm.

    <details>
    <summary>CODE</summary>


    ```python

    ## Aim: For a given set of training data examples stored in a .CSV file implement Least Square Regression algorithm. 

    # Making imports

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    plt.rcParams["figure.figsize"] = (12.0, 9.0)

    np.random.seed(42)
    X = np.linspace(0, 10, 100)
    Y = 2.5 * X + 1.5 + np.random.normal(0, 2, 100)
    data = pd.DataFrame({"X": X, "Y": Y})
    plt.scatter(X, Y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Synthetic Data for Least Square Regression")
    plt.show()

    import numpy as np

    # Assuming X and Y are your data arrays
    X_mean = np.mean(X)
    Y_mean = np.mean(Y)

    num = 0
    den = 0

    for i in range(len(X)):
        num += (X[i] - X_mean) * (Y[i] - Y_mean)
        den += (X[i] - X_mean) ** 2

    m = num / den
    c = Y_mean - m * X_mean

    print(m, c)

    # Making predictions

    Y_pred = m * X + c
    plt.scatter(X, Y)  # actual
    plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color="red")  # prediction
    plt.show()


    ```

    </details>

    <br>

    ### 8B. Logistic Regression algorithm.

    <details>
    <summary>CODE</summary>


    ```python

    # Importing the libraries
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

    # Importing the dataset
    dataset = pd.read_csv('https://raw.githubusercontent.com/mk-gurucharan/Classification/master/DMVWrittenTests.csv')
    X = dataset.iloc[:, [0, 1]].values
    Y = dataset.iloc[:, 2].values
    dataset.head(5)


    # Splitting the dataset into the training set and test set.
    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # Training the logistic regression model on the training set
    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression()
    classifier.fit(X_train, Y_train)

    # Predicting the test set results.
    y_pred = classifier.predict(X_test)
    y_pred


    # Confusion Matrix and Accuracy.
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(Y_test, y_pred)
    from sklearn.metrics import accuracy_score
    print("Accuracy:", accuracy_score(Y_test, y_pred))
    cm



    ```

    </details>

******************************************************

## Prac9

9. Backpropagation algorithm and Text pre-processing, Text clustering, classification


    ###  9A. Build an artificial Neural Network by implementing the Backpropagation algorithm and test the same using appropriate data sets.

    <details>
    <summary>CODE</summary>


    ```python

    # 9A. Build an artificial Neural Network by implementing the Backpropagation algorithm and test the same using appropriate data sets.

    import numpy as np

    X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
    Y = np.array(([92], [86], [89]), dtype=float)

    # Normalize input data
    X = X / np.amax(X, axis=0)
    Y = Y / 100

    class NeuralNetwork(object):
        def __init__(self):
            self.input_size = 2
            self.output_size = 1
            self.hidden_size = 3
            self.W1 = np.random.randn(self.input_size, self.hidden_size)
            self.W2 = np.random.randn(self.hidden_size, self.output_size)

        def forward(self, X):
            self.z = np.dot(X, self.W1)
            self.z2 = self.sigmoidal(self.z)
            self.z3 = np.dot(self.z2, self.W2)
            op = self.sigmoidal(self.z3)
            return op

        def sigmoidal(self, s):
            return 1 / (1 + np.exp(-s))

        def sigmoidalprime(self, s):
            return s * (1 - s)

        def backward(self, X, Y, o):
            self.o_error = Y - o
            self.o_delta = self.o_error * self.sigmoidalprime(o)
            self.z2_error = self.o_delta.dot(self.W2.T)
            self.z2_delta = self.z2_error * self.sigmoidalprime(self.z2)
            self.W1 = self.W1 + X.T.dot(self.z2_delta)
            self.W2 = self.W2 + self.z2.T.dot(self.o_delta)

        def train(self, X, Y):
            o = self.forward(X)
            self.backward(X, Y, o)

    # Create an instance of the NeuralNetwork class
    nn = NeuralNetwork()

    # Training loop
    for i in range(2000):
        print("Input: " + str(X))
        print("Actual Output: " + str(Y))
        print("Predicted Output: " + str(nn.forward(X)))
        print("Loss: " + str(np.mean(np.square(Y - nn.forward(X)))))
        nn.train(X, Y)


    ```

    </details>

    <br>

    ### 9B. Perform Text pre-processing, Text clustering, classification with Prediction, Test Score and Confusion Matrix.

    <details>
    <summary>CODE</summary>


    ```python

    # 9B. Perform Text pre-processing, Text clustering, classification with Prediction, Test Score and Confusion Matrix

    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

    # Load the dataset

    csv_file = 'Restaurant_Reviews.tsv'
    #csv_file = 'https://raw.githubusercontent.com/SarthakRana/Restaurant-Reviews-using-NLP-/master/Restaurant_Reviews.tsv'

    dataset = pd.read_csv(csv_file, delimiter='\t', quoting=3)

    # Text preprocessing using Natural Language Toolkit (nltk)
    import re
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer

    corpus = []
    for i in range(0, 1000):    
        review = re.sub('[^a-zA-Z]', '', dataset['Review'][i]) # Remove non-alphabetic characters
        review = review.lower()  # Convert to lowercase
        review = review.split() # Tokenize the words
        ps = PorterStemmer() # Stemming and removing stopwords
        review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
        # Join the words to form the processed review
        review = ' '.join(review)
        corpus.append(review)

    # Creating the bag of words model
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(max_features=1500)
    X = cv.fit_transform(corpus).toarray()
    Y = dataset.iloc[:, 1].values

    # Splitting the dataset into the training set and test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=100)

    # Fitting Naive Bayes to the training set
    from sklearn.naive_bayes import GaussianNB
    classifier = GaussianNB()
    classifier.fit(X_train, Y_train)

    # Predicting the test set results
    Y_pred = classifier.predict(X_test)

    # Model Accuracy
    from sklearn import metrics
    from sklearn.metrics import confusion_matrix
    print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))

    # Making the confusion matrix
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(Y_test, Y_pred)
    print(cm)


    ```

    </details>

******************************************************

## Prac10

10. Distance methods with Prediction | K – Means Clustering.

    ###  10A. Implement the different Distance methods (Euclidean) with Prediction, Test Score and Confusion Matrix.

    <details>
    <summary>CODE</summary>


    ```python

    #10 A) Aim:  Implement the different Distance methods (Euclidean) with Prediction, Test Score and Confusion Matrix. 

    import numpy as np
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import accuracy_score

    #Load the dataset

    # csv_file = 'iris.csv'
    csv_file = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'

    df = pd.read_csv(csv_file)

    #quick look into the data
    print(df.head(5))
    print("\n")

    #Separate data and label
    x = df.drop(['Species'], axis=1)
    y = df['Species']

    #Prepare data for classification process
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

    #Create a model , p = 2 => Euclidean Distance:
    knn = KNeighborsClassifier(n_neighbors = 6, p = 2, metric='minkowski')

    #Train the model
    knn.fit(x_train, y_train)

    # Calculate the accuracy of the model
    print(knn.score(x_test, y_test))
    y_pred = knn.predict(x_test)

    #confusion matrix 
    from sklearn.metrics import  confusion_matrix
    cm=np.array(confusion_matrix(y_test,y_pred))
    print(cm)
    print("\n")

    #Create a model , p = 1 => Manhattan Distance
    knn = KNeighborsClassifier(n_neighbors = 6, p = 1, metric='minkowski')

    #Train the model
    knn.fit(x_train, y_train)

    # Calculate the accuracy of the model
    print(knn.score(x_test, y_test))
    y_pred = knn.predict(x_test)

    #confusion matrix 
    from sklearn.metrics import  confusion_matrix
    cm=np.array(confusion_matrix(y_test,y_pred))
    print(cm)
    print("\n")

    #Create a model ,p = ∞, Chebychev Distance
    #let ∞ = 10000
    knn = KNeighborsClassifier(n_neighbors = 6, p = 10000, metric='minkowski')

    #Train the model
    knn.fit(x_train, y_train)

    # Calculate the accuracy of the model
    print(knn.score(x_test, y_test))
    y_pred = knn.predict(x_test)

    #confusion matrix 
    from sklearn.metrics import  confusion_matrix
    cm=np.array(confusion_matrix(y_test,y_pred))
    print(cm)
    print("\n") 


    ```

    </details>

    <br>

    ### 10B. Implement the classification model using K means clustering with Prediction, Test Score and Confusion Matrix.

    <details>
    <summary>CODE</summary>


    ```python

    #10B: AIM: Implement the classification model using K-means clustering with Prediction, Test score and Confusion Matrix.

    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import sklearn

    #Import the dataset and slice the important features

    # csv_file = 'Mall_Customers.csv'
    csv_file = 'https://raw.githubusercontent.com/tirthajyoti/Machine-Learning-with-Python/master/Datasets/Mall_Customers.csv'

    dataset = pd.read_csv(csv_file)
    
    X = dataset.iloc[:, [3,4]].values

    #Find the optimal k value for clustering the data.
    from sklearn.cluster import KMeans
    wcss = []
    for i in range(1,11):
        kmeans = KMeans(n_clusters=i, init='k-means++',random_state=42)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)
        
    plt.plot(range(1,11),wcss)
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()

    #The point at which the elbow shape is created is 5.
    kmeans = KMeans(n_clusters=5,init="k-means++",random_state=42)
    y_kmeans = kmeans.fit_predict(X)

    plt.scatter(X[y_kmeans == 0,0], X[y_kmeans == 0,1], s = 60, c = 'red', label = 'Cluster1')
    plt.scatter(X[y_kmeans == 1,0], X[y_kmeans == 1,1], s = 60, c = 'blue', label = 'Cluster2')
    plt.scatter(X[y_kmeans == 2,0], X[y_kmeans == 2,1], s = 60, c = 'green', label = 'Cluster3')
    plt.scatter(X[y_kmeans == 3,0], X[y_kmeans == 3,1], s = 60, c = 'violet', label = 'Cluster4')
    plt.scatter(X[y_kmeans == 4,0], X[y_kmeans == 4,1], s = 60, c = 'yellow', label = 'Cluster5')
    plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],s=100,c='black',label='Centroids')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100')
    plt.legend()
    plt.show()



    ```

    </details>


******************************************************
