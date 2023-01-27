# Research In Computing Practicals

M. Sc (Information Technology)
PSIT1P1 Research In Computing



## Index

| Sr.No. | Name | README |
| --- | --- | --- |
| [Prac1A(By Python)](/MscIT/Semester%201/Research_In_Computing/Practical%201/) <br> [Prac1A(By Excel)](/MscIT/Semester%201/Research_In_Computing/RIC%20Excel.pdf)| 1 A.	Write a program for obtaining descriptive statistics of data. | [prac1a(By Python)](#prac1a) <br> [prac1a(By Excel)](#prac1aexcel) |
| [Prac1B-1(From_CSV)(By Python)](/MscIT/Semester%201/Research_In_Computing/Practical%201/) <br> [Prac1B-1(By Excel)](/MscIT/Semester%201/Research_In_Computing/RIC%20Excel.pdf) | 1 B.	Import data from different data sources (from **csv** to R/Python/Excel) | [prac1b-1(By Python)](#prac1b-1) <br> [prac1b-1(By excel)](#prac1b-1excel) |
| [Prac1B-2(From_Excel)(By Python)](/MscIT/Semester%201/Research_In_Computing/Practical%201/) <Br> [Prac1B-2(From_Excel)(By Excel)](/MscIT/Semester%201/Research_In_Computing/RIC%20Excel.pdf) | 1 B.	Import data from different data sources (from **Excel** to R/Python/Excel) | [prac1b-2(By Python)](#prac1b-2) <br> [prac1b-2(By excel)](#prac1b-2excel) |
| [Prac2A(By Google Form)](/MscIT/Semester%201/Research_In_Computing/RIC%20Excel.pdf) |2 A. Design a survey form for a given case study, collect the primary data and analyse it | [prac2a](#prac2agoogle-form) |
| [Prac2B(By Excel)](/MscIT/Semester%201/Research_In_Computing/RIC%20Excel.pdf)  |2 B. Perform analysis of given secondary data. | [prac2b(By Excel)](#prac2bexcel) |
| [Prac3A(By Python)](/MscIT/Semester%201/Research_In_Computing/Practical%203/)  |3 A.	Perform testing of hypothesis using one sample t-test. | [prac3a](#prac3a) |
| [Prac3B(By Python)](/MscIT/Semester%201/Research_In_Computing/Practical%203/) <br> [Prac3B(By Excel)](/MscIT/Semester%201/Research_In_Computing/RIC%20Excel.pdf)|3 B.	Write a program for t-test comparing two means for independent samples. | [prac3b](#prac3b) <br> [prac3b(By excel)](#prac3bexcel) |
| [Prac3C(By Python)](/MscIT/Semester%201/Research_In_Computing/Practical%203/) |3 C.	Perform testing of hypothesis using paired t-test. | [prac3c(By Python)](#prac3c) |
| [Prac4A(By Excel)](/MscIT/Semester%201/Research_In_Computing/RIC%20Excel.pdf) |4 A.	Perform testing of hypothesis using chi-squared goodness-of-fit test. | [prac4a(By Excel)](#prac4aexcel) |
| [Prac4B(By Python)](/MscIT/Semester%201/Research_In_Computing/Practical%204/)<br> [Prac4B(By Excel)](/MscIT/Semester%201/Research_In_Computing/RIC%20Excel.pdf) |B.	Perform testing of hypothesis using chi-squared Test of Independence. | [prac4b](#prac4b) <br> [prac4b(By excel)](#prac4bexcel) |
| [Prac5A(By Python)](/MscIT/Semester%201/Research_In_Computing/Practical%205/) |5 A.	Perform testing of hypothesis using Z-test. | [prac5a(By Python)](#prac5a) |
| [Prac5B(By Python)](/MscIT/Semester%201/Research_In_Computing/Practical%205/) |5 B.	Two-Sample Z test | [prac5b(By Python)](#prac5b) |
| [Prac6A(By Excel)](/MscIT/Semester%201/Research_In_Computing/RIC%20Excel.pdf) |6 A.	Perform testing of hypothesis using one-way ANOVA |  [prac6a(By excel)](#prac6aexcel) |
| [Prac6B(By Excel)](/MscIT/Semester%201/Research_In_Computing/RIC%20Excel.pdf) |6 B.	Perform testing of hypothesis using two-way ANOVA. |  [prac6b(By excel)](#prac6bexcel) |
| [Prac6C(By Python)](/MscIT/Semester%201/Research_In_Computing/Practical%206/) |6 C.	Perform testing of hypothesis using multivariate ANOVA (MANOVA) | [prac6c(By Python)](#prac6c) |
| [Prac7A(Excel)](/MscIT/Semester%201/Research_In_Computing/RIC%20Excel.pdf)|7 A.	Perform the Random sampling for the given data and analyse it. |  [prac7a(By excel)](#prac7aexcel) |
| [Prac7B(By Python)](/MscIT/Semester%201/Research_In_Computing/Practical%207/) |7 B.	Perform the Stratified sampling for the given data and analyse it | [prac7b(By Python)](#prac7b) |
| [Prac8A(By Python)](/MscIT/Semester%201/Research_In_Computing/Practical%208/) <br> [Prac8B(By Python)](/MscIT/Semester%201/Research_In_Computing/Practical%208/) <br> [Prac8C(By Python)](/MscIT/Semester%201/Research_In_Computing/Practical%208/)|Compute different types of correlation. <br> 8A.	Positive Correlation: <br> 8B.	Negative Correlation: <br> 8C.	No/Weak Correlation:| [prac8a(By Python)](#prac8a) <br> [prac8b(By Python)](#prac8b) <br> [prac8c(By Python)](#prac8c) |
| [Prac9A(By Python)](/MscIT/Semester%201/Research_In_Computing/Practical%209/) |9A.	Write a program to Perform linear regression for prediction. | [prac9a(By Python)](#prac9a) |
| [Prac9B(By Python)](/MscIT/Semester%201/Research_In_Computing/Practical%209/) <br> [Prac9B(By Excel)](/MscIT/Semester%201/Research_In_Computing/RIC%20Excel.pdf)  |9B.	Perform polynomial regression for prediction. | [prac9b(By Python)](#prac9b) <br> [prac9b(By Excel)](#prac9bexcel) |

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

## Prac1B-1(Excel)

- To Import data from ***csv*** file.

<details>
<summary>Steps(Excel) & OUTPUT</summary>

1. In **Data tab**, Click on **Get Data**.
    
2. Select From **file** -> Select From **Text/CSV**
    
    ![excelRic1B_1](https://user-images.githubusercontent.com/88243315/215115182-a6c09c03-a0e4-4e2f-b611-e5ffb9dbe572.png)
    
3. Select the **csv** file and Click on **Import**
4. Preview window will open -> click on **Load**
    
    ![excelRic1B_2](https://user-images.githubusercontent.com/88243315/215115250-8e23b3f3-1c4e-455e-9d73-aac5bbedeb24.png)

    
5. The File will be Imported and will be shown.
    
    ![excelRic1B_3](https://user-images.githubusercontent.com/88243315/215115300-b169e2b1-af1f-4244-88e8-015d3a433253.png)


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

*****************

## Prac1B-2(Excel)

- To Import data from ***Excel*** file.

<details>
<summary>Steps(Excel) & OUTPUT</summary>

1. In Data tab, Click on Get Data
2. Select From file -> Select From Excel Workbook.
    
    ![excelRic1B(excel)_1](https://user-images.githubusercontent.com/88243315/215115720-da806203-b6b9-4198-8b36-29703a0b5cf3.png)
    
3. Select the Excel worksheet to import -> click on OK
4. Navigator Window will open -> Select the sheets you want to import -> Click on Load
    
    ![excelRic1B(excel)_2](https://user-images.githubusercontent.com/88243315/215116037-75972361-2f1e-4703-bdd1-c8784fe2afdb.png)
    
5. Data will be imported from the selected file and will be displayed
    
    ![excelRic1B(excel)_3](https://user-images.githubusercontent.com/88243315/215116067-b1940acf-322c-4a18-87a2-771dea89304a.png)


</details>

****************************************

## Prac2A(Google Form)

- Design a survey form for a given case study, collect the **primary data** and **analyse it**.

<details>
<summary>Steps(Google Form) & OUTPUT</summary>

![excelRic2A_1](https://user-images.githubusercontent.com/88243315/215127285-2a7269e5-7b1c-4610-9052-399078ee9525.png)
![excelRic2A_2](https://user-images.githubusercontent.com/88243315/215127293-df56527b-3a89-486f-8b5c-a6bcce49c5de.png)
![excelRic2A_3](https://user-images.githubusercontent.com/88243315/215127298-e21802ac-a28a-46a8-8e87-c268c57c9f76.png)
![excelRic2A_4](https://user-images.githubusercontent.com/88243315/215127299-757cb23e-1a9f-4ca2-beb2-019a70cf26b9.png)
![excelRic2A_5](https://user-images.githubusercontent.com/88243315/215127304-2d143479-3785-4e05-9508-c6e879d654e9.png)
![excelRic2A_6](https://user-images.githubusercontent.com/88243315/215127308-70e1a9fe-292f-4bcb-8e8f-380385026c7f.png)
![excelRic2A_7](https://user-images.githubusercontent.com/88243315/215127312-5cde3920-bd0b-4d99-a0d3-e03c92f9c259.png)
![excelRic2A_8](https://user-images.githubusercontent.com/88243315/215127314-7ad19ba4-0e23-455a-af25-d5fb7e3a4752.png)
![excelRic2A_9](https://user-images.githubusercontent.com/88243315/215127316-71baf463-7e71-4572-8d77-3d925940547e.png)
![excelRic2A_10](https://user-images.githubusercontent.com/88243315/215127319-5c741c5a-af55-47c4-848c-6ede48850c9b.png)
![excelRic2A_11](https://user-images.githubusercontent.com/88243315/215127326-d484819d-d5f7-447d-a6c8-ad3ace39abb0.png)
![excelRic2A_12](https://user-images.githubusercontent.com/88243315/215127332-1c05f369-d682-4305-b5aa-a976a9e4fb82.png)
![excelRic2A_13](https://user-images.githubusercontent.com/88243315/215127337-ca430615-0b8f-4656-9ccb-c13356e517a8.png)
![excelRic2A_14](https://user-images.githubusercontent.com/88243315/215127340-e048df9a-4448-42d2-a2ca-4af7424b38b0.png)


</details>

*******************************

## Prac2B(Excel)

- Perform analysis of given secondary data.

<details>
<summary>Steps(Excel) & OUTPUT</summary>

1. Open ***World_population 2010*** excel file.
    
2. Find the sum of **Male** and **Female** Column.
    
    ![excelRic2B_1](https://user-images.githubusercontent.com/88243315/215127464-d183b7aa-d266-4376-baa4-780d640be14a.png)

3. Create and find **total** of **Male** and **Female** coloumn <br> ***`(=B4+C4)`***
    
    ![excelRic2B_2](https://user-images.githubusercontent.com/88243315/215127505-fc9978a7-a305-4588-baed-ba871bfe8248.png)
    
4. Find **Sum** of all Total column values.
    
    ![excelRic2B_3](https://user-images.githubusercontent.com/88243315/215127590-22827bae-b1a8-4532-8871-9c7e207cad7e.png)

5. Find **Percentage of Male** <br> ***`(= -1*100*male column value/ sum of all total values)`*** <br> ***`(=-1*100*B4/$D$22)`***.
    
    ![excelRic2B_4](https://user-images.githubusercontent.com/88243315/215127669-62fd9b61-f44e-4fe1-bcc8-2efec70b352d.png)

6. Find Percentage of Male <br> ***`(= 100*Female column value/ sum of all total values)`*** <br> ***`(100*C4/$D$22)`***.

7. Find sum of both male% and female%

8. Select Male% and Female% -> insert -> clustered Bar
    
    ![excelRic2B_5](https://user-images.githubusercontent.com/88243315/215128215-4f0cc6d9-a817-495b-b76a-7d304f0ed537.png)
    ![excelRic2B_6](https://user-images.githubusercontent.com/88243315/215128221-ddb916fa-4083-40d9-af47-340ea6090764.png)


9. Put the tip of your mouse arrow on the Y-axis (vertical axis) so it says “Category Axis”, right click and chose Format Axis
    
    ![excelRic2B_7](https://user-images.githubusercontent.com/88243315/215128360-ee351c34-53f6-46bb-831c-c9cef6c84fbf.png)
    
10. Choose Axis options tab and set the major and minor tick mark type to None, Axis labels to Low, and click OK

11. Click on any of the bars in your pyramid, click right and select “format data series”. Set the Overlap to 100 and Gap Width to 0. Click OK.

- OUTPUT    
    
    ![excelRic2B_8](https://user-images.githubusercontent.com/88243315/215128427-1eb1943f-596c-4145-b175-dc06b5e229a3.png)

    

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


## Prac3B(Excel)

- Write a program for t-test comparing two means for independent samples.

<details>
<summary>Steps(Excel) & OUTPUT</summary>

1. Open Excel file.
    
2. Find the **average(mean)** of both **Experimental** and **comparison** columns.
    
    ![excelRic3B_1](https://user-images.githubusercontent.com/88243315/215128743-1dea356e-8306-48db-96c7-88fb754f71e6.png)

3. Find the **Standard deviation** of both **Experimental** and **comparison** columns.
    
    ![excelRic3B_2](https://user-images.githubusercontent.com/88243315/215128848-dea98dbd-17f8-47d6-9482-9a489210bc67.png)

4. Go to **Data analysis** -> Select **t-test: Paired Two Sample for Means** -> **OK**.
    
    ![excelRic3B_3](https://user-images.githubusercontent.com/88243315/215128875-6e004742-b894-4440-bcba-9497bfda9740.png)

5. For Variable 1 range(Experimental)= `A1 to A21` <br> For Variable 2 range(Comparison)= `B1 to B21` <br> For Output Range= `D5 to F17`
    
    ![excelRic3B_4](https://user-images.githubusercontent.com/88243315/215129028-d8291b5f-f70e-4e36-b241-d8d17f2b1fce.png)

6. Write 2 Hypothesis <br> H0 - Difference in gain score is not likely the result of experiment. <br> H1 - Difference in gain score is likely the result of experimental treatment and not the result of change variation.
7. To calculate the T-Test square value go to cell E20 and type <br>
`=(A22-B22)/SQRT((A23*A23)/COUNT(A2:A21)+(B23*B23)/COUNT(A2:A21))` <br> Formula `=(Mean A-Mean B)/SQRT((STDEV A*STDEV B)/COUNT(of A) + (STDEV*STDEV)/COUNT(of A))`
    
    ![excelRic3B_5](https://user-images.githubusercontent.com/88243315/215129090-2d162c20-93d4-4ed0-95cc-8e3b496c4479.png)

8. Now go to cell E21 and type <br> ***`=IF(E20<E12,"H0 is Accepted", "H0 is Rejected and H1 is Accepted")`***

- OUTPUT

![excelRic3B_6](https://user-images.githubusercontent.com/88243315/215129194-668aa89e-9a19-4237-b98d-8691bff9d58e.png)


</details>

****************************************

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


## Prac4A(Excel)

- Perform testing of hypothesis using chi-squared goodness-of-fit test.

<details>
<summary>Steps(Excel) & OUTPUT</summary>

1. Find total of both columns.
    
    ![excelRic4A_1](https://user-images.githubusercontent.com/88243315/215129391-d7dbc899-8d65-4bba-b3c1-18db26da5a42.png)
    ![excelRic4A_2](https://user-images.githubusercontent.com/88243315/215129386-493b6f1b-dc35-4682-9965-a8ebabe53689.png)

2. Enter the Formula.
    
    ![excelRic4A_3](https://user-images.githubusercontent.com/88243315/215129549-096e52a5-8b3b-4af7-a2b7-fd7d395fef98.png)
    ![excelRic4A_4](https://user-images.githubusercontent.com/88243315/215129553-5b22f72b-ff85-49dd-80e7-75598ee53cac.png)
    
3. Find the sum of all
    
    ![excelRic4A_5](https://user-images.githubusercontent.com/88243315/215129715-16ede277-264b-48c3-9c94-d239a041b722.png)
    ![excelRic4A_6](https://user-images.githubusercontent.com/88243315/215129719-46899601-356d-4b83-8426-100b78487d1d.png)

4. At cell D8 type <br> ***`=IF(D5>D7, "H0 Accepted","H0 Rejected")`***.

- OUTPUT
    
    ![excelRic4A_7](https://user-images.githubusercontent.com/88243315/215129830-239bacf7-98b3-47bd-ba14-56d0e6c08b8a.png)    

</details>


*****************


## Prac4B(Excel)

- Perform testing of hypothesis using chi-squared test of independence.

<details>
<summary>Steps(Excel) & OUTPUT</summary>

1. Find the total for all columns and rows.
    
    ![excelRic4B_1](https://user-images.githubusercontent.com/88243315/215129972-f5dc9e33-e737-4c4c-9801-8ac3ffeb2b65.png)

2. To calculate the expected value Ei <br> 
Go to Cell N9 and type ***`=N8/2`*** <br>
Go to Cell O9 and type ***`=O8/2`***  <br> 
Go to Cell P9 and type ***`=P8/2`***  <br> 
Go to Cell Q9 and type ***`=Q8/2`***  <br> 
Go to Cell R9 and type ***`=R8/2`***

    ![excelRic4B_2](https://user-images.githubusercontent.com/88243315/215130007-af19e1ff-f170-478a-871a-0515c1c599c4.png)

3. Go to cell T6 and type <br>
***`=SUM((N6-$N$9)^2/$N$9,(O6-$O$9)^2/$O$9,(P6-$P$9)^2/$P$9,(Q6-Q$9)^2/$Q$9, (R6-$R$9)^2/$R$9)`*** <br>
Go to cell T7 and type
***`=SUM((N7-$N$9)^2/$N$9,(O7-$O$9)^2/$O$9,(P7-$P$9)^2/$P$9,(Q7-Q$9)^2/$Q$9, (R7-$R$9)^2/$R$9)`***

4. To get the table value go to cell T11 and type <br>
***`=CHIINV(0.05,4)`***

5. Go to cell O13 and type <br> ***`=IF(T8>=T11," H0 is Accepted", "H0 is Rejected")`***

- OUTPUT
    
    ![excelRic4B_3](https://user-images.githubusercontent.com/88243315/215130174-e2f2232c-9763-42cd-89a3-f0c56e029cf8.png)


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


## Prac6A(Excel)

- Perform testing of hypothesis using one-way ANOVA

<details>
<summary>Steps(Excel) & OUTPUT</summary>

1. Open ***scores.csv*** file
2. Go to **Data analysis** -> **Anova single factor** -> **ok**
    
    ![excelRic6A_1](https://user-images.githubusercontent.com/88243315/215130351-8ee23bd8-08e2-45a1-8d57-e089f324dbd7.png)

3. Select input range as all values from `[Average Score (SAT Math), Average Score (SAT Reading), Average Score (SAT Writing)]` columns
    
    ![excelRic6A_2](https://user-images.githubusercontent.com/88243315/215130413-6cd7e338-f0ed-4d72-92fa-39bef09165c3.png)
    
- OUTPUT
    
    ![excelRic6A_3](https://user-images.githubusercontent.com/88243315/215130459-64cce15f-a2db-4e89-935b-0a114a0d8870.png)


</details>


*****************


## Prac6B(Excel)

- Perform testing of hypothesis using two-way ANOVA.

<details>
<summary>Steps(Excel) & OUTPUT</summary>

1. Open ***`ToothGrowth.csv`*** file
2. Go to **Data analysis** -> **Anova two factor with replication** -> **ok**.
    
    ![excelRic6B_1](https://user-images.githubusercontent.com/88243315/215130710-d57079f8-229b-4cbb-a4ba-fbfcfdf089a3.png)

3. Select all cell in input range , <br> **Rows per sample=30** <br> **Alpha=0.05**
    
    ![excelRic6B_2](https://user-images.githubusercontent.com/88243315/215130762-68f85a22-631c-4c62-9663-f7ba1b063a86.png)

- OUTPUT
    
    ![excelRic6B_3](https://user-images.githubusercontent.com/88243315/215130797-a325dd8e-6922-4c2c-9150-0e07f306e2e0.png)

    

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


## Prac7A(Excel)

- Perform the Random sampling for the given data and analyse it.

<details>
<summary>Steps(Excel) & OUTPUT</summary>

1. Open existing excel sheet with population data. <br> Sample Sheet looks as given below: <br> Set **Cell O1 = Male** and **Cell O2 = Female**
2. To generate a random sample for male students from given population go to Cell O1 and type <br> ***`=INDEX(E$2:E$62,RANK(B2,B$2:B$62))`*** <br> Drag the formula to the desired no of cell to select random sample.
3. Now, to generate a random sample for female students go to cell P1 and type <br> ***`=INDEX(K$2:K$40,RANK(H2,H$2:H$40))`*** <br> Drag the formula to the desired no of cell to select random sample.
    
    ![excelRic7A_1](https://user-images.githubusercontent.com/88243315/215130974-db0f76f5-c544-4bdd-ba2c-cc224e60530e.png)

    
- OUTPUT
    
    ![excelRic7A_2](https://user-images.githubusercontent.com/88243315/215131023-c6ac72af-4adf-4b3c-9edf-a7aa7ca6f201.png)

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


*****************


## Prac9B(Excel)

- Perform polynomial regression for prediction.

<details>
<summary>Steps(Excel) & OUTPUT</summary>

1. Insert the data as follows
    
    ![excelRic9B_1](https://user-images.githubusercontent.com/88243315/215131224-6d9cc01d-23cf-491b-945c-e39a64d58a13.png)

2. Go to Data -> Data Analysis -> Regression
    
    ![excelRic9B_2](https://user-images.githubusercontent.com/88243315/215131300-ee99b41a-0e82-4312-8b90-7e3d921f7dbd.png)

3. Enter the **input** range and **output** range
    
    ![excelRic9B_3](https://user-images.githubusercontent.com/88243315/215131333-0c87e048-7886-487f-8923-d51b97bf1828.png)

4. Click on OK
    
    ![excelRic9B_4](https://user-images.githubusercontent.com/88243315/215131411-85e713e4-79cd-4960-bcdd-27d33637c7e7.png)
    
5. Select the ***PREDICTED QUANTITY SOLD*** and ***RESIDUALS*** column and paste on above table
    
    ![excelRic9B_5](https://user-images.githubusercontent.com/88243315/215131544-0f9931ba-7b86-4055-a662-1cecf79678ec.png)
    ![excelRic9B_6](https://user-images.githubusercontent.com/88243315/215131548-0f98639d-c535-4d23-8cf5-dec77486bf66.png)

- OUTPUT:
    
    ![excelRic9B_7](https://user-images.githubusercontent.com/88243315/215131629-158c011d-6973-47d0-a4ea-d97c78d504ce.png)
    ![excelRic9B_8](https://user-images.githubusercontent.com/88243315/215131639-c949af37-7af3-45af-bae9-fab050f276ba.png)
    ![excelRic9B_9](https://user-images.githubusercontent.com/88243315/215131642-76141230-823f-404d-834b-8ccab420c0bb.png)



- Result:
R square equals **0.962**, which is a very good fit. 6% of the variation in Qunatity Sold is explained by the independent variables Price and Advertising. The closer to 1, the better the regression line (read on) fits the data. <br>
Significance **F is 0.001464128** which is **less than 0.05** (good fit).

</details>


*****************************************************

### [Go To Top](#research-in-computing-practicals)



