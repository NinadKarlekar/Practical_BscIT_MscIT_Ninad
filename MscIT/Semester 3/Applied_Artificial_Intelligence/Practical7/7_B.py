### 7b)	AIM: Implement Conditional Probability using Python.
import pandas as pd
import numpy as np

df = pd.read_csv("student-mat.csv")

df.head(3)
len(df)

df["grade_A"] = np.where(df["G3"] * 5 >= 80, 1, 0)
df["high_absenses"] = np.where(df["absences"] >= 10, 1, 0)
df["count"] = 1

df = df[["grade_A", "high_absenses", "count"]]

df.head()

pd.pivot_table(
    df,
    values="count",
    index=["grade_A"],
    columns=["high_absenses"],
    aggfunc=np.size,
    fill_value=0,
)