[33mcommit 0a4e6f647add0b2c222cc24c181738a900fb756d[m[33m ([m[1;36mHEAD -> [m[1;32mmain[m[33m)[m
Author: ebizho <ebizhonix@gmail.com>
Date:   Tue Nov 28 02:22:18 2023 +0100

    numeric values in csv

[1mdiff --git a/basic_comp_results.csv b/basic_comp_results.csv[m
[1mnew file mode 100644[m
[1mindex 0000000..3725ec3[m
[1m--- /dev/null[m
[1m+++ b/basic_comp_results.csv[m
[36m@@ -0,0 +1,4 @@[m
[32m+[m[32m"REG. NO","NAME","MS WORD","MS EXCEL"[m
[32m+[m[32m12,"Kam Livinus",45,38[m
[32m+[m[32m14,"Brian Obire",52,65[m
[32m+[m[32m13,"Festus Friday",50,60[m
[1mdiff --git a/writing_csv_numbers.py b/writing_csv_numbers.py[m
[1mnew file mode 100644[m
[1mindex 0000000..0e282cb[m
[1m--- /dev/null[m
[1m+++ b/writing_csv_numbers.py[m
[36m@@ -0,0 +1,42 @@[m
[32m+[m[32mimport csv[m
[32m+[m[32mfrom pprint import pprint[m
[32m+[m
[32m+[m[32m"""NUMERIC VALUES in csv can be achieved by using the quote keyword as an argument in the[m[41m [m
[32m+[m[32mwrite method"""[m
[32m+[m
[32m+[m[32m# create a nested list with scores for two subjects[m
[32m+[m
[32m+[m[32mresult = [[m
[32m+[m[32m    ['REG. NO', 'NAME', 'MS WORD', 'MS EXCEL'],[m
[32m+[m[32m    [12, 'Kam Livinus', 45, 38],[m
[32m+[m[32m    [14, 'Brian Obire', 52, 65],[m
[32m+[m[32m    [13, 'Festus Friday', 50, 60][m
[32m+[m
[32m+[m[32m][m
[32m+[m
[32m+[m[32mfilename = 'basic_comp_results.csv '[m
[32m+[m
[32m+[m[32mwith open(filename, 'w', newline='') as file:[m
[32m+[m[32m    quote = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)[m
[32m+[m[32m    quote.writerows(result)[m
[32m+[m[32m    print(f'{filename} created successfully')[m
[32m+[m
[32m+[m[32mwith open(filename, 'r') as f:[m
[32m+[m[32m    quote = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)[m
[32m+[m[32m    sheet = [][m
[32m+[m
[32m+[m[32m    for row in quote:[m
[32m+[m[32m        sheet.append(row)[m
[32m+[m
[32m+[m[32mpprint(sheet)[m
[32m+[m
[32m+[m[32m"""ACHIEVEMENTS[m
[32m+[m[32mThe major take away in this is the use of the quoting  property[m
[32m+[m[32mthis allows for the writer to ignore the quoting of numeric values[m
[32m+[m[32mThis shoul also be applied to reader object so as to maintain the[m[41m [m
[32m+[m[32mrequirement for numeric values to be treated as integers thereby[m[41m [m
[32m+[m[32mleaving them unquoted[m
[32m+[m[32mnote that the numbers returned are of type float[m
[32m+[m[32mAlternatively, the use of  csv.QUOTE_ALL[m
[32m+[m[32mwill ensure the nubers and all the other values are quoted[m
[32m+[m[32mirrespective of type"""[m
