# 7B-ii. Implement membership and identity operators is not

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

