# NLP 3A. Study of Wordnet Dictionary with methods as synsets, definitions, examples, antonyms
# Import necessary libraries
import nltk
from nltk.corpus import wordnet

# Download WordNet (if not already downloaded)
nltk.download('wordnet')

# Get synsets (collection of synonyms) for "phone"
synsets = wordnet.synsets("phone")

# Print information about "phone"
print("**Word:** phone")
print("  * Synsets:")

# Loop through each synset and print its definition and examples
for synset in synsets:
    # Get the first word from the synset (considered the most representative)
    word = synset.lemmas()[0].name()
    print(f"      - Word: {word}")
    print(f"        - Definition: {synset.definition()}")
    print(f"          - Examples: {synset.examples()}")


print("-"*40)
# Get antonyms for "buy" (verb)
antonyms = wordnet.lemma('buy.v.01.buy').antonyms()

# Print antonyms for "buy"
print("\n**Antonyms for 'buy':")
for antonym in antonyms:
    print(f"  - {antonym.name()}")
