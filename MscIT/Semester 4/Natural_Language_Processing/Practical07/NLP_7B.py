# 7B. Accept the input string with Regular expression of FA: 101+

def FA(s):
    # If the length is less than 3, then it can't be accepted. Therefore, end the process.
    if len(s) < 3:
        return "Rejected"
    # The first three characters are fixed. Therefore, checking them using index.
    if s[0] == '1':
        if s[1] == '0':
            if s[2] == '1':
                # After index 2, only "1" can appear. Therefore, break the process if any other character is detected.
                for i in range(3, len(s)):
                    if s[i] != '1':
                        return "Rejected"
                return "Accepted"  # if all conditions are true
            return "Rejected"  # else of 3rd if
        return "Rejected"  # else of 2nd if
    return "Rejected"  # else of 1st if

inputs = ['1', '10101', '101', '10111', '01010', '100', '', '10111101', '1011111']
for i in inputs:
    print(FA(i))



############# Another method ##############
'''

################################

# Accept the input string with Regular expression of FA 101.txt
import re

def validate_string(input_string):
    # Define the regular expression pattern
    pattern = r'^101+$'

    # Check if the input string matches the pattern
    if re.match(pattern, input_string):
        return True
    else:
        return False

# Accept user input
input_string = input("Enter a string: ")

# Validate the input string
if validate_string(input_string):
    print("The input string is valid and matches the pattern 101+.")
else:
    print("The input string is invalid and does not match the pattern 101+.")

# Example inputs:
# Valid: "101", "10101", "1010101", etc.
# Invalid: "1001", "111", "1010", etc.

'''