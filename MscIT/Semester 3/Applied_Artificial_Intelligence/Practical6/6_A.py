# AAI 6A)	AIM: Design a Fuzzy based operations using Python / R.

A = dict()
B = dict()
Y = dict()

# Initialize the dictionaries for fuzzy sets A, B, and the result
A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}
result = {}

# Display the fuzzy sets A and B
print('The First Fuzzy Set is:', A)
print('The Second Fuzzy Set is:', B)

# Fuzzy Set Union
for i in A:
    if A[i] > B[i]:
        result[i] = A[i]
    else:
        result[i] = B[i]
print("Union of two sets is", result)

# Fuzzy Set Intersection
result = {}
for i in A:
    if A[i] < B[i]:
        result[i] = A[i]
    else:
        result[i] = B[i]
print("Intersection of two sets is", result)

# Fuzzy Set Complement
result = {}
for i in A:
    result[i] = round(1 - A[i], 2)
print("Complement of First set is", result)

# Fuzzy Set Difference
result = {}
for i in A:
    result[i] = round(min(A[i], 1 - B[i]), 2)
print("Difference of two sets is", result)

