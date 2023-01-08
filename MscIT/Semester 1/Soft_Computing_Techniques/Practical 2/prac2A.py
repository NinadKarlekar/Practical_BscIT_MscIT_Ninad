# 2A. Generate AND/NOT function using McCulloch- Pitts neural net.

print("ANDNOT function using McCulloch-pitts\n")
x1inputs = [1, 1, 0, 0]
x2inputs = [1, 0, 1, 0]

print("Considering all weights as excitatory")
w1 = [1, 1, 1, 1]
w2 = [-1, -1, -1, -1]

yin = []
print("x1", "x2", "yin")
for i in range(0, 4):
    yin.append(x1inputs[i] * w1[i] + x2inputs[i] * w2[i])
    print(x1inputs[i], "   ", x2inputs[i], "  ", yin[i])

theta = 2 * 1 - 1  # n *w -p
print("Threshold-theta - ", theta)
print("Applying Threshold - ", theta)
Y = []
for i in range(0, 4):
    if yin[i] >= theta:
        value = 1
        Y.append(value)
    else:
        value = 0
        Y.append(value)
print("x1 ", "x2", "Y")
for i in range(0, 4):
    print(x1inputs[i], " ", x2inputs[i], " ", Y[i])
