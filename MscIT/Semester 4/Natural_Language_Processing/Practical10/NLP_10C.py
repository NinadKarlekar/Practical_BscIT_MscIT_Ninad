# c. Malt parsing: i. Parse a sentence and draw a tree using malt parsing

# Copy maltparser-1.7.2 (unzipped version) and engmalt.linear-1.7.mco files to
# C:\Users\Beena Kapadia\AppData\Local\Programs\Python\Python39 folder
# Java should be installed
# Environment variables should be set:
# MALT_PARSER - C:\Users\Beena Kapadia\AppData\Local\Programs\Python\Python39\maltparser-1.7.2
# MALT_MODEL - C:\Users\Beena Kapadia\AppData\Local\Programs\Python\Python39\engmalt.linear-1.7.mco

from nltk.parse import malt

mp = malt.MaltParser('maltparser-1.7.2', 'engmalt.linear-1.7.mco')
t = mp.parse_one('I saw a bird from my window.'.split()).tree()
print(t)
t.draw()
