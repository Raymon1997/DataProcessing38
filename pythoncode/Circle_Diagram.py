# from collections import Counter
# from math import pi

# import pandas as pd

# from bokeh.models import HoverTool, ColumnDataSource

# from bokeh.io import output_file, show
# # from bokeh.palettes import Category20c
# from bokeh.plotting import figure
# # from bokeh.transform import cumsum

# output_file("pie.html")

# x = Counter({
#     'United States': 157,
#     'United Kingdom': 93,
#     'Japan': 89,
#     'China': 63,
#     'Germany': 44,
#     'India': 42,
#     'Italy': 40,
#     'Australia': 35,
#     'Brazil': 32,
#     'France': 31,
#     'Taiwan': 31,
#     'Spain': 29
# })
# k = sum(x.values())
# percents = [157/k, 93/k, 89/k, 63/k, 44/k, 42/k, 40/k, 35/k, 32/k, 31/k, 31/k, 29/k]
# starts = [1/2*pi-(p*2*pi) for p in percents[:-1]]
# ends = [1/2*pi-(p*2*pi) for p in percents[1:]]
# print(starts)
# print(ends)
# source = ColumnDataSource(
#     data=dict(
#         x=[0 for x in percents],
#         y=[0 for x in percents],
#         radius = [0.5 for x in percents],
#         percents=percents,
#         starts=starts,
#         ends=ends,
#         color=['#0C0786', '#40039C', '#6A00A7', '#8F0DA3', '#B02A8F', '#CA4678', '#E06461', '#F1824C', '#FCA635', '#FCCC25', '#EFF821', '#FCE8AA']
#     )
# )

# data = pd.DataFrame.from_dict(dict(x), orient='index').reset_index().rename(index=str, columns={0:'value', 'index':'country'})
# data['angle'] = data['value']/sum(x.values()) * 2*pi
# data['color'] = ['#0C0786', '#40039C', '#6A00A7', '#8F0DA3', '#B02A8F', '#CA4678', '#E06461', '#F1824C', '#FCA635', '#FCCC25', '#EFF821', '#FCE8AA']

# p = figure(plot_height=350, title="Pie Chart", toolbar_location=None)

# p.wedge(x=0, y=1, radius=0.4, start_angle='starts', end_angle='ends',
#             line_color="white", fill_color='color', legend='country', source=source)

# p.axis.axis_label=None
# p.axis.visible=False
# p.grid.grid_line_color = None

# show(p)

# import numpy as np
# from bokeh.plotting import figure
# from bokeh.io import show, output_file
# from bokeh.models import HoverTool, ColumnDataSource
# from math import pi

# percents = [0, 5/143, 51/143, 88/143, 108/143, 141/143, 1.0]
# category = ['A ', 'B ', 'C ', 'D ', 'E ', 'F']
# counts = [5, 46, 37, 20, 33, 2]
# starts = [1/2*pi-(p*2*pi) for p in percents[:-1]]
# ends = [1/2*pi-(p*2*pi) for p in percents[1:]]
# colors = ['#889dba', '#1f356f', '#1e92b8', '#33748a', '#a5d3e3', '#bbc2d4']
# # create source
# source = ColumnDataSource(
#     data=dict(
#         x=[0 for x in percents],
#         y=[0 for x in percents],
#         radius = [0.5 for x in percents],
#         percents=percents,
#         category= category,
#         starts=starts,
#         colors=colors,
#         ends=ends,
#         counts = counts
#     )
# )

# TOOLS = "hover"

# p = figure(plot_width = 500, plot_height = 500, x_axis_label = None, y_axis_label = None,
# title = 'Type', tools = TOOLS)

# p.title.align = 'center'
# p.title.text_font = 'arial narrow'

# p.wedge(x='x', y='y',  radius = 'radius', direction="clock",
#                 start_angle='starts', end_angle='ends', color='colors', source=source)

# hover = p.select(dict(type=HoverTool))
# hover.tooltips = [
#     ('category', '@category'),
#     ('percents','@counts')
# ]

# p.axis.visible = False
# p.ygrid.visible = False
# p.xgrid.visible = False

# output_file('pie.html')
# show(p)


import matplotlib.pyplot as plt
# Pie chart
labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
sizes = [15, 30, 45, 10]
#colors
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
#explsion
explode = (0.05,0.05,0.05,0.05)
 
plt.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode)
#draw circle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')  
plt.tight_layout()
plt.show()