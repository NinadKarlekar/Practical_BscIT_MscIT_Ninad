# Install required packages
# !pip install torch==1.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
# !pip install inltk
# !pip install tornado==4.5.3

# Setup for Gujarati language
from inltk.inltk import setup
setup('gu')

# Import identify_language from inltk
from inltk.inltk import identify_language

# Identify the language of the given text
# output = identify_language('બીના કાપડિયા')
output = identify_language('निनाद कार्लेकर')



# Print the identified language
print(output)
