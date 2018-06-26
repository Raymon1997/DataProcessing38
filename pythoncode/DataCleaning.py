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
for i in range(235677):
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


#for i in range(len(row_list)):
#    if i == 0:
#        continue
#    else:
#        lat = row_list[i][8]
#        lon = row_list[i][9]
#        if lat != 'NA' and lon != 'NA':
#            new_address = reverse_geocoder(lat, lon)
#            while new_address == False:
#                new_address = reverse_geocoder(lat, lon)
#            row_list[i][4] = new_address




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

# maakt dictionary met aantal guns involved
# month_dict = {}
# for i in range(len(header_dict['date'])):
#     if header_dict['date'][i][5:7] in year_dict:
#         if header_dict['n_guns_involved'][i] == 'NA':
#             year_dict[header_dict['date'][i][5:7]] += 1
#         else:
#             year_dict[header_dict['date'][i][5:7]] += int(header_dict['n_guns_involved'][i])
#     else:
#         if header_dict['n_guns_involved'][i] == 'NA':
#             year_dict[header_dict['date'][i][5:7]] = 1
#         else:
#             year_dict[header_dict['date'][i][5:7]] = int(header_dict['n_guns_involved'][i])


year_dict = {}
for i in range(len(header_dict['date'])):
    if header_dict['date'][i][0:4] in year_dict:
        year_dict[header_dict['date'][i][0:4]] += int(header_dict['n_killed'][i])
    else:
        year_dict[header_dict['date'][i][0:4]] = int(header_dict['n_killed'][i])

# maakt dictionary met aantal doden per state



state_dict = {}
for i in range(len(header_dict['state'])):
    if header_dict['state'][i] in state_dict:
        state_dict[header_dict['state'][i]] += int(header_dict['n_injured'][i])
    else:
        state_dict[header_dict['state'][i]] = int(header_dict['n_injured'][i])

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

def check_if_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# participant_age_group_dict = {"C" : {"S" : 0, "V" : 0}, "T" : {"S" : 0, "V" : 0}, "A" : {"S" : 0, "V" : 0}}
# participant_dict = {"C" : 0, "T" : 0, "A" : 0}

# index = -1
# SofV = "0"
# for i in range(len(header_dict['participant_age_group'])):
#     for j in range(len(header_dict['participant_age_group'][i])-1):
#         if check_if_number(header_dict['participant_age_group'][i][j]) and header_dict['participant_age_group'][i][j+1] == ":":
#             index = int(header_dict['participant_age_group'][i][j])
#         if header_dict['participant_age_group'][i][j] in participant_age_group_dict:
#             for k in range(len(header_dict['participant_type'][i])):
#                 if header_dict['participant_type'][i][k] == str(index) and (header_dict['participant_type'][i][k+3] == "S" or header_dict['participant_type'][i][k+3] == "V"):
#                     SofV = header_dict['participant_type'][i][k+3]
#                     participant_age_group_dict[header_dict['participant_age_group'][i][j]][SofV] += 1
#             participant_dict[header_dict['participant_age_group'][i][j]] +=1
#     index = -1
# print(participant_age_group_dict)
# print(participant_dict)


# participant_gender_dict = {"M" : {"S" : 0, "V" : 0}, "F" : {"S" : 0, "V" : 0}}
# gender_dict = {"M" : 0, "F" : 0}

# index = -1
# SofV = "0"
# for i in range(len(header_dict['participant_gender'])):
#     for j in range(len(header_dict['participant_gender'][i])-1):
#         if check_if_number(header_dict['participant_gender'][i][j]) and header_dict['participant_gender'][i][j+1] == ":":
#             index = int(header_dict['participant_gender'][i][j])
#         if header_dict['participant_gender'][i][j] in participant_gender_dict:
#             for k in range(len(header_dict['participant_type'][i])):
#                 if header_dict['participant_type'][i][k] == str(index) and (header_dict['participant_type'][i][k+3] == "S" or header_dict['participant_type'][i][k+3] == "V"):
#                     SofV = header_dict['participant_type'][i][k+3]
#                     participant_gender_dict[header_dict['participant_gender'][i][j]][SofV] += 1
#             gender_dict[header_dict['participant_gender'][i][j]] +=1
#     index = -1
# print(participant_gender_dict)
# print(gender_dict)

participant_age_group_dict = {"C" : {"S" : {"M" : 0, "F" : 0}, "V" : {"M" : 0, "F" : 0}}, "T" : {"S" : {"M" : 0, "F" : 0}, "V" : {"M" : 0, "F" : 0}}, "A" : {"S" : {"M" : 0, "F" : 0}, "V" : {"M" : 0, "F" : 0}}}
participant_dict = {"C" : 0, "T" : 0, "A" : 0}

index = -1
SofV = "0"
MofF = "0"
for i in range(len(header_dict['participant_age_group'])):
    for j in range(len(header_dict['participant_age_group'][i])-1):
        if check_if_number(header_dict['participant_age_group'][i][j]) and header_dict['participant_age_group'][i][j+1] == ":":
            index = int(header_dict['participant_age_group'][i][j])
        if header_dict['participant_age_group'][i][j] in participant_age_group_dict:
            for k in range(len(header_dict['participant_type'][i])):
                if header_dict['participant_type'][i][k] == str(index) and (header_dict['participant_type'][i][k+3] == "S" or header_dict['participant_type'][i][k+3] == "V"):
                    SofV = header_dict['participant_type'][i][k+3]
                    for ind in range(len(header_dict['participant_gender'][i])):
                        if header_dict['participant_gender'][i][ind] == str(index) and (header_dict['participant_gender'][i][ind+3] == "M" or header_dict['participant_gender'][i][ind+3] == "F"):
                            MofF = header_dict['participant_gender'][i][ind+3]
                            participant_age_group_dict[header_dict['participant_age_group'][i][j]][SofV][MofF] += 1
            participant_dict[header_dict['participant_age_group'][i][j]] +=1
    index = -1
print(participant_age_group_dict)
print(participant_dict)

# # maakt dictionary met aantal doden per state
# address_dict = {}
# for i in range(len(header_dict['address'])):
#     max_index = 0
#     address = list(header_dict['address'][i])
#     for index in range(len(address)):
#         if address[index].isdigit() == True:
#             max_index = index
#         else:
#             break
#     if max_index != 0:
#         max_index += 2
#     street_name = "".join(address[max_index:len(address)])

#     if street_name in address_dict:
#         address_dict[street_name] += int(header_dict['n_killed'][i])
#     else:
#         address_dict[street_name] = int(header_dict['n_killed'][i])
# max_killed_key = 'Coursin St'

# for key in address_dict:
#     if int(address_dict[key]) > int(address_dict[max_killed_key]) and key != 'NA' :
#         max_killed_key = key
# print(max_killed_key, address_dict[max_killed_key])
