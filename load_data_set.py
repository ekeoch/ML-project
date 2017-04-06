import csv


def load_dataset(filename):
    with open(filename, 'rt') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            #exclude string in iteration
            for y in range(0, 16):
                dataset[x][y] = float(dataset[x][y])
        return dataset[slice(0, 16000)] , dataset[slice(16000, 20000)]

#trainingSet = []
#testSet = []

#load_dataset('letter-recognition.data', trainingSet, testSet)
#print len(trainingSet)
#print len(testSet)




