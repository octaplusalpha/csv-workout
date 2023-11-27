import csv

my_students = []
# open target file
with open('my_students.csv') as file:
    reader = csv.DictReader(file)

    for row in reader:
        my_students.append(row)
