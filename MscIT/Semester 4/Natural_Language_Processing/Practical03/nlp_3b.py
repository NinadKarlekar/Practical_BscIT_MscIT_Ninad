# NLP 3B Study lemmas, hyponyms, hypernyms.

# Import necessary libraries
import nltk
from nltk.corpus import wordnet

# Download WordNet (if not already downloaded)
nltk.download('wordnet')

# Exploring Lemmas
print("\n**Lemmas**")
synsets = wordnet.synsets("computer")
print("  * Synsets and Lemmas:")
for synset in synsets:
    lemma_names = [lemma.name() for lemma in synset.lemmas()]
    print(f"      - Synset: {synset} --> Lemmas: {lemma_names}")

# Exploring Hyponyms
print("\n**Hyponyms**")
computer_synset = wordnet.synset("computer.n.01")
hyponyms = computer_synset.hyponyms()
print("  * Hyponyms of 'computer.n.01':")
for synset in hyponyms:
    lemma_names = [lemma.name() for lemma in synset.lemmas()]
    print(f"      - Synset: {synset} --> Lemmas: {lemma_names}")

# Exploring Hypernyms
print("\n**Hypernyms**")
vehicle_synset = wordnet.synset("vehicle.n.01")
car_synset = wordnet.synset("car.n.01")
lowest_common_hypernym = car_synset.lowest_common_hypernyms(vehicle_synset)
print(f"  * Lowest common hypernym of 'vehicle' and 'car': {lowest_common_hypernym[0]}")
