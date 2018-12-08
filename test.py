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

### locating missing word
while(1):
        print('input sentence= ')
        line=input()
        #fR.write('id,"sentence"\n')
        cnt = 1

            # Sentence preprocessing
        words = line.split()

        wordsOriginal = words[:]
        for k in range(0,len(words)):
            if words[k] not in vocabulary:
                words[k] = 'UNKA'

        # Missing word location
        score = numpy.zeros(len(words)-1)
        for k in range(1,len(words)):
            key = words[k-1] + ' ' + words[k] + ' ' + str(0)
            if key in bigram_table:
                numNeg = bigram_table[key]
            else:
                numNeg = 0
            key = words[k-1] + ' ' + words[k] + ' ' + str(1)
            if key in bigram_table:
                numPos = bigram_table[key]
            else:
                numPos = 0
            if numNeg+numPos!=0:
                if words[k-1]=='UNKA' or words[k]=='UNKA':
                    score[k-1] = 1.0*numPos/(numNeg+numPos) - 1.0*numNeg/(numNeg+numPos)
                else:
                    score[k-1] = 1.0*numPos**(1+gamma)/(numNeg+numPos) - 1.0*numNeg**(1+gamma)/(numNeg+numPos)
        location = numpy.argmax(score) + 1
        print('missing word location= '+str(location))
