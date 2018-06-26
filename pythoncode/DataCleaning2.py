import csv
import pandas as pd
import sys
import bokeh
from collections import Counter
from numpy import pi
from bokeh.embed import file_html
import matplotlib.pyplot as pyplot
from sklearn.linear_model import LinearRegression
import seaborn as sns

header_dict = {}
index = 0
row_list = []

# Inladen eerste 500 rows van dataset
ifile  = open('stage3.csv', "r", encoding='UTF-8')
read = csv.reader(ifile)
headers = next(read)
row_list.append(headers)
for i in range(500):
    row_list.append(next(read))

# Veranderd missende data in NA
for row in row_list:
    for i in range(len(row)):
        if row[i] == '':
            row[i] = 'NA'

# Exporteer aangepaste data naar output.csv
writer = csv.writer(open('output.csv', 'w', encoding='UTF-8'))
writer.writerows(row_list)

# Maak dicitonary met als keys de headers
for header in headers:
    header_dict[header] = []
    for i in range(1, len(row_list)):
        header_dict[header].append(row_list[i][index])
    index += 1

# Bepaal hoeveel totaal aantal wapens
number_of_guns = 0
for value in header_dict['n_guns_involved']:
    if value != 'NA':
        number_of_guns += int(value)

#bepaal totaal aantal gestolen wapens
# number_of_guns_stolen = 0
# for value in header_dict['gun_stolen']:
#     if 'Unknown' in value:
#     if len(list(value)) < 2:
#         number_of_guns_stolen += int(value)

# maakt dictionary met aantal doden per jaar
year_dict = {}
for i in range(len(header_dict['date'])):
    if header_dict['date'][i][0:4] in year_dict:
        year_dict[header_dict['date'][i][0:4]] += int(header_dict['n_killed'][i])
    else:
        year_dict[header_dict['date'][i][0:4]] = int(header_dict['n_killed'][i])

# maakt dictionary met aantal doden per state
state_dict = {}
for i in range(len(header_dict['state'])):
    if header_dict['state'][i] in state_dict:
        state_dict[header_dict['state'][i]] += int(header_dict['n_killed'][i])
    else:
        state_dict[header_dict['state'][i]] = int(header_dict['n_killed'][i])

# maakt dictionary met aantal doden per city/county
city_or_county_dict = {}
for i in range(len(header_dict['city_or_county'])):
    lengte = int(len(header_dict['city_or_county'][i]))
    # countys vinden
    # if header_dict['city_or_county'][i][lengte - 8:lengte] == '(county)':
    #     print(header_dict['city_or_county'][i], "is a county")

    if header_dict['city_or_county'][i] in city_or_county_dict:
        city_or_county_dict[header_dict['city_or_county'][i]] += int(header_dict['n_killed'][i])
    else:
        city_or_county_dict[header_dict['city_or_county'][i]] = int(header_dict['n_killed'][i])



family_dict = {}
gang_dict = {}

for i in range(len(header_dict['participant_relationship'])):
    if 'Family' in header_dict['participant_relationship'][i]:
        if header_dict['date'][i][0:4] in family_dict:
            family_dict[header_dict['date'][i][0:4]] += 1
        else:
            family_dict[header_dict['date'][i][0:4]] = 1  
    if 'Gang vs Gang' in header_dict['participant_relationship'][i]:
            if header_dict['date'][i][0:4] in gang_dict:
                gang_dict[header_dict['date'][i][0:4]] += 1
            else:
                gang_dict[header_dict['date'][i][0:4]] = 1
    
relation_type = []

for i in range(len(header_dict['participant_relationship'])):
    if '|' in header_dict['participant_relationship'][i]:
        string = header_dict['participant_relationship'][i]
        substring = string[string.find(":"):string.find("|")]
        if substring not in relation_type:
            relation_type.append(substring)
    elif header_dict['participant_relationship'][i] != 'NA' and header_dict['participant_relationship'][i][3:] not in relation_type:
        if ":" in header_dict['participant_relationship'][i][3:]:
            string = header_dict['participant_relationship'][i][3:]
            relation_type.append(string.replace(":" , ""))
        else:
            relation_type.append(header_dict['participant_relationship'][i][3:])


relation_dict = {}

for i in range(len(header_dict['participant_relationship'])):
    if 'Aquaintance' in header_dict['participant_relationship'][i]:
        if 'Aquaintance' in relation_dict:
            relation_dict['Aquaintance'] += 1
        else:
            relation_dict['Aquaintance'] = 1  
    elif 'Armed Robbery' in header_dict['participant_relationship'][i]:
            if 'Armed Robbery' in relation_dict:
                relation_dict['Armed Robbery'] += 1
            else:
                relation_dict['Armed Robbery'] = 1
    elif 'Co-worker' in header_dict['participant_relationship'][i]:
            if 'Co-worker' in relation_dict:
                relation_dict['Co-worker'] += 1
            else:
                relation_dict['Co-worker'] = 1
    elif 'Drive by' in header_dict['participant_relationship'][i]:
            if 'Drive by' in relation_dict:
                relation_dict['Drive by'] += 1
            else:
                relation_dict['Drive by'] = 1
    elif 'Family' in header_dict['participant_relationship'][i]:
            if 'Family' in relation_dict:
                relation_dict['Family'] += 1
            else:
                relation_dict['Family'] = 1
    elif 'Friends' in header_dict['participant_relationship'][i]:
            if 'Friends' in relation_dict:
                relation_dict['Friends'] += 1
            else:
                relation_dict['Friends'] = 1
    elif 'Gang vs Gang' in header_dict['participant_relationship'][i]:
            if 'Gang vs Gang' in relation_dict:
                relation_dict['Gang vs Gang'] += 1
            else:
                relation_dict['Gang vs Gang'] = 1
    elif 'Home Invasion' in header_dict['participant_relationship'][i]:
            if 'Home Invasion' in relation_dict:
                relation_dict['Home Invasion'] += 1
            else:
                relation_dict['Home Invasion'] = 1
    elif 'Mass shooting' in header_dict['participant_relationship'][i]:
            if 'Mass shooting' in relation_dict:
                relation_dict['Mass shooting'] += 1
            else:
                relation_dict['Mass shooting'] = 1
    elif 'Neighbor' in header_dict['participant_relationship'][i]:
            if 'Neighbor' in relation_dict:
                relation_dict['Neighbor'] += 1
            else:
                relation_dict['Neighbor'] = 1
    elif 'Significant others ' in header_dict['participant_relationship'][i]:
            if 'Significant others ' in relation_dict:
                relation_dict['Significant others '] += 1
            else:
                relation_dict['Significant others '] = 1



relation_values = relation_dict.values()
relation_keys = relation_dict.keys()


pyplot.axis("equal")
pyplot.pie([float(v) for v in relation_values], labels=relation_keys)
pyplot.savefig("pie-chart.png")

n_guns = []
n_killed = []



for i in range(len(header_dict['n_guns_involved'])):
    if "NA" not in header_dict['n_guns_involved'][i] and "" != header_dict['n_guns_involved'][i]:
        n_guns.append(int(header_dict['n_guns_involved'][i]))
        n_killed.append(int(header_dict['n_killed'][i]))

# line = LinearRegression()
# line.fit(n_guns,n_killed)
# pyplot.scatter(n_guns,n_killed)
# pyplot.plot(n_guns, line.predict(n_guns), color="k")
# pyplot.show()