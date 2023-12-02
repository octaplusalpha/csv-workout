import csv
import shutil
from tempfile import NamedTemporaryFile

source = 'dict_students.csv'

with open(source) as source_file:
    result = csv.DictReader(source_file)
    data = list(result)
    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        header_row = ['Name', 'Program', 'Duration']
        new_result = csv.DictWriter(temp_file, fieldnames=header_row, lineterminator='\n')
        new_result.writeheader()
        for row in data:
            new_result.writerow({'Name': row['First Name'] + ' ' + row['Last Name'],
                                 'Program': row['Program'],
                                 'Duration': row['Duration (months)']
                                 })
        print(temp_file.name)
shutil.move(temp_file.name, 'new_header_row.csv')



"""ACHIEVEMENTS
the change header row code is similar to that of the changee record of
either one field or the whole record the difference lies in the removal of
the iteration using if to check for a required field and replacing it with the 
new structure of the header row
steps remain
1. read the source file 
2. write on the temp file using the NamedTemporaryFile instead of 
the open keyword. 
use a key value pair to concatenate where required remember to add
the lineterminator to ensure that the data is placed on new lines each
time a record is written into the temp file
3. transfer the contents of the temp file into a csv file that may be new
or by overwriting the old one with the updated content"""