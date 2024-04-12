#d. Write a program using python to find synonym and antonym of word "active" using Wordnet.

from nltk.corpus import wordnet as wn

def compare_nouns(noun1, noun2):
    # Get synsets for each noun
    synsets1 = wn.synsets(noun1, pos=wn.NOUN)
    synsets2 = wn.synsets(noun2, pos=wn.NOUN)
    
    if not synsets1 or not synsets2:
        return "Unable to compare. Make sure both nouns are valid." 
    
    max_wup_similarity = 0
    max_path_similarity = 0
    
    for synset1 in synsets1:
        for synset2 in synsets2:
            # Calculate Wu-Palmer Similarity
            wup_similarity = synset1.wup_similarity(synset2)
            if wup_similarity is not None and wup_similarity > max_wup_similarity:
                max_wup_similarity = wup_similarity
            
            # Calculate Path Similarity
            path_similarity = synset1.path_similarity(synset2)
            if path_similarity is not None and path_similarity > max_path_similarity:
                max_path_similarity = path_similarity
    
    return max_wup_similarity, max_path_similarity

if __name__ == "__main__":
    noun1 = input("Enter the first noun: ")
    noun2 = input("Enter the second noun: ") 
    
    wup_similarity_score, path_similarity_score = compare_nouns(noun1, noun2)
    
    print(f"The Wu-Palmer Similarity between '{noun1}' and '{noun2}' is: {wup_similarity_score}")
    print(f"The Path Similarity between '{noun1}' and '{noun2}' is: {path_similarity_score}")
