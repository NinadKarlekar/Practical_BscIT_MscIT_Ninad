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
