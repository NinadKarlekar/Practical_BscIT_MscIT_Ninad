# 7C. Accept the input string with Regular expression of FA: (a+b)*bba

def FA(s):
    size = 0
    # Scan complete string and make sure that it contains only 'a' & 'b'
    for i in s:
        if i == 'a' or i == 'b':
            size += 1
        else:
            return "Rejected"
    # After checking that it contains only 'a' & 'b'
    # Check its length, it should be at least 3
    if size >= 3:
        # Check the last 3 elements
        if s[size - 3] == 'b':
            if s[size - 2] == 'b':
                if s[size - 1] == 'a':
                    return "Accepted"  # if all 4 if true
                return "Rejected"  # else of 4th if
            return "Rejected"  # else of 3rd if
        return "Rejected"  # else of 2nd if
    return "Rejected"  # else of 1st if

inputs = ['bba', 'ababbba', 'abba', 'abb', 'baba', 'bbb', '']
for i in inputs:
    print(FA(i))


########################## OR  ######################

'''

# Accept the input string with Regular expression of FA a b bba.txt
import re

def validate_string(input_string):
    # Define the regular expression pattern
    pattern = r'^(a|b)*bba$'

    # Check if the input string matches the pattern
    if re.match(pattern, input_string):
        return True
    else:
        return False

# Accept user input
input_string = input("Enter a string: ")

# Validate the input string
if validate_string(input_string):
    print("The input string is valid and matches the pattern (a+b)*bba.")
else:
    print("The input string is invalid and does not match the pattern (a+b)*bba.")

'''

# Example inputs:
# Valid: "bba", "abbbba", "abbba", "aaaaabbbba", etc.
# Invalid: "ba", "abbb", "ababba", "bbbbaa", etc.
