from bokeh.io import show, output_file
from bokeh.models import FactorRange
from bokeh.plotting import figure
import pandas as pd
import numpy as np
from bokeh.models import LogColorMapper, LogTicker, ColorBar, HoverTool, ColumnDataSource, ColumnarDataSource, LinearColorMapper, Plot, Range1d, BasicTickFormatter, LinearAxis, LogTicker, FixedTicker, FuncTickFormatter


#colnames = ['date', 'state', 'city_or_county', 'address', 'n_killed', 'n_injured', 'congressional_district', 'gun_stolen', 'latitude', 'longitude', 'n_guns_involved', 'participant_age_group', 'participant_gender', 'participant_relationship', 'participant_type', 'state_house_district', 'state_senate_district' ]
#data = pandas.read_csv('output.csv', names=colnames)
#killed = data.n_killed.tolist()



output_file("average per month.html")


y1 = 1104
y2 = 1169
y3 = 1256
y4 = 1207

factors = [
    ("Q1", "jan"), ("Q1", "feb"), ("Q1", "mar"),
    ("Q2", "apr"), ("Q2", "may"), ("Q2", "jun"),
    ("Q3", "jul"), ("Q3", "aug"), ("Q3", "sep"),
    ("Q4", "oct"), ("Q4", "nov"), ("Q4", "dec"),
    ]
months = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
killed_by_month = [ 1202, 986, 1123, 1089, 1202, 1215, 1311, 1273, 1185, 1191, 1205, 1224 ]
standard_deviation = [129, 131, 83, 123, 128, 128, 110, 129, 107, 165, 160, 112]
quadrant_average = [1104,1104,1104,1169,1169,1169,1256,1256,1256,1207,1207,1207]
killed_by_quadrant = [y1, y2, y3, y4]

data = {
        'killed_by_month' : killed_by_month,
        #'killed_by_quadrant' : killed_by_quadrant,
        'months' : months,
        'factors' : factors,
        'standard_deviation' : standard_deviation,
        'quadrant_average' : quadrant_average
        }
source = ColumnDataSource(data=data)


p = figure(height= 350, x_range=FactorRange(*factors),
           toolbar_location=None, tools = "hover")
hover = p.select(dict(type=HoverTool))
hover.names=["foo"]
hover.tooltips=[("month", "@months"), ("killed", "@killed_by_month"), ("standard deviation", "@standard_deviation"), ("quadrant average", "@quadrant_average")]



p.vbar(x='factors', top='killed_by_month', width=0.9, alpha=0.5, legend='average killed per month', name="foo", source= source)
p.circle(x=["Q1", "Q2", "Q3", "Q4"], y= killed_by_quadrant, color="red", line_width=2, legend='average killed by quadrant ')

p.y_range.start = 0
p.y_range.end = 1800
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None

#show(p)


# Read the data from a csv into a dataframe
crime = pd.read_csv('output.csv', index_col=0)

# Summary stats for the column of interest
print(crime['n_killed'].describe())


arr_hist, edges = np.histogram(crime['n_killed'],
                               bins = int(365/7),
                               range = [-60, 120])

# Put the information in a dataframe
kills = pd.DataFrame({'n_killed': arr_hist,
                       'left': edges[:-1],
                       'right': edges[1:]})

p.title.text = "Average people killed per month"
p.legend.location = "top_left"
p.legend.background_fill_alpha = 0.8
p.grid.grid_line_alpha = 0
p.xaxis.axis_label = 'month'
p.yaxis.axis_label = 'number killed'

show(p)
