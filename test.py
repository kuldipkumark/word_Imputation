import pickle
import numpy
import re


trainSize = 200
testSize = 527
M = 1               # Maximum distance
gamma = 0.01



#fetching data in all dictionaries
with open('vocabulary.pickle', 'rb') as handle:
    vocabulary = pickle.load(handle)

with open('bigram_table.pickle', 'rb') as handle:
    bigram_table = pickle.load(handle)

with open('trigram_table.pickle', 'rb') as handle:
    trigram_table = pickle.load(handle)

# for i in vocabulary:
#     print(i+str(vocabulary[i]))


