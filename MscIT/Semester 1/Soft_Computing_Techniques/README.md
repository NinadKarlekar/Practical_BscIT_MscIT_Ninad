# Soft Computing Techniques

M. Sc (Information Technology)
PSIT1P4 Soft Computing Techniques



## Index

| Sr.No. | Name | Copy |
| --- | --- | --- |
| [Prac1A-i](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%201/) <br> [Prac1A-ii](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%201/)| 1A-i. Design a **simple linear neural network** model. <br> 1A-ii. Calculate the **output** of **neural net** for given data. | [Prac1A-i](#prac1a-i) <br>  [Prac1A-ii](#prac1a-ii) | |
| [Prac1B](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%201/) | 1B. Calculate the output of neural net using both **binary** and **bipolar sigmoidal** function.| [Prac1B](#prac1b) |
| [Prac2A](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%202/) | 2A. Generate **AND/NOT** function using **McCulloch- Pitts** neural net.| [Prac2A](#prac2a) |
| [Prac2B](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%202/) | 2B. Generate **XOR** function using **McCulloch-Pitts** neural net.| [Prac2B](#prac2b) |
| [Prac3A](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%203/) | 3A. Write a program to implement **Hebb’s rule**.| [Prac3A](#prac3a) |
| [Prac3B](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%203/) | 3B. Write a program to implement of **delta rule**. | [Prac3B](#prac3b) |
| [Prac4A](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%204/) | 4A. Write a program for **Back Propagation Algorithm**.| [Prac4A](#prac4a) |
| [Prac4B](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%204/) | 4B. Write a program for **error Backpropagation algorithm**. | [Prac4B](#prac4b) |
| [Prac5A](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%205/) | 5A. Write a program for **hopfield network**.| [Prac5A](#prac5a) |
| [Prac5B](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%205/) | 5B. Write a program for **radial basis function**. | [Prac5B](#prac5b) |
| [Prac6A](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%206/) | 6A. **Kohonen self organizing map**.| [Prac6A](#prac6a) |
| [Prac6B](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%206/) | 6B. **Hopfield network**. | [Prac6B](#prac6b) |
| [Prac7A-i](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%207/) <br> [Prac7A-ii](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%207/) | 7A-i. Implement membership and identity operators - **in** <br> 7A-ii. Implement membership and identity operators- **not in**.| [Prac7A-i](#prac7a-i) <br> [Prac7A-ii](#prac7a-ii) |
| [Prac7B-i](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%207/) <br> [Prac7B-ii](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%207/) | 7B-i. Implement membership and identity operators- **is**. <br> 7B-ii. Implement membership and identity operators- **is not**. | [Prac7B-i](#prac7b-i) <br> [Prac7B-ii](#prac7b-ii) |
| [Prac8A](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%208/) | 8A. Find **ratios** using **fuzzy logic**.| [Prac8A](#prac8a) |
| [Prac8B](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%208/) | 8B. Solve **tipping** problem using **fuzzy logic**. | [Prac8B](#prac8b) |

*************************
***********************

<BR>

## Prac1A-i

- 1A-i. Design a simple linear neural network model.

```python
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
```


- **OUTPUT**

![MSCIT_SCTprac1A_i](https://user-images.githubusercontent.com/88243315/214325496-08105a22-1075-4a39-a6f4-be2b798383ff.png)

**************

## Prac1A-ii

- 1A-ii. Calculate the output of neural net for given data.

```python
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
```

- **OUTPUT**

![MSCIT_SCTprac1A_ii](https://user-images.githubusercontent.com/88243315/214325547-5ef312ca-e921-4d3d-bca6-7a0ea7c75c8b.png)


**************

## Prac1B

- 1B. Calculate the output of neural net using both binary and bipolar sigmoidal function.

```python
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
print("Bipolar Sigmoidal = ", round(bipolar_sigmoidal, 3))
```

- **OUTPUT**

![MSCIT_SCTprac1B](https://user-images.githubusercontent.com/88243315/214325646-6198411a-92e0-4b9b-b872-0c726aab4d70.png)


**************

## Prac2A

- 2A. Generate AND/NOT function using McCulloch- Pitts neural net.

```python
# 2A. Generate AND/NOT function using McCulloch- Pitts neural net.

print("ANDNOT function using McCulloch-pitts\n")
x1inputs = [1, 1, 0, 0]
x2inputs = [1, 0, 1, 0]

print("Considering one weight as excitatory and other as inhibitory")
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
```

- **OUTPUT**

![MSCIT_SCTprac2A](https://user-images.githubusercontent.com/88243315/214325726-694e87a0-0e4f-400b-b3e7-8e938f02fde4.png)


**************

## Prac2B

- 2B. Generate XOR function using McCulloch-Pitts neural net.

```python
# 2B. Generate XOR function using McCulloch-Pitts neural net.

print("XOR function using McCulloch-pitts\n")
x1inputs = [1, 1, 0, 0]
x2inputs = [1, 0, 1, 0]

print("Calculating z1 = x1w11 + x2w21")
print("Considering one weights as excitatory and other as inhibitory")
w11 = [1, 1, 1, 1]
w21 = [-1, -1, -1, -1]

print("x1", "x2", "z1")
z1 = []
for i in range(0, 4):
    z1.append(x1inputs[i] * w11[i] + x2inputs[i] * w21[i])
    print(x1inputs[i], "   ", x2inputs[i], "  ", z1[i])

# Z2
print("Calculating z2 = x1w12 + x2w22")
print("Considering one weights as inhibitory and other as excitatory")
w12 = [-1, -1, -1, -1]
w22 = [1, 1, 1, 1]

print("x1", "x2", "z2")
z2 = []
for i in range(0, 4):
    z2.append(x1inputs[i] * w12[i] + x2inputs[i] * w22[i])
    print(x1inputs[i], "   ", x2inputs[i], "  ", z2[i])

print("Applying threshold for x1 and x2")
for i in range(0, 4):
    if z1[i] >= 1:
        z1[i] = 1
    else:
        z1[i] = 0
    if z2[i] >= 1:
        z2[i] = 1
    else:
        z2[i] = 0
print("z1", "z2")
for i in range(0, 4):
    print(z1[i], " ", z2[i])

print("x1 ", "x2", "Yin")
yin = []
v1 = 1
v2 = 1
for i in range(0, 4):
    yin.append(z1[i] * v1 + z2[i] * v2)
    print(x1inputs[i], " ", x2inputs[i], " ", yin[i])

print("Applying Threshold=1 for yin")
print("x1", "x2", "yin")
y = []
for i in range(0, 4):
    if yin[i] >= 1:
        y.append(1)
    else:
        y.append(0)
for i in range(0, 4):
    print(x1inputs[i], " ", x2inputs[i], " ", y[i])

print("END")
```

- **OUTPUT**

![MSCIT_SCTprac2B_1](https://user-images.githubusercontent.com/88243315/214325793-d019d473-1c80-4137-8f93-8942ee4c1862.png)
![MSCIT_SCTprac2B_2](https://user-images.githubusercontent.com/88243315/214325817-f98d9061-35d5-4992-90d1-ee4cf1ef9e62.png)

**************

## Prac3A

- 3A. Write a program to implement Hebb’s rule.

```python
# 3A. Write a program to implement Hebb’s rule.

import numpy as np

x1 = np.array([1, -1, -1, 1, -1, -1, 1, 1, 1])
x2 = np.array([1, -1, 1, 1, -1, 1, 1, 1, 1])
b = 0

y = np.array([1, -1])
wtold = np.zeros((9,))
wtnew = np.zeros((9,))

wtnew = wtnew.astype(int)
wtold = wtold.astype(int)

bais = 0
print("First input with target = 1")
for i in range(0, 9):
    wtnew[i] = wtold[i] + x1[i] * y[0]
wtold = wtnew
b = b + y[0]
print("New wt=", wtnew)
print("Bias value ", b)
print("**********************************")
print("second input with target = 1")
for i in range(0, 9):
    wtnew[i] = wtold[i] + x2[i] * y[1]
wtold = wtnew
b = b + y[1]
print("New wt=", wtnew)
print("Bias value= ", b)
```

- **OUTPUT**

![MSCIT_SCTprac3A](https://user-images.githubusercontent.com/88243315/214325868-bd8ecc82-e9b5-4fb0-b656-02ab598ddd51.png)


**************

## Prac3B

- 3B. Write a program to implement of delta rule.

```python
# 3B. Write a program to implement of delta rule.

print("b) Aim: - Write a program to implement delta rule")
import numpy as np
import time

np.set_printoptions(precision=2)
x = np.zeros((3,))
weights = np.zeros((3,))
desired = np.zeros((3,))
actual = np.zeros((3,))
for i in range(0, 3):
    x[i] = float(input("Intial inputs: "))
for i in range(0, 3):
    weights[i] = float(input("Intial weights: "))
for i in range(0, 3):
    desired[i] = float(input("Desired output: "))
a = float(input("Enter learning rate: "))
actual = x * weights
print("Acrual ", actual)
print("Desired ", desired)
while True:
    if np.array_equal(desired, actual):
        break
    else:
        for i in range(0, 3):
            weights[i] = weights[i] + a * (desired[i] - actual[i])
            actual = x * weights
print("Weights ", weights)
print("Actual ", actual)
print("Desired ", desired)
print("*" * 30)
print("Final output")
print("Corrected weights", weights)
print("Actual", actual)
print("Desired ", desired)
```

- **OUTPUT**

![MSCIT_SCTprac3B](https://user-images.githubusercontent.com/88243315/214325901-ab9a583d-8a30-4c1f-88cc-87c518d82ae1.png)


**************

## Prac4A

- 4A. Write a program for Back Propagation Algorithm.

```python
# 4A. Write a program for Back Propagation Algorithm.

import numpy as np

X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
Y = np.array(([92], [86], [89]), dtype=float)
X = X / np.amax(X, axis=0)
Y = Y / 100

class NN(object):
    def __init__(self):
        self.inputsize = 2
        self.outputsize = 1
        self.hiddensize = 3
        self.W1 = np.random.randn(self.inputsize, self.hiddensize)
        self.W2 = np.random.randn(self.hiddensize, self.outputsize)

    def forward(self, X):
        self.z = np.dot(X, self.W1)
        self.z2 = self.sigmoidal(self.z)
        self.z3 = np.dot(self.z2, self.W2)
        op = self.sigmoidal(self.z3)
        return op

    def sigmoidal(self, s):
        return 1 / (1 + np.exp(-s))

obj = NN()
op = obj.forward(X)
print("actual output\n" + str(op))
print("expected output\n" + str(Y))
```

- **OUTPUT**

![MSCIT_SCTprac4A](https://user-images.githubusercontent.com/88243315/214325923-f97b2929-2643-45d7-a51e-233641340f72.png)


**************

## Prac4B

- 4B. Write a program for error Backpropagation algorithm.

```python
# 4B. Write a program for error Backpropagation algorithm.

import numpy as np

X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
Y = np.array(([92], [86], [89]), dtype=float)

X = X / np.amax(X, axis=0)
Y = Y / 100

class NN(object):
    def __init__(self):
        self.inputsize = 2
        self.outputsize = 1
        self.hiddensize = 3
        self.W1 = np.random.randn(self.inputsize, self.hiddensize)
        self.W2 = np.random.randn(self.hiddensize, self.outputsize)

    def forward(self, X):
        self.z = np.dot(X, self.W1)
        self.z2 = self.sigmoidal(self.z)
        self.z3 = np.dot(self.z2, self.W2)
        op = self.sigmoidal(self.z3)
        return op

    def sigmoidal(self, s):
        return 1 / (1 + np.exp(-s))

    def sigmoidalprime(self, s):
        return s * (1 - s)

    def backward(self, X, Y, o):
        self.o_error = Y - o
        self.o_delta = self.o_error * self.sigmoidalprime(o)
        self.z2_error = self.o_delta.dot(self.W2.T)
        self.z2_delta = self.z2_error * self.sigmoidalprime(self.z2)
        self.W1 = self.W1 + X.T.dot(self.z2_delta)
        self.W2 = self.W2 + self.z2.T.dot(self.o_delta)

    def train(self, X, Y):
        o = self.forward(X)
        self.backward(X, Y, o)

obj = NN()
for i in range(2000):
    print("input\n" + str(X))
    print("Actual output\n" + str(Y))
    print("Predicted output\n" + str(obj.forward(X)))
    print("loss\n" + str(np.mean(np.square(Y - obj.forward(X)))))
    obj.train(X, Y)
```

- **OUTPUT**

![MSCIT_SCTprac4B](https://user-images.githubusercontent.com/88243315/214325970-230fed11-1c68-437b-bbf0-cb9997e5ab91.png)

**************

## Prac5A

- 5A. Write a program for hopfield network.

```python
# 5A. Write a program for hopfield network.

import numpy as np

def compute_next_state(state, weight):
    # @ is a shorthand for 'np.matmul()'
    # the numpy.where() function return thr indices of
    # element in an input array where condition is satisfied
    next_state = np.where(weight @ state >= 0, +1, -1)
    return next_state

def compute_final_state(initial_state, weight, max_iter=1000):
    previous_state = initial_state
    next_state = compute_next_state(previous_state, weight)
    is_stable = np.all(previous_state == next_state)
    n_iter = 0
    while (not is_stable) and (n_iter <= max_iter):
        previous_state = next_state
        next_state = compute_next_state(previous_state, weight)
        print("Previous State: ", previous_state)
        print("Next State: ", next_state)
        is_stable = np.all(previous_state == next_state)
        n_iter += 1
    return previous_state, is_stable, n_iter

initial_state = np.array([+1, -1, -1, -1])
weight = np.array([[0, -1, -1, +1], [-1, 0, +1, -1], [-1, +1, 0, -1], [+1, -1, -1, 0]])
final_state, is_stable, n_iter = compute_final_state(initial_state, weight)
print("final State : ", final_state)
print("is_stable : ", is_stable)
```

- **OUTPUT**

![MSCIT_SCTprac5A](https://user-images.githubusercontent.com/88243315/214326007-6459b4c4-d845-4473-862e-924ccca64be0.png)

**************

## Prac5B

- 5B. Write a program for radial basis function(R language).

```r
# 5B. Write a program for radial basis function.
# R language
D <- matrix(c(-3, 1, 4), ncol = 1) # 3 datapoints
N <- length(D)
rbf.gauss <- function(gamma = 1.0) {
    function(x) {
        exp(-gamma * norm(as.matrix(x), "F")^2)
    }
}
xlim <- c(-5, 7)
print(N)
print(xlim)
plot(NULL, xlim = xlim, ylim = c(0, 1.25), type = "n")
points(D, rep(0, length(D)), col = 1:N, pch = 19)
x.coord <- seq(-7, 7, length = 250)
gamma <- 1.5
for (i in 1:N) {
    points(x.coord, lapply(x.coord - D[i, ], rbf.gauss(gamma)), type = "l", col = i)
}
```

- **OUTPUT**

![MSCIT_SCTprac5B_1](https://user-images.githubusercontent.com/88243315/214326057-51a64f3b-6a6b-4865-ae65-7b6d131840d5.png)
![MSCIT_SCTprac5B_2](https://user-images.githubusercontent.com/88243315/214326086-e373338f-5887-4f0d-86ee-bc01da5f1b10.png)

**************

## Prac6A

- 6A. Kohonen self organizing map

```python
# 6A. Kohonen self organizing map.
from minisom import MiniSom
import numpy as np
import matplotlib.pyplot as plt

colors = [
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 1.0],
    [0.0, 0.0, 0.5],
    [0.125, 0.529, 1.0],
    [0.33, 0.4, 0.67],
    [0.6, 0.5, 1.0],
    [0.0, 1.0, 0.0],
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 1.0],
    [1.0, 0.0, 1.0],
    [1.0, 1.0, 0.0],
    [1.0, 1.0, 1.0],
    [0.33, 0.33, 0.33],
    [0.5, 0.5, 0.5],
    [0.66, 0.66, 0.66],
]

color_names = [
    "black",
    "blue",
    "darkblue",
    "skyblue",
    "greyblue",
    "lilac",
    "green",
    "red",
    "cyan",
    "violet",
    "yellow",
    "white",
    "darkgrey",
    "mediumgrey",
    "lightgrey",
]

som = MiniSom(30, 30, 3, sigma=3.0, learning_rate=2.5, neighborhood_function="gaussian")

plt.imshow(abs(som.get_weights()), interpolation="none")
som = MiniSom(30, 30, 3, sigma=8.0, learning_rate=0.5, neighborhood_function="bubble")

som.train_random(colors, 500, verbose=True)
plt.imshow(abs(som.get_weights()), interpolation="none")
```

- **OUTPUT**

![MSCIT_SCTprac6A](https://user-images.githubusercontent.com/88243315/214326134-670a3db6-06e4-4b5a-82fc-c716889c7c4e.png)

**************

## Prac6B

- 6B. Hopfield network.

```python
# 6B. Hopfield network.

from neurodynex.hopfield_network import network, pattern_tools, plot_tools
import matplotlib.pyplot as plt

pattern_size = 5
# create an instance of the class HopfieldNetwork
hopfield_net = network.HopfieldNetwork(nr_neurons=pattern_size ** 2)
# instantiate a pattern factory
factory = pattern_tools.PatternFactory(pattern_size, pattern_size)

# create a checkerboard pattern and add it to the pattern list
checkerboard = factory.create_checkerboard()
pattern_list = [checkerboard]

# add random patterns to the list
pattern_list.extend(
    factory.create_random_pattern_list(nr_patterns=3, on_probability=0.5)
)
plot_tools.plot_pattern_list(pattern_list)

# how similar are the random patterns and the checkerboard? Check the overlaps
overlap_matrix = pattern_tools.compute_overlap_matrix(pattern_list)
plot_tools.plot_overlap_matrix(overlap_matrix)

# let the hopfield network "learn" the patterns. Note: they are not stored
# explicitly but only network weights are updated !
hopfield_net.store_patterns(pattern_list)

# create a noisy version of a pattern and use that to initialize the network
noisy_init_state = pattern_tools.flip_n(checkerboard, nr_of_flips=4)
hopfield_net.set_state_from_pattern(noisy_init_state)

# from this initial state, let the network dynamics evolve.
states = hopfield_net.run_with_monitoring(nr_steps=4)

# each network state is a vector. reshape it to the same shape used to create the patterns.
states_as_patterns = factory.reshape_patterns(states)

# plot the states of the network
plot_tools.plot_state_sequence_and_overlap(
    states_as_patterns, pattern_list, reference_idx=0, suptitle="Network dynamics"
)
```

- **OUTPUT**

![MSCIT_SCTprac6B_1](https://user-images.githubusercontent.com/88243315/214326203-475d9c82-2eda-4413-bc58-1ef005a004f2.png)
![MSCIT_SCTprac6B_2](https://user-images.githubusercontent.com/88243315/214326230-06f81d01-480d-4d8b-8295-a2dbc8a0ab98.png)

**************

## Prac7A-i

- 7A-i. Implement membership and identity operators *in*

```python
# 7A-i. Implement membership and identity operators *in*.

list1 = []
print("Enter 5 numbers")
for i in range(0, 5):
    v = int(input())
    list1.append(v)
list2 = []
print("Enter 5 numbers")
for i in range(0, 5):
    v = int(input())
    list2.append(v)
flag = 0
for i in list1:
    if i in list2:
        flag = 1
if flag == 1:
    print("The Lists Overlap")
else:
    print("The Lists do Not overlap")
```

- **OUTPUT**

![MSCIT_SCTprac7A_i](https://user-images.githubusercontent.com/88243315/214326287-d24dd785-6f54-4be1-b009-b5f1e92eeed8.png)


**************

## Prac7A-ii

- 7A-ii. Implement membership and identity operators *not in*

```python
# 7A-ii. Implement membership and identity operators *not in*.

list1 = []
c = int(input("Enter the number of elements that you want to insert in List 1:"))
for i in range(0, c):
    ele = int(input("Enter the element :"))
    list1.append(ele)
a = int(input("enter the number that you want to find in List 1:"))
if a not in list1:
    print("The list does not contain ", a)
else:
    print("The list contains", a)
```

- **OUTPUT**

![MSCIT_SCTprac7A_ii](https://user-images.githubusercontent.com/88243315/214326329-776f1261-9f0e-450c-b7a7-2b185767c1b0.png)

**************

## Prac7B-i

- 7B-i. Implement membership and identity operators *is*.

```python
# 7B-i. Implement membership and identity operators *is*.

details = []
name = input("Enter your name : ")
details.append(name)
age = float(input("Enter your exact age : "))
details.append(age)
roll_no = int(input("Enter your roll no : "))
details.append(roll_no)
for i in details:
    print(i)
    print("Int = ", type(i) is int)
    print("Float = ", type(i) is float)
    print("String = ", type(i) is str)
    print()
```

- **OUTPUT**

![MSCIT_SCTprac7B_i](https://user-images.githubusercontent.com/88243315/214326419-5f74dcd3-eaee-4408-9616-7e74694f6ad2.png)

**************

## Prac7B-ii

- 7B-ii. Implement membership and identity operators *is not*.

```python
# 7B-ii. Implement membership and identity operators *is not*.

details = []
name = input("Enter your name : ")
details.append(name)
age = float(input("Enter your exact age : "))
details.append(age)
roll_no = int(input("Enter your roll no : "))
details.append(roll_no)
print()
for i in details:
    print(i)
    print("Not Int = ", type(i) is not int)
    print("Not Float = ", type(i) is not float)
    print("Not String = ", type(i) is not str)
    print()
```

- **OUTPUT**

![MSCIT_SCTprac7B_ii](https://user-images.githubusercontent.com/88243315/214326463-e7c6ded8-eb23-4a2b-94f9-185fa41d682f.png)

**************

## Prac8A

- 8A. Find ratios using fuzzy logic.

```python
# 8A. Find ratios using fuzzy logic.

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

s1 = "My name is ABC"
s2 = "I am ABC"
print("FuzzyWuzzy Ratio:", fuzz.ratio(s1, s2))
print("FuzzyWuzzy PartialRatio: ", fuzz.partial_ratio(s1, s2))
print("FuzzyWuzzy TokenSortRatio: ", fuzz.token_sort_ratio(s1, s2))
print("FuzzyWuzzy TokenSetRatio: ", fuzz.token_set_ratio(s1, s2))
print("FuzzyWuzzy WRatio: ", fuzz.WRatio(s1, s2), "\n\n")

# for process library,
query = "fuzzys for fuzzys"
choices = ["fuzzy for fuzzy", "fuzzy fuzzy", "g. for fuzzys"]
print("List of ratios: ")
print(process.extract(query, choices), "\n")
print("Best among the above list: ", process.extractOne(query, choices))
```

- **OUTPUT**

![MSCIT_SCTprac8A](https://user-images.githubusercontent.com/88243315/214326514-e6e281ae-1660-4216-958c-36720c3f803d.png)


**************

## Prac8B

- 8B. Solve tipping problem using fuzzy logic.

```python
# 8B. Solve tipping problem using fuzzy logic.
# google.colab
!pip install fuzzywuzzy
!pip install -U scikit-fuzzy

import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

quality.automf(3)
service.automf(3)

tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

quality['average'].view()
service.view()
tip.view()

rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(service['good'] | quality['good'], tip['high'])

rule1.view()

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['quality'] = 6.5
tipping.input['service'] = 9.8

tipping.compute()
print (tipping.output['tip'])
tip.view(sim=tipping)
```

- **OUTPUT**

![MSCIT_SCTprac8B_1](https://user-images.githubusercontent.com/88243315/214326567-4ae3e324-0e7c-4704-8c65-f1e5592aac25.png)
![MSCIT_SCTprac8B_2](https://user-images.githubusercontent.com/88243315/214326597-4bb472cb-4495-48e3-a36a-ca9b37c23774.png)
![MSCIT_SCTprac8B_3](https://user-images.githubusercontent.com/88243315/214326618-160d3535-1664-481a-8513-624327dc634f.png)
![MSCIT_SCTprac8B_4](https://user-images.githubusercontent.com/88243315/214326629-0c1ea3dc-db2e-4647-9914-9e60dbe0e32f.png)
![MSCIT_SCTprac8B_5](https://user-images.githubusercontent.com/88243315/214326647-6b5eb8e7-64ab-4d30-93ec-6d902e99f3d3.png)


**************

### [Go To Top](#soft-computing-techniques)