import csv
import pandas
import sys

categorie_dict = {}
index = 0
row_list = []

ifile  = open('stage3.csv', "r")
read = csv.reader(ifile)
read = csv.reader(ifile)
for row in read:
    row_list.append(row)
categorie_list = row_list[0]

for row in row_list:
    for i in range(len(row)):
        if row[i] == '':
            row[i] == 'NA'

writer = csv.writer(open('output.csv', 'w'))
writer.writerows(row_list)



# for categorie in categorie_list:
#     categorie_dict[categorie] = []
# for categorie in categorie_list:
#     for i in range(1, len(row_list)):
#         categorie_dict[categorie].append(row_list[i][index])
#     index += 1