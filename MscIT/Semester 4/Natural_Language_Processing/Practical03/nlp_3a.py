# Import necessary libraries
import nltk
from nltk.corpus import wordnet

# Download WordNet (if not already downloaded)
nltk.download('wordnet')

# Get synsets (collection of synonyms) for "computer"
synsets = wordnet.synsets("computer")

# Print information about "computer"
print("**Word:** computer")
print("  * Synsets:")

# Loop through each synset and print its definition and examples
for synset in synsets:
    print(f"      - Definition: {synset.definition()}")
    print(f"        - Examples: {synset.examples()}")

# Get antonyms for "buy" (verb)
antonyms = wordnet.lemma('buy.v.01.buy').antonyms()

# Print antonyms for "buy"
print("\n**Antonyms for 'buy':")
for antonym in antonyms:
    print(f"  - {antonym.name()}")
