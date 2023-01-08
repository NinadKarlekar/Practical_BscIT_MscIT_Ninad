# 1B. Calculate the output of neural net using both binary and bipolar sigmoidal function.
import math

n = int(input("Enter the number of element "))

yin = 0
for i in range(0, n):
    x = float(input("Enter x :"))
    w = float(input("Enter weight w: "))
    yin = yin + x * w

b = float(input("B "))
yin = yin + b

print("yin ", yin)

binary_sigmoidal = 1 / (1 + (math.e ** (-yin)))
print("Binary Sigmoidal = ", round(binary_sigmoidal, 3))

bipolar_sigmoidal = (2 / (1 + (math.e ** (-yin)))) - 1
print("Bipolar Sigmoidal = ", round(binary_sigmoidal, 3))
