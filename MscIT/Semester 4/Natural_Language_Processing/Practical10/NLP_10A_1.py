# 10. Speech Tagging
## a_1. Speech tagging using spacy

import spacy

sp = spacy.load('en_core_web_sm')
sen = sp(u"I like to play Table tennis. I hated it in my childhood though")

print(sen.text)
print(sen[7].pos_)
print(sen[7].tag_)
print(spacy.explain(sen[7].tag_))

for word in sen:
    print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')

sen = sp(u'Can you google it?')
word = sen[2]
print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')

sen = sp(u'Can you search it on google?')
word = sen[5]
print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')

# Finding the Number of POS Tags
sen = sp(u"I like to play Table tennis. I hated it in my childhood though")
num_pos = sen.count_by(spacy.attrs.POS)
num_pos

for k,v in sorted(num_pos.items()):
    print(f'{k}. {sen.vocab[k].text:{8}}: {v}')

# Visualizing Parts of Speech Tags
from spacy import displacy

sen = sp(u"I like to play Table tennis. I hated it in my childhood though")
displacy.serve(sen, style='dep', options={'distance': 120}, port=8000)

