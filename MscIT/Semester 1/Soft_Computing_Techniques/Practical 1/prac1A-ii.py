# 1A-ii. Calculate the output of neural net for given data.
n = int(input("Enter the number of input: "))
yin = 0

for i in range(n):
    x = float(input("Enter x :"))
    w = float(input("Enter weight w: "))
    yin = yin + x * w

print("Output ", yin)

if yin < 0:
    output = 0
elif yin > 1:
    output = 1
else:
    output = yin

print("Output: ", output)
