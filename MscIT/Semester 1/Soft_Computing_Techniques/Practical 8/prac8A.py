# 8A. Find ratios using fuzzy logic.

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

s1 = "My name is ABC"
s2 = "I am ABC"
print("FuzzyWuzzy Ratio:", fuzz.ratio(s1, s2))
print("FuzzyWuzzy PartialRatio: ", fuzz.partial_ratio(s1, s2))
print("FuzzyWuzzy TokenSortRatio: ", fuzz.token_sort_ratio(s1, s2))
print("FuzzyWuzzy TokenSetRatio: ", fuzz.token_set_ratio(s1, s2))
print("FuzzyWuzzy WRatio: ", fuzz.WRatio(s1, s2), "\n\n")

# for process library,
query = "fuzzys for fuzzys"
choices = ["fuzzy for fuzzy", "fuzzy fuzzy", "g. for fuzzys"]
print("List of ratios: ")
print(process.extract(query, choices), "\n")
print("Best among the above list: ", process.extractOne(query, choices))

