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
