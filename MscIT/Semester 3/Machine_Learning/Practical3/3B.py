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
