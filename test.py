import pickle
import collections
import numpy
import re

def fetch_data():
    #fetching data in all dictionaries
    with open('vocabulary.pickle', 'rb') as handle:
        vocabulary = pickle.load(handle)

    with open('bigram_table.pickle', 'rb') as handle:
        bigram_table = pickle.load(handle)

    with open('trigram_table.pickle', 'rb') as handle:
        trigram_table = pickle.load(handle)

    return vocabulary, bigram_table, trigram_table

# for i in vocabulary:
#     print(i+str(vocabulary[i]))

### locating missing word
def locate_missin_word(sentence, vocabulary, bigram_table, trigram_table):

    trainSize = 200
    testSize = 527
    M = 1               #Maximum distance
    gamma = 0.01

    line=sentence
    #fR.write('id,"sentence"\n')
    cnt = 1

        # Sentence preprocessing
    score_dict={}
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
    #print('missing word location= '+str(location))


    for word in vocabulary:
        if word == 'UNKA':
            continue
        score = 0
        key = words[location - 1] + ' ' + word + ' ' + str(0)
        if key in bigram_table:
            score = score + 0.25 * bigram_table[key] / vocabulary[words[location - 1]]
            if location - 2 >= 0:
                key = words[location - 2] + ' ' + words[location - 1] + ' ' + word
                if key in trigram_table:
                    score = score + 0.5 * trigram_table[key] / bigram_table[
                        words[location - 2] + ' ' + words[location - 1] + ' ' + str(0)]
        key = word + ' ' + words[location] + ' ' + str(0)
        if key in bigram_table:
            score = score + 0.25 * bigram_table[key] / vocabulary[words[location]]
            if location + 1 < len(words):
                key = word + ' ' + words[location] + ' ' + words[location + 1]
                if key in trigram_table:
                    score = score + 0.5 * trigram_table[key] / bigram_table[
                        words[location] + ' ' + words[location + 1] + ' ' + str(0)]
            key = words[location - 1] + ' ' + word + ' ' + words[location]
            if key in trigram_table:
                score = score + 1.0 * trigram_table[key] / bigram_table[
                    words[location - 1] + ' ' + words[location] + ' ' + str(1)]
            score_dict[score] = word
    result=[]
    score_dict = collections.OrderedDict(sorted(score_dict.items()))
    for key in list(reversed(list(score_dict)))[0:5]:
        a = wordsOriginal.copy()
        a.insert(location, score_dict[key])
        b = ' '.join(a)
        result.append(b)
    return result, location
    # print('correct sentence = ' + ' '.join(wordsOriginal))
    # print('\n')