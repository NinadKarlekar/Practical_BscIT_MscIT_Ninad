# Research In Computing Practicals

M. Sc (Information Technology)
PSIT1P1 Research In Computing



## Index

| Sr.No. | Name | Copy |
| --- | --- | --- |
| [Prac1A(Python)](/MscIT/Semester%201/Research_In_Computing/Practical%201/) <br> [Prac1A(Excel)](/MscIT/Semester%201/Research_In_Computing/RIC%20Excel.docx)| A.	Write a program for obtaining descriptive statistics of data. | [prac1a](#prac1a) |
| [Prac1B(From_CSV)](/MscIT/Semester%201/Research_In_Computing/Practical%201/Practical%201/)<br>  [Prac1B(From_Excel)](/MscIT/Semester%201/Research_In_Computing/Practical%201/) | B.	Import data from different data sources (from Excel, csv, mysql, sql server, oracle to R/Python/Excel) | [prac1b(csv)](#prac1b-1) <br> [prac1b(excel)](#prac1b-2)|
| [Prac3A(Python)](/MscIT/Semester%201/Research_In_Computing/Practical%203/)  |A.	Perform testing of hypothesis using one sample t-test. | [prac3a](#prac3a) |
| [Prac3B(Python)](/MscIT/Semester%201/Research_In_Computing/Practical%203/) <br> [Prac3B(Excel)](/MscIT/Semester%201/Research_In_Computing/RIC%20Excel.docx)|B.	Write a program for t-test comparing two means for independent samples. | [prac3b](#prac3b) |
| [Prac3C(Python)](/MscIT/Semester%201/Research_In_Computing/Practical%203/) |C.	Perform testing of hypothesis using paired t-test. | [prac3c](#prac3c) |
| [Prac4A(Excel)](/MscIT/Semester%201/Research_In_Computing/RIC%20Excel.docx) |A.	Perform testing of hypothesis using chi-squared goodness-of-fit test. |
| [Prac4B(Python)](/MscIT/Semester%201/Research_In_Computing/Practical%204/)<br> [Prac4B(Excel)](/MscIT/Semester%201/Research_In_Computing/RIC%20Excel.docx) |B.	Perform testing of hypothesis using chi-squared Test of Independence. | [prac4b](#prac4b) |
| [Prac5A(PythonMain)](/MscIT/Semester%201/Research_In_Computing/Practical%205/) |A.	Perform testing of hypothesis using Z-test. | [prac5a](#prac5a) |
| [Prac5B(Python)](/MscIT/Semester%201/Research_In_Computing/Practical%205/) |B.	Two-Sample Z test | [prac5b](#prac5b) |
| [Prac6A(Excel)](/MscIT/Semester%201/Research_In_Computing/RIC%20Excel.docx) |A.	Perform testing of hypothesis using one-way ANOVA |
| [Prac6B(Excel)](/MscIT/Semester%201/Research_In_Computing/RIC%20Excel.docx) |B.	Perform testing of hypothesis using two-way ANOVA. |
| [Prac6C(Python)](/MscIT/Semester%201/Research_In_Computing/Practical%206/) |C.	Perform testing of hypothesis using multivariate ANOVA (MANOVA) | [prac6c](#prac6c) |
| [Prac7A(Excel)](/MscIT/Semester%201/Research_In_Computing/RIC%20Excel.docx)|A.	Perform the Random sampling for the given data and analyse it. |
| [Prac7B(Python)](/MscIT/Semester%201/Research_In_Computing/Practical%207/) |B.	Perform the Stratified sampling for the given data and analyse it | [prac7b](#prac7b) |
| [Prac8A(Python)](/MscIT/Semester%201/Research_In_Computing/Practical%208/) <br> [Prac8B(Python)](/MscIT/Semester%201/Research_In_Computing/Practical%208/) <br> [Prac8C(Python)](/MscIT/Semester%201/Research_In_Computing/Practical%208/)|Compute different types of correlation. <br> A.	Positive Correlation: <br> B.	Negative Correlation: <br> C.	No/Weak Correlation:| [prac8a](#prac8a) <br> [prac8b](#prac8b) <br> [prac8c](#prac8c) |
| [Prac9A(Python)](/MscIT/Semester%201/Research_In_Computing/Practical%209/) |A.	Write a program to Perform linear regression for prediction. | [prac9a](#prac9a) |
| [Prac9B(Python)](/MscIT/Semester%201/Research_In_Computing/Practical%209/) |B.	Perform polynomial regression for prediction. | [prac9b](#prac9b) |

********************

## Prac1A
- Practical 1A: Write a python program on descriptive statistics analysis.
```python

#Practical 1A: Write a python program on descriptive statistics analysis.
################################################################
import pandas as pd
#Create a Dictionary of series
d = {'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
#Create a DataFrame
df = pd.DataFrame(d)
print(df)
print('############ Sum ########## ')
print (df.sum())
print('############ Mean ########## ')
print (df.mean())
print('############ Standard Deviation ########## ')
print (df.std())

```

<details>
<summary>OUTPUT</summary>

![prac1a-1](https://user-images.githubusercontent.com/88243315/215099498-565f6481-3a28-41a8-be95-cca67adb0882.jpg)
![prac1a-2](https://user-images.githubusercontent.com/88243315/215099509-e678d086-30a0-40db-9275-f84d23c30d4c.jpg)



</details>

*****************************


## Prac1A(Excel)
- Practical 1A(Excel). Write a program for obtaining descriptive statistics of data.

<details>
<summary>Steps(Excel) & OUTPUT</summary>

1. Open Excel file.

2. Go to File -> Options -> Add-ins -> Click on **Analysis Toolpack** -> click on **Go**
    
    ![excelRic1A_1](https://user-images.githubusercontent.com/88243315/215110912-4c25d982-d180-4cf4-aed1-9e6584e3dbf9.png)


3. Tick mark **Analysis toolpack** -> click on **OK** -> The Data Analysis option will be added in Data tab
    
    ![excelRic1A_2](https://user-images.githubusercontent.com/88243315/215111614-9fa32936-56b4-4527-bd45-7258dd535030.png)

4. Now click on Data analysis -> Descriptive Statistiscs -> click on OK
    
    ![excelRic1A_3](https://user-images.githubusercontent.com/88243315/215111695-2e2dcc25-1d5b-43ba-8b6b-da0f2c917aae.png)

5. Click on input range -> select **Age** column in input column -> and select any blank column in output range -> Tick Mark on **Summery statistics**, **confidence level for mean(95%)**, **kth Largest(1)**, **kth smallest(1)**. -> click on Ok
    
    ![excelRic1A_4](https://user-images.githubusercontent.com/88243315/215111721-8cdc29dc-e9cc-416f-8b5c-48d1a263447d.png)


- **Output:**    
    
    ![excelRic1A_5](https://user-images.githubusercontent.com/88243315/215111762-7bad73fe-cf76-4fac-b45e-2bd3706e480f.png)


</details>

*****************

## Prac1B-1
- Import data from different data sources (from Excel, csv, mysql, sql server, oracle to R/Python/Excel)
- From csv
```python
#1B-1.	Import data from different data sources (from Excel, csv, mysql, sql server, oracle to R/Python/Excel)
#From csv
import sqlite3 as sq
import pandas as pd
Base='C:/VKHCG'
sDatabaseName=Base + '/01-Vermeulen/00-RawData/SQLite/vermeulen.db'
conn = sq.connect(sDatabaseName)
sFileName='C:/VKHCG/01-Vermeulen/01-Retrieve/01-EDS/02-Python/Retrieve_IP_DATA.csv'
print('Loading :',sFileName)
IP_DATA_ALL_FIX=pd.read_csv(sFileName,header=0,low_memory=False)
IP_DATA_ALL_FIX.index.names = ['RowIDCSV']
sTable='IP_DATA_ALL'
print('Storing :',sDatabaseName,' Table:',sTable)
IP_DATA_ALL_FIX.to_sql(sTable, conn, if_exists="replace")
print('Loading :',sDatabaseName,' Table:',sTable)
TestData=pd.read_sql_query("select * from IP_DATA_ALL;", conn)
print('## Data Values')
print(TestData)
print('################')
print('## Data Profile')
print('################')
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])
print('### Done!! ############################################')
```
<details>
<summary>OUTPUT</summary>

![prac1b1(csv)](https://user-images.githubusercontent.com/88243315/215099595-25d9a68b-f40a-49c9-8ba7-2a2882400f3c.png)



</details>

*****************

## Prac1B-2
- Import data from different data sources (from Excel, csv, mysql, sql server, oracle to R/Python/Excel)
- From Excel
```python
#1B-2.	Import data from different data sources (from Excel, csv, mysql, sql server, oracle to R/Python/Excel)
#From Excel
import os
import pandas as pd
Base='F:/tmp/practical-data-science/VKHCG'
sFileDir=Base + '/01-Vermeulen/01-Retrieve/01-EDS/02-Python'

CurrencyRawData = pd.read_excel('F:/tmp/practical-data-science/VKHCG/01-Vermeulen/00-RawData/Country_Currency.xlsx')
sColumns = ['Country or territory', 'Currency', 'ISO-4217']
CurrencyData = CurrencyRawData[sColumns]
CurrencyData.rename(columns={'Country or territory': 'Country', 'ISO-4217': 'CurrencyCode'}, inplace=True)
CurrencyData.dropna(subset=['Currency'],inplace=True)
CurrencyData['Country'] = CurrencyData['Country'].map(lambda x: x.strip())
CurrencyData['Currency'] = CurrencyData['Currency'].map(lambda x: x.strip())
CurrencyData['CurrencyCode'] = CurrencyData['CurrencyCode'].map(lambda x: x.strip())
print(CurrencyData)

print('~~~~~~ Data from Excel Sheet Retrived Successfully ~~~~~~~ ')

```

<details>
<summary>OUTPUT</summary>

![prac1b2(excel)](https://user-images.githubusercontent.com/88243315/215099613-90b5f84d-0aeb-4e46-9603-962643a0b8bd.png)



</details>

****************************************

## Prac3A
- Perform testing of hypothesis using one sample t-test
```python
#3A.Perform testing of hypothesis using one sample t-test.
#Google colab
from scipy.stats import ttest_1samp
import numpy as np

ages = np.genfromtxt("/content/ages.csv")
print(ages)
ages_mean = np.mean(ages)
print(ages_mean)
tset, pval = ttest_1samp(ages, 30)
print("p-values - ", pval)
if pval < 0.05:  # alpha value is 0.05
    print(" we are rejecting null hypothesis")
else:
    print("we are accepting null hypothesis")

```

<details>
<summary>OUTPUT</summary>

![prac3A(one_sample_T_test)](https://user-images.githubusercontent.com/88243315/215099682-e887aac3-22df-4c27-9a73-59376a1c5e1f.png)



</details>

*****************

## Prac3B
- Perform testing of hypothesis using two sample t-test
```python
#3B-Perform testing of hypothesis using two sample t-test.
#Google colab
import numpy as np
from scipy import stats
from numpy.random import randn

N = 20
a = 5 * randn(100) + 50
b = 5 * randn(100) + 51
var_a = a.var(ddof=1)
var_b = b.var(ddof=1)
s = np.sqrt((var_a + var_b) / 2)
t = (a.mean() - b.mean()) / (s * np.sqrt(2 / N))
df = 2 * N - 2
# p-value after comparison with the t
p = 1 - stats.t.cdf(t, df=df)
print("t = " + str(t))
print("p = " + str(2 * p))
if t > p:
    print("Mean of two distribution are differnt and significant")
else:
    print("Mean of two distribution are same and not significant")

```

<details>
<summary>OUTPUT</summary>


![prac3B(Two_sample_T_test)](https://user-images.githubusercontent.com/88243315/215099719-ea758aa1-8ff1-40c6-ad0f-64410c977e22.png)


</details>

*****************

## Prac3C
- Perform testing of hypothesis using paired t-test.
```python
#3C-Perform testing of hypothesis using paired t-test.
#Google colab
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("blood_pressure.csv")
print(df[['bp_before','bp_after']].describe())
#First let’s check for any significant outliers in
#each of the variables.
df[['bp_before', 'bp_after']].plot(kind='box')
# This saves the plot as a png file
plt.savefig('boxplot_outliers.png')
#################**#############################
# make a histogram to differences between the two scores.
df['bp_difference'] = df['bp_before'] - df['bp_after']
df['bp_difference'].plot(kind='hist', title= 'Blood Pressure Difference Histogram')
#Again, this saves the plot as a png file
#################**#############################
plt.savefig('blood pressure difference histogram.png')
stats.probplot(df['bp_difference'], plot= plt)
plt.title('Blood pressure Difference Q-Q Plot')
plt.savefig('blood pressure difference qq plot.png')
stats.shapiro(df['bp_difference'])
stats.ttest_rel(df['bp_before'], df['bp_after'])
```

<details>
<summary>OUTPUT</summary>

![prac3C-1(paired_T_test)](https://user-images.githubusercontent.com/88243315/215099755-e32f66e5-da0f-4d8d-b34d-5f6d426910d8.png)
![prac3C-2(paired_T_test)](https://user-images.githubusercontent.com/88243315/215099758-8488d8d8-21ed-4fe3-9cb4-1e10ba23106a.png)
![prac3C-3(paired_T_test)](https://user-images.githubusercontent.com/88243315/215099753-aded7051-a3f0-4086-a056-8ac3053a159c.png)



</details>

*****************

## Prac4B
- Perform testing of hypothesis using chi-squared
```python
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

```

<details>
<summary>OUTPUT</summary>


![prac4B-1(python)](https://user-images.githubusercontent.com/88243315/215099824-8110db3c-1ad4-43fb-8c5d-4078814b9ffc.png)
![prac4B-2(python)](https://user-images.githubusercontent.com/88243315/215099827-3c0c7a4c-7e52-471d-8ae3-a18688de60ef.png)


</details>

*****************

## Prac5A
- Perform testing of hypothesis using Z-test.
```python
# Google colab
#A.	Perform testing of hypothesis using Z-test.
from statsmodels.stats import weightstats as stests
import pandas as pd
from scipy import stats

df = pd.read_csv("blood_pressure.csv")
df[["bp_before", "bp_after"]].describe()
print(df)
ztest, pval = stests.ztest(df["bp_before"], x2=None, value=156)
print(float(pval))
if pval < 0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")

```

<details>
<summary>OUTPUT</summary>

![prac5A(Main)](https://user-images.githubusercontent.com/88243315/215099895-ce8e92b3-7b06-4c89-b6a7-3601a67bf12b.png)



</details>

*****************

## Prac5B
- Two-Sample Z test
```python
# Google colab
# B.	Two-Sample Z test
import pandas as pd
from statsmodels.stats import weightstats as stests

df = pd.read_csv("blood_pressure.csv")
df[["bp_before", "bp_after"]].describe()
print(df)
ztest, pval = stests.ztest(
    df["bp_before"], x2=df["bp_after"], value=0, alternative="two-sided"
)
print(float(pval))
if pval < 0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")


```

<details>
<summary>OUTPUT</summary>

![prac5B(TwoSampleZtest)](https://user-images.githubusercontent.com/88243315/215099910-b75535c0-953b-4fa9-9f6b-8d7e91843026.png)



</details>

*****************

## Prac6C
- Perform testing of hypothesis using multivariate ANOVA (MANOVA)
```python
# Google colab
import pandas as pd
from statsmodels.multivariate.manova import MANOVA
df = pd.read_csv('Iris.csv', index_col=0)
df.columns = df.columns.str.replace(".", "_")
df.head()
print('~~~~~~~~ Data Set ~~~~~~~~')
print(df)
maov = MANOVA.from_formula('SepalLengthCm + SepalWidthCm + \
PetalLengthCm + PetalWidthCm ~ Species', data=df)
print('~~~~~~~~ MANOVA Test Result ~~~~~~~~')
print(maov.mv_test())

```

<details>
<summary>OUTPUT</summary>


![prac6C-1](https://user-images.githubusercontent.com/88243315/215099955-0943ad3e-f648-4510-801b-cbcf03d0188e.png)
![prac6C-2](https://user-images.githubusercontent.com/88243315/215099957-5016732f-97f2-42fe-b4d6-99ceac1e0caf.png)


</details>

*****************

## Prac7B
- Perform the Stratified sampling for the given data and analyse it.
- We are to carry out a hypothetical housing quality survey across Lagos state,Nigeria. And we looking at a total of 5000 houses (hypothetically). We don’t just go to one local government and select 5000 houses, rather we ensure that the 5000 houses are a representative of the whole 20 local government areas Lagos state is comprised of. This is called stratified sampling. The population is divided into homogenous strata and the right number of instances is sampled from each stratum to guarantee that the test-set (which in this case is the 5000 houses) is a representative of the overall population. If we used random sampling, there would be a significant chance of having bias in the survey results.

```python
# Google colab
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
import seaborn as sns
color = sns.color_palette()
sns.set_style('darkgrid')
import sklearn
from sklearn.model_selection import train_test_split
housing =pd.read_csv('housing.csv')
print(housing.head())
print(housing.info())
#creating a heatmap of the attributes in the dataset

correlation_matrix = housing.corr()
plt.subplots(figsize=(8,6))
sns.heatmap(correlation_matrix, center=0, annot=True, linewidths=.3)
corr =housing.corr()
print(corr['median_house_value'].sort_values(ascending=False))
sns.distplot(housing.median_income)
plt.show()


```

<details>
<summary>OUTPUT</summary>

![prac7B-1](https://user-images.githubusercontent.com/88243315/215100006-3d0ee092-6d16-491d-810a-5f582727c5b1.png)
![prac7B-2](https://user-images.githubusercontent.com/88243315/215100008-76f351ca-d006-4493-aa9c-0dc551534b63.png)
![prac7B-3](https://user-images.githubusercontent.com/88243315/215099997-fbb9df4a-65fc-4ef8-a8d3-a4fc55a2e98e.png)
![prac7B-4](https://user-images.githubusercontent.com/88243315/215100003-52b87ca3-ac60-4b24-9c5b-31b05f9ba819.png)



</details>

*****************

## Prac8A
- 8.Write a program for computing different correlation
- A.	Positive Correlation:

```python
# Google colab
#8.Write a program for computing different correlation
#A.	Positive Correlation:
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
# 1000 random integers between 0 and 50
x = np.random.randint(0, 50, 1000)
# Positive Correlation with some noise
y = x + np.random.normal(0, 10, 1000)
np.corrcoef(x, y)
matplotlib.style.use('ggplot')
plt.scatter(x, y)
plt.show()

```

<details>
<summary>OUTPUT</summary>


![prac8A](https://user-images.githubusercontent.com/88243315/215100077-3e1ce39e-bfd8-4c3a-b889-694753300232.png)


</details>

*****************

## Prac8B
- B.	Negative Correlation:
```python
# Google colab
#8.Write a program for computing different correlation
#B.	Negative Correlation: 
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
# 1000 random integers between 0 and 50
x = np.random.randint(0, 50, 1000)
# Negative Correlation with some noise
y = 100 - x + np.random.normal(0, 5, 1000)
np.corrcoef(x, y)
plt.scatter(x, y)
plt.show()
print("Practical 8-B")

```

<details>
<summary>OUTPUT</summary>


![prac8B](https://user-images.githubusercontent.com/88243315/215100111-34ab23cd-0567-435d-a60c-712f2f2ddf6c.png)


</details>

*****************

## Prac8C
- 8C.	No/Weak Correlation:
```python
# Google colab
#8.Write a program for computing different correlation
#C.	No/Weak Correlation:
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
x = np.random.randint(0, 50, 1000)
y = np.random.randint(0, 50, 1000)
np.corrcoef(x, y)
plt.scatter(x, y)
plt.show()
print("Practical 8-C")
```

<details>
<summary>OUTPUT</summary>

![prac8C](https://user-images.githubusercontent.com/88243315/215100139-653fd856-e11f-4717-9355-cc63455b6f38.png)



</details>

*****************

## Prac9A
- 9A.	Write a program to Perform linear regression for prediction.
```python
# PRAC 9A #Jupyter
#A.	Write a program to Perform linear regression for prediction.
import quandl, math
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import datetime

style.use("ggplot")
df = quandl.get("WIKI/GOOGL")
df = df[["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume"]]
df["HL_PCT"] = (df["Adj. High"] - df["Adj. Low"]) / df["Adj. Close"] * 100.0
df["PCT_change"] = (df["Adj. Close"] - df["Adj. Open"]) / df["Adj. Open"] * 100.0
df = df[["Adj. Close", "HL_PCT", "PCT_change", "Adj. Volume"]]
forecast_col = "Adj. Close"
df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(df)))
df["label"] = df[forecast_col].shift(-forecast_out)
X = np.array(df.drop(["label"], 1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]
df.dropna(inplace=True)
y = np.array(df["label"])
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, y, test_size=0.2
)
clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
forecast_set = clf.predict(X_lately)
df["Forecast"] = np.nan
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day
for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
df.loc[next_date] = [np.nan for _ in range(len(df.columns) - 1)] + [i]
df["Adj. Close"].plot()
df["Forecast"].plot()
plt.legend(loc=4)
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

print("Practical 9-A")
```

<details>
<summary>OUTPUT</summary>

![prac9A](https://user-images.githubusercontent.com/88243315/215100163-83c9befc-5c03-402f-bd97-bf7aed0b253c.png)



</details>

*****************

## Prac9B
- 9B Perform polynomial regression for prediction.

```python
# PRAC 9B
# B.	Perform polynomial regression for prediction.
# Google colab
import numpy as np
import matplotlib.pyplot as plt


def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x
    return (b_0, b_1)


def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m", marker="o", s=30)
    # predicted response vector
    y_pred = b[0] + b[1] * x
    # plotting the regression line
    plt.plot(x, y_pred, color="g")
    # putting labels
    plt.xlabel("x")
    plt.ylabel("y")
    # function to show plot
    plt.show()


def main():
    # observations
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
    # estimating coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients:\nb_0 = {} b_1 = {}".format(b[0], b[1]))
    # plotting regression line
    plot_regression_line(x, y, b)


if __name__ == "__main__":
    main()
print("Practical 9-B")

```

<details>
<summary>OUTPUT</summary>


![prac9B](https://user-images.githubusercontent.com/88243315/215100182-4f02be37-63aa-4098-876c-790ee44087bc.png)


</details>

*****************************************************

### [Go To Top](#research-in-computing-practicals)



