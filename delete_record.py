import  csv
import shutil
from tempfile import NamedTemporaryFile

source = 'dict_students.csv'
headers = ['First Name', 'Last Name', 'Program', 'Duration (months)']
with open(source) as file:
    result = csv.DictReader(file)
    data = list(result)

    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        new_result = csv.DictWriter(temp_file, fieldnames=headers, lineterminator='\n')
        new_result.writeheader()
        for row in data:
            if row['First Name'] == 'Tobi':
                continue
            new_result.writerow(row)
        print(temp_file.name)
shutil.move(temp_file.name, 'computer_students_only.csv')

