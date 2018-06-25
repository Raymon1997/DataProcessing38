
import numpy as np

from bokeh.plotting import figure, output_file, show

datelist = []
for key in year_dict.keys():
    datelist.append(key)
killed = np.array(year_dict.values())
dates = np.array(datelist, dtype = datetime64
window_size = 30
window = np.ones(window_size)/float(window_size)


# output to static HTML file
output_file("killed.html", title="normal graph")

# create a new plot with a a datetime axis type
p = figure(width=800, height=350, x_axis_type="datetime")

# add renderers
p.circle(dates, killed, size=4, color='darkgrey', alpha=0.2, legend='close')
p.line(dates, killed, color='navy', legend='avg')

# NEW: customize by setting attributes
p.title.text = "People killed by date"
p.legend.location = "top_left"
p.grid.grid_line_alpha = 0
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Killed'
p.ygrid.band_fill_color = "olive"
p.ygrid.band_fill_alpha = 0.1

# show the results
show(p)
