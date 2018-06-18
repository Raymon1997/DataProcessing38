from bokeh.io import show, output_file
from bokeh.models import FactorRange
from bokeh.plotting import figure
import pandas


#colnames = ['date', 'state', 'city_or_county', 'address', 'n_killed', 'n_injured', 'congressional_district', 'gun_stolen', 'latitude', 'longitude', 'n_guns_involved', 'participant_age_group', 'participant_gender', 'participant_relationship', 'participant_type', 'state_house_district', 'state_senate_district' ]
#data = pandas.read_csv('output.csv', names=colnames)
#killed = data.n_killed.tolist()



output_file("mixed.html")

factors = [
    ("Q1", "jan"), ("Q1", "feb"), ("Q1", "mar"),
    ("Q2", "apr"), ("Q2", "may"), ("Q2", "jun"),
    ("Q3", "jul"), ("Q3", "aug"), ("Q3", "sep"),
    ("Q4", "oct"), ("Q4", "nov"), ("Q4", "dec"),
    ]


p = figure(x_range=FactorRange(*factors), plot_height=250,
           toolbar_location=None, tools="")
y1 = (6035 + 4945 + 5641)/3
y2 = (4383 + 4830 + 4886)/3
y3 = (5275 + 5127 + 4770)/3
y4 = (4791 + 4848 + 4927)/3
x = [ 6035, 4945, 5641, 4383, 4830, 4886, 5275, 5127, 4770, 4791, 4848, 4927 ]
p.vbar(x=factors, top=x, width=0.9, alpha=0.5)

p.line(x=["Q1", "Q2", "Q3", "Q4"], y=[y1, y2, y3, y4], color="red", line_width=2)

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None

show(p)
