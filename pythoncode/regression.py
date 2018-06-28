import numpy as np

import pandas as pd
from pandas import Series,DataFrame
from bokeh.layouts import gridplot, row, column

from bokeh.io import push_notebook, show, output_notebook
from bokeh.plotting import figure, output_file, save

from sklearn.datasets import load_boston

df = pd.read_csv("output.csv")

X = df["n_killed"]

Y = df["n_injured"]

X = np.vstack([X, np.ones(X.shape[0])]).T
# = np.vstack([x, np.ones(len(x))]).T
a, b = np.linalg.lstsq(X, Y)[0]

f = figure(plot_width=400, plot_height=250)


f.scatter([x for x in df["n_killed"] if x < 50], [y for y in df["n_injured"] if y < 50])

x = df["n_killed"]

f.line(x, a * -x + b, color= "red")

f.xaxis.axis_label = "Number Killed People"
f.yaxis.axis_label = "Number Injured People"

output_file("regression.html")
save(f)
