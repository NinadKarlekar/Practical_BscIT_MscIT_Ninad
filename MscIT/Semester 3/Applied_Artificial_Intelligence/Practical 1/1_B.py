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
