import csv
with open('letter-recognition.data', 'rb') as csvfile:
    lines = csv.reader(csvfile)
    for row in lines:
        print ', '.join(row)
