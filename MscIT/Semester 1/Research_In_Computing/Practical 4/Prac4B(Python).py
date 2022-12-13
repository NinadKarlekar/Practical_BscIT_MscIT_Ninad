# Google colab
import numpy as np
import pandas as pd
import scipy.stats as stats

np.random.seed(10)
stud_grade = np.random.choice(
    a=["O", "A", "B", "C", "D"], p=[0.20, 0.20, 0.20, 0.20, 0.20], size=100
)
stud_gen = np.random.choice(a=["Male", "Female"], p=[0.5, 0.5], size=100)
mscpart1 = pd.DataFrame({"Grades": stud_grade, "Gender": stud_gen})
print(mscpart1)
stud_tab = pd.crosstab(mscpart1.Grades, mscpart1.Gender, margins=True)
stud_tab.columns = ["Male", "Female", "row_totals"]
stud_tab.index = ["O", "A", "B", "C", "D", "col_totals"]
observed = stud_tab.iloc[0:5, 0:2]
print(observed)
expected = np.outer(stud_tab["row_totals"][0:5], stud_tab.loc["col_totals"][0:2]) / 100
print(expected)
chi_squared_stat = (((observed - expected) ** 2) / expected).sum().sum()
print("Calculated : ", chi_squared_stat)
crit = stats.chi2.ppf(q=0.95, df=4)
print("Table Value : ", crit)
if chi_squared_stat >= crit:
    print("H0 is Accepted ")
else:
    print("H0 is Rejected ")
print("\nNinad Karlekar 22306A1012")