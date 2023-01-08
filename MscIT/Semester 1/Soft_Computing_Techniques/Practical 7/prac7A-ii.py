# 7A-ii. Implement membership and identity operators *not in*

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