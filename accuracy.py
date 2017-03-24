def accuracy(test_set, predictions):
    correct = 0
    for x in range(len(test_set)):
        if test_set[x][-1] is predictions[x]:
            correct += 1
    return (correct/float(len(test_set))) * 100.0


#test = [[1, 1, 1, 'a'], [2, 2, 2, 'a'], [3, 3, 3, 'b']]
#predict = ['a', 'a', 'a']
#acc = accuracy(test, predict)
#print acc

