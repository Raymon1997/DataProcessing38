import csv
import pandas

from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.us_states import data as states

from bokeh.models import FixedTicker, LogColorMapper, ColorBar, ColumnDataSource, HoverTool

relative_dict = {'Pennsylvania': 0.0581020460950177, 'California': 0.03320023239659872, 'Ohio': 0.0702115084281173, 'Colorado': 0.033936156045095506, 'North Carolina': 0.06596633022298333, 'Oklahoma': 0.06321499111411917, 'New Mexico': 0.049648253127648624, 'Louisiana': 0.1404588864645001, 'Maryland': 0.07990654651406456, 'Tennessee': 0.09291471484824912, 'Missouri':0.09323833811829682, 'Illinois': 0.1325389714543495, 'Delaware': 0.11017525072592105, 'Utah': 0.021650057211225746, 'Michigan': 0.04582042736306243, 'Georgia': 0.06175357780998219, 'Indiana':0.06812317517880467, 'Mississippi': 0.10255516237341947, 'New York': 0.03405410151545786, 'Florida': 0.05152445234330685, 'Washington': 0.028417571514013848, 'South Carolina': 0.09223968326456951, 'Arizona': 0.030741596805569087, 'Kentucky': 0.06618570232309579, 'New Jersey': 0.04105006691116624, 'Virginia': 0.05893971844994992, 'Wisconsin': 0.051202731362351886, 'Rhode Island': 0.03852268788522688, 'Texas': 0.038851281322364956, 'Alabama': 0.0997760459354352, 'Kansas': 0.05047087302960581, 'Connecticut': 0.04455673571613876, 'West Virginia': 0.05457337651137473, 'Minnesota': 0.024466246707184336, 'Nevada': 0.057248961667403814, 'Nebraska':0.046518872225232065, 'Massachusetts': 0.031511400151712964, 'Hawaii': 0.01037582209110673, 'New Hampshire': 0.017177868685559854, 'Iowa': 0.03461419568031291, 'Alaska': 0.08020941159893126, 'Arkansas': 0.07019107533720687, 'Idaho': 0.01796038452328008, 'Oregon': 0.02714568158639363, 'Wyoming': 0.021787631597294847, 'Maine': 0.018187483135581724, 'North Dakota': 0.02634930975401132, 'Montana': 0.027298485404723582, 'Vermont': 0.02083466888903135, 'South Dakota': 0.02324018273163285}

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
        rate = float(relative_dict[states[state_id]['name']]) - 0.017177868685559854
        idx = int(rate/((0.1404588864645001 - 0.017177868685559854) / 240))
        print(0.2663414855999363/((0.2663414855999363 - 0.017177868685559854) / 240))
        state_colors.append(colors[idx])
    except KeyError:
        state_colors.append("black")

p = figure(title="Poverty in the US", toolbar_location="left",
           plot_width=1100, plot_height=700)

p.patches(state_xs, state_ys, fill_alpha=1, fill_color=state_colors,
          line_color="#884444", line_width=2, line_alpha=0.3)

ticker = FixedTicker(ticks=[0.017177868685559854, 0.1404588864645001])
color_mapper = LogColorMapper(palette=colors, low=0.017177868685559854, high=0.1404588864645001)

color_bar = ColorBar(color_mapper=color_mapper, orientation="horizontal", ticker=ticker,
                     label_standoff=12, border_line_color=None, location=(0,0))

p.add_layout(color_bar, 'below')
output_file("choropleth.html", title="choropleth.py example")
show(p)
