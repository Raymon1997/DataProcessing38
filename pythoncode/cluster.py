import pandas as pd

import pylab as pl
import plotly

from sklearn.cluster import KMeans

from sklearn.decomposition import PCA
from bokeh.plotting import figure, output_file, save, show

df = pd.read_csv('output.csv')

Y = df[['n_killed']]

X = df[['n_injured']]

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
    