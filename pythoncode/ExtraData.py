import csv
import pandas

header_dict = {}
row_list = []
index = 0

ifile  = open('statepov.csv', "r")
read = csv.reader(ifile)
x = next(read)
headers = next(read)
row_list.append(headers)
for i in range(51):
    row_list.append(next(read))
writer = csv.writer(open('extradata.csv', 'w'))
writer.writerows(row_list)

for header in headers:
    header_dict[header] = []
    for i in range(1, len(row_list)):
        header_dict[header].append(row_list[i][index])
    index += 1

state_percentage_dict = {}
for i in range(len(header_dict['state'])):
    state_percentage_dict[header_dict['state'][i]] = header_dict['Percentage 2014-2016'][i]

