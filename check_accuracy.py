import numpy

train_size=960000
test_size=2000

max_distance=1
gamma=0.01

##dictionary used
vocabulary={}
bi_table={}
tri_table={}

##filling vocabulary{}
file_vocab=open('vocabulary.txt','r')
while(1):
    get_line=file_vocab.readline()
    if(get_line==''):
        break
    get_words=get_line.split()
    vocabulary[get_words[0]]=int(get_words[1])
    vocabulary['unknown']=58417315                  ## it is frequency of unknown word in training data
    print('vocabulary built\n')
    file_vocab.close()


	
