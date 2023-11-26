import csv

"""READING CSV FILE"""

# create a file name
filename = 'people.csv'
# create a list to hold all the records from the csv file
people = []

# open the csv file
with open("C:\\Users\\ebizh\\OneDrive\\Desktop\\cmdresources\\people.csv", 'r') as f:
    # create a reader object to read from the csv file
    reader = csv.reader(f)
    # get all the fields or column names from the first row of the csv file
    fields = next(reader)
    # extract every record to the list of person
    for row in reader:
        people.append(row)

    # get the total count of records in the data set using the reader.line_num
    # which is a synonym for len().
    person_count = reader.line_num

# output the total number of people
print(f"Total number of records: {person_count} people")

# output the columns using a list comprehension
print(f"Fields:{[field for field in fields]}")

# print the records with its respective field name
for row in people:
    print(row)

"""ACHIEVEMENT
- locate a csv fiel
- open the csv file using the with open keywords stating the filename
and directory if it is not located in the working directory of the project
by default the mode is the read mode and does not need to be stated
-create a reader object that enables for the reading of the csv file through
the use of csv.reader() method while passing the file opened as an argument
then getting the content of the file by first of all obtaining the column names
using the next() function and passing the reader object as an argument
then getting the records from the reader object using a for loop. the count of the 
records can also be obtained through the reader object by the use of  
reader.line_num. all these values stored in a variable can be obtained"""