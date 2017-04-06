import csv
with open('letter_recognition.data', 'rt') as csvfile:
    lines = csv.reader(csvfile)
    for row in lines:
        print(', '.join(row))
