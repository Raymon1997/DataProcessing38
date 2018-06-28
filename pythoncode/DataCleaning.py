import csv
import pandas
import sys
import geocoder
import unicodecsv
import logging

import numpy as np
from bokeh.plotting import figure, output_file, show

def check_if_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

header_dict = {}
index = 0
row_list = []

# Inladen dataset
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

# Bepaal killed per staat
killed_dict = {}
for i in range(len(header_dict['state'])):
    if header_dict['state'][i] in killed_dict:
        killed_dict[header_dict['state'][i]] += int(1)
    else:
        killed_dict[header_dict['state'][i]] = int()

# Bepaal injured per year
injured_dict = {}
for i in range(len(header_dict['date'])):
    if header_dict['date'][i][0:7] in injured_dict:
        injured_dict[header_dict['date'][i][0:7]] += int(header_dict['n_injured'][i])
    else:
        injured_dict[header_dict['date'][i][0:7]] = int(header_dict['n_injured'][i])

# bepaal aantal incidenten per staat
killed_dict = {}
for i in range(len(header_dict['state'])):
    if header_dict['state'][i] in killed_dict:
        killed_dict[header_dict['state'][i]] += int(1)
    else:
        killed_dict[header_dict['state'][i]] = int()

# maak dict met injured per jaar
injured_dict = {}
for i in range(len(header_dict['date'])):
    if header_dict['date'][i][0:7] in injured_dict:
        injured_dict[header_dict['date'][i][0:7]] += int(header_dict['n_injured'][i])
    else:
        injured_dict[header_dict['date'][i][0:7]] = int(header_dict['n_injured'][i])

# maak lijst met killed per jaar
year_dict = {}
for i in range(len(header_dict['date'])):
    if header_dict['date'][i][0:7] in year_dict:
        year_dict[header_dict['date'][i][0:7]] += int(header_dict['n_killed'][i])
    else:
        year_dict[header_dict['date'][i][0:7]] = int(header_dict['n_killed'][i])

dates = []
killed = []
injured = []
for key in year_dict.keys():
    dates.append(np.datetime64(key))
for value in year_dict.values():
    killed.append(value)
for value in injured_dict.values():
    injured.append(value)

window_size = 30
window = np.ones(window_size)/float(window_size)

# output to static HTML file
output_file("killed.html", title="normal graph")

# create a new plot with a a datetime axis type
p = figure(width=800, height=350, x_axis_type="datetime")

# add renderers
p.circle(dates, killed, size=4, color='darkgrey', alpha=3, legend='close')
p.circle(dates, injured, size=4, color='darkgrey', alpha=3, legend='close')
p.line(dates, killed, color='red', legend='killed', line_width=0.9)
p.line(dates, injured, color='navy', legend='injured', line_width=0.9)
# NEW: customize by setting attributes
p.title.text = "People killed by date"
p.legend.location = "top_left"
p.grid.grid_line_alpha = 0
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Killed'
p.ygrid.band_fill_color = "olive"
p.ygrid.band_fill_alpha = 0.1
# show(p)

# maakt dictionary met aantal doden per state
state_dict = {}
for i in range(len(header_dict['state'])):
    if header_dict['state'][i] in state_dict:
        state_dict[header_dict['state'][i]] += int(header_dict['n_killed'][i]) + int(header_dict['n_injured'][i])
    else:
        state_dict[header_dict['state'][i]] = int(header_dict['n_killed'][i]) + int(header_dict['n_injured'][i])

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

# Laad data in met populaties per staat
# header_dict2={}
# row_list2 = []
# index2 = 0
# ifile  = open('data.csv', "r")
# read = csv.reader(ifile)
# headers = next(read)
# row_list2.append(headers)
# for i in range(51):
#     row_list2.append(next(read))
#
#
# for header in headers:
#     header_dict2[header] = []
#     for i in range(1, len(row_list2)):
#         header_dict2[header].append(row_list2[i][index2])
#     index2 += 1
#
#
# # Maak dictionary aan met als keys de staten en als values hun populatie
# pop_dict = {}
# for i in range(len(header_dict2['State'])):
#     if header_dict2['State'][i] in pop_dict:
#         pop_dict[header_dict2['State'][i]] += int(header_dict2['2018 Population'][i])
#     else:
#         pop_dict[header_dict2['State'][i]] = int(header_dict2['2018 Population'][i])
#
# # vind relatief gevaarlijkste staat
# max_state = 0
# max_pop = 1000000
# state_pop_dict = {}
# for state in state_dict:
#     state_pop_dict[state] = float(state_dict[state]/pop_dict[state]) * 100
#     if float(state_dict[state]/pop_dict[state])*100 > max_pop:
#         max_state = state
#         max_pop = float(state_dict[state]/pop_dict[state])*100
#
# print(state_pop_dict)
# print(max_state, max_pop)
#

# averages

killed_2014 = {}
for i in range(len(header_dict['state'])):
    if header_dict['state'][i] in killed_2014:
        if header_dict['date'][i][0:4] == '2014':
            killed_2014[header_dict['state'][i]] += int(header_dict['n_killed'][i])
    else:
         if header_dict['date'][i][0:4] == '2014':
             killed_2014[header_dict['state'][i]] = int(header_dict['n_killed'][i])

killed_2015 = {}
for i in range(len(header_dict['state'])):
    if header_dict['state'][i] in killed_2015:
        if header_dict['date'][i][0:4] == '2015':
            killed_2015[header_dict['state'][i]] += int(header_dict['n_killed'][i])
    else:
         if header_dict['date'][i][0:4] == '2015':
             killed_2015[header_dict['state'][i]] = int(header_dict['n_killed'][i])

killed_2016 = {}
for i in range(len(header_dict['state'])):
    if header_dict['state'][i] in killed_2016:
        if header_dict['date'][i][0:4] == '2016':
            killed_2016[header_dict['state'][i]] += int(header_dict['n_killed'][i])
    else:
         if header_dict['date'][i][0:4] == '2016':
             killed_2016[header_dict['state'][i]] = int(header_dict['n_killed'][i])


killed_2017 = {}
for i in range(len(header_dict['state'])):
    if header_dict['state'][i] in killed_2017:
        if header_dict['date'][i][0:4] == '2017':
            killed_2017[header_dict['state'][i]] += int(header_dict['n_killed'][i])
    else:
         if header_dict['date'][i][0:4] == '2017':
             killed_2017[header_dict['state'][i]] = int(header_dict['n_killed'][i])

killed_average = {}
for i in range(len(header_dict['state'])):
    if header_dict['state'][i] in killed_average:
        if header_dict['date'][i][0:4] != '2013' and header_dict['date'][i][0:4] != '2018':
            killed_average[header_dict['state'][i]] += int(header_dict['n_killed'][i])/4
    else:
        if header_dict['date'][i][0:4] != '2013' and header_dict['date'][i][0:4] != '2018':
            killed_average[header_dict['state'][i]] = int(header_dict['n_killed'][i])/4
print(killed_average)

# killed_change_2014
