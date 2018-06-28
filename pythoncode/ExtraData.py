import csv
import pandas

from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.us_states import data as states

from bokeh.models import FixedTicker, LogColorMapper, ColorBar, ColumnDataSource, HoverTool

# Krijg de jusit data
header_dict = {}
row_list = []
index = 0

ifile  = open('statepov.csv', "r")
read = csv.reader(ifile)
x = next(read)
headers = next(read)
row_list.append(headers)
for i in range(49):
    row_list.append(next(read))
writer = csv.writer(open('extradata.csv', 'w'))
writer.writerows(row_list)

for header in headers:
    header_dict[header] = []
    for i in range(1, len(row_list)):
        header_dict[header].append(row_list[i][index])
    index += 1


state_list = []
percentage_list = []
lat = []
lon = []
state_percentage_dict = {}
for i in range(len(header_dict['state'])):
    state_percentage_dict[header_dict['state'][i]] = header_dict['Percentage 2014-2016'][i]
    state_list.append(header_dict['state'][i])
    lat.append(header_dict['state'][i])
    lon.append(header_dict['state'][i])
    percentage_list.append(header_dict['Percentage 2014-2016'][i])


# data =  {
#     "state_list" : state_list,
#     "percentage_list" : percentage_list,
#     "lat" : lat,
#     "lon" : lon
#     }
# source = ColumnDataSource(data=data)

# maak de GeoMap
del states["HI"]
del states["AK"]

state_xs = [states[code]["lons"] for code in states]
state_ys = [states[code]["lats"] for code in states]

colors = list(reversed([
            '#440154', '#440255', '#440357', '#450558', '#45065A', '#45085B', '#46095C', '#460B5E', '#460C5F', '#460E61', '#470F62', '#471163',
            '#471265', '#471466', '#471567', '#471669', '#47186A', '#48196B', '#481A6C', '#481C6E', '#481D6F', '#481E70', '#482071', '#482172',
            '#482273', '#482374', '#472575', '#472676', '#472777', '#472878', '#472A79', '#472B7A', '#472C7B', '#462D7C', '#462F7C', '#46307D',
            '#46317E', '#45327F', '#45347F', '#453580', '#453681', '#443781', '#443982', '#433A83', '#433B83', '#433C84', '#423D84', '#423E85',
            '#424085', '#414186', '#414286', '#404387', '#404487', '#3F4587', '#3F4788', '#3E4888', '#3E4989', '#3D4A89', '#3D4B89', '#3D4C89',
            '#3C4D8A', '#3C4E8A', '#3B508A', '#3B518A', '#3A528B', '#3A538B', '#39548B', '#39558B', '#38568B', '#38578C', '#37588C', '#37598C',
            '#365A8C', '#365B8C', '#355C8C', '#355D8C', '#345E8D', '#345F8D', '#33608D', '#33618D', '#32628D', '#32638D', '#31648D', '#31658D',
            '#31668D', '#30678D', '#30688D', '#2F698D', '#2F6A8D', '#2E6B8E', '#2E6C8E', '#2E6D8E', '#2D6E8E', '#2D6F8E', '#2C708E', '#2C718E',
            '#2C728E', '#2B738E', '#2B748E', '#2A758E', '#2A768E', '#2A778E', '#29788E', '#29798E', '#287A8E', '#287A8E', '#287B8E', '#277C8E',
            '#277D8E', '#277E8E', '#267F8E', '#26808E', '#26818E', '#25828E', '#25838D', '#24848D', '#24858D', '#24868D', '#23878D', '#23888D',
            '#23898D', '#22898D', '#228A8D', '#228B8D', '#218C8D', '#218D8C', '#218E8C', '#208F8C', '#20908C', '#20918C', '#1F928C', '#1F938B',
            '#1F948B', '#1F958B', '#1F968B', '#1E978A', '#1E988A', '#1E998A', '#1E998A', '#1E9A89', '#1E9B89', '#1E9C89', '#1E9D88', '#1E9E88',
            '#1E9F88', '#1EA087', '#1FA187', '#1FA286', '#1FA386', '#20A485', '#20A585', '#21A685', '#21A784', '#22A784', '#23A883', '#23A982',
            '#24AA82', '#25AB81', '#26AC81', '#27AD80', '#28AE7F', '#29AF7F', '#2AB07E', '#2BB17D', '#2CB17D', '#2EB27C', '#2FB37B', '#30B47A',
            '#32B57A', '#33B679', '#35B778', '#36B877', '#38B976', '#39B976', '#3BBA75', '#3DBB74', '#3EBC73', '#40BD72', '#42BE71', '#44BE70',
            '#45BF6F', '#47C06E', '#49C16D', '#4BC26C', '#4DC26B', '#4FC369', '#51C468', '#53C567', '#55C666', '#57C665', '#59C764', '#5BC862',
            '#5EC961', '#60C960', '#62CA5F', '#64CB5D', '#67CC5C', '#69CC5B', '#6BCD59', '#6DCE58', '#70CE56', '#72CF55', '#74D054', '#77D052',
            '#79D151', '#7CD24F', '#7ED24E', '#81D34C', '#83D34B', '#86D449', '#88D547', '#8BD546', '#8DD644', '#90D643', '#92D741', '#95D73F',
            '#97D83E', '#9AD83C', '#9DD93A', '#9FD938', '#A2DA37', '#A5DA35', '#A7DB33', '#AADB32', '#ADDC30', '#AFDC2E', '#B2DD2C', '#B5DD2B',
            '#B7DD29', '#BADE27', '#BDDE26', '#BFDF24', '#C2DF22', '#C5DF21', '#C7E01F', '#CAE01E', '#CDE01D', '#CFE11C', '#D2E11B', '#D4E11A',
            '#D7E219', '#DAE218', '#DCE218', '#DFE318', '#E1E318', '#E4E318', '#E7E419', '#E9E419', '#ECE41A', '#EEE51B', '#F1E51C', '#F3E51E',
            '#F6E61F', '#F8E621', '#FAE622', '#FDE724']))

state_colors = []
for state_id in states:
    try:
        rate = float(state_percentage_dict[states[state_id]['name']]) - 6.9
        idx = int(rate/0.055)
        state_colors.append(colors[idx])
    except KeyError:
        state_colors.append("black")

p = figure(title="Poverty in the US", toolbar_location="left",
           plot_width=1100, plot_height=700)

# hover = p.select(dict(type=HoverTool))
# hover.names=["foo"]
# hover.tooltips=[("State", "@state_list"), ("Percentage", "@percentage_list")]

p.patches(state_xs, state_ys, fill_alpha=1, fill_color=state_colors,
          line_color="#884444", line_width=2, line_alpha=0.3)


ticker = FixedTicker(ticks=[6.9, 20.8])
color_mapper = LogColorMapper(palette=colors, low=6.9, high=20.8)

color_bar = ColorBar(color_mapper=color_mapper, orientation="horizontal", ticker=ticker,
                     label_standoff=12, border_line_color=None, location=(0,0))

p.add_layout(color_bar, 'below')

output_file("choropleth.html", title="choropleth.py example")

show(p)