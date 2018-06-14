import csv
import collections
import pandas as pd

data = pd.read_csv("output.csv")

relation = collections.Counter()
with open('output.csv') as input_file:
    for row in csv.reader(input_file, delimiter=';'):
        relation[row[1]] += 1

print('Number of related participants: %s' % relation['NA'])
print(relation.most_common())