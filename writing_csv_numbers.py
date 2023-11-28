import csv
from pprint import pprint

"""NUMERIC VALUES in csv can be achieved by using the quote keyword as an argument in the 
write method"""

# create a nested list with scores for two subjects

result = [
    ['REG. NO', 'NAME', 'MS WORD', 'MS EXCEL'],
    [12, 'Kam Livinus', 45, 38],
    [14, 'Brian Obire', 52, 65],
    [13, 'Festus Friday', 50, 60]

]

filename = 'basic_comp_results.csv '

with open(filename, 'w', newline='') as file:
    quote = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    quote.writerows(result)
    print(f'{filename} created successfully')

with open(filename, 'r') as f:
    quote = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    sheet = []

    for row in quote:
        sheet.append(row)

pprint(sheet)

"""ACHIEVEMENTS
The major take away in this is the use of the quoting  property
this allows for the writer to ignore the quoting of numeric values
This shoul also be applied to reader object so as to maintain the 
requirement for numeric values to be treated as integers thereby 
leaving them unquoted
note that the numbers returned are of type float
Alternatively, the use of  csv.QUOTE_ALL
will ensure the nubers and all the other values are quoted
irrespective of type"""
