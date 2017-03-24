import csv


def load_dataset(filename, training_set=[], test_set=[]):
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            for y in range(1, 17):
                dataset[x][y] = float(dataset[x][y])
        tmp = list(chunks(dataset, 16000))
        dataset = None
        training_set.append(tmp[0])
        test_set.append(tmp[1])
        

def chunks(list, chunk_size):
    for i in range(0, len(list), chunk_size):
        yield list[i:i+chunk_size]

#trainingSet = []
#testSet = []

#load_dataset('letter-recognition.data', trainingSet, testSet)
#print len(trainingSet)
#print len(testSet)




