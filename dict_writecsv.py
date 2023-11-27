import csv

filename = "dict_students.csv"

# create the fields for the data
fields = ["First Name", "Last Name", "Program", "Duration (months)"]

# setting values for the number of individuals in the record
records = [
    {"First Name": "Festus", "Last Name": "Friday", "Program": "Computer basics", "Duration (months)": 6},
    {"First Name": "Bestlife", "Last Name": "Ineye", "Program": "Computer basics", "Duration (months)": 6},
    {"First Name": "Brian", "Last Name": "Obire", "Program": "Computer basics", "Duration (months)": 3},
    {"First Name": "Tobi", "Last Name": "Oluwafemi", "Program": "Drawing basics", "Duration (months)": 1},
    {"First Name": "Livinus", "Last Name": "Kam", "Program": "Computer basics", "Duration (months)": 3}
]
# create a file object
with open(filename, 'w', ) as file:
    # create a writer object
    new_record = csv.DictWriter(file, fieldnames=fields, lineterminator='\n')
    # write the fields into the file
    new_record.writeheader()
    # write the rows into the file
    new_record.writerows(records)
    print(f'{filename} created successfully')

"""ACHIEVEMENTS
the process is similar to that of the writer the difference is that the writer 
will return a list that can be accessed through indexes while the DictWriter 
can be accessed through a key.
other notable differnces are the fieldnames argument and 
writeheader() method that creates the header row"""
