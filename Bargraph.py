from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import dodge

output_file("dodged_bars.html")

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ['2013', '2014', '2015', '2016', '2017', '2018']

data = {'fruits' : fruits,
        '2013'   : [2, 1, 4, 3, 2, 4],
        '2014'   : [5, 3, 3, 2, 4, 6],
        '2015'   : [5, 3, 3, 2, 4, 6],
        '2016'   : [5, 3, 3, 2, 4, 6],
        '2017'   : [3, 2, 4, 4, 5, 3],
        '2018'   : [3, 2, 4, 4, 5, 3]}

source = ColumnDataSource(data=data)

p = figure(x_range=fruits, y_range=(0, 10), plot_height=250, title="Fruit Counts by Year",
           toolbar_location=None, tools="")

p.vbar(x=dodge('fruits', -0.25, range=p.x_range), top='2013', width=0.11, source=source,
       color="royalblue", legend=value("2013"))

p.vbar(x=dodge('fruits', -0.125, range=p.x_range), top='2014', width=0.11, source=source,
       color="seagreen", legend=value("2014"))

p.vbar(x=dodge('fruits', 0.0, range=p.x_range), top='2015', width=0.11, source=source,
       color="lightcoral", legend=value("2015"))

p.vbar(x=dodge('fruits',  0.125,  range=p.x_range), top='2016', width=0.11, source=source,
       color="lightyellow", legend=value("2016"))

p.vbar(x=dodge('fruits',  0.25, range=p.x_range), top='2017', width=0.11, source=source,
       color="lightpink", legend=value("2017"))

p.vbar(x=dodge('fruits', 0.375, range=p.x_range), top='2018', width=0.11, source=source,
       color="violet", legend=value("2018"))

p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"

show(p)