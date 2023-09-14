import csv

a = []
with open("book2.csv", "r") as csvfile:
    next(csvfile)
    for row in csv.reader(csvfile):
        a.append(row)

for x in a:
    print(x)

print("\nThe total number of training instances are : ", len(a))

num_attribute = len(a[0]) - 1
print("\nThe initial hypothesis is : ")
hypothesis = ["0"] * num_attribute
print(hypothesis)

for i in range(0, len(a)):
    if a[i][num_attribute] == "yes":
        print("\nInstance ", i + 1, "is", a[i], " and is Positive Instance")

        for j in range(0, num_attribute):
            if hypothesis[j] == "0" or hypothesis[j] == a[i][j]:
                hypothesis[j] = a[i][j]

            else:
                hypothesis[j] = "?"

        print(
            "The hypothesis for the training instance", i + 1, " is: ", hypothesis, "\n"
        )

    if a[i][num_attribute] == "no":
        print(
            "\nInstance ", i + 1, "is", a[i], " and is Negative Instance Hence Ignored"
        )

        print(
            "The hypothesis for the training instance", i + 1, " is: ", hypothesis, "\n"
        )

print("\nThe Maximally specific hypothesis for the training instance is ", hypothesis)
