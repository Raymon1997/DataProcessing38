from bokeh.io import show
from bokeh.models import LogColorMapper, HoverTool, ColumnDataSource
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure

from bokeh.sampledata.us_states import data as states
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.unemployment import data as unemployment

def County_Geo_Map(header_dict, state):
    
    # Vinden lon an lat van elke case binnen aangegeven state
    latitudes_per_case = []
    longitudes_per_case = []
    for i in range(len(header_dict['latitude'])):
        if header_dict['latitude'][i] == 'NA' or header_dict['longitude'][i] == 'NA' or header_dict['state'][i] != state:
            continue
        else:
            latitudes_per_case.append(float(header_dict['latitude'][i]))
            longitudes_per_case.append(float(header_dict['longitude'][i]))

    # Maak dictionary met aantal incidenten per county
    county_dict = {}
    for i in range(len(header_dict['state'])):
        if header_dict['state'][i] == state:
            if header_dict['county'][i] in county_dict:
                county_dict[header_dict['county'][i]] += 1
            else:
                county_dict[header_dict['county'][i]] = 1

    # for county_id in counties:
    #     print(counties[county_id]['name'])

    palette.reverse()

    counties_of_state = {
        code: county for code, county in counties.items() if county["state"] == "tx"
    }

    county_xs = [county["lons"] for county in counties.values()]
    county_ys = [county["lats"] for county in counties.values()]

    county_names = [county['name'] for county in counties.values()]
    # county_rates = [unemployment[county_id] for county_id in counties_of_state]
    color_mapper = LogColorMapper(palette=palette)

    data=dict(
        x=county_xs,
        y=county_ys,
        name=county_names,
        # rate=county_rates,
    )
    # hover = HoverTool(
    #         tooltips=[
    #             ("Name", "@name"), ("Unemployment rate)", "@rate%"), ("(Long, Lat)", "($x, $y)")
    #     ]
    # )

    TOOLS = "pan,wheel_zoom,reset,hover,save"

    p = figure(
        title="Texas Unemployment, 2009", 
        # tools=[hover],
        x_axis_location=None, y_axis_location=None,
    )
    p.grid.grid_line_color = None
    # p.hover.point_policy = "follow_mouse"

    p.patches('x', 'y', source=data,
            fill_color={'field': 'rate', 'transform': color_mapper},
            fill_alpha=0.7, line_color="white", line_width=0.5)
    

    # Create scatterplot
    source = ColumnDataSource(data = dict(lon= longitudes_per_case, lat=latitudes_per_case))
    p.circle(x='lon', y='lat', size = 2, fill_alpha=1, fill_color = "blue", source = source)

    show(p)