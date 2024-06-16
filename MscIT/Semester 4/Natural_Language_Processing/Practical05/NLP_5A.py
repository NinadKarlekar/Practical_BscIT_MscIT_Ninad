## 5A. Word tokenization in Hindi

# cd "e:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 4/Natural_Language_Processing/Practical05/" for VSCODE terminal

# Clone the Indic NLP Library and Resources

# !git clone https://github.com/anoopkunchukuttan/indic_nlp_library.git
# !git clone https://github.com/anoopkunchukuttan/indic_nlp_resources.git

import sys
import os

#!pip install indic
# !pip install indic-nlp-library

# The path to the local git repo for Indic NLP library
INDIC_NLP_LIB_HOME = 'indic_nlp_library'

# The path to the local git repo for Indic NLP Resources
INDIC_NLP_RESOURCES = 'indic_nlp_resources'

# Add library to Python path
sys.path.append(os.path.join(INDIC_NLP_LIB_HOME, 'src'))

# Verify if the path was added correctly
print(sys.path)

# Set environment variable for resources folder
from indicnlp import common
common.set_resources_path(INDIC_NLP_RESOURCES)

from indicnlp.tokenize import indic_tokenize

indic_string = 'सुनो, कुछ आवाज़ आ रही है। फोन?'
print('Input String: {}'.format(indic_string))
print('Tokens: ')
for t in indic_tokenize.trivial_tokenize(indic_string):
    print(t)