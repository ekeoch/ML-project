import csv

with open('letter_recognition.data', 'rt') as csvfile:
    lines = csv.reader(csvfile)
    with open('formatted_file.data', 'w', newline='') as new_file:
        for line in lines:
            line.reverse()
            wr = csv.writer(new_file)
            wr.writerow(line)
    new_file.close()

