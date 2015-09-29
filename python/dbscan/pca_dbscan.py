import os
import numpy
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition.pca import PCA
import matplotlib.pyplot as plt

data_dir = '../../data/'
plot_dir = 'plots'

eps = 2.6
min_samples = 2
n_pca_components = 10

# data
derivatives = numpy.loadtxt(os.path.join(data_dir, 'derivatives.dat'))

# apply PCA + DBSCAN
pca = PCA(n_components=n_pca_components)
pca.fit(derivatives)
X = pca.transform(derivatives)
X = StandardScaler().fit_transform(X)

model = DBSCAN(eps=eps, min_samples=min_samples, algorithm='kd_tree')
model.fit(X)

# output
core_samples_mask = numpy.zeros_like(model.labels_, dtype=bool)
core_samples_mask[model.core_sample_indices_] = True
labels = model.labels_
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print('Number of clusters: %d' % n_clusters_)

# plot resuls
fig, ax = plt.subplots(figsize=(15,15))
unique_labels = set(labels)
colors = plt.cm.Spectral(numpy.linspace(0, 1, len(unique_labels)))

for k, col in zip(unique_labels, colors):

    # noise
    if k == -1:
        col = 'k'

    class_member_mask = (labels == k)

    xy = X[class_member_mask & core_samples_mask]
    ax.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=10, alpha=0.6)

    xy = X[class_member_mask & ~core_samples_mask]
    ax.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor='k', markeredgecolor='k', markersize=4)
    
plt.title('Estimated number of clusters: %d' % n_clusters_)


plt.savefig(os.path.join(plot_dir, "pca_dbscan.png"))

