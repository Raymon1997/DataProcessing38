import csv

from bokeh.io import show
from bokeh.models import LogColorMapper, ColumnDataSource, HoverTool
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure

from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.unemployment import data as unemployment


from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("175 5th Avenue NYC")


from bokeh.plotting import figure, output_file, show, ColumnDataSource

output_file("toolbar.html")

source = ColumnDataSource(data=dict(
    x=[1, 2, 3, 4, 5],
    y=[2, 5, 8, 2, 7],
    desc=['A', 'b', 'C', 'd', 'E'],
))

TOOLTIPS = [
    ("index", "$index"),
    ("(x,y)", "($x, $y)"),
    ("desc", "@desc"),
]

p = figure(plot_width=400, plot_height=400, tools=TOOLTIPS,
           title="Mouse over the dots")

p.circle('x', 'y', size=20, source=source)

show(p)


# header_dict = {}
# index = 0
# row_list = []

# # Inladen eerste 500 rows van dataset
# ifile  = open('output.csv', "r")
# read = csv.reader(ifile)
# headers = next(read)
# row_list.append(headers)
# for i in range(235677):
#     row_list.append(next(read))

# # Veranderd missende data in NA
# for row in row_list:
#     for i in range(len(row)):
#         if row[i] == '':
#             row[i] = 'NA'

# # Exporteer aangepaste data naar output.csv
# writer = csv.writer(open('output.csv', 'w'))
# writer.writerows(row_list)

# # Maak dicitonary met als keys de headers
# for header in headers:
#     header_dict[header] = []
#     for i in range(1, len(row_list)):
#         header_dict[header].append(row_list[i][index])
#     index += 1

# latitudes_per_case = []
# longitudes_per_case = []
# for i in range(len(header_dict['latitude'])):
#     if header_dict['latitude'][i] == 'NA' or header_dict['longitude'][i] == 'NA' or header_dict['state'][i] != 'Texas':
#         continue
#     else:
#         latitudes_per_case.append(float(header_dict['latitude'][i]))
#         longitudes_per_case.append(float(header_dict['longitude'][i]))
# source = ColumnDataSource(data = dict(lon= longitudes_per_case, lat=latitudes_per_case))
# palette.reverse()

# counties = {
#     code: county for code, county in counties.items() if county["state"] == "tx"
# }

# county_xs = [county["lons"] for county in counties.values()]
# county_ys = [county["lats"] for county in counties.values()]

# county_names = [county['name'] for county in counties.values()]
# county_rates = [unemployment[county_id] for county_id in counties]
# color_mapper = LogColorMapper(palette=palette)

# data=dict(
#     x=county_xs,
#     y=county_ys,
#     name=county_names,
#     rate=county_rates,
# )

# hover = HoverTool(
#         tooltips=[
#             ("Name", "@name"), ("Unemployment rate)", "@rate%"), ("(Long, Lat)", "($x, $y)")
#     ]
# )

# TOOLS = "pan,wheel_zoom,reset,hover,save"

# p = figure(
#     title="Texas Unemployment, 2009", tools=[hover],
#     x_axis_location=None, y_axis_location=None,
# )
# p.grid.grid_line_color = None

# p.patches('x', 'y', source=data,
#           fill_color={'field': 'rate', 'transform': color_mapper},
#           fill_alpha=0.7, line_color="white", line_width=0.5)

# p.circle(x='lon', y='lat', size=2, fill_alpha=1, fill_color="blue", source=source)

# show(p)