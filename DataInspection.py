# Maak dicitonary met als keys de headers
for header in headers:
    header_dict[header] = []
    for i in range(1, len(row_list)):
        header_dict[header].append(row_list[i][index])
    index += 1

# Bepaal hoeveel totaal aantal wapens
guns_used_list = []
number_of_guns = 0
for value in header_dict['n_guns_involved']:
    if value != 'NA':
        guns_used_list.append(value)
        number_of_guns += int(value)
average_used = number_of_guns/len(guns_used_list)
print(average_used)
#bepaal totaal aantal gestolen wapens
# number_of_guns_stolen = 0
# for value in header_dict['gun_stolen']:
#     if 'Unknown' in value:
#     if len(list(value)) < 2:
#         number_of_guns_stolen += int(value)

# maakt dictionary met aantal guns involved
year_dict = {}
for i in range(len(header_dict['date'])):
    if header_dict['date'][i][0:4] in year_dict:
        if header_dict['n_guns_involved'][i] == 'NA':
            year_dict[header_dict['date'][i][0:4]] += 1
        else:
            year_dict[header_dict['date'][i][0:4]] += int(header_dict['n_guns_involved'][i])
    else:
        if header_dict['n_guns_involved'][i] == 'NA':
            year_dict[header_dict['date'][i][0:4]] = 1
        else:
            year_dict[header_dict['date'][i][0:4]] = int(header_dict['n_guns_involved'][i])
print(year_dict)
# maakt dictionary met aantal doden per state
state_dict = {}
for i in range(len(header_dict['state'])):
    if header_dict['state'][i] in state_dict:
        state_dict[header_dict['state'][i]] += int(header_dict['n_injured'][i])
    else:
        state_dict[header_dict['state'][i]] = int(header_dict['n_injured'][i])

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

def check_if_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# maakt dictionary met aantal doden per state
address_dict = {}
for i in range(len(header_dict['address'])):
    max_index = 0
    address = list(header_dict['address'][i])
    for index in range(len(address)):
        if address[index].isdigit() == True:
            max_index = index
        else:
            break
    if max_index != 0:
        max_index += 2
    street_name = "".join(address[max_index:len(address)])

    if street_name in address_dict:
        address_dict[street_name] += int(header_dict['n_killed'][i])
    else:
        address_dict[street_name] = int(header_dict['n_killed'][i])
max_killed_key = 'Coursin St'

for key in address_dict:
    if int(address_dict[key]) > int(address_dict[max_killed_key]) and key != 'NA' :
        max_killed_key = key
# print(max_killed_key, address_dict[max_killed_key])
