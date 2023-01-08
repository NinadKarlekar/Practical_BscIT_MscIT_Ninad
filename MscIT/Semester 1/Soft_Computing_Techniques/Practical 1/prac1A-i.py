# Prac 1A-i. Design a simple linear neural network model. 


x = float(input("\n Enter the input x = "))

w = float(input("\n Enter the weight w = "))

b = float(input("\n Enter the bias b  = "))

yin = w * x + b
print("\n Next input yin ", yin)

print("\n ************OUTPUT**************")
if yin < 0:
    output = 0
elif yin > 1:
    output = 1
else:
    output = yin

print("Output", output)

