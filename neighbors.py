import operator
import euclideanDistance


def get_neighbors(training_set, test_instance, k):
    distances = []
    length = len(test_instance) - 1
    for x in range(len(training_set)):
        dist = euclideanDistance.euclidean_distance(test_instance, training_set[x], length)
        distances.append((training_set, dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


#train_set = [[2, 2, 2, 'a'], [4, 4, 4, 'b']]
#test_inst = [5, 5, 5]

#neighborss = get_neighbors(train_set, test_inst, 1)
#print(neighborss)
