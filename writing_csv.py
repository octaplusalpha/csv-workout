import csv

"""WRITING TO  CSV"""
# create the fields for the data
fields = ["First Name", "Last Name", "Program", "Duration (months)"]

# setting values for the number of individuals in the record
records = [
    ["Festus", "Friday", "Computer basics", 6],
    ["Bestlife", "Ineye", "Computer basics", 6],
    ["Brian", "Obire", "Computer basics", 3],
    ["Tobi", "Oluwafemi", "Drawing basics", 1],
    ["Livinus", "Kam", "Computer basics", 3],
]

# use content manager to open the new file with the mode set to write
with open("my_students.csv", 'w') as f:
    # create a writer object
    writer = csv.writer(f, lineterminator='\n',)
    # write content into object first the row header
    writer.writerow(fields)
    # then the rows
    writer.writerows(records)
    print(f'{filename} written successfully')

"""ACHIEVEMENTS
- create a list of fields for the data to be identified by
- create a list of records for the file
- create a filename remember to add the extension
-use the content manager to create the new file by stating the file name,
its location if it is not meant to be in the cwd and the mode which in this 
case is write
-create the writer object using csv.writer() and passing the file object as 
an argument
- write the data into the file using the file object and the writer using 
file_obj.writerow() for the fields passing the fields as an argument
-write the data rows using the file_obj.writerows() for multiple row or
file_obj.writerow() for single record passing in the records as an argument
however note that a for loop is required to enter the full content of the 
data if the records are many."""