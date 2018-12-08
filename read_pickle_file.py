import pickle

print('\n*****Bi Gram Table***** \n')
with open('bigram_table.pickle', 'rb') as handle:
    b = pickle.load(handle)

count = 0
for lines in b:
    print(lines)
    count = count + 1
    if (count > 20):
        break

print('\n*****Tri Gram Table***** \n')
with open('trigram_table.pickle', 'rb') as handle:
    b = pickle.load(handle)
for lines in b:
    print(lines)
    count = count + 1
    if (count > 40):
        break
