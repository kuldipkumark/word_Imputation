import pickle
from random import randint
import numpy

# Global settings
trainSize = 2000000
testSize = 1757
M = 1  # Maximum distance
gamma = 0.01

# Initialization
vocabulary = {}
bigram_table = {}
trigram_table = {}

# Read high-frequency words from vocabularyfile
fVocab = open('data/vocabulary-14216.txt', 'r')
while True:
    line = fVocab.readline()
    if line == '':
        break
    words = line.split()
    vocabulary[words[0]] = int(words[1])
vocabulary['UNKA'] = 58417315
print('vocabulary dictionary size: ' + str(len(vocabulary)))
fVocab.close()

# Statistics collection
f = open('data/train_v2.txt', 'r')
cnt = 0
a=0
while cnt < trainSize:
    line = f.readline()
    cnt = cnt + 1
    words = line.split()
    for k in range(0, len(words)):
        if words[k] not in vocabulary:
            words[k] = 'UNKA'
    for i in range(0, len(words)):
        for m in range(0, M + 1):
            if i + m + 1 >= len(words):
                break
            key = words[i] + ' ' + words[i + m + 1] + ' ' + str(m)
            if key in bigram_table:
                bigram_table[key] = bigram_table[key] + 1
            else:
                bigram_table[key] = 1
        if i <= len(words) - 3:
            key = words[i] + ' ' + words[i + 1] + ' ' + words[i + 2]
            if key in trigram_table:
                trigram_table[key] = trigram_table[key] + 1
            else:
                trigram_table[key] = 1
    if (cnt % 200000 == 0):
        print('milestone='+str(a)+'\n')
        a = a + 1
print('bigram  table size: ' + str(len(bigram_table)))
print('Trigram table size: ' + str(len(trigram_table)))


###using pickle
with open('vocabulary.pickle','wb') as handle:
    pickle.dump(vocabulary,handle,protocol=pickle.HIGHEST_PROTOCOL)
with open('bigram_table.pickle', 'wb') as handle:
    pickle.dump(bigram_table, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('trigram_table.pickle','wb') as handle:
    pickle.dump(trigram_table,handle,protocol=pickle.HIGHEST_PROTOCOL)
