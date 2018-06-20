import csv
import pandas
import sys
import bokeh
import numpy



header_dict = {}
index = 0
row_list = []

# Inladen eerste 500 rows van dataset
ifile  = open('output.csv', "r")
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

    
# maakt lijst met latitudes
latitudes_per_case_str = []
for i in range(len(header_dict['latitude'])):
    if i == 'NA':
        del(i)
    else:
        latitudes_per_case_str.append(header_dict['latitude'][i])        
index += 1
latitudes_per_case = []
for i in latitudes_per_case_str:
    latitudes_per_case.append(float(i))
print(latitudes_per_case)


# maakt lijst met longitudes
longitudes_per_case_str = []
for i in range(len(header_dict['longitude'])):
    if i == 'NA':
        del(i)
    else:
        latitudes_per_case_str.append(header_dict['latitude'][i])
index += 1
longitudes_per_case = []
for i in longitudes_per_case_str:
    longitudes_per_case.append(float(i))
print(longitudes_per_case)
# maak er nog een float van

# importing necessary libraries
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.us_states import data as states
from bokeh.models import ColumnDataSource, ColumnarDataSource

del states["HI"]
del states["AK"]

# convert into columndatasource
source = ColumnDataSource(data = dict(lon= longitudes_per_case,
            lat=latitudes_per_case))


state_xs = [states[code]["lons"] for code in states]
state_ys = [states[code]["lats"] for code in states]


colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]


# Make figure
p = figure(title = "Muders on map", toolbar_location = "right",
 plot_width = 1500, plot_height = 1000)
# Draw state lines
p.patches(state_xs, state_ys, fill_alpha=0.0,
    line_color="#884444", line_width=1.5)
# Create scatterplot
p.circle(x='lon', y='lat', size = 8, fill_alpha=1, fill_color = "blue", source = source)

output_file("murdersonmap.html")

show(p)