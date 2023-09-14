import csv

num_attributes = 6
a = []

print("\n The Given Training Dataset \n")
with open("Book1.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    for row in reader:
        if count == 0:
            print(row)
            count += 1
        else:
            a.append(row)
            print(row)
            count += 1

print("\n The initial value of hypothesis: ")
hypothesis = ["0"] * num_attributes
print(hypothesis)

for j in range(0, num_attributes):
    hypothesis[j] = a[0][j]
    print(hypothesis)

print("\n find S:finding a Maximally specific Hypothesis\n")
for i in range(0, len(a)):
    if a[i][num_attributes] == "Yes":
        for j in range(0, num_attributes):
            if a[i][j] != hypothesis[j]:
                hypothesis[j] = "?"
            else:
                hypothesis[j] = a[i][j]
    print("for training example no :{0} the hypothesis is".format(i), hypothesis)

print(hypothesis)
