import load_data_set as data
import neighbors as ns
import response as rs
import accuracy as acc


def main():
    training_set, test_set = data.load_dataset('formatted_file.data')

    print('Train Set: ' + repr(len(training_set)))
    print('Test Set: ' + repr(len(test_set)))

    predictions = []
    k = 3
    for x in range(len(test_set)):
        neighbors = ns.get_neighbors(training_set, test_set[x], k)
        result = rs.get_response(neighbors)
#        print('> predicted = ' + repr(result) + ', actual = ' + repr(test_set[x][-1]))
    accuracy = acc.accuracy(test_set, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')


main()
