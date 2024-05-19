# 10 b. Statistical parsing:
# 1. Usage of Give and Gave in the Penn Treebank sample.

import nltk
import nltk.parse.viterbi
import nltk.parse.pchart

def give(t):
    return (t.label() == 'VP' and len(t) > 2 and t[1].label() == 'NP' and 
            (t[2].label() == 'PP-DTV' or t[2].label() == 'NP') and 
            ('give' in t[0].leaves() or 'gave' in t[0].leaves()))

def sent(t):
    return ' '.join(token for token in t.leaves() if token[0] not in '*-0')

def print_node(t, width):
    output = "%s %s: %s / %s: %s" % (
        sent(t[0]), t[1].label(), sent(t[1]), t[2].label(), sent(t[2]))
    if len(output) > width:
        output = output[:width] + "..."
    print(output)

for tree in nltk.corpus.treebank.parsed_sents():
    for t in tree.subtrees(give):
        print_node(t, 72)
