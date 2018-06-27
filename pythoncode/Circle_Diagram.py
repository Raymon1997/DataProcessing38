from math import pi
import pandas as pd
from collections import Counter
from bokeh.palettes import Category20c
from bokeh.plotting import figure, show

from bokeh.plotting import figure, show, output_file
from bokeh.models import LogColorMapper, LogTicker, ColorBar, HoverTool, ColumnDataSource, ColumnarDataSource, LinearColorMapper, Plot, Range1d, BasicTickFormatter, LinearAxis, LogTicker, FixedTicker, FuncTickFormatter
from bokeh.io import show
from bokeh.palettes import Viridis6 as palette

from bokeh.models import LogColorMapper, LogTicker, ColorBar
from bokeh.models import ColorBar, LinearColorMapper, Plot, Range1d, BasicTickFormatter, LinearAxis, LogTicker, FixedTicker, FuncTickFormatter


output_file("circle.html")



x = Counter({'Friends': 1041,
 'Family': 3481,
 'Home Invasion': 973,
 'Drive by': 31,
 'Significant others ': 3450,
 'Gang vs Gang': 288,
 'Aquaintance': 948,
 'Neighbor': 701,
 'Mass shooting': 16,
 'Co-worker': 137,
 'Armed Robbery': 4708})

x = pd.DataFrame.from_dict(dict(x), orient='index').reset_index().rename(index=str, \
                                                                         columns={0:'value', 'index':'country'})
x['val'] = x['value']
x['value'] = x['value']/x['value'].sum()*360.0
x['end']=x['value'].expanding(1).sum()
x['start'] = x['end'].shift(1)
x['start'][0]=0
r=[]
p = figure(plot_height=450, plot_width=800, title="Relationships between victims and suspects 2013-2018", toolbar_location=None, tools="")
for i in range(len(x)):
    r1 = p.wedge(x=0, y=1, radius=0.5,start_angle=x.iloc[i]['start'], end_angle=x.iloc[i]['end'],\
               start_angle_units='deg', end_angle_units = 'deg', fill_color=Category20c[20][i],\
                legend = x.iloc[i]['country'])
    relation = x.iloc[i]['country']
    times_occured = x.iloc[i]['val']
    hover = HoverTool(tooltips=[
        ("Relation", "%s" %relation),
        ("Times Occured", "%s" %times_occured)
    ], renderers=[r1])
    p.add_tools(hover)

p.xaxis.axis_label=None
p.yaxis.axis_label=None
p.yaxis.visible=False
p.xaxis.visible=False
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

show(p)
