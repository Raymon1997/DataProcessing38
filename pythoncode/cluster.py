import pandas as pd

import pylab as pl


from sklearn.cluster import KMeans

from sklearn.decomposition import PCA
from bokeh.plotting import figure, output_file, save, show

df = pd.read_csv('output.csv')

Y = df[['n_killed']]

X = df[['guns_used']]

Nc = range(1, 50)

kmeans = [KMeans(n_clusters=i) for i in Nc]

pca = PCA(n_components=1).fit(Y)

pca_d = pca.transform(Y)

pca_c = pca.transform(X)

kmeans=KMeans(n_clusters=3)

kmeansoutput=kmeans.fit(Y)

pl.figure('Clustering')

pl.scatter(pca_c[:, 0], pca_d[:, 0], c=kmeansoutput.labels_)

pl.xlabel('Number of people killed')

pl.ylabel('Number of people injured')

pl.title('Clustering')

pl.show()

# row_list = []
# index  = 0
# header_dict = {}
# ifile  = open('output.csv')
# read = csv.reader(ifile)
# headers = next(read)
# row_list.append(headers)
# for i in range(239677):
#     row_list.append(next(read))

# for header in headers:
#     header_dict[header] = []
#     for i in range(1, len(row_list)):
#         header_dict[header].append(row_list[i][index])
#     index += 1

# month_incident_dict = {}
# for i in range(len(header_dict['date'])):
#     if header_dict['date'][i][0:7] in month_incident_dict:
#         month_incident_dict[header_dict['date'][i][0:7]] += 1
#     else:
#         month_incident_dict[header_dict['date'][i][0:7]] = 1

# month_list = []
# incident_list = []
# for key in month_incident_dict.keys():
#     month_list.append(key)
#     incident_list.append(month_incident_dict[key])
    