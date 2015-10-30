import os
import numpy
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition.pca import PCA
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from operator import itemgetter

data_dir = '/home/emille/Documents/github/mlsnespectra/MLSNeSpectra/python/SN_simulator/simulated_data/6/'

n_pca_components = 4
eps_range = numpy.arange(0.01,20,0.1)
min_samples_range = range(2,15)
allowed_noise_ratio = 0.2

# data
derivatives = numpy.loadtxt(os.path.join(data_dir, 'derivatives.dat'))

# PCA
pca = PCA(n_components=n_pca_components)
pca.fit(derivatives)
X = pca.transform(derivatives)
X = StandardScaler().fit_transform(X)

results = []

for eps in eps_range:
    for minsamp in min_samples_range:

        model = DBSCAN(eps=eps, min_samples=minsamp, algorithm='kd_tree')
        model.fit(X)

        labels = model.labels_
        noise_ratio = float(sum(labels==-1)) / len(labels)
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
        if noise_ratio <= allowed_noise_ratio:
            results.append([eps, minsamp, noise_ratio, n_clusters])


results = numpy.array(results)

plt.figure()
plt.scatter(results[:,0], results[:,-1])
plt.show()

results = sorted(results, key=itemgetter(3), reverse=True)
for i in xrange(40):
    print results[i]

