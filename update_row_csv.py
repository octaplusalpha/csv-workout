import csv

filename = 'dict_students.csv'
# read the target file using the write mode
with open(filename) as file:
    update_val = csv.DictReader(file)
    # iterate over the file using a for loop to find a match using an if statement
    data = list(update_val)

    with open('updated_dict_students.csv', 'w') as f:
        fields = ['First Name', 'Last Name', 'Program',  'Duration (months)']
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
        writer.writeheader()
        for row in data:
            if row['First Name'] == 'Bestlife':
                row['Duration (months)'] = 2
            writer.writerow(row)
        print('data updated successfully')

"""ACHIEVEMENTS
The logic for this is;
 -to first open the file in read mode
-save the content in a variable of type list
-create another file for the updated record
-using the write mode and stating the header row
- in the for loop that writes each row to the file
 check the value to be updated and state the new value for the 
key;
write the rows as they are looped to the end.
if the original file is to be over written use the name of the original 
file instead of stating a new one 
"""
