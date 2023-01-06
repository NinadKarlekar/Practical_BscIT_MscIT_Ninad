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

