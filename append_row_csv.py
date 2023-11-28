import csv

filename = "my_students.csv"

new_data = ['Ruth', 'Ajibola', 'C sharp', 9]


with open(filename, 'a') as file:
    record = csv.writer(file)
    record.writerow(new_data)

"""ACHIEVEMENT
The difference at this point is the append mode in the writer"""
