import math


def euclidean_distance(instance1, instance2, length):
    distance = 0

    for x in range(length):
            distance += pow(instance1[x] - instance2[x], 2)
    return math.sqrt(distance)


#data1 = [2, 2, 2, 'a']
#data2 = [4, 4, 4, 'b']
#distance = euclidean_distance(data1, data2, 3)

#print 'Distance: ' + repr(distance)
