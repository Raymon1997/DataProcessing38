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

print(relation_values)

pyplot.axis("equal")
pyplot.pie([float(v) for v in relation_values], labels=relation_keys,
           autopct=None)
pyplot.show()