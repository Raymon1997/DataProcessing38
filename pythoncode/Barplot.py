from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import dodge
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool


output_file("injured_killed_guns_barplot.html", mode="inline")

incidents = ['killed', 'injured', 'guns used']
years = ['2013', '2014', '2015', '2016', '2017', '2018']
number = [317, 979, 299,12557, 23002, 53964,13484, 26967, 69655,15066, 30580, 74106,15511, 30703, 76325, 3533, 6171, 17554]
data = {'incidents' : incidents,
        # 'years'  : years,
        # 'number' : number,
        '2013'   : [317, 979, 299],
        '2014'   : [12557, 23002, 53964],
        '2015'   : [13484, 26967, 69655],
        '2016'   : [15066, 30580, 74106],
        '2017'   : [15511, 30703, 76325],
        '2018'   : [3533, 6171, 17554]}

#hier start HoverTool

source = ColumnDataSource(data=data)

p = figure(x_range=incidents, y_range=(0, 80000), plot_height=400, title="Incidents per Year",
           toolbar_location=None, tools="")

hover = p.select(dict(type=HoverTool))
hover.tooltips = [('type',' @incidents'),('2013','@2013'),('2014',' @2014'),('2015',' @2015'),('2016',' @2016'),('2017',' @2017'),('2018',' @2018'),]
#hier eindigd HoverTool

p.vbar(x=dodge('incidents', -0.25, range=p.x_range), top='2013', width=0.11, source=source,
       color="royalblue", legend=value("2013"))

p.vbar(x=dodge('incidents', -0.125, range=p.x_range), top='2014', width=0.11, source=source,
       color="seagreen", legend=value("2014"))

p.vbar(x=dodge('incidents', 0.0, range=p.x_range), top='2015', width=0.11, source=source,
       color="lightcoral", legend=value("2015"))

p.vbar(x=dodge('incidents',  0.125,  range=p.x_range), top='2016', width=0.11, source=source,
       color="red", legend=value("2016"))

p.vbar(x=dodge('incidents',  0.25, range=p.x_range), top='2017', width=0.11, source=source,
       color="lightpink", legend=value("2017"))

p.vbar(x=dodge('incidents', 0.375, range=p.x_range), top='2018', width=0.11, source=source,
       color="violet", legend=value("2018 up to march"))

p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"

show(p)
