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
print("\nNinad Karlekar 22306A1012")
