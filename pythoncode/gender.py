from datetime import date
from random import randint

from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn

output_file("data_data_table.html")

data = dict(
        SuspectVictim =["Suspect", "Victim", "Suspect", "Victim"],
        child=[389, 2147, 42, 1276],
        teen=[10402, 9599, 542, 2232],
        adult=[139185, 122354, 10820, 27603],
        gender=["Male", "Male", "Female", "Female"],
    )
source = ColumnDataSource(data)

columns = [
        TableColumn(field="SuspectVictim", title="Suspect/Victim"),
        TableColumn(field="child", title="Child"),
        TableColumn(field="teen", title="Teen"),
        TableColumn(field="adult", title="Adult"),
        TableColumn(field="gender", title="Gender"),
    ]
data_table = DataTable(source=source, columns=columns, width=500, height=300)

show(widgetbox(data_table))