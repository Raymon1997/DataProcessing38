from datetime import date
from random import randint
from bokeh.layouts import widgetbox
from bokeh.io import output_file, show

from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn

output_file("data_table.html")

data = dict(
        month=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        killed=[6035, 4945, 5641, 4383, 4830, 4886, 5276, 5127, 4779, 4791, 4848, 4927],
        injured=[10946, 8420, 10475, 8907, 10244, 9797, 11259, 10809, 9766, 9756, 9087, 8936],
        total=[16981, 15365, 16116, 15290, 15077, 15130, 16535, 15936, 14535, 14547, 13935, 13863],
    )
source = ColumnDataSource(data)

columns = [
        TableColumn(field="month", title="Month"),
        TableColumn(field="killed", title="Killed"),
        TableColumn(field="injured", title="Injured"),
        TableColumn(field="total", title="Total"),
    ]
data_table = DataTable(source=source, columns=columns, width=400, height=280)

show(widgetbox(data_table))

print(longitudes_per_case)
print(latitudes_per_case)
