import csv
import pandas
import sys
import bokeh



header_dict = {}
index = 0
row_list = []

# Inladen eerste 500 rows van dataset
ifile  = open('stage3.csv', "r")
read = csv.reader(ifile)
headers = next(read)
row_list.append(headers)
for i in range(500):
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

    
# importing necessary libraries
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.us_states import data as states


# maakt dictionary met latitudes
latitudes_per_case = {}
for value in header_dict['latitude']:
    for i in range(len(header_dict['latitudes'])):
        value.append(latitudes_per_case)
    index += 1

# maakt dictionary met longitudes
longitudes_per_case = {}
for value in header_dict['longitude']:
    for i in range(len(header_dict['longitudes'])):
        value.append(longitudes_per_case)
    index += 1


state_xs = longitudes_per_case
state_ys = latitudes_per_case

p = figure(title = "Muders on map", toolbar_location = "left",
 plot_width = 1000, plot_height = 1000)
p.circle(x=state_xs, y=state_ys)

output_file("murdersonmap.html")

show(p)