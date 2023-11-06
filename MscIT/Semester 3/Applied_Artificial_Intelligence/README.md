# Applied Artificial Intelligence

M. Sc (Information Technology)
Applied Artificial Intelligence



## Index

| Sr.No. | Name | README | DOWNLOAD |
| --- | --- | --- | --- |
| [Prac1A](/MscIT/Semester%203/Applied_Artificial_Intelligence/Practical1/) <br> [Prac1B](/MscIT/Semester%203/Applied_Artificial_Intelligence/Practical1/) | 1A.Design An Expert System using AIML <br> 1B. Design An Expert System using AIML. | [Prac1A](#prac1A) <br> [Prac1B](#prac1B) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Applied_Artificial_Intelligence/Practical1/1_A.py) <br> [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Applied_Artificial_Intelligence/Practical1/1_B.py) |
| [Prac2](/MscIT/Semester%203/Applied_Artificial_Intelligence/Practical2/) | Design a Chatbot using AIML | [Prac2](#prac2) | |
| [Prac3A](/MscIT/Semester%203/Applied_Artificial_Intelligence/Practical3/) <br> [Prac3B](/MscIT/Semester%203/Applied_Artificial_Intelligence/Practical3/) | 3A. Implement Bayes Theorem using Python. <br> 3B. Bayes Theorem. | [Prac3A](#prac3A) <br> [Prac3B](#prac3B) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Applied_Artificial_Intelligence/Practical3/3_A.py) <br> [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Applied_Artificial_Intelligence/Practical3/3_B.py) |
| [Prac4A](/MscIT/Semester%204/Applied_Artificial_Intelligence/Practical4/) <br> [Prac4B](/MscIT/Semester%204/Applied_Artificial_Intelligence/Practical4/) | 4A. Write an application to implement DFS algorithm. <br> 4B. Write an application to implement BFS algorithm. | [Prac4A](#prac4A) <br> [Prac4B](#prac4B) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Applied_Artificial_Intelligence/Practical4/4_A.py) <br> [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Applied_Artificial_Intelligence/Practical4/4_B.py) |
| [Prac5A](/MscIT/Semester%205/Applied_Artificial_Intelligence/Practical5/) <br> [Prac5B](/MscIT/Semester%205/Applied_Artificial_Intelligence/Practical5/) | 5A. Rule Based System. <br> 5B. Rule Based System. | [Prac5A](#prac5A) <br> [Prac5B](#prac5B) |   |
| [Prac6A](/MscIT/Semester%206/Applied_Artificial_Intelligence/Practical6/) <br> [Prac6B](/MscIT/Semester%206/Applied_Artificial_Intelligence/Practical6/) | 6A. Design a Fuzzy based operations using Python / R. <br> 6B. Design a Fuzzy based application using Python / R. | [Prac6A](#prac6A) <br> [Prac6B](#prac6B) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Applied_Artificial_Intelligence/Practical6/6_A.py) <br> [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Applied_Artificial_Intelligence/Practical6/6_B.py) |
| [Prac7A](/MscIT/Semester%207/Applied_Artificial_Intelligence/Practical7/) <br> [Prac7B](/MscIT/Semester%207/Applied_Artificial_Intelligence/Practical7/) | 7A. Implement joint probability using Python. <br> 7B. Implement Conditional Probability using Python. | [Prac7A](#prac7A) <br> [Prac7B](#prac7B) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Applied_Artificial_Intelligence/Practical7/7_A.py) <br> [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Applied_Artificial_Intelligence/Practical7/7_B.py) |
| [Prac8A](/MscIT/Semester%208/Applied_Artificial_Intelligence/Practical8/) <br> [Prac8B](/MscIT/Semester%208/Applied_Artificial_Intelligence/Practical8/) | 8A.  <br> 8B.  | [Prac8A](#prac8A) <br> [Prac8B](#prac8B) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Applied_Artificial_Intelligence/Practical8/8_A.py) <br> [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Applied_Artificial_Intelligence/Practical8/8_B.py) |
| [Prac9](/MscIT/Semester%203/Applied_Artificial_Intelligence/Practical9/) | 9. SUPERVISED LEARNING METHODS USING PYTHON| [Prac9](#prac9) | |

******************
---------------------

## Prac1A

1. Design An Expert System using AIML.


<details>
<summary>CODE</summary>


```python

# Design An Expert System using AIML

# An Expert system for responding the patient query for identifying the flu.

# Create an empty list to store information
info = []

# Input the user's name and add it to the 'info' list
name = input("Enter Your name: ")
info.append(name)

# Input the user's age as an integer and add it to the 'info' list
age = int(input("Enter Your age: "))
info.append(age)

# Lists of common symptoms for Malaria and Diabetes
a = ["Fever", "Headache", "Tiredness", "Vomiting"]
b = ["Urinate A Lot", "Feels Thirsty", "Weight Loss", "Blurry Vision", "Feels Very Hungry", "Feels Very Tired"]

# Print the lists of symptoms
print("Common Symptoms for Malaria:", a)
print("Common Symptoms for Diabetes:", b)

# Input symptoms separated by a comma and split them into a list
symp = input("Enter Symptoms As Above Separated By Comma: ")
lst = symp.split(",")

# Print the user's information
print("User Information:")
print("Name:", info[0])
print("Age:", info[1])

print("Symptoms:")
# Loop through the list of symptoms and print each one
for symptom in lst:
    print(symptom.strip())

# Check if any symptom matches the symptoms for Malaria or Diabetes
for symptom in lst:
    if symptom.strip() in a:
        print("You May Have Malaria")
        print("Please Visit A Doctor")
        break
    elif symptom.strip() in b:
        print("You May Have Diabetes")
        print("Consider Reducing Sugar Intake")
        break
else:
    print("Symptoms Do Not Match Common Health Conditions")


```

</details>

******************************************************

## Prac1B

1. Design An Expert System using AIML 2.


<details>
<summary>CODE</summary>


```python

# Design An Expert System using AIML

# Input user's name
name = input("Enter your name: ")

# Input whether the user has a fever, cough, shortness of breath, sore throat, muscle pain, and headache (Y/N)
fever = input("DO YOU HAVE fever (Y/N)").lower()
cough = input("DO YOU HAVE cough (Y/N)").lower()
sob = input("DO YOU HAVE shortness of breath (Y/N)").lower()
st = input("DO YOU HAVE sore throat (Y/N)").lower()
mp = input("DO YOU HAVE muscle pain (Y/N)").lower()
hc = input("DO YOU HAVE headache(Y/N)").lower()

# Input whether the user has diarrhea, conjunctivitis, loss of taste, chest pain or pressure, and loss of speech or movement (Y/N)
diarrhoea = input("DO YOU HAVE diarrhea (Y/N)").lower()
conjunctivitis = input("DO YOU HAVE conjunctivitis (Y/N)").lower()
lot = input("DO YOU HAVE Loss OF taste (Y/N)").lower()
cp = input("DO YOU HAVE chest pain or pressure (Y/N)").lower()
lsp = input("DO YOU HAVE Loss Of Speech or movement (Y/N)").lower()

# Check for different conditions based on symptoms
if fever == "y" and cough == "y" and sob == "y" and st == "y" and mp == "y" and hc == "y":
    print(name + " YOU HAVE FLU")
    med = input("Sir/Ma'am would you like to look at some medicine for flu (Y/N)").lower()
    if med == "y":
        print("Disclaimer: Contact a doctor for better guidance")
        print("There are four FDA-approved antiviral drugs recommended by CDC to treat flu this season")
        print("1. Oseltamivir phosphate")
        print("2. Zanamivir")
        print("3. Peramivir")
        print("4. Baloxavir marboxil")
elif diarrhoea == "y" and st == "y" and fever == "y" and cough == "y" and conjunctivitis == "y" and lot == "y":
    print(name + " YOU HAVE CORONA")
    med = input("Sir/Ma'am would you like to look at some remedies for Corona (Y/N)").lower()
    if med == "y":
        print("TAKE VACCINE AND QUARANTINE")
elif fever == "y" and cough == "y":
    print(name + " YOU HAVE Common Cold")
    med = input("Sir/Ma'am would you like to look at some remedies for common cold (Y/N)").lower()
    if med == "y":
        print("Disclaimer: Contact a doctor for better guidance")
        print("Treatment consists of anti-inflammatories and decongestants")
        print("Most people recover on their own")
        print("1. Nonsteroidal anti-inflammatory drug")
        print("2. Analgesic")
        print("3. Antihistamine")
        print("4. Cough medicine")
        print("5. Decongestant")
else:
    print("Unable to identify")



```

</details>

******************************************************
