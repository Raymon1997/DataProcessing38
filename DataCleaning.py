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
    if header_dict['date'][i] in year_dict:
        year_dict[header_dict['date'][i]] += int(header_dict['n_killed'][i])
    else:
        year_dict[header_dict['date'][i]] = int(header_dict['n_killed'][i])

import numpy as np

from bokeh.plotting import figure, output_file, show

dates = []
killed = []
for key in year_dict.keys():
    dates.append(np.datetime64(key))
for value in year_dict.value():
    killed.append(value)


window_size = 30
window = np.ones(window_size)/float(window_size)


# output to static HTML file
output_file("killed.html", title="normal graph")

# create a new plot with a a datetime axis type
p = figure(width=800, height=350, x_axis_type="datetime")

# add renderers
p.circle(dates, killed, size=4, color='darkgrey', alpha=3, legend='close')
p.line(dates, killed, color='navy', legend='avg', linewidth=0.4)

# NEW: customize by setting attributes
p.title.text = "People killed by date"
p.legend.location = "top_left"
p.grid.grid_line_alpha = 0
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Killed'
p.ygrid.band_fill_color = "olive"
p.ygrid.band_fill_alpha = 0.1

# show the results
show(p)






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


# maakt dictionary met aantal doden per state
address_dict = {}
for i in range(len(header_dict['address'])):
    max_index = 0
    address = list(header_dict['address'][i])
    for index in range(len(address)):
        if address[index].isdigit() == True:
            max_index = index
        else:
            break
    if max_index != 0:
        max_index += 2
    street_name = "".join(address[max_index:len(address)])

    if street_name in address_dict:
        address_dict[street_name] += int(header_dict['n_killed'][i])
    else:
        address_dict[street_name] = int(header_dict['n_killed'][i])
max_killed_key = 'Coursin St'

for key in address_dict:
    if int(address_dict[key]) > int(address_dict[max_killed_key]) and key != 'NA' :
        max_killed_key = key
# print(max_killed_key, address_dict[max_killed_key])
