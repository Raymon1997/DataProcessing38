import csv
import pandas
import sys
import geocoder
import unicodecsv
import logging

def reverse_geocoder(lat, lon):
    g = geocoder.google([lat,lon], method='reverse')

    
    if len(g) > 0:
        address = str(g[0]).split(',')
        address = address[0][1:]
        max_index = 0
        for index in range(len(address)):
            if address[index].isdigit() == True:
                max_index = index
            else:
                break
        if max_index != 0:
            max_index += 2
        street_name = "".join(address[max_index:len(address)])
        return street_name
    else:
        return False

header_dict = {}
index = 0
row_list = []

# Inladen eerste 500 rows van dataset
ifile  = open('stage3.csv', "r")
read = csv.reader(ifile)
headers = next(read)
row_list.append(headers)
del row_list[0][0]
del row_list[0][6:9]
del row_list[0][9]
del row_list[0][10]
del row_list[0][12]
del row_list[0][15]
del row_list[0][18]
del row_list[0][16]
del row_list[0][12]
del row_list[0][8]
for i in range(239677):
    row_list.append(next(read))
    del row_list[i+1][0]
    del row_list[i+1][6:9]
    del row_list[i+1][9]
    del row_list[i+1][10]
    del row_list[i+1][12]
    del row_list[i+1][15]
    del row_list[i+1][18]
    del row_list[i+1][16]
    del row_list[i+1][12]
    del row_list[i+1][8]

# Veranderd missende data in NA
for row in row_list:
    for i in range(len(row)):
        if row[i] == '':
            row[i] = 'NA'


for i in range(len(row_list)):
    if i == 0:
        continue
    else:
        lat = row_list[i][8]
        lon = row_list[i][9]
        if lat != 'NA' and lon != 'NA':
            new_address = reverse_geocoder(lat, lon)
            while new_address == False:
                new_address = reverse_geocoder(lat, lon)
            row_list[i][4] = new_address




# Exporteer aangepaste data naar output.csv
writer = csv.writer(open('output.csv', 'w'))
writer.writerows(row_list)






