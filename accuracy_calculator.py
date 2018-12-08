import numpy
from random import randint
import pickle

#fetching data in all dictionaries
with open('vocabulary.pickle', 'rb') as handle:
    vocabulary = pickle.load(handle)

with open('bigram_table.pickle', 'rb') as handle:
    bigram_table = pickle.load(handle)

with open('trigram_table.pickle', 'rb') as handle:
    trigram_table = pickle.load(handle)

### some variables
size=2000
f = open('data/train_v2.txt', 'r')
line = f.readline()
cnt = 0
cntLocation = 0
cntFilling = 0

###
while cnt < size:
    line = f.readline()

    # Sentence preprocessing

    words = line.split()
    if len(words) <= 2:  # Sentence too short, ignore!
        continue
    cnt = cnt + 1
    location = randint(1, len(
        words) - 2)  ### sentence mai se koi random word le liya usse trueWord variable mai store kar liya
    trueWord = words[location]  ### uss word ko delete kar diya
    del words[location]
    for k in xrange(0, len(words)):
        if words[k] not in vocab:
            words[k] = 'UNKA'  ### agar koi word vocabulary mai nahi ha then usko UNKA se replace kar do
