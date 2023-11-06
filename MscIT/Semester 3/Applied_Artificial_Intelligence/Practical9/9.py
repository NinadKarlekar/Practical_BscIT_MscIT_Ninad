### Step 1: First we need to import pandas and numpy. Pandas are basically use for table manipulations. Using Pandas package, we are going to upload Titanic training dataset and then by using head () function we will look at first five rows.
import pandas as pd
import numpy as np
titanic= pd.read_csv("train.csv")
titanic.head()

### Step 2: Create Two Data Frames, one containing categories and one containing numbers
titanic_cat = titanic.select_dtypes(object)
titanic_num = titanic.select_dtypes(np.number)

### Step 3: Now we need to drop two columns (name column and ticket column)
titanic_cat.head()
titanic_num.head()
titanic_cat.drop(['Name','Ticket'], axis=1, inplace=True)

### Step 4: Now to find the null values present in the above column
titanic_cat.isnull().sum()

### Step 5: Replace all the null values present with the maximum count category
titanic_cat.Cabin.fillna(titanic_cat.Cabin.value_counts().idxmax(), inplace=True)
titanic_cat.Embarked.fillna(titanic_cat.Embarked.value_counts().idxmax(), inplace=True)

### Step 6: After successfully removing all the null values our new data set is ready.
titanic_cat.head(20)

### Step 7: The next step will be to replace all the categories with Numerical Labels.For that we will be using LabelEncoders Method.
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
titanic_cat = titanic_cat.apply(le.fit_transform)
titanic_cat.head()
titanic_num.isna().sum()

### Step 8: Now we have only one column left which contain null value in it (Age). Let’s replace it with mean
titanic_num.Age.fillna(titanic_num.Age.mean(), inplace=True)
titanic_num.isna().sum()

### Step 9: Now we need to remove the unnecessary columns,since the passengerid is an unnecessary column, we need to drop it
titanic_num.drop(['PassengerId'], axis=1, inplace=True)
titanic_num.head()

### Step 10: Now we will combine two data frames and make it as one
titanic_final = pd.concat([titanic_cat,titanic_num],axis=1)
titanic_final.head()

### Step 11: Now we will define dependent and independent variables
X=titanic_final.drop(['Survived'],axis=1)
Y= titanic_final['Survived']
X_train = np.array(X[0:int(0.80*len(X))])
Y_train = np.array(Y[0:int(0.80*len(Y))])
X_test = np.array(X[int(0.80*len(X)):])
Y_test = np.array(Y[int(0.80*len(Y)):])
len(X_train), len(Y_train), len(X_test), len(Y_test)

### Step 13: Now we will import all the algorithms
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

### Step 14: Now we will initialize them in respective variables
LR = LogisticRegression()
KNN = KNeighborsClassifier()
NB = GaussianNB()
LSVM = LinearSVC()
NLSVM = SVC(kernel='rbf')
DT = DecisionTreeClassifier()
RF = RandomForestClassifier()

### Step 15: Now we will train our model
LR_fit = LR.fit(X_train, Y_train)
KNN_fit = KNN.fit(X_train, Y_train)
NB_fit = NB.fit(X_train, Y_train)
LSVM_fit = LSVM.fit(X_train, Y_train)
NLSVM_fit = NLSVM.fit(X_train, Y_train)
DT_fit = DT.fit(X_train, Y_train)
RF_fit = RF.fit(X_train, Y_train)

### Step 16: Now we need to predict the test data set and compare the accuracy score
LR_pred = LR_fit.predict(X_test)
KNN_pred = KNN_fit.predict(X_test)
NB_pred = NB_fit.predict(X_test)
LSVM_pred = LSVM_fit.predict(X_test)
NLSVM_pred = NLSVM_fit.predict(X_test)
DT_pred = DT_fit.predict(X_test)
RF_pred = RF_fit.predict(X_test)

from sklearn.metrics import accuracy_score
print("Logistic Regression is %f percent accurate" % (accuracy_score(LR_pred, Y_test)*100))
print("KNN is %f percent accurate" % (accuracy_score(KNN_pred, Y_test)*100))
print("Naive Bayes is %f percent accurate" % (accuracy_score(NB_pred, Y_test)*100))
print("Linear SVMs is %f percent accurate" % (accuracy_score(LSVM_pred, Y_test)*100))
print("Non Linear SVMs is %f percent accurate" % (accuracy_score(NLSVM_pred, Y_test)*100))
print("Decision Trees is %f percent accurate" % (accuracy_score(DT_pred, Y_test)*100))
print("Random Forests is %f percent accurate" % (accuracy_score(RF_pred, Y_test)*100))

