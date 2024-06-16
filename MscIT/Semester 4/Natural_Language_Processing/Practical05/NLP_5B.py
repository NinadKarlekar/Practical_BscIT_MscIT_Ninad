## 5B. Generate similar sentences from a given Hindi text input.

synonyms = {
    "खुश": ["प्रसन्न", "आनंदित", "खुशी"],
    "बहुत": ["अधिक", "बहुत ज्यादा", "काफी"]
}
 
# Function to generate similar sentences by replacing some words with synonyms
def generate_similar_sentences(input_sentence, num_sentences=5):
    similar_sentences = []
 
    # Replace some words with synonyms 
    for word, word_synonyms in synonyms.items():
        for synonym in word_synonyms:
            modified_sentence = input_sentence.replace(word, synonym)
            similar_sentences.append(modified_sentence)
    return similar_sentences[:num_sentences]
 
input_sentence = "मैं आज बहुत खुश हूँ।"
similar_sentences = generate_similar_sentences(input_sentence)
print("Original sentence:", input_sentence)
print("Similar sentences:")
for sentence in similar_sentences:
    print("-", sentence)
