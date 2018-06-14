import csv
import pandas
import sys

header_dict = {}
index = 0
row_list = []

# Inladen eerste 500 rows van dataset
ifile  = open('stage3.csv', "r")
read = csv.reader(ifile)
headers = next(read)
row_list.append(headers)
for i in range(239677):
    row_list.append(next(read))

# Veranderd missende data in NA
for row in row_list:
    for i in range(len(row)):
        if row[i] == '':
            row[i] = 'NA'


# Exporteer aangepaste data naar output.csv
writer = csv.writer(open('output.csv', 'w'))
writer.writerows(row_list)

# Maak dicitonary met als keys de headers
for header in headers:
    header_dict[header] = []
    for i in range(1, len(row_list)):
        header_dict[header].append(row_list[i][index])
    index += 1

# Bepaal hoeveel totaal aantal wapens
guns_used_list = []
number_of_guns = 0
for value in header_dict['n_guns_involved']:
    if value != 'NA':
        guns_used_list.append(value)
        number_of_guns += int(value)
average_used = number_of_guns/len(guns_used_list)
print(average_used)
#bepaal totaal aantal gestolen wapens
# number_of_guns_stolen = 0
# for value in header_dict['gun_stolen']:
#     if 'Unknown' in value:
#     if len(list(value)) < 2:
#         number_of_guns_stolen += int(value)

# maakt dictionary met aantal gebruikte per jaar
year_dict = {}
for i in range(len(header_dict['date'])):
    if header_dict['date'][i][0:4] in year_dict:
        if header_dict['n_guns_involved'][i] == 'NA':
            year_dict[header_dict['date'][i][0:4]] += 1
        else:
            year_dict[header_dict['date'][i][0:4]] += int(header_dict['n_guns_involved'][i])
    else:
        if header_dict['n_guns_involved'][i] == 'NA':
            year_dict[header_dict['date'][i][0:4]] = 1
        else:
            year_dict[header_dict['date'][i][0:4]] = int(header_dict['n_guns_involved'][i])

# maakt dictionary met aantal doden per state
state_dict = {}
for i in range(len(header_dict['state'])):
    while header_dict['date'][i][0:4] == '2013':
        if header_dict['state'][i] in state_dict:
            state_dict[header_dict['state'][i]] += int(header_dict['n_injured'][i])
        else:
            state_dict[header_dict['state'][i]] = int(header_dict['n_injured'][i])
print(state_dict)
# maakt dictionary met aantal doden per city/county
city_or_county_dict = {}
for i in range(len(header_dict['city_or_county'])):
    lengte = int(len(header_dict['city_or_county'][i]))
    # countys vinden
    # if header_dict['city_or_county'][i][lengte - 8:lengte] == '(county)':
    #     print(header_dict['city_or_county'][i], "is a county")

    if header_dict['city_or_county'][i] in city_or_county_dict:
        city_or_county_dict[header_dict['city_or_county'][i]] += int(header_dict['n_killed'][i])
    else:
        city_or_county_dict[header_dict['city_or_county'][i]] = int(header_dict['n_killed'][i])
