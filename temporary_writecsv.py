import csv
import shutil
from tempfile import NamedTemporaryFile

# create a temporary file
temp_file = NamedTemporaryFile(mode='w', delete=False)
# Open the file to be written from
with open("dict_students.csv") as f:
    source = csv.DictReader(f)
    data = list(source)

    # declare the header row
    h_row = ['First Name', 'Last Name', 'Program', 'Duration (months)']
    # create the writer object
    writer = csv.DictWriter(temp_file, fieldnames=h_row, lineterminator='\n')

    # write into the temporary file
    writer.writeheader()
    for row in data:
        if row["First Name"] == "Bestlife":
            row["Duration (months)"] = 2
        writer.writerow(row)
    print('Data updated successfully')
    print(temp_file.name)
    # close the temp file
    temp_file.close()

# parse the temp_file into a csv file
shutil.move(temp_file.name, 'new_students.csv')

"""ACHIEVEMENTS
updates are done to a temporary file before creating a new or
overwriting the original file 
note that the temp file will be deleted as soon as the move cmd
through shutil is executed. the move method requires two 
arguments the temp file name and the destination for the 
content
in all dictionaries are better managed when working with files
that are strictly string values data or better stated as key value 
pair type data.
the update function can be applied to an entire row as well
in which case all keys are stated"""